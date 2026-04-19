# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import file_list_params, file_rename_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.file_list_response import FileListResponse
from ..types.file_rename_response import FileRenameResponse
from ..types.file_retrieve_response import FileRetrieveResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    """File management endpoints (API key required)"""

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        file_no: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRetrieveResponse:
        """
        Get file details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_no:
            raise ValueError(f"Expected a non-empty value for `file_no` but received {file_no!r}")
        return self._get(
            path_template("/api/v1/files/{file_no}", file_no=file_no),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRetrieveResponse,
        )

    def list(
        self,
        *,
        folder_no: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        path: str | Omit = omit,
        sort: Literal["created_at_asc", "created_at_desc", "size_asc", "size_desc"] | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List/search files with pagination, filtering, and sorting.

        Args:
          folder_no: Exact folder number

          name: Partial name match (case-insensitive)

          path: Folder prefix (e.g. products/sku123/)

          tags: Comma-separated tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "folder_no": folder_no,
                        "limit": limit,
                        "name": name,
                        "page": page,
                        "path": path,
                        "sort": sort,
                        "tags": tags,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    def delete(
        self,
        file_no: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_no:
            raise ValueError(f"Expected a non-empty value for `file_no` but received {file_no!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/files/{file_no}", file_no=file_no),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def rename(
        self,
        file_no: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRenameResponse:
        """
        Rename file

        Args:
          name: New file name without extension or path separators

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_no:
            raise ValueError(f"Expected a non-empty value for `file_no` but received {file_no!r}")
        return self._patch(
            path_template("/api/v1/files/{file_no}/rename", file_no=file_no),
            body=maybe_transform({"name": name}, file_rename_params.FileRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRenameResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    """File management endpoints (API key required)"""

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        file_no: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRetrieveResponse:
        """
        Get file details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_no:
            raise ValueError(f"Expected a non-empty value for `file_no` but received {file_no!r}")
        return await self._get(
            path_template("/api/v1/files/{file_no}", file_no=file_no),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRetrieveResponse,
        )

    async def list(
        self,
        *,
        folder_no: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        path: str | Omit = omit,
        sort: Literal["created_at_asc", "created_at_desc", "size_asc", "size_desc"] | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List/search files with pagination, filtering, and sorting.

        Args:
          folder_no: Exact folder number

          name: Partial name match (case-insensitive)

          path: Folder prefix (e.g. products/sku123/)

          tags: Comma-separated tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "folder_no": folder_no,
                        "limit": limit,
                        "name": name,
                        "page": page,
                        "path": path,
                        "sort": sort,
                        "tags": tags,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    async def delete(
        self,
        file_no: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_no:
            raise ValueError(f"Expected a non-empty value for `file_no` but received {file_no!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/files/{file_no}", file_no=file_no),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def rename(
        self,
        file_no: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRenameResponse:
        """
        Rename file

        Args:
          name: New file name without extension or path separators

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_no:
            raise ValueError(f"Expected a non-empty value for `file_no` but received {file_no!r}")
        return await self._patch(
            path_template("/api/v1/files/{file_no}/rename", file_no=file_no),
            body=await async_maybe_transform({"name": name}, file_rename_params.FileRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRenameResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = to_raw_response_wrapper(
            files.retrieve,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.rename = to_raw_response_wrapper(
            files.rename,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = async_to_raw_response_wrapper(
            files.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.rename = async_to_raw_response_wrapper(
            files.rename,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = to_streamed_response_wrapper(
            files.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.rename = to_streamed_response_wrapper(
            files.rename,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = async_to_streamed_response_wrapper(
            files.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.rename = async_to_streamed_response_wrapper(
            files.rename,
        )
