# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from autorender import Autorender, AsyncAutorender
from tests.utils import assert_matches_type
from autorender.types import (
    Upload,
    UploadGenerateTokenResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Autorender) -> None:
        upload = client.uploads.create(
            file=b"Example data",
            file_name="file_name",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Autorender) -> None:
        upload = client.uploads.create(
            file=b"Example data",
            file_name="file_name",
            custom_id="custom_id",
            folder="folder",
            metadata="metadata",
            random_prefix="random_prefix",
            tags="tags",
            transform="transform",
            webhook_url="webhook_url",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Autorender) -> None:
        response = client.uploads.with_raw_response.create(
            file=b"Example data",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Autorender) -> None:
        with client.uploads.with_streaming_response.create(
            file=b"Example data",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_from_url(self, client: Autorender) -> None:
        upload = client.uploads.create_from_url(
            remote_url="remote_url",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_method_create_from_url_with_all_params(self, client: Autorender) -> None:
        upload = client.uploads.create_from_url(
            remote_url="remote_url",
            custom_id="custom_id",
            file_name="file_name",
            folder="folder",
            metadata="metadata",
            random_prefix="random_prefix",
            tags="tags",
            transform="transform",
            webhook_url="webhook_url",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_raw_response_create_from_url(self, client: Autorender) -> None:
        response = client.uploads.with_raw_response.create_from_url(
            remote_url="remote_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_streaming_response_create_from_url(self, client: Autorender) -> None:
        with client.uploads.with_streaming_response.create_from_url(
            remote_url="remote_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_with_token(self, client: Autorender) -> None:
        upload = client.uploads.create_with_token(
            token="up_tok_01JHD8X4BX3HQM8NFMD9ZCQ9QN",
            body=b"Example data",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_raw_response_create_with_token(self, client: Autorender) -> None:
        response = client.uploads.with_raw_response.create_with_token(
            token="up_tok_01JHD8X4BX3HQM8NFMD9ZCQ9QN",
            body=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_streaming_response_create_with_token(self, client: Autorender) -> None:
        with client.uploads.with_streaming_response.create_with_token(
            token="up_tok_01JHD8X4BX3HQM8NFMD9ZCQ9QN",
            body=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_with_token(self, client: Autorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.uploads.with_raw_response.create_with_token(
                token="",
                body=b"Example data",
            )

    @parametrize
    def test_method_generate_token(self, client: Autorender) -> None:
        upload = client.uploads.generate_token(
            file_name="avatar.jpg",
        )
        assert_matches_type(UploadGenerateTokenResponse, upload, path=["response"])

    @parametrize
    def test_method_generate_token_with_all_params(self, client: Autorender) -> None:
        upload = client.uploads.generate_token(
            file_name="avatar.jpg",
            allow_override={
                "folder": True,
                "tags": True,
                "transform": True,
            },
            custom_id="custom_id",
            folder="user-uploads/avatars",
            max_file_size=5242880,
            metadata={"foo": "bar"},
            random_prefix=True,
            tags=["string"],
            transform="w_400,h_400,fit_cover",
            ttl_seconds=900,
        )
        assert_matches_type(UploadGenerateTokenResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_generate_token(self, client: Autorender) -> None:
        response = client.uploads.with_raw_response.generate_token(
            file_name="avatar.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadGenerateTokenResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_generate_token(self, client: Autorender) -> None:
        with client.uploads.with_streaming_response.generate_token(
            file_name="avatar.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadGenerateTokenResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create(
            file=b"Example data",
            file_name="file_name",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create(
            file=b"Example data",
            file_name="file_name",
            custom_id="custom_id",
            folder="folder",
            metadata="metadata",
            random_prefix="random_prefix",
            tags="tags",
            transform="transform",
            webhook_url="webhook_url",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.with_raw_response.create(
            file=b"Example data",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.with_streaming_response.create(
            file=b"Example data",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_from_url(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create_from_url(
            remote_url="remote_url",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_method_create_from_url_with_all_params(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create_from_url(
            remote_url="remote_url",
            custom_id="custom_id",
            file_name="file_name",
            folder="folder",
            metadata="metadata",
            random_prefix="random_prefix",
            tags="tags",
            transform="transform",
            webhook_url="webhook_url",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_raw_response_create_from_url(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.with_raw_response.create_from_url(
            remote_url="remote_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_streaming_response_create_from_url(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.with_streaming_response.create_from_url(
            remote_url="remote_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_with_token(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.create_with_token(
            token="up_tok_01JHD8X4BX3HQM8NFMD9ZCQ9QN",
            body=b"Example data",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_raw_response_create_with_token(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.with_raw_response.create_with_token(
            token="up_tok_01JHD8X4BX3HQM8NFMD9ZCQ9QN",
            body=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_streaming_response_create_with_token(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.with_streaming_response.create_with_token(
            token="up_tok_01JHD8X4BX3HQM8NFMD9ZCQ9QN",
            body=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_with_token(self, async_client: AsyncAutorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.uploads.with_raw_response.create_with_token(
                token="",
                body=b"Example data",
            )

    @parametrize
    async def test_method_generate_token(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.generate_token(
            file_name="avatar.jpg",
        )
        assert_matches_type(UploadGenerateTokenResponse, upload, path=["response"])

    @parametrize
    async def test_method_generate_token_with_all_params(self, async_client: AsyncAutorender) -> None:
        upload = await async_client.uploads.generate_token(
            file_name="avatar.jpg",
            allow_override={
                "folder": True,
                "tags": True,
                "transform": True,
            },
            custom_id="custom_id",
            folder="user-uploads/avatars",
            max_file_size=5242880,
            metadata={"foo": "bar"},
            random_prefix=True,
            tags=["string"],
            transform="w_400,h_400,fit_cover",
            ttl_seconds=900,
        )
        assert_matches_type(UploadGenerateTokenResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_generate_token(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.with_raw_response.generate_token(
            file_name="avatar.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadGenerateTokenResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_generate_token(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.with_streaming_response.generate_token(
            file_name="avatar.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadGenerateTokenResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True
