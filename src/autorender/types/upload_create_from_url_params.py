# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UploadCreateFromURLParams"]


class UploadCreateFromURLParams(TypedDict, total=False):
    remote_url: Required[str]
    """The HTTP or HTTPS URL of the image to download"""

    custom_id: str
    """Custom identifier for tracking the upload"""

    folder: str
    """Folder path where the file should be stored"""

    metadata: str
    """JSON string containing custom metadata object"""

    random_prefix: str
    """Set to 'true' to generate a random suffix for the filename"""

    tags: str
    """Comma-separated list of tags to apply to the file"""

    transform: str
    """Transformation string to apply during upload (e.g., w_800,h_600,c_crop)"""

    webhook_url: str
    """URL to receive webhook notification when upload completes"""
