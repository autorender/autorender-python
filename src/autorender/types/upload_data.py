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
    """File size in bytes (after processing)"""

    format: Optional[str] = None
    """File format/extension (e.g., jpg, png, webp)"""

    height: Optional[int] = None
    """Image height in pixels (null for non-image files)"""

    name: Optional[str] = None
    """Final filename (may include random suffix if requested)"""

    path: Optional[str] = None
    """Folder path where the file is stored"""

    url: Optional[str] = None
    """Full CDN URL to access the uploaded file"""

    width: Optional[int] = None
    """Image width in pixels (null for non-image files)"""

    workspace_no: Optional[str] = None
    """Workspace identifier"""
