# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["PagePaginationMeta", "SyncPagePagination", "AsyncPagePagination"]

_T = TypeVar("_T")


class PagePaginationMeta(BaseModel):
    has_next: Optional[bool] = FieldInfo(alias="hasNext", default=None)

    page: Optional[int] = None


class SyncPagePagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    files: List[_T]
    meta: Optional[PagePaginationMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        files = self.files
        if not files:
            return []
        return files

    @override
    def has_next_page(self) -> bool:
        has_next = None
        if self.meta is not None:
            if self.meta.has_next is not None:
                has_next = self.meta.has_next
        if has_next is not None and has_next is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page is not None:
                current_page = self.meta.page
        if current_page is None:
            current_page = 1

        return PageInfo(params={"page": current_page + 1})


class AsyncPagePagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    files: List[_T]
    meta: Optional[PagePaginationMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        files = self.files
        if not files:
            return []
        return files

    @override
    def has_next_page(self) -> bool:
        has_next = None
        if self.meta is not None:
            if self.meta.has_next is not None:
                has_next = self.meta.has_next
        if has_next is not None and has_next is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page is not None:
                current_page = self.meta.page
        if current_page is None:
            current_page = 1

        return PageInfo(params={"page": current_page + 1})
