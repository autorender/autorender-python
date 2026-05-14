#!/usr/bin/env python3
"""Multipart upload lifecycle: start session → (upload parts via presigned URLs) → complete."""
import os
import sys
import tempfile
import urllib.request
from autorender import Autorender

CHUNK_SIZE = 5 * 1024 * 1024  # 5 MB minimum per S3 part

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python multipart.py <path-to-file>")
        sys.exit(1)

    path = sys.argv[1]
    file_name = os.path.basename(path)
    file_size = os.path.getsize(path)
    ext = os.path.splitext(file_name)[1].lstrip(".") or "bin"

    client = Autorender()

    # Start session
    start = client.multipart_uploads.start(
        file_name=file_name,
        format=ext,
        size=file_size,
    )
    print(f"Session: {start.session_id}")
    print(f"Parts:   {len(start.parts)} presigned URL(s)")

    # Upload each part
    with open(path, "rb") as f:
        for i, url in enumerate(start.parts):
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            req = urllib.request.Request(url, data=chunk, method="PUT")
            req.add_header("Content-Length", str(len(chunk)))
            with urllib.request.urlopen(req) as resp:
                print(f"  Part {i + 1}: {resp.status}")

    # Complete
    result = client.multipart_uploads.complete(session_id=start.session_id)
    print(f"Complete: {result.file_no}")
    print(f"URL:      {result.url}")

if __name__ == "__main__":
    main()
