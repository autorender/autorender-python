# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .folder_list_item import FolderListItem

__all__ = ["FolderListResponse"]


class FolderListResponse(BaseModel):
    folders: Optional[List[FolderListItem]] = None
