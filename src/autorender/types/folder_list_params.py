# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FolderListParams"]


class FolderListParams(TypedDict, total=False):
    parent_folder_no: str
    """Filter by parent folder number"""

    search: str
    """Partial name match (case-insensitive)"""

    sort: Literal["name_asc", "name_desc", "created_at_asc", "created_at_desc"]
