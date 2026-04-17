# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    folder_no: str
    """Filter to files in this folder"""

    limit: int
    """Items per page"""

    name: str
    """Partial filename match (case-insensitive)"""

    page: int
    """Page number (1-based)"""

    path: str
    """Filter by path prefix (e.g., products/sku123/)"""

    sort_field: Literal["file_size", "name", "created_at", "updated_at"]
    """Field to sort by"""

    sort_order: Literal["asc", "desc"]
    """Sort direction"""

    tags: str
    """Comma-separated tags to filter by"""
