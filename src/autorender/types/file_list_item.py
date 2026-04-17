# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileListItem"]


class FileListItem(BaseModel):
    created_at: Optional[datetime] = None

    extension: Optional[str] = None

    file_no: Optional[str] = None

    file_size: Optional[int] = None

    format: Optional[str] = None

    height: Optional[int] = None

    name: Optional[str] = None

    path: Optional[str] = None

    thumbnail: Optional[str] = None
    """Thumbnail CDN URL"""

    url: Optional[str] = None

    width: Optional[int] = None

    workspace_no: Optional[str] = None
