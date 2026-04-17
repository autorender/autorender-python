# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileObject", "Data", "DataDimensions", "DataWorkspace"]


class DataDimensions(BaseModel):
    height: Optional[int] = None

    width: Optional[int] = None


class DataWorkspace(BaseModel):
    name: Optional[str] = None

    workspace_no: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    asset_key: Optional[str] = None

    asset_url: Optional[str] = None

    dimensions: Optional[DataDimensions] = None

    extension: Optional[str] = None

    file_no: Optional[str] = None

    folder: Optional[object] = None

    format: Optional[str] = None

    name: Optional[str] = None

    path: Optional[str] = None

    size: Optional[int] = None
    """File size in bytes"""

    uploaded_at: Optional[datetime] = None

    uploaded_by: Optional[str] = None

    url: Optional[str] = None

    workspace: Optional[DataWorkspace] = None


class FileObject(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
