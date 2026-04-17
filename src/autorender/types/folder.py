# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Folder", "Workspace"]


class Workspace(BaseModel):
    workspace_no: Optional[str] = None


class Folder(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    folder_no: Optional[str] = None

    is_active: Optional[bool] = None

    is_delete: Optional[bool] = None

    name: Optional[str] = None

    parent_folder: Optional[str] = None

    path: Optional[str] = None

    source: Optional[str] = None

    updated_at: Optional[datetime] = None

    workspace: Optional[Workspace] = None

    workspace_id: Optional[str] = None

    workspace_no: Optional[str] = None
