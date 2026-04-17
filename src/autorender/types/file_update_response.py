# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileUpdateResponse"]


class FileUpdateResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    extension: Optional[str] = None

    file_no: Optional[str] = None

    file_size: Optional[int] = None

    folder_id: Optional[str] = None

    format: Optional[str] = None

    height: Optional[int] = None

    meta_data: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    path: Optional[str] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None

    width: Optional[int] = None

    workspace_no: Optional[str] = None
