# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Dict, Mapping, cast

import httpx

from ...types import (
    upload_create_params,
    upload_generate_token_params,
    upload_create_from_url_params,
)
from ..._files import read_file_content, async_read_file_content
from ..._types import (
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
from ..._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from .multipart import (
    MultipartResource,
    AsyncMultipartResource,
    MultipartResourceWithRawResponse,
    AsyncMultipartResourceWithRawResponse,
    MultipartResourceWithStreamingResponse,
    AsyncMultipartResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.upload import Upload
from ...types.upload_generate_token_response import UploadGenerateTokenResponse

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    """Upload files to your workspace"""

    @cached_property
    def multipart(self) -> MultipartResource:
        """Large file uploads via multipart"""
        return MultipartResource(self._client)

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
    ) -> Upload:
        """
        Upload a file to your AutoRender workspace with optional transformations, tags,
        and folder organization

        Args:
          file: The file to upload (binary data)

          file_name: File name for the uploaded file (e.g., my-image.jpg)

          custom_id: Custom identifier for the file

          folder: Folder path where the file will be stored (e.g., products/sku123)

          metadata: JSON string for custom metadata (e.g., {"productId": "123"})

          random_prefix: Set to "true" to add a random suffix to the filename

          tags: Comma-separated tags (e.g., product,thumbnail)

          transform: Image transformation string (e.g., w_800,h_600,q_90)

          webhook_url: URL to receive a webhook notification when the upload completes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
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
            }
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
            cast_to=Upload,
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
        transform: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """
        Download a file from a remote HTTP/HTTPS URL and store it in your AutoRender
        workspace. Supports optional transformations and metadata.

        Args:
          remote_url: HTTP or HTTPS URL of the file to download

          custom_id: Custom identifier for the file

          file_name: Override filename. Defaults to filename from URL.

          folder: Destination folder path

          metadata: JSON string of custom metadata

          random_prefix: Set to "true" to add a random suffix

          tags: Comma-separated tags

          transform: Transformation string applied after download

          webhook_url: URL to receive a webhook notification on completion

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
                    "transform": transform,
                    "webhook_url": webhook_url,
                },
                upload_create_from_url_params.UploadCreateFromURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Upload,
        )

    def create_with_token(
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
    ) -> Upload:
        """
        Upload a file directly from a browser or mobile client using a token from POST
        /api/v1/generate-token. Send raw file bytes as the request body. Filename and
        upload policy are taken from the token.

        Args:
          body: Raw file bytes. Any file type accepted.

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
            cast_to=Upload,
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
        transform: str | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadGenerateTokenResponse:
        """
        Generate a short-lived signed token that allows a browser or mobile client to
        upload directly to AutoRender without exposing your secret API key. The token
        encodes upload policy (folder, tags, transforms, file size limit). No file
        record is created until the token is used.

        Args:
          file_name: Filename for the upload (e.g., avatar.jpg)

          allow_override: Which policy fields the uploader may override

          custom_id: Custom identifier for the file

          folder: Destination folder path

          max_file_size: Maximum allowed file size in bytes

          metadata: Custom metadata to attach

          random_prefix: Add a random prefix to the filename

          tags: Tags to apply to the uploaded file

          transform: Transformation string applied on upload

          ttl_seconds: Token lifetime in seconds (default: 300)

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
                    "transform": transform,
                    "ttl_seconds": ttl_seconds,
                },
                upload_generate_token_params.UploadGenerateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadGenerateTokenResponse,
        )


class AsyncUploadsResource(AsyncAPIResource):
    """Upload files to your workspace"""

    @cached_property
    def multipart(self) -> AsyncMultipartResource:
        """Large file uploads via multipart"""
        return AsyncMultipartResource(self._client)

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
    ) -> Upload:
        """
        Upload a file to your AutoRender workspace with optional transformations, tags,
        and folder organization

        Args:
          file: The file to upload (binary data)

          file_name: File name for the uploaded file (e.g., my-image.jpg)

          custom_id: Custom identifier for the file

          folder: Folder path where the file will be stored (e.g., products/sku123)

          metadata: JSON string for custom metadata (e.g., {"productId": "123"})

          random_prefix: Set to "true" to add a random suffix to the filename

          tags: Comma-separated tags (e.g., product,thumbnail)

          transform: Image transformation string (e.g., w_800,h_600,q_90)

          webhook_url: URL to receive a webhook notification when the upload completes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
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
            }
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
            cast_to=Upload,
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
        transform: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """
        Download a file from a remote HTTP/HTTPS URL and store it in your AutoRender
        workspace. Supports optional transformations and metadata.

        Args:
          remote_url: HTTP or HTTPS URL of the file to download

          custom_id: Custom identifier for the file

          file_name: Override filename. Defaults to filename from URL.

          folder: Destination folder path

          metadata: JSON string of custom metadata

          random_prefix: Set to "true" to add a random suffix

          tags: Comma-separated tags

          transform: Transformation string applied after download

          webhook_url: URL to receive a webhook notification on completion

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
                    "transform": transform,
                    "webhook_url": webhook_url,
                },
                upload_create_from_url_params.UploadCreateFromURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Upload,
        )

    async def create_with_token(
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
    ) -> Upload:
        """
        Upload a file directly from a browser or mobile client using a token from POST
        /api/v1/generate-token. Send raw file bytes as the request body. Filename and
        upload policy are taken from the token.

        Args:
          body: Raw file bytes. Any file type accepted.

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
            cast_to=Upload,
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
        transform: str | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadGenerateTokenResponse:
        """
        Generate a short-lived signed token that allows a browser or mobile client to
        upload directly to AutoRender without exposing your secret API key. The token
        encodes upload policy (folder, tags, transforms, file size limit). No file
        record is created until the token is used.

        Args:
          file_name: Filename for the upload (e.g., avatar.jpg)

          allow_override: Which policy fields the uploader may override

          custom_id: Custom identifier for the file

          folder: Destination folder path

          max_file_size: Maximum allowed file size in bytes

          metadata: Custom metadata to attach

          random_prefix: Add a random prefix to the filename

          tags: Tags to apply to the uploaded file

          transform: Transformation string applied on upload

          ttl_seconds: Token lifetime in seconds (default: 300)

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
                    "transform": transform,
                    "ttl_seconds": ttl_seconds,
                },
                upload_generate_token_params.UploadGenerateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadGenerateTokenResponse,
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
        self.create_with_token = to_raw_response_wrapper(
            uploads.create_with_token,
        )
        self.generate_token = to_raw_response_wrapper(
            uploads.generate_token,
        )

    @cached_property
    def multipart(self) -> MultipartResourceWithRawResponse:
        """Large file uploads via multipart"""
        return MultipartResourceWithRawResponse(self._uploads.multipart)


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_raw_response_wrapper(
            uploads.create,
        )
        self.create_from_url = async_to_raw_response_wrapper(
            uploads.create_from_url,
        )
        self.create_with_token = async_to_raw_response_wrapper(
            uploads.create_with_token,
        )
        self.generate_token = async_to_raw_response_wrapper(
            uploads.generate_token,
        )

    @cached_property
    def multipart(self) -> AsyncMultipartResourceWithRawResponse:
        """Large file uploads via multipart"""
        return AsyncMultipartResourceWithRawResponse(self._uploads.multipart)


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_streamed_response_wrapper(
            uploads.create,
        )
        self.create_from_url = to_streamed_response_wrapper(
            uploads.create_from_url,
        )
        self.create_with_token = to_streamed_response_wrapper(
            uploads.create_with_token,
        )
        self.generate_token = to_streamed_response_wrapper(
            uploads.generate_token,
        )

    @cached_property
    def multipart(self) -> MultipartResourceWithStreamingResponse:
        """Large file uploads via multipart"""
        return MultipartResourceWithStreamingResponse(self._uploads.multipart)


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_streamed_response_wrapper(
            uploads.create,
        )
        self.create_from_url = async_to_streamed_response_wrapper(
            uploads.create_from_url,
        )
        self.create_with_token = async_to_streamed_response_wrapper(
            uploads.create_with_token,
        )
        self.generate_token = async_to_streamed_response_wrapper(
            uploads.generate_token,
        )

    @cached_property
    def multipart(self) -> AsyncMultipartResourceWithStreamingResponse:
        """Large file uploads via multipart"""
        return AsyncMultipartResourceWithStreamingResponse(self._uploads.multipart)
