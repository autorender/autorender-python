# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FolderListResponse", "Folder"]


class Folder(BaseModel):
    id: str

    created_at: datetime

    folder_no: str

    name: str

    parent_folder_no: Optional[str] = None

    path: str

    updated_at: Optional[datetime] = None


class FolderListResponse(BaseModel):
    """List of folders"""

    folders: List[Folder]
