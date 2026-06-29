# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["UploadCreateFromURLParams"]


class UploadCreateFromURLParams(TypedDict, total=False):
    remote_url: Required[str]
    """HTTP/HTTPS URL to fetch"""

    custom_id: str

    file_name: str
    """Override file name"""

    folder: str
    """Destination folder path"""

    metadata: str
    """JSON string of metadata object"""

    random_prefix: str
    """true/false to append random suffix"""

    tags: Union[SequenceNotStr[str], str]
    """Tags array or comma-separated string"""

    webhook_url: str
