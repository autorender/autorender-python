# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import file_list_params, file_rename_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.file_object import FileObject
from ..types.file_list_response import FileListResponse
from ..types.file_delete_response import FileDeleteResponse
from ..types.file_rename_response import FileRenameResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
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
    ) -> FileObject:
        """
        Retrieve detailed information about a file by numeric file id (`file_no`).

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
            cast_to=FileObject,
        )

    def list(
        self,
        *,
        folder_no: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        path: str | Omit = omit,
        sort_field: Literal["file_size", "name", "created_at", "updated_at"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """Paginated list of files in the workspace.

        Filter by folder, sort by field and
        order, and page through results.

        Args:
          folder_no: Restrict results to files in this folder (folder number)

          limit: Items per page

          name: Filter by filename (partial match, if supported)

          page: Page number (1-based)

          path: Filter by path prefix (if supported)

          sort_field: Field to sort by

          sort_order: Sort direction

          tags: Comma-separated tags (if supported)

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
                        "sort_field": sort_field,
                        "sort_order": sort_order,
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
    ) -> FileDeleteResponse:
        """Permanently delete a file.

        No request body is required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_no:
            raise ValueError(f"Expected a non-empty value for `file_no` but received {file_no!r}")
        return self._delete(
            path_template("/api/v1/files/{file_no}", file_no=file_no),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDeleteResponse,
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
        """Rename a file.

        The API may preserve or normalize the file extension (e.g. `demo`
        → `demo.png`).

        Args:
          name: New base name; extension may be applied by the server

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
    ) -> FileObject:
        """
        Retrieve detailed information about a file by numeric file id (`file_no`).

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
            cast_to=FileObject,
        )

    async def list(
        self,
        *,
        folder_no: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        path: str | Omit = omit,
        sort_field: Literal["file_size", "name", "created_at", "updated_at"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """Paginated list of files in the workspace.

        Filter by folder, sort by field and
        order, and page through results.

        Args:
          folder_no: Restrict results to files in this folder (folder number)

          limit: Items per page

          name: Filter by filename (partial match, if supported)

          page: Page number (1-based)

          path: Filter by path prefix (if supported)

          sort_field: Field to sort by

          sort_order: Sort direction

          tags: Comma-separated tags (if supported)

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
                        "sort_field": sort_field,
                        "sort_order": sort_order,
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
    ) -> FileDeleteResponse:
        """Permanently delete a file.

        No request body is required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_no:
            raise ValueError(f"Expected a non-empty value for `file_no` but received {file_no!r}")
        return await self._delete(
            path_template("/api/v1/files/{file_no}", file_no=file_no),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDeleteResponse,
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
        """Rename a file.

        The API may preserve or normalize the file extension (e.g. `demo`
        → `demo.png`).

        Args:
          name: New base name; extension may be applied by the server

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
