# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from autorender import Autorender, AsyncAutorender
from tests.utils import assert_matches_type
from autorender.types import (
    UploadCreateResponse,
    UploadCreateFromURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Autorender) -> None:
        upload = client.uploads.create(
            file=b"Example data",
            file_name="product.jpg",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Autorender) -> None:
        upload = client.uploads.create(
            file=b"Example data",
            file_name="product.jpg",
            custom_id="sku123",
            folder="products/sku123",
            metadata='{"productId":"123"}',
            random_prefix="random_prefix",
            tags="product,thumbnail",
            transform="transform",
            webhook_url="webhook_url",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Autorender) -> None:
        response = client.uploads.with_raw_response.create(
            file=b"Example data",
            file_name="product.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Autorender) -> None:
        with client.uploads.with_streaming_response.create(
            file=b"Example data",
            file_name="product.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadCreateResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_from_url(self, client: Autorender) -> None:
        upload = client.uploads.create_from_url(
            remote_url="https://example.com",
        )
        assert_matches_type(UploadCreateFromURLResponse, upload, path=["response"])

    @parametrize
    def test_method_create_from_url_with_all_params(self, client: Autorender) -> None:
        upload = client.uploads.create_from_url(
            remote_url="https://example.com",
            custom_id="custom_id",
            file_name="file_name",
            folder="folder",
            metadata="metadata",
            random_prefix="random_prefix",
            tags="tags",
            webhook_url="https://example.com",
        )
        assert_matches_type(UploadCreateFromURLResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_create_from_url(self, client: Autorender) -> None:
        response = client.uploads.with_raw_response.create_from_url(
            remote_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadCreateFromURLResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_create_from_url(self, client: Autorender) -> None:
        with client.uploads.with_streaming_response.create_from_url(
            remote_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadCreateFromURLResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create(
            file=b"Example data",
            file_name="product.jpg",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create(
            file=b"Example data",
            file_name="product.jpg",
            custom_id="sku123",
            folder="products/sku123",
            metadata='{"productId":"123"}',
            random_prefix="random_prefix",
            tags="product,thumbnail",
            transform="transform",
            webhook_url="webhook_url",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.with_raw_response.create(
            file=b"Example data",
            file_name="product.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.with_streaming_response.create(
            file=b"Example data",
            file_name="product.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadCreateResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_from_url(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create_from_url(
            remote_url="https://example.com",
        )
        assert_matches_type(UploadCreateFromURLResponse, upload, path=["response"])

    @parametrize
    async def test_method_create_from_url_with_all_params(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create_from_url(
            remote_url="https://example.com",
            custom_id="custom_id",
            file_name="file_name",
            folder="folder",
            metadata="metadata",
            random_prefix="random_prefix",
            tags="tags",
            webhook_url="https://example.com",
        )
        assert_matches_type(UploadCreateFromURLResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_create_from_url(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.with_raw_response.create_from_url(
            remote_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadCreateFromURLResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_create_from_url(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.with_streaming_response.create_from_url(
            remote_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadCreateFromURLResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True
