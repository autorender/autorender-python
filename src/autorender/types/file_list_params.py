# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    folder_no: str
    """Restrict results to files in this folder (folder number)"""

    limit: int
    """Items per page"""

    name: str
    """Filter by filename (partial match, if supported)"""

    page: int
    """Page number (1-based)"""

    path: str
    """Filter by path prefix (if supported)"""

    sort_field: Literal["file_size", "name", "created_at", "updated_at"]
    """Field to sort by"""

    sort_order: Literal["asc", "desc"]
    """Sort direction"""

    tags: str
    """Comma-separated tags (if supported)"""
