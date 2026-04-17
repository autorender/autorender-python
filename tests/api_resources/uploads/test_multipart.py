# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from autorender import Autorender, AsyncAutorender
from tests.utils import assert_matches_type
from autorender.types import Upload
from autorender.types.uploads import (
    Session,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMultipart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_complete(self, client: Autorender) -> None:
        multipart = client.uploads.multipart.complete(
            session_id="session_id",
        )
        assert_matches_type(Upload, multipart, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Autorender) -> None:
        response = client.uploads.multipart.with_raw_response.complete(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = response.parse()
        assert_matches_type(Upload, multipart, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Autorender) -> None:
        with client.uploads.multipart.with_streaming_response.complete(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = response.parse()
            assert_matches_type(Upload, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: Autorender) -> None:
        multipart = client.uploads.multipart.start(
            file_name="file_name",
            format="format",
            size=0,
        )
        assert_matches_type(Session, multipart, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Autorender) -> None:
        multipart = client.uploads.multipart.start(
            file_name="file_name",
            format="format",
            size=0,
            custom_id="custom_id",
            folder="folder",
            metadata={"foo": "bar"},
            random_prefix=True,
            tags=["string"],
            ttl_seconds=0,
        )
        assert_matches_type(Session, multipart, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Autorender) -> None:
        response = client.uploads.multipart.with_raw_response.start(
            file_name="file_name",
            format="format",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = response.parse()
        assert_matches_type(Session, multipart, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Autorender) -> None:
        with client.uploads.multipart.with_streaming_response.start(
            file_name="file_name",
            format="format",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = response.parse()
            assert_matches_type(Session, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_part(self, client: Autorender) -> None:
        multipart = client.uploads.multipart.upload_part(
            b"Example data",
        )
        assert multipart is None

    @parametrize
    def test_raw_response_upload_part(self, client: Autorender) -> None:
        response = client.uploads.multipart.with_raw_response.upload_part(
            b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = response.parse()
        assert multipart is None

    @parametrize
    def test_streaming_response_upload_part(self, client: Autorender) -> None:
        with client.uploads.multipart.with_streaming_response.upload_part(
            b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = response.parse()
            assert multipart is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMultipart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_complete(self, async_client: AsyncAutorender) -> None:
        multipart = await async_client.uploads.multipart.complete(
            session_id="session_id",
        )
        assert_matches_type(Upload, multipart, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.multipart.with_raw_response.complete(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = await response.parse()
        assert_matches_type(Upload, multipart, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.multipart.with_streaming_response.complete(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = await response.parse()
            assert_matches_type(Upload, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncAutorender) -> None:
        multipart = await async_client.uploads.multipart.start(
            file_name="file_name",
            format="format",
            size=0,
        )
        assert_matches_type(Session, multipart, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncAutorender) -> None:
        multipart = await async_client.uploads.multipart.start(
            file_name="file_name",
            format="format",
            size=0,
            custom_id="custom_id",
            folder="folder",
            metadata={"foo": "bar"},
            random_prefix=True,
            tags=["string"],
            ttl_seconds=0,
        )
        assert_matches_type(Session, multipart, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.multipart.with_raw_response.start(
            file_name="file_name",
            format="format",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = await response.parse()
        assert_matches_type(Session, multipart, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.multipart.with_streaming_response.start(
            file_name="file_name",
            format="format",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = await response.parse()
            assert_matches_type(Session, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_part(self, async_client: AsyncAutorender) -> None:
        multipart = await async_client.uploads.multipart.upload_part(
            b"Example data",
        )
        assert multipart is None

    @parametrize
    async def test_raw_response_upload_part(self, async_client: AsyncAutorender) -> None:
        response = await async_client.uploads.multipart.with_raw_response.upload_part(
            b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = await response.parse()
        assert multipart is None

    @parametrize
    async def test_streaming_response_upload_part(self, async_client: AsyncAutorender) -> None:
        async with async_client.uploads.multipart.with_streaming_response.upload_part(
            b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = await response.parse()
            assert multipart is None

        assert cast(Any, response.is_closed) is True
