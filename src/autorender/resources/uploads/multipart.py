# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Dict

import httpx

from ..._files import read_file_content, async_read_file_content
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    BinaryTypes,
    FileContent,
    SequenceNotStr,
    AsyncBinaryTypes,
    omit,
    not_given,
)
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.upload import Upload
from ...types.uploads import multipart_start_params, multipart_complete_params
from ...types.uploads.session import Session

__all__ = ["MultipartResource", "AsyncMultipartResource"]


class MultipartResource(SyncAPIResource):
    """Large file uploads via multipart"""

    @cached_property
    def with_raw_response(self) -> MultipartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return MultipartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultipartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
        """
        return MultipartResourceWithStreamingResponse(self)

    def complete(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """Finalize a multipart upload after all parts have been uploaded.

        Assembles the
        parts and creates the file record.

        Args:
          session_id: Session ID from POST /api/v1/multipart/start

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/multipart/complete",
            body=maybe_transform({"session_id": session_id}, multipart_complete_params.MultipartCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Upload,
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
        tags: SequenceNotStr[str] | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """Initiate a multipart upload session for large files.

        Returns presigned PUT URLs
        for each part. Upload each part to its URL in order, then call POST
        /api/v1/multipart/complete.

        Args:
          file_name: Original filename (e.g., big-video.mp4)

          format: MIME type (e.g., video/mp4, image/jpeg)

          size: Total file size in bytes

          folder: Destination folder path

          ttl_seconds: Presigned URL lifetime in seconds

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
                multipart_start_params.MultipartStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def upload_part(
        self,
        body: FileContent | BinaryTypes,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Upload a single part using one of the presigned URLs from POST
        /api/v1/multipart/start. Send raw bytes directly — do not include the AutoRender
        Authorization header, as auth is embedded in the presigned URL.

        Args:
          body: One multipart chunk uploaded to a presigned URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return self._put(
            "/api/v1/multipart/parts",
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMultipartResource(AsyncAPIResource):
    """Large file uploads via multipart"""

    @cached_property
    def with_raw_response(self) -> AsyncMultipartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMultipartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultipartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
        """
        return AsyncMultipartResourceWithStreamingResponse(self)

    async def complete(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """Finalize a multipart upload after all parts have been uploaded.

        Assembles the
        parts and creates the file record.

        Args:
          session_id: Session ID from POST /api/v1/multipart/start

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/multipart/complete",
            body=await async_maybe_transform(
                {"session_id": session_id}, multipart_complete_params.MultipartCompleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Upload,
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
        tags: SequenceNotStr[str] | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """Initiate a multipart upload session for large files.

        Returns presigned PUT URLs
        for each part. Upload each part to its URL in order, then call POST
        /api/v1/multipart/complete.

        Args:
          file_name: Original filename (e.g., big-video.mp4)

          format: MIME type (e.g., video/mp4, image/jpeg)

          size: Total file size in bytes

          folder: Destination folder path

          ttl_seconds: Presigned URL lifetime in seconds

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
                multipart_start_params.MultipartStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def upload_part(
        self,
        body: FileContent | AsyncBinaryTypes,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Upload a single part using one of the presigned URLs from POST
        /api/v1/multipart/start. Send raw bytes directly — do not include the AutoRender
        Authorization header, as auth is embedded in the presigned URL.

        Args:
          body: One multipart chunk uploaded to a presigned URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return await self._put(
            "/api/v1/multipart/parts",
            content=await async_read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MultipartResourceWithRawResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

        self.complete = to_raw_response_wrapper(
            multipart.complete,
        )
        self.start = to_raw_response_wrapper(
            multipart.start,
        )
        self.upload_part = to_raw_response_wrapper(
            multipart.upload_part,
        )


class AsyncMultipartResourceWithRawResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

        self.complete = async_to_raw_response_wrapper(
            multipart.complete,
        )
        self.start = async_to_raw_response_wrapper(
            multipart.start,
        )
        self.upload_part = async_to_raw_response_wrapper(
            multipart.upload_part,
        )


class MultipartResourceWithStreamingResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

        self.complete = to_streamed_response_wrapper(
            multipart.complete,
        )
        self.start = to_streamed_response_wrapper(
            multipart.start,
        )
        self.upload_part = to_streamed_response_wrapper(
            multipart.upload_part,
        )


class AsyncMultipartResourceWithStreamingResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

        self.complete = async_to_streamed_response_wrapper(
            multipart.complete,
        )
        self.start = async_to_streamed_response_wrapper(
            multipart.start,
        )
        self.upload_part = async_to_streamed_response_wrapper(
            multipart.upload_part,
        )
