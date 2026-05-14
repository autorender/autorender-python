# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    folder_no: str
    """Filter by folder number"""

    limit: int

    page: int

    search: str
    """Partial name match (case-insensitive)"""

    sort: Literal["name_asc", "name_desc", "size_asc", "size_desc", "created_at_asc", "created_at_desc"]
