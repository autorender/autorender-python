# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    part_size: Optional[int] = None
    """Part size in bytes"""

    parts: Optional[List[str]] = None
    """Presigned PUT URLs in order, one per part"""

    session_id: Optional[str] = None
    """Session UUID; required for the complete call"""
