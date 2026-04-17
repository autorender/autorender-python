# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .upload_data import UploadData

__all__ = ["Upload"]


class Upload(BaseModel):
    data: UploadData

    success: bool
