# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    add_tags: SequenceNotStr[str]
    """Tags to add to the existing set"""

    metadata: Dict[str, object]
    """Metadata to merge into existing metadata"""

    remove_tags: SequenceNotStr[str]
    """Tags to remove from the existing set"""
