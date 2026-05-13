# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPagePagination", "AsyncPagePagination"]

_T = TypeVar("_T")


class SyncPagePagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    current_page: Optional[int] = None
    has_next: Optional[bool] = Field(None, alias="has_next_page")
    total_results: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        items = self._get_page_items()
        if not items:
            return False
        if self.has_next is not None:
            return self.has_next
        return self.next_page_info() is not None

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.current_page
        if current_page is None:
            current_page = 1

        return PageInfo(params={"page": current_page + 1})


class AsyncPagePagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    current_page: Optional[int] = None
    has_next: Optional[bool] = Field(None, alias="has_next_page")
    total_results: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        items = self._get_page_items()
        if not items:
            return False
        if self.has_next is not None:
            return self.has_next
        return self.next_page_info() is not None

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.current_page
        if current_page is None:
            current_page = 1

        return PageInfo(params={"page": current_page + 1})
