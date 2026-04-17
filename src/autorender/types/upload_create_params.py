# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to upload (binary data)"""

    file_name: Required[str]
    """File name for the uploaded file (e.g., my-image.jpg)"""

    custom_id: str
    """Custom identifier for the file"""

    folder: str
    """Folder path where the file will be stored (e.g., uploads/my-folder)"""

    metadata: str
    """JSON string for custom metadata (e.g., {"key": "value"})"""

    random_prefix: str
    """Set to "true" to add a random suffix to filename"""

    tags: str
    """Comma-separated tags (e.g., tag1,tag2,tag3)"""

    transform: str
    """Image transformation string (e.g., w_800,h_600,q_90)"""
