# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

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

    tags: str
    """Comma-separated tags"""

    webhook_url: str
