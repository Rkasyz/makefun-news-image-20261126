"""Entry for make.fun news-image-20261126.

Copies the front-page image for Thursday 26 November 2026 to the
output directory as entry.png. The image is a JPEG (the .png name is
required by the competition); it is copied byte for byte, so repeated
runs produce identical output.
"""

import os
import shutil

SOURCE = os.path.join(
    os.path.dirname(__file__),
    "media-generation-entry-0-2a4a2291-e01c-4265-9b90-a984a17be5f3.jpg",
)


MAX_BYTES = 1048576  # competition cap: entry.png must be at most 1 MiB


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    dest = os.path.join(output_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    size = os.path.getsize(dest)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB cap")


if __name__ == "__main__":
    main()
