# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["UploadGenerateTokenParams", "AllowOverride"]


class UploadGenerateTokenParams(TypedDict, total=False):
    file_name: Required[str]
    """Filename for the upload (e.g., avatar.jpg)"""

    allow_override: AllowOverride
    """Which policy fields the uploader may override"""

    custom_id: str
    """Custom identifier for the file"""

    folder: str
    """Destination folder path"""

    max_file_size: int
    """Maximum allowed file size in bytes"""

    metadata: Dict[str, object]
    """Custom metadata to attach"""

    random_prefix: bool
    """Add a random prefix to the filename"""

    tags: SequenceNotStr[str]
    """Tags to apply to the uploaded file"""

    transform: str
    """Transformation string applied on upload"""

    ttl_seconds: int
    """Token lifetime in seconds (default: 300)"""


class AllowOverride(TypedDict, total=False):
    """Which policy fields the uploader may override"""

    folder: bool

    tags: bool

    transform: bool
