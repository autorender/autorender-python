# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FolderCreateParams"]


class FolderCreateParams(TypedDict, total=False):
    folder_name: Required[str]
    """Folder name without slashes"""

    path: str
    """Optional parent path, e.g. products/sku123"""
