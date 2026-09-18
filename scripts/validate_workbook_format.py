#!/usr/bin/env python3
"""Validate that a generated workbook still preserves the bundled template layout."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"m": MAIN, "r": REL, "p": PKG_REL}
EXPECTED_SHEETS = ["关键词分析", "关键词库", "ASIN与标题", "卖家精灵原始数据", "产品信息", "Listing文案"]


def workbook_map(zf: zipfile.ZipFile) -> tuple[list[str], dict[str, str]]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    targets = {r.attrib["Id"]: r.attrib["Target"].lstrip("/") for r in rels}
    names: list[str] = []
    paths: dict[str, str] = {}
    sheet_nodes = wb.find("m:sheets", NS)
    for sheet in [] if sheet_nodes is None else sheet_nodes:
        name = sheet.attrib["name"]
        rid = sheet.attrib[f"{{{REL}}}id"]
        target = targets[rid]
        if target.startswith("xl/"):
            path = target
        else:
            path = f"xl/{target}"
        names.append(name)
        paths[name] = path
    return names, paths


def view_signature(root: ET.Element) -> tuple[tuple[tuple[str, str], ...], tuple[tuple[str, str], ...]]:
    views = root.find("m:sheetViews", NS)
    if views is None or len(views) == 0:
        return (), ()
    view = views[0]
    retained = {key: value for key, value in view.attrib.items() if key in {"showGridLines", "rightToLeft", "zoomScale"}}
    pane = view.find("m:pane", NS)
    pane_attrs = {} if pane is None else pane.attrib
    return tuple(sorted(retained.items())), tuple(sorted(pane_attrs.items()))


def sheet_signature(zf: zipfile.ZipFile, path: str) -> tuple[set[str], dict[int, float], dict[int, float], object, str, str]:
    root = ET.fromstring(zf.read(path))
    merge_node = root.find("m:mergeCells", NS)
    merges = {n.attrib["ref"] for n in ([] if merge_node is None else merge_node)}
    widths: dict[int, float] = {}
    cols = root.find("m:cols", NS)
    for col in [] if cols is None else cols:
        start, end = int(col.attrib["min"]), int(col.attrib["max"])
        width = float(col.attrib["width"])
        for index in range(start, end + 1):
            widths[index] = width
    heights: dict[int, float] = {}
    sheet_data = root.find("m:sheetData", NS)
    for row in [] if sheet_data is None else sheet_data:
        if "ht" in row.attrib and row.attrib.get("customHeight") == "1":
            heights[int(row.attrib["r"])] = float(row.attrib["ht"])
    view = view_signature(root)
    page_margins = root.find("m:pageMargins", NS)
    margins = "" if page_margins is None else ET.tostring(page_margins, encoding="unicode")
    page_setup = root.find("m:pageSetup", NS)
    setup = "" if page_setup is None else ET.tostring(page_setup, encoding="unicode")
    return merges, widths, heights, view, margins, setup


def shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    return ["".join(node.text or "" for node in item.findall(".//m:t", NS)) for item in root]


def cell_map(zf: zipfile.ZipFile, path: str) -> dict[str, tuple[str, str]]:
    strings = shared_strings(zf)
    root = ET.fromstring(zf.read(path))
    result: dict[str, tuple[str, str]] = {}
    for cell in root.findall(".//m:sheetData/m:row/m:c", NS):
        ref = cell.attrib.get("r", "")
        style = cell.attrib.get("s", "0")
        kind = cell.attrib.get("t")
        if kind == "inlineStr":
            value = "".join(node.text or "" for node in cell.findall(".//m:t", NS))
        else:
            node = cell.find("m:v", NS)
            raw = "" if node is None or node.text is None else node.text
            if kind == "s" and raw.isdigit() and int(raw) < len(strings):
                value = strings[int(raw)]
            else:
                value = raw
        result[ref] = (value, style)
    return result


def normalized(value: str) -> str:
    return " ".join(value.replace("\n", " ").split()).strip()


def image_hash(zf: zipfile.ZipFile) -> str:
    data = zf.read("xl/media/image1.png")
    return hashlib.sha256(data).hexdigest()


LISTING_ANCHORS = {
    "A6": "一、基础产品信息合规校验",
    "A12": "二、主标题",
    "A18": "三、商品亮点",
    "A24": "四、五点描述",
    "A33": "五、产品描述",
    "A46": "六、后台搜索关键词",
    "A53": "七、关键词位置核验表",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--require-replaced-image", action="store_true")
    parser.add_argument(
        "--template",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "amazon-keyword-listing-output-template.xlsx",
    )
    args = parser.parse_args()
    errors: list[str] = []
    try:
        with zipfile.ZipFile(args.template) as template_zip, zipfile.ZipFile(args.workbook) as output_zip:
            template_names, template_paths = workbook_map(template_zip)
            output_names, output_paths = workbook_map(output_zip)
            if output_names != EXPECTED_SHEETS:
                errors.append(f"sheet order mismatch: {output_names!r}")
            if template_names != EXPECTED_SHEETS:
                errors.append("bundled template sheet order is invalid")
            for sheet_name in EXPECTED_SHEETS:
                if sheet_name not in output_paths or sheet_name not in template_paths:
                    continue
                template_merges, template_widths, template_heights, template_view, template_margins, template_setup = sheet_signature(template_zip, template_paths[sheet_name])
                output_merges, output_widths, output_heights, output_view, output_margins, output_setup = sheet_signature(output_zip, output_paths[sheet_name])
                missing = sorted(template_merges - output_merges)
                if missing:
                    errors.append(f"{sheet_name} missing {len(missing)} required merged ranges; first: {missing[:8]}")
                for index, expected in template_widths.items():
                    actual = output_widths.get(index)
                    if actual is None or abs(actual - expected) > 0.01:
                        errors.append(f"{sheet_name} column {index} width changed: expected {expected}, got {actual}")
                for index, expected in template_heights.items():
                    actual = output_heights.get(index)
                    if actual is None or abs(actual - expected) > 0.01:
                        errors.append(f"{sheet_name} row {index} height changed: expected {expected}, got {actual}")
                if output_view != template_view:
                    errors.append(f"{sheet_name} sheet view/freeze/gridline state changed")
                if output_margins != template_margins:
                    errors.append(f"{sheet_name} page margins changed")
                if output_setup != template_setup:
                    errors.append(f"{sheet_name} page setup changed")

            if "Listing文案" in output_paths:
                template_cells = cell_map(template_zip, template_paths["Listing文案"])
                output_cells = cell_map(output_zip, output_paths["Listing文案"])
                for ref, prefix in LISTING_ANCHORS.items():
                    actual, actual_style = output_cells.get(ref, ("", ""))
                    expected_style = template_cells.get(ref, ("", ""))[1]
                    if not normalized(actual).startswith(prefix):
                        errors.append(f"Listing文案 {ref} section anchor missing or overwritten: {actual!r}")
                    if actual_style != expected_style:
                        errors.append(f"Listing文案 {ref} section style changed: expected {expected_style}, got {actual_style}")

                section8_rows = []
                for ref, (value, _style) in output_cells.items():
                    if re.fullmatch(r"A\d+", ref) and normalized(value).startswith("八、全链路合规与埋词自检"):
                        section8_rows.append(int(ref[1:]))
                if len(section8_rows) != 1 or section8_rows[0] < 81:
                    errors.append(f"Listing文案 section 8 anchor invalid: {section8_rows}")
                else:
                    section8_row = section8_rows[0]
                    header = normalized(output_cells.get("A54", ("", ""))[0])
                    if header != "序号":
                        errors.append("Listing文案 keyword table header must remain at row 54")
                    expected_number = 1
                    for row in range(55, section8_row):
                        raw_number = normalized(output_cells.get(f"A{row}", ("", ""))[0])
                        keyword = normalized(output_cells.get(f"B{row}", ("", ""))[0])
                        placement = normalized(output_cells.get(f"F{row}", ("", ""))[0])
                        if not raw_number and not keyword and not placement:
                            continue
                        if raw_number and not raw_number.isdigit() and expected_number > 25 and not keyword and not placement:
                            continue
                        if raw_number != str(expected_number):
                            errors.append(f"Listing文案 keyword row {row} sequence invalid: expected {expected_number}, got {raw_number!r}")
                            break
                        if not keyword or not placement:
                            errors.append(f"Listing文案 keyword row {row} missing keyword or placement")
                            break
                        expected_number += 1
                    if expected_number - 1 < 25:
                        errors.append(f"Listing文案 contains fewer than 25 populated keyword rows: {expected_number - 1}")

            if "产品信息" in output_paths:
                product_cells = cell_map(output_zip, output_paths["产品信息"])
                required_values = {
                    "A2": "产品信息",
                    "A5": "图片",
                    "B5": "产品名称",
                    "C5": "本链接品牌",
                    "D5": "尺寸",
                    "E5": "重量",
                    "F5": "材质",
                    "G5": "使用场景",
                    "H5": "使用规格（如有）",
                    "I5": "注意事项",
                }
                for ref, expected in required_values.items():
                    actual = normalized(product_cells.get(ref, ("", ""))[0])
                    if actual != expected:
                        errors.append(f"产品信息 {ref} expected {expected!r}, got {actual!r}")
                if normalized(product_cells.get("A6", ("", ""))[0]):
                    errors.append("产品信息 A6 must be blank; product image must be an embedded drawing, not filename text")
                if not normalized(product_cells.get("B6", ("", ""))[0]):
                    errors.append("产品信息 B6 product name is blank")

            if args.require_replaced_image:
                try:
                    if image_hash(output_zip) == image_hash(template_zip):
                        errors.append("embedded product image is unchanged from the floor-chair template")
                except KeyError:
                    errors.append("embedded product image xl/media/image1.png is missing")
    except (OSError, KeyError, ET.ParseError, zipfile.BadZipFile) as exc:
        errors.append(f"cannot inspect workbook package: {exc}")

    if errors:
        print("FORMAT_VALIDATION_FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("FORMAT_VALIDATION_PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
