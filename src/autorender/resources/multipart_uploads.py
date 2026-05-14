# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union

import httpx

from ..types import multipart_upload_start_params, multipart_upload_complete_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.multipart_upload_start_response import MultipartUploadStartResponse
from ..types.multipart_upload_complete_response import MultipartUploadCompleteResponse

__all__ = ["MultipartUploadsResource", "AsyncMultipartUploadsResource"]


class MultipartUploadsResource(SyncAPIResource):
    """Upload endpoints (API key required)"""

    @cached_property
    def with_raw_response(self) -> MultipartUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return MultipartUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultipartUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
        """
        return MultipartUploadsResourceWithStreamingResponse(self)

    def complete(
        self,
        *,
        session_id: str,
        uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartUploadCompleteResponse:
        """
        Finalise a multipart upload session and return the stored file record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/multipart/complete",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "uuid": uuid,
                },
                multipart_upload_complete_params.MultipartUploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartUploadCompleteResponse,
        )

    def start(
        self,
        *,
        file_name: str,
        format: str,
        size: int,
        custom_id: str | Omit = omit,
        folder: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        random_prefix: bool | Omit = omit,
        tags: Union[SequenceNotStr[str], str] | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartUploadStartResponse:
        """
        Initialise a multipart upload session and receive pre-signed part URLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/multipart/start",
            body=maybe_transform(
                {
                    "file_name": file_name,
                    "format": format,
                    "size": size,
                    "custom_id": custom_id,
                    "folder": folder,
                    "metadata": metadata,
                    "random_prefix": random_prefix,
                    "tags": tags,
                    "ttl_seconds": ttl_seconds,
                },
                multipart_upload_start_params.MultipartUploadStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartUploadStartResponse,
        )


class AsyncMultipartUploadsResource(AsyncAPIResource):
    """Upload endpoints (API key required)"""

    @cached_property
    def with_raw_response(self) -> AsyncMultipartUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMultipartUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultipartUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
        """
        return AsyncMultipartUploadsResourceWithStreamingResponse(self)

    async def complete(
        self,
        *,
        session_id: str,
        uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartUploadCompleteResponse:
        """
        Finalise a multipart upload session and return the stored file record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/multipart/complete",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "uuid": uuid,
                },
                multipart_upload_complete_params.MultipartUploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartUploadCompleteResponse,
        )

    async def start(
        self,
        *,
        file_name: str,
        format: str,
        size: int,
        custom_id: str | Omit = omit,
        folder: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        random_prefix: bool | Omit = omit,
        tags: Union[SequenceNotStr[str], str] | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartUploadStartResponse:
        """
        Initialise a multipart upload session and receive pre-signed part URLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/multipart/start",
            body=await async_maybe_transform(
                {
                    "file_name": file_name,
                    "format": format,
                    "size": size,
                    "custom_id": custom_id,
                    "folder": folder,
                    "metadata": metadata,
                    "random_prefix": random_prefix,
                    "tags": tags,
                    "ttl_seconds": ttl_seconds,
                },
                multipart_upload_start_params.MultipartUploadStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartUploadStartResponse,
        )


class MultipartUploadsResourceWithRawResponse:
    def __init__(self, multipart_uploads: MultipartUploadsResource) -> None:
        self._multipart_uploads = multipart_uploads

        self.complete = to_raw_response_wrapper(
            multipart_uploads.complete,
        )
        self.start = to_raw_response_wrapper(
            multipart_uploads.start,
        )


class AsyncMultipartUploadsResourceWithRawResponse:
    def __init__(self, multipart_uploads: AsyncMultipartUploadsResource) -> None:
        self._multipart_uploads = multipart_uploads

        self.complete = async_to_raw_response_wrapper(
            multipart_uploads.complete,
        )
        self.start = async_to_raw_response_wrapper(
            multipart_uploads.start,
        )


class MultipartUploadsResourceWithStreamingResponse:
    def __init__(self, multipart_uploads: MultipartUploadsResource) -> None:
        self._multipart_uploads = multipart_uploads

        self.complete = to_streamed_response_wrapper(
            multipart_uploads.complete,
        )
        self.start = to_streamed_response_wrapper(
            multipart_uploads.start,
        )


class AsyncMultipartUploadsResourceWithStreamingResponse:
    def __init__(self, multipart_uploads: AsyncMultipartUploadsResource) -> None:
        self._multipart_uploads = multipart_uploads

        self.complete = async_to_streamed_response_wrapper(
            multipart_uploads.complete,
        )
        self.start = async_to_streamed_response_wrapper(
            multipart_uploads.start,
        )
