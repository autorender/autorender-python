#!/usr/bin/env python3
"""Upload a file from a remote URL."""
import sys
from autorender import Autorender

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python upload_from_url.py <url>")
        sys.exit(1)

    remote_url = sys.argv[1]
    client = Autorender()
    result = client.uploads.create_from_url(remote_url=remote_url)

    print(f"Uploaded: {result.file_no}")
    print(f"URL:      {result.url}")

if __name__ == "__main__":
    main()
