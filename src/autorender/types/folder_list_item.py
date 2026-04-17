# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FolderListItem"]


class FolderListItem(BaseModel):
    created_at: Optional[datetime] = None

    folder_no: Optional[str] = None

    name: Optional[str] = None

    total_items: Optional[int] = None

    total_size: Optional[int] = None
    """Total size of items in bytes"""
