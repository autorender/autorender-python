# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileUpdateResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: datetime

    file_no: str

    folder_name: Optional[str] = None

    folder_no: Optional[str] = None

    format: Optional[str] = None

    height: Optional[int] = None

    metadata: Optional[Dict[str, object]] = None

    mime_type: str

    name: str

    path: str

    size: int

    source: str

    tags: List[str]

    updated_at: Optional[datetime] = None

    url: str

    width: Optional[int] = None


class FileUpdateResponse(BaseModel):
    """Updated file"""

    data: Data

    success: Literal[True]
