# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Dict, Mapping, cast

import httpx

from ..types import (
    upload_create_params,
    upload_generate_token_params,
    upload_create_from_url_params,
)
from .._files import read_file_content, deepcopy_with_paths, async_read_file_content
from .._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    BinaryTypes,
    FileContent,
    SequenceNotStr,
    AsyncBinaryTypes,
    omit,
    not_given,
)
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
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
from ..types.upload_generate_token_response import UploadGenerateTokenResponse
from ..types.upload_create_from_url_response import UploadCreateFromURLResponse
from ..types.upload_upload_with_token_response import UploadUploadWithTokenResponse

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    """Upload endpoints (API key required)"""

    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
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
        tags: str | Omit = omit,
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

          tags: Comma-separated tags

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

    def generate_token(
        self,
        *,
        file_name: str,
        allow_override: upload_generate_token_params.AllowOverride | Omit = omit,
        custom_id: str | Omit = omit,
        folder: str | Omit = omit,
        max_file_size: int | Omit = omit,
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
    ) -> UploadGenerateTokenResponse:
        """Generate a short-lived token for direct browser uploads.

        No file is created at
        this stage.

        Args:
          file_name: File name for the uploaded file (e.g., avatar.jpg)

          folder: Destination folder path

          max_file_size: Max file size in bytes

          ttl_seconds: Token lifetime in seconds. Defaults to 300.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/generate-token",
            body=maybe_transform(
                {
                    "file_name": file_name,
                    "allow_override": allow_override,
                    "custom_id": custom_id,
                    "folder": folder,
                    "max_file_size": max_file_size,
                    "metadata": metadata,
                    "random_prefix": random_prefix,
                    "tags": tags,
                    "ttl_seconds": ttl_seconds,
                },
                upload_generate_token_params.UploadGenerateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadGenerateTokenResponse,
        )

    def upload_with_token(
        self,
        token: str,
        body: FileContent | BinaryTypes,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadUploadWithTokenResponse:
        """Upload a file directly from the browser using a token from /generate-token.

        Send
        the raw file as binary in the request body.

        Args:
          body: Raw file bytes. Accepts any file type (images, documents, videos, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            path_template("/api/v1/uploads/{token}", token=token),
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadUploadWithTokenResponse,
        )


class AsyncUploadsResource(AsyncAPIResource):
    """Upload endpoints (API key required)"""

    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/autorenderhq/autorender-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/autorenderhq/autorender-python#with_streaming_response
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
        tags: str | Omit = omit,
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

          tags: Comma-separated tags

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

    async def generate_token(
        self,
        *,
        file_name: str,
        allow_override: upload_generate_token_params.AllowOverride | Omit = omit,
        custom_id: str | Omit = omit,
        folder: str | Omit = omit,
        max_file_size: int | Omit = omit,
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
    ) -> UploadGenerateTokenResponse:
        """Generate a short-lived token for direct browser uploads.

        No file is created at
        this stage.

        Args:
          file_name: File name for the uploaded file (e.g., avatar.jpg)

          folder: Destination folder path

          max_file_size: Max file size in bytes

          ttl_seconds: Token lifetime in seconds. Defaults to 300.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/generate-token",
            body=await async_maybe_transform(
                {
                    "file_name": file_name,
                    "allow_override": allow_override,
                    "custom_id": custom_id,
                    "folder": folder,
                    "max_file_size": max_file_size,
                    "metadata": metadata,
                    "random_prefix": random_prefix,
                    "tags": tags,
                    "ttl_seconds": ttl_seconds,
                },
                upload_generate_token_params.UploadGenerateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadGenerateTokenResponse,
        )

    async def upload_with_token(
        self,
        token: str,
        body: FileContent | AsyncBinaryTypes,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadUploadWithTokenResponse:
        """Upload a file directly from the browser using a token from /generate-token.

        Send
        the raw file as binary in the request body.

        Args:
          body: Raw file bytes. Accepts any file type (images, documents, videos, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            path_template("/api/v1/uploads/{token}", token=token),
            content=await async_read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadUploadWithTokenResponse,
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
        self.generate_token = to_raw_response_wrapper(
            uploads.generate_token,
        )
        self.upload_with_token = to_raw_response_wrapper(
            uploads.upload_with_token,
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
        self.generate_token = async_to_raw_response_wrapper(
            uploads.generate_token,
        )
        self.upload_with_token = async_to_raw_response_wrapper(
            uploads.upload_with_token,
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
        self.generate_token = to_streamed_response_wrapper(
            uploads.generate_token,
        )
        self.upload_with_token = to_streamed_response_wrapper(
            uploads.upload_with_token,
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
        self.generate_token = async_to_streamed_response_wrapper(
            uploads.generate_token,
        )
        self.upload_with_token = async_to_streamed_response_wrapper(
            uploads.upload_with_token,
        )
