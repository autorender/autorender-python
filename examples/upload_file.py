#!/usr/bin/env python3
"""Upload a local file via multipart/form-data."""
import sys
import os
from autorender import Autorender

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python upload_file.py <path-to-file>")
        sys.exit(1)

    path = sys.argv[1]
    file_name = os.path.basename(path)
    client = Autorender()

    with open(path, "rb") as f:
        result = client.uploads.create(file=f, file_name=file_name)

    print(f"Uploaded: {result.file_no}")
    print(f"URL:      {result.url}")
    print(f"Size:     {result.size} bytes")
    if result.format:
        print(f"Format:   {result.format}")

if __name__ == "__main__":
    main()
