# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, cast

import httpx

from ..types import upload_create_params, upload_create_from_url_params
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.upload_create_response import UploadCreateResponse
from ..types.upload_create_from_url_response import UploadCreateFromURLResponse

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    """Upload endpoints (API key required)"""

    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorender/autorender-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorender/autorender-python#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        file_name: str,
        custom_id: str | Omit = omit,
        folder: str | Omit = omit,
        metadata: str | Omit = omit,
        random_prefix: str | Omit = omit,
        tags: str | Omit = omit,
        transform: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateResponse:
        """
        Upload a file from your backend server using multipart/form-data.

        Args:
          file: File to upload.

          file_name: File name (e.g. product.jpg)

          custom_id: Custom identifier

          folder: Optional folder path

          metadata: JSON string of metadata

          random_prefix: true/false to append random suffix

          tags: Comma-separated tags

          transform: Transform string (w_300,h_300,c_crop,...)

          webhook_url: URL to notify on success

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "file_name": file_name,
                "custom_id": custom_id,
                "folder": folder,
                "metadata": metadata,
                "random_prefix": random_prefix,
                "tags": tags,
                "transform": transform,
                "webhook_url": webhook_url,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/uploads",
            body=maybe_transform(body, upload_create_params.UploadCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateResponse,
        )

    def create_from_url(
        self,
        *,
        remote_url: str,
        custom_id: str | Omit = omit,
        file_name: str | Omit = omit,
        folder: str | Omit = omit,
        metadata: str | Omit = omit,
        random_prefix: str | Omit = omit,
        tags: Union[SequenceNotStr[str], str] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateFromURLResponse:
        """
        Download a file from a remote URL and store it in AutoRender.

        Args:
          remote_url: HTTP/HTTPS URL to fetch

          file_name: Override file name

          folder: Destination folder path

          metadata: JSON string of metadata object

          random_prefix: true/false to append random suffix

          tags: Tags array or comma-separated string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/uploads/remote",
            body=maybe_transform(
                {
                    "remote_url": remote_url,
                    "custom_id": custom_id,
                    "file_name": file_name,
                    "folder": folder,
                    "metadata": metadata,
                    "random_prefix": random_prefix,
                    "tags": tags,
                    "webhook_url": webhook_url,
                },
                upload_create_from_url_params.UploadCreateFromURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateFromURLResponse,
        )


class AsyncUploadsResource(AsyncAPIResource):
    """Upload endpoints (API key required)"""

    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorender/autorender-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorender/autorender-python#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        file_name: str,
        custom_id: str | Omit = omit,
        folder: str | Omit = omit,
        metadata: str | Omit = omit,
        random_prefix: str | Omit = omit,
        tags: str | Omit = omit,
        transform: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateResponse:
        """
        Upload a file from your backend server using multipart/form-data.

        Args:
          file: File to upload.

          file_name: File name (e.g. product.jpg)

          custom_id: Custom identifier

          folder: Optional folder path

          metadata: JSON string of metadata

          random_prefix: true/false to append random suffix

          tags: Comma-separated tags

          transform: Transform string (w_300,h_300,c_crop,...)

          webhook_url: URL to notify on success

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "file_name": file_name,
                "custom_id": custom_id,
                "folder": folder,
                "metadata": metadata,
                "random_prefix": random_prefix,
                "tags": tags,
                "transform": transform,
                "webhook_url": webhook_url,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/uploads",
            body=await async_maybe_transform(body, upload_create_params.UploadCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateResponse,
        )

    async def create_from_url(
        self,
        *,
        remote_url: str,
        custom_id: str | Omit = omit,
        file_name: str | Omit = omit,
        folder: str | Omit = omit,
        metadata: str | Omit = omit,
        random_prefix: str | Omit = omit,
        tags: Union[SequenceNotStr[str], str] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateFromURLResponse:
        """
        Download a file from a remote URL and store it in AutoRender.

        Args:
          remote_url: HTTP/HTTPS URL to fetch

          file_name: Override file name

          folder: Destination folder path

          metadata: JSON string of metadata object

          random_prefix: true/false to append random suffix

          tags: Tags array or comma-separated string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/uploads/remote",
            body=await async_maybe_transform(
                {
                    "remote_url": remote_url,
                    "custom_id": custom_id,
                    "file_name": file_name,
                    "folder": folder,
                    "metadata": metadata,
                    "random_prefix": random_prefix,
                    "tags": tags,
                    "webhook_url": webhook_url,
                },
                upload_create_from_url_params.UploadCreateFromURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateFromURLResponse,
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_raw_response_wrapper(
            uploads.create,
        )
        self.create_from_url = to_raw_response_wrapper(
            uploads.create_from_url,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_raw_response_wrapper(
            uploads.create,
        )
        self.create_from_url = async_to_raw_response_wrapper(
            uploads.create_from_url,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_streamed_response_wrapper(
            uploads.create,
        )
        self.create_from_url = to_streamed_response_wrapper(
            uploads.create_from_url,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_streamed_response_wrapper(
            uploads.create,
        )
        self.create_from_url = async_to_streamed_response_wrapper(
            uploads.create_from_url,
        )
