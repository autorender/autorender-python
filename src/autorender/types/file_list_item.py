# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileListItem"]


class FileListItem(BaseModel):
    """File summary row in list responses"""

    created_at: Optional[datetime] = None

    extension: Optional[str] = None
    """Asset category, e.g. image"""

    file_no: Optional[str] = None

    file_size: Optional[int] = None

    format: Optional[str] = None

    height: Optional[int] = None

    name: Optional[str] = None

    path: Optional[str] = None
    """Relative path / display path"""

    thumbanil: Optional[str] = None
    """Thumbnail CDN URL (field name as returned by the API)"""

    url: Optional[str] = None

    width: Optional[int] = None

    workspace_no: Optional[str] = None
