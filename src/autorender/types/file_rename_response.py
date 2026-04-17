# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileRenameResponse"]


class FileRenameResponse(BaseModel):
    """Updated file record after rename"""

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    extension: Optional[str] = None

    file_no: Optional[str] = None

    file_size: Optional[int] = None

    folder_id: Optional[str] = None

    format: Optional[str] = None

    height: Optional[int] = None

    is_active: Optional[bool] = None

    is_default: Optional[bool] = None

    is_delete: Optional[bool] = None

    meta_data: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    orientation: Optional[str] = None

    original_url: Optional[str] = None

    path: Optional[str] = None

    source: Optional[str] = None

    transform_string: Optional[str] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None

    width: Optional[int] = None

    workspace_id: Optional[str] = None

    workspace_no: Optional[str] = None
