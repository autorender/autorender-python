# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from autorender import Autorender, AsyncAutorender
from tests.utils import assert_matches_type
from autorender.types import (
    MultipartUploadStartResponse,
    MultipartUploadCompleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMultipartUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_complete(self, client: Autorender) -> None:
        multipart_upload = client.multipart_uploads.complete(
            session_id="x",
        )
        assert_matches_type(MultipartUploadCompleteResponse, multipart_upload, path=["response"])

    @parametrize
    def test_method_complete_with_all_params(self, client: Autorender) -> None:
        multipart_upload = client.multipart_uploads.complete(
            session_id="x",
            uuid="uuid",
        )
        assert_matches_type(MultipartUploadCompleteResponse, multipart_upload, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Autorender) -> None:
        response = client.multipart_uploads.with_raw_response.complete(
            session_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart_upload = response.parse()
        assert_matches_type(MultipartUploadCompleteResponse, multipart_upload, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Autorender) -> None:
        with client.multipart_uploads.with_streaming_response.complete(
            session_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart_upload = response.parse()
            assert_matches_type(MultipartUploadCompleteResponse, multipart_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: Autorender) -> None:
        multipart_upload = client.multipart_uploads.start(
            file_name="x",
            format="x",
            size=1,
        )
        assert_matches_type(MultipartUploadStartResponse, multipart_upload, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Autorender) -> None:
        multipart_upload = client.multipart_uploads.start(
            file_name="x",
            format="x",
            size=1,
            custom_id="custom_id",
            folder="folder",
            metadata={"foo": "bar"},
            random_prefix=True,
            tags=["string"],
            ttl_seconds=1,
        )
        assert_matches_type(MultipartUploadStartResponse, multipart_upload, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Autorender) -> None:
        response = client.multipart_uploads.with_raw_response.start(
            file_name="x",
            format="x",
            size=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart_upload = response.parse()
        assert_matches_type(MultipartUploadStartResponse, multipart_upload, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Autorender) -> None:
        with client.multipart_uploads.with_streaming_response.start(
            file_name="x",
            format="x",
            size=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart_upload = response.parse()
            assert_matches_type(MultipartUploadStartResponse, multipart_upload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMultipartUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_complete(self, async_client: AsyncAutorender) -> None:
        multipart_upload = await async_client.multipart_uploads.complete(
            session_id="x",
        )
        assert_matches_type(MultipartUploadCompleteResponse, multipart_upload, path=["response"])

    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncAutorender) -> None:
        multipart_upload = await async_client.multipart_uploads.complete(
            session_id="x",
            uuid="uuid",
        )
        assert_matches_type(MultipartUploadCompleteResponse, multipart_upload, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncAutorender) -> None:
        response = await async_client.multipart_uploads.with_raw_response.complete(
            session_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart_upload = await response.parse()
        assert_matches_type(MultipartUploadCompleteResponse, multipart_upload, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncAutorender) -> None:
        async with async_client.multipart_uploads.with_streaming_response.complete(
            session_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart_upload = await response.parse()
            assert_matches_type(MultipartUploadCompleteResponse, multipart_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncAutorender) -> None:
        multipart_upload = await async_client.multipart_uploads.start(
            file_name="x",
            format="x",
            size=1,
        )
        assert_matches_type(MultipartUploadStartResponse, multipart_upload, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncAutorender) -> None:
        multipart_upload = await async_client.multipart_uploads.start(
            file_name="x",
            format="x",
            size=1,
            custom_id="custom_id",
            folder="folder",
            metadata={"foo": "bar"},
            random_prefix=True,
            tags=["string"],
            ttl_seconds=1,
        )
        assert_matches_type(MultipartUploadStartResponse, multipart_upload, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncAutorender) -> None:
        response = await async_client.multipart_uploads.with_raw_response.start(
            file_name="x",
            format="x",
            size=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart_upload = await response.parse()
        assert_matches_type(MultipartUploadStartResponse, multipart_upload, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncAutorender) -> None:
        async with async_client.multipart_uploads.with_streaming_response.start(
            file_name="x",
            format="x",
            size=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart_upload = await response.parse()
            assert_matches_type(MultipartUploadStartResponse, multipart_upload, path=["response"])

        assert cast(Any, response.is_closed) is True
