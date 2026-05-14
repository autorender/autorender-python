#!/usr/bin/env python3
"""Folders lifecycle: create → list → rename → delete."""
from autorender import Autorender

def main() -> None:
    client = Autorender()

    # Create
    folder = client.folders.create(name="sdk-example-folder")
    folder_no = folder.folder_no
    print(f"Created folder: {folder_no}")

    # List
    listing = client.folders.list()
    print(f"Total folders: {len(listing.folders)}")

    # Rename
    renamed = client.folders.rename(folder_no, name="sdk-example-folder-renamed")
    print(f"Renamed to: {renamed.name}")

    # Delete
    client.folders.delete(folder_no)
    print("Deleted.")

if __name__ == "__main__":
    main()
