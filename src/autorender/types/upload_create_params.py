# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to upload."""

    file_name: Required[str]
    """File name (e.g. product.jpg)"""

    custom_id: str
    """Custom identifier"""

    folder: str
    """Optional folder path"""

    metadata: str
    """JSON string of metadata"""

    random_prefix: str
    """true/false to append random suffix"""

    tags: str
    """Comma-separated tags"""

    transform: str
    """Transform string (w_300,h_300,c_crop,...)"""

    webhook_url: str
    """URL to notify on success"""
