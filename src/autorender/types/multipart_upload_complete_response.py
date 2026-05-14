# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MultipartUploadCompleteResponse"]


class MultipartUploadCompleteResponse(BaseModel):
    """Upload completed"""

    id: str

    created_at: datetime

    custom_id: Optional[str] = None

    extension: str

    file_no: str

    folder_no: Optional[str] = None

    height: Optional[int] = None

    is_duplicate: bool

    metadata: Optional[Dict[str, object]] = None

    mime_type: str

    name: str

    path: str

    size: int

    tags: List[str]

    thumbnail: str

    upload_source: str

    url: str

    width: Optional[int] = None

    workspace_id: str

    format: Optional[str] = None

    hash: Optional[str] = None

    is_private: Optional[bool] = None
