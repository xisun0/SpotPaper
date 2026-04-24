#!/usr/bin/env python3
"""
Call GPT Image 2 edit endpoint for IMAGE2 polish stage.

Usage:
    python3 scripts/image2_edit.py -i input.png -o output.png -p "polish instructions"

Output is always written to a new file; the input image is never overwritten.
Requires OPENAI_API_KEY in environment or ~/.env.
"""
import argparse
import base64
import os
import sys
from pathlib import Path

from dotenv import load_dotenv


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="image2_edit.py",
        description="GPT Image 2 edit wrapper for IMAGE2 polish stage.",
    )
    p.add_argument("-i", "--input", required=True, type=Path, help="Input image path.")
    p.add_argument("-o", "--output", required=True, type=Path, help="Output image path (must differ from input).")
    p.add_argument("-p", "--prompt", required=True, help="Edit instruction prompt.")
    p.add_argument("--size", default="1536x1024", help="Image size (default: 1536x1024).")
    p.add_argument("--quality", default="high", choices=["auto", "low", "medium", "high"])
    return p.parse_args()


def main() -> int:
    args = parse_args()

    load_dotenv(Path.home() / ".env", override=True)

    if not os.environ.get("OPENAI_API_KEY"):
        print("error: OPENAI_API_KEY not set.", file=sys.stderr)
        return 2

    if not args.input.is_file():
        print(f"error: input not found: {args.input}", file=sys.stderr)
        return 2

    if args.input.resolve() == args.output.resolve():
        print("error: output path must differ from input — original is never overwritten.", file=sys.stderr)
        return 2

    from openai import OpenAI, APIError
    client = OpenAI()

    print(f"calling GPT Image 2 edit: {args.input} → {args.output}")

    try:
        with open(args.input, "rb") as f:
            result = client.images.edit(
                model="gpt-image-2",
                image=f,
                prompt=args.prompt,
                size=args.size,
                quality=args.quality,
            )
    except APIError as e:
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        return 1

    data = result.data
    if not data:
        print("error: no image data in response.", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    img_bytes = base64.b64decode(data[0].b64_json)
    args.output.write_bytes(img_bytes)
    print(f"saved: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
