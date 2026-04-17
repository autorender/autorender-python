# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    add_tags: SequenceNotStr[str]
    """Tags to add"""

    metadata: Dict[str, object]
    """Metadata to merge"""

    remove_tags: SequenceNotStr[str]
    """Tags to remove"""
