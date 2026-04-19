# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FolderRenameResponse"]


class FolderRenameResponse(BaseModel):
    """Renamed folder"""

    id: str

    created_at: datetime

    folder_no: str

    name: str

    parent_folder_no: Optional[str] = None

    path: str

    updated_at: Optional[datetime] = None
