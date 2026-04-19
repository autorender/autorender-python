# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["UploadGenerateTokenParams", "AllowOverride"]


class UploadGenerateTokenParams(TypedDict, total=False):
    file_name: Required[str]
    """File name for the uploaded file (e.g., avatar.jpg)"""

    allow_override: AllowOverride

    custom_id: str

    folder: str
    """Destination folder path"""

    max_file_size: int
    """Max file size in bytes"""

    metadata: Dict[str, object]

    random_prefix: bool

    tags: SequenceNotStr[str]

    ttl_seconds: int
    """Token lifetime in seconds. Defaults to 300."""


class AllowOverride(TypedDict, total=False):
    folder: bool

    tags: bool
