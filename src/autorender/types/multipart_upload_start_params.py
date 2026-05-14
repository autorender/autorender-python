# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MultipartUploadStartParams"]


class MultipartUploadStartParams(TypedDict, total=False):
    file_name: Required[str]

    format: Required[str]

    size: Required[int]

    custom_id: str

    folder: str

    metadata: Dict[str, object]

    random_prefix: bool

    tags: Union[SequenceNotStr[str], str]

    ttl_seconds: int
