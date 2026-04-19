# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    folder_no: Annotated[str, PropertyInfo(alias="folderNo")]
    """Exact folder number"""

    limit: int

    name: str
    """Partial name match (case-insensitive)"""

    page: int

    path: str
    """Folder prefix (e.g. products/sku123/)"""

    sort: Literal["created_at_asc", "created_at_desc", "size_asc", "size_desc"]

    tags: str
    """Comma-separated tags"""
