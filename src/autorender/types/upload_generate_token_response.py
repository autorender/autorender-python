# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UploadGenerateTokenResponse", "Policy", "PolicyAllowOverride"]


class PolicyAllowOverride(BaseModel):
    folder: Optional[bool] = None

    tags: Optional[bool] = None


class Policy(BaseModel):
    allow_override: PolicyAllowOverride

    folder: str

    max_file_size: int

    tags: List[str]


class UploadGenerateTokenResponse(BaseModel):
    """Token generated"""

    token: str

    expire_at: int

    policy: Policy

    public_key: str

    signature: str

    workspace_id: str
