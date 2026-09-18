#!/usr/bin/env python3
"""Check that the skill package contains every required workflow resource."""

from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET


REQUIRED = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/input-output.md",
    "references/keyword-library-logic.md",
    "references/listing-writing-logic.md",
    "references/keyword-analysis.md",
    "references/listing-generation.md",
    "references/final-output-format.md",
    "references/excel-template-contract.md",
    "assets/amazon-keyword-listing-output-template.xlsx",
    "scripts/validate_listing.py",
    "scripts/validate_workbook_format.py",
    "scripts/prepare_workbook.py",
]

EXPECTED_SHEETS = [
    "关键词分析",
    "关键词库",
    "ASIN与标题",
    "卖家精灵原始数据",
    "产品信息",
    "Listing文案",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [name for name in REQUIRED if not (root / name).is_file()]
    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    dangling = [name for name in REQUIRED[2:] if name not in skill_text and name.startswith("references/")]
    template_errors = []
    template = root / "assets/amazon-keyword-listing-output-template.xlsx"
    if template.is_file():
        try:
            with zipfile.ZipFile(template) as archive:
                workbook = ET.fromstring(archive.read("xl/workbook.xml"))
            namespace = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            sheet_names = [item.attrib["name"] for item in workbook.findall("m:sheets/m:sheet", namespace)]
            if sheet_names != EXPECTED_SHEETS:
                template_errors.append(f"unexpected worksheet order: {sheet_names}")
        except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
            template_errors.append(f"invalid template workbook: {exc}")
    if missing or dangling or template_errors:
        if missing:
            print("Missing files:", *missing, sep="\n- ")
        if dangling:
            print("Unreferenced workflow files:", *dangling, sep="\n- ")
        if template_errors:
            print("Template errors:", *template_errors, sep="\n- ")
        return 1
    print("Skill package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
