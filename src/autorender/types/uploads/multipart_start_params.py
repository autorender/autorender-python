# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MultipartStartParams"]


class MultipartStartParams(TypedDict, total=False):
    file_name: Required[str]
    """Original filename (e.g., big-video.mp4)"""

    format: Required[str]
    """MIME type (e.g., video/mp4, image/jpeg)"""

    size: Required[int]
    """Total file size in bytes"""

    custom_id: str

    folder: str
    """Destination folder path"""

    metadata: Dict[str, object]

    random_prefix: bool

    tags: SequenceNotStr[str]

    ttl_seconds: int
    """Presigned URL lifetime in seconds"""
