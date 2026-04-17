# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UploadData"]


class UploadData(BaseModel):
    id: Optional[str] = None
    """Unique file record ID"""

    file_no: Optional[str] = None
    """10-character file number identifier"""

    file_size: Optional[int] = None
    """File size in bytes"""

    format: Optional[str] = None
    """File format (e.g., jpeg, png, mp4)"""

    height: Optional[int] = None
    """Image height in pixels"""

    name: Optional[str] = None
    """Final filename"""

    path: Optional[str] = None
    """Folder path where the file is stored"""

    url: Optional[str] = None
    """CDN URL to access the file"""

    width: Optional[int] = None
    """Image width in pixels"""

    workspace_no: Optional[str] = None
    """Workspace identifier"""
