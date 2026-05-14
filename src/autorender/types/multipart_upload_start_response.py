# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["MultipartUploadStartResponse", "Policy"]


class Policy(BaseModel):
    folder: str

    format: str

    size: int

    tags: List[str]


class MultipartUploadStartResponse(BaseModel):
    """Session created"""

    expire_at: int
    """Unix timestamp when the session expires"""

    min_part_size: int

    part_size: int

    parts: List[str]
    """Pre-signed S3 upload URLs, one per part"""

    policy: Policy

    public_key: str

    session_id: str

    uuid: str

    workspace_id: str
