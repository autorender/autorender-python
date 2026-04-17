# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import upload_create_params, upload_create_from_url_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.upload import Upload

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
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

          folder: Folder path where the file will be stored (e.g., uploads/my-folder)

          metadata: JSON string for custom metadata (e.g., {"key": "value"})

          random_prefix: Set to "true" to add a random suffix to filename

          tags: Comma-separated tags (e.g., tag1,tag2,tag3)

          transform: Image transformation string (e.g., w_800,h_600,q_90)

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
        Fetch a file from a remote URL and store it in your AutoRender workspace.

        Args:
          remote_url: The HTTP or HTTPS URL of the image to download

          custom_id: Custom identifier for tracking the upload

          folder: Folder path where the file should be stored

          metadata: JSON string containing custom metadata object

          random_prefix: Set to 'true' to generate a random suffix for the filename

          tags: Comma-separated list of tags to apply to the file

          transform: Transformation string to apply during upload (e.g., w_800,h_600,c_crop)

          webhook_url: URL to receive webhook notification when upload completes

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


class AsyncUploadsResource(AsyncAPIResource):
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

          folder: Folder path where the file will be stored (e.g., uploads/my-folder)

          metadata: JSON string for custom metadata (e.g., {"key": "value"})

          random_prefix: Set to "true" to add a random suffix to filename

          tags: Comma-separated tags (e.g., tag1,tag2,tag3)

          transform: Image transformation string (e.g., w_800,h_600,q_90)

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
        Fetch a file from a remote URL and store it in your AutoRender workspace.

        Args:
          remote_url: The HTTP or HTTPS URL of the image to download

          custom_id: Custom identifier for tracking the upload

          folder: Folder path where the file should be stored

          metadata: JSON string containing custom metadata object

          random_prefix: Set to 'true' to generate a random suffix for the filename

          tags: Comma-separated list of tags to apply to the file

          transform: Transformation string to apply during upload (e.g., w_800,h_600,c_crop)

          webhook_url: URL to receive webhook notification when upload completes

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
