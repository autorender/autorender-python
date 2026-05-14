#!/usr/bin/env python3
"""Files lifecycle: list → retrieve → rename → delete."""
import os
import tempfile
from autorender import Autorender
from autorender.resources.uploads import UploadsResource

def main() -> None:
    client = Autorender()

    # Upload a temp file so we have something to work with
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
        f.write(b"hello from autorender python sdk example")
        tmp_path = f.name

    try:
        upload = client.uploads.create(
            file=open(tmp_path, "rb"),
            file_name="sdk-example.txt",
        )
        file_no = upload.file_no
        print(f"Uploaded: {file_no}")

        # List files
        listing = client.files.list(limit=10)
        print(f"Total files: {listing.meta.total}")

        # Retrieve
        detail = client.files.retrieve(file_no)
        print(f"Retrieved: {detail.name} ({detail.size} bytes)")

        # Rename
        renamed = client.files.rename(file_no, name="sdk-example-renamed")
        print(f"Renamed to: {renamed.data.name}")

        # Delete
        client.files.delete(file_no)
        print("Deleted.")
    finally:
        os.unlink(tmp_path)

if __name__ == "__main__":
    main()
