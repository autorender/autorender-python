# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UploadCreateFromURLParams"]


class UploadCreateFromURLParams(TypedDict, total=False):
    remote_url: Required[str]
    """HTTP or HTTPS URL of the file to download"""

    custom_id: str
    """Custom identifier for the file"""

    file_name: str
    """Override filename. Defaults to filename from URL."""

    folder: str
    """Destination folder path"""

    metadata: str
    """JSON string of custom metadata"""

    random_prefix: str
    """Set to "true" to add a random suffix"""

    tags: str
    """Comma-separated tags"""

    transform: str
    """Transformation string applied after download"""

    webhook_url: str
    """URL to receive a webhook notification on completion"""
