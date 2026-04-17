# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FolderListParams"]


class FolderListParams(TypedDict, total=False):
    parent_folder_no: str
    """Only return direct children of this folder (folder number)"""
