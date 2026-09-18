#!/usr/bin/env python3
"""Copy the bundled workbook and replace its embedded sample product image."""

from __future__ import annotations

import argparse
import io
import os
import tempfile
import zipfile
from pathlib import Path

from PIL import Image


def png_bytes(source: Path, size: tuple[int, int]) -> bytes:
    with Image.open(source) as image:
        image = image.convert("RGBA")
        image.thumbnail(size, Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", size, (255, 255, 255, 0))
        left = (size[0] - image.width) // 2
        top = (size[1] - image.height) // 2
        canvas.alpha_composite(image, (left, top))
        output = io.BytesIO()
        canvas.save(output, format="PNG", optimize=True)
        return output.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("product_image", type=Path)
    parser.add_argument("output_workbook", type=Path)
    parser.add_argument(
        "--template",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "amazon-keyword-listing-output-template.xlsx",
    )
    args = parser.parse_args()
    if not args.product_image.is_file():
        parser.error(f"product image not found: {args.product_image}")
    if not args.template.is_file():
        parser.error(f"template not found: {args.template}")
    args.output_workbook.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(args.template) as source_zip:
        old_image = source_zip.read("xl/media/image1.png")
        with Image.open(io.BytesIO(old_image)) as template_image:
            target_size = template_image.size
        replacement = png_bytes(args.product_image, target_size)
        fd, temp_name = tempfile.mkstemp(suffix=".xlsx", dir=args.output_workbook.parent)
        os.close(fd)
        try:
            with zipfile.ZipFile(temp_name, "w") as output_zip:
                for item in source_zip.infolist():
                    data = replacement if item.filename == "xl/media/image1.png" else source_zip.read(item.filename)
                    output_zip.writestr(item, data)
            os.replace(temp_name, args.output_workbook)
        finally:
            if os.path.exists(temp_name):
                os.unlink(temp_name)
    print(f"PREPARED_WORKBOOK: {args.output_workbook}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
