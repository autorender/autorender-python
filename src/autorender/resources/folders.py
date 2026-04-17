# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import folder_list_params, folder_create_params, folder_rename_params
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
from ..types.folder import Folder
from ..types.folder_list_response import FolderListResponse
from ..types.folder_create_response import FolderCreateResponse
from ..types.folder_delete_response import FolderDeleteResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    """Manage folder structure"""

    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        parent_folder_no: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """Create a new folder.

        Optionally nest it under an existing folder by providing
        parent_folder_no.

        Args:
          name: Folder display name

          parent_folder_no: Parent folder number; omit for root level

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/folders",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_folder_no": parent_folder_no,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    def list(
        self,
        *,
        parent_folder_no: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """List folders in the workspace.

        Omit parent_folder_no to list root-level folders.

        Args:
          parent_folder_no: Return only direct children of this folder

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/folders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"parent_folder_no": parent_folder_no}, folder_list_params.FolderListParams),
            ),
            cast_to=FolderListResponse,
        )

    def delete(
        self,
        folder_no: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """
        Delete a folder by its folder number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_no:
            raise ValueError(f"Expected a non-empty value for `folder_no` but received {folder_no!r}")
        return self._delete(
            path_template("/api/v1/folders/{folder_no}", folder_no=folder_no),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )

    def rename(
        self,
        folder_no: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Rename a folder by its folder number.

        Args:
          name: New folder name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_no:
            raise ValueError(f"Expected a non-empty value for `folder_no` but received {folder_no!r}")
        return self._post(
            path_template("/api/v1/folders/rename/{folder_no}", folder_no=folder_no),
            body=maybe_transform({"name": name}, folder_rename_params.FolderRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )


class AsyncFoldersResource(AsyncAPIResource):
    """Manage folder structure"""

    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        parent_folder_no: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """Create a new folder.

        Optionally nest it under an existing folder by providing
        parent_folder_no.

        Args:
          name: Folder display name

          parent_folder_no: Parent folder number; omit for root level

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/folders",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_folder_no": parent_folder_no,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    async def list(
        self,
        *,
        parent_folder_no: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """List folders in the workspace.

        Omit parent_folder_no to list root-level folders.

        Args:
          parent_folder_no: Return only direct children of this folder

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/folders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"parent_folder_no": parent_folder_no}, folder_list_params.FolderListParams
                ),
            ),
            cast_to=FolderListResponse,
        )

    async def delete(
        self,
        folder_no: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """
        Delete a folder by its folder number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_no:
            raise ValueError(f"Expected a non-empty value for `folder_no` but received {folder_no!r}")
        return await self._delete(
            path_template("/api/v1/folders/{folder_no}", folder_no=folder_no),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )

    async def rename(
        self,
        folder_no: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Rename a folder by its folder number.

        Args:
          name: New folder name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_no:
            raise ValueError(f"Expected a non-empty value for `folder_no` but received {folder_no!r}")
        return await self._post(
            path_template("/api/v1/folders/rename/{folder_no}", folder_no=folder_no),
            body=await async_maybe_transform({"name": name}, folder_rename_params.FolderRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.list = to_raw_response_wrapper(
            folders.list,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )
        self.rename = to_raw_response_wrapper(
            folders.rename,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.list = async_to_raw_response_wrapper(
            folders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )
        self.rename = async_to_raw_response_wrapper(
            folders.rename,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.list = to_streamed_response_wrapper(
            folders.list,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )
        self.rename = to_streamed_response_wrapper(
            folders.rename,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.list = async_to_streamed_response_wrapper(
            folders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
        self.rename = async_to_streamed_response_wrapper(
            folders.rename,
        )
