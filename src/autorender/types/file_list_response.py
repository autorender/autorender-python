# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .file_list_item import FileListItem

__all__ = ["FileListResponse", "Meta"]


class Meta(BaseModel):
    has_next: bool = FieldInfo(alias="hasNext")

    has_prev: bool = FieldInfo(alias="hasPrev")

    limit: int

    page: int

    total: int
    """Total matching files"""


class FileListResponse(BaseModel):
    files: List[FileListItem]

    meta: Meta
