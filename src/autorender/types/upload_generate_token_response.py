# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UploadGenerateTokenResponse", "Policy", "PolicyAllowOverride"]


class PolicyAllowOverride(BaseModel):
    folder: Optional[bool] = None

    tags: Optional[bool] = None

    transform: Optional[bool] = None


class Policy(BaseModel):
    allow_override: Optional[PolicyAllowOverride] = None

    folder: Optional[str] = None

    max_file_size: Optional[int] = None

    tags: Optional[List[str]] = None

    transform: Optional[str] = None


class UploadGenerateTokenResponse(BaseModel):
    token: Optional[str] = None

    expire_at: Optional[int] = None
    """Unix timestamp of expiry"""

    policy: Optional[Policy] = None

    public_key: Optional[str] = None

    signature: Optional[str] = None

    workspace_id: Optional[str] = None
