# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from autorender import Autorender, AsyncAutorender
from tests.utils import assert_matches_type
from autorender.types import (
    Folder,
    FolderListResponse,
    FolderCreateResponse,
    FolderDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Autorender) -> None:
        folder = client.folders.create(
            name="demo2",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Autorender) -> None:
        folder = client.folders.create(
            name="demo2",
            parent_folder_no="sD1LvqoDzG",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Autorender) -> None:
        response = client.folders.with_raw_response.create(
            name="demo2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Autorender) -> None:
        with client.folders.with_streaming_response.create(
            name="demo2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Autorender) -> None:
        folder = client.folders.list()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Autorender) -> None:
        folder = client.folders.list(
            parent_folder_no="sD1LvqoDzG",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Autorender) -> None:
        response = client.folders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Autorender) -> None:
        with client.folders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Autorender) -> None:
        folder = client.folders.delete(
            "my8JeLg4tr",
        )
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Autorender) -> None:
        response = client.folders.with_raw_response.delete(
            "my8JeLg4tr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Autorender) -> None:
        with client.folders.with_streaming_response.delete(
            "my8JeLg4tr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderDeleteResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Autorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_no` but received ''"):
            client.folders.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_rename(self, client: Autorender) -> None:
        folder = client.folders.rename(
            folder_no="53855hxPoq",
            name="demo2",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @parametrize
    def test_raw_response_rename(self, client: Autorender) -> None:
        response = client.folders.with_raw_response.rename(
            folder_no="53855hxPoq",
            name="demo2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @parametrize
    def test_streaming_response_rename(self, client: Autorender) -> None:
        with client.folders.with_streaming_response.rename(
            folder_no="53855hxPoq",
            name="demo2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rename(self, client: Autorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_no` but received ''"):
            client.folders.with_raw_response.rename(
                folder_no="",
                name="demo2",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncAutorender) -> None:
        folder = await async_client.folders.create(
            name="demo2",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAutorender) -> None:
        folder = await async_client.folders.create(
            name="demo2",
            parent_folder_no="sD1LvqoDzG",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAutorender) -> None:
        response = await async_client.folders.with_raw_response.create(
            name="demo2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAutorender) -> None:
        async with async_client.folders.with_streaming_response.create(
            name="demo2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncAutorender) -> None:
        folder = await async_client.folders.list()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAutorender) -> None:
        folder = await async_client.folders.list(
            parent_folder_no="sD1LvqoDzG",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAutorender) -> None:
        response = await async_client.folders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAutorender) -> None:
        async with async_client.folders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAutorender) -> None:
        folder = await async_client.folders.delete(
            "my8JeLg4tr",
        )
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAutorender) -> None:
        response = await async_client.folders.with_raw_response.delete(
            "my8JeLg4tr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAutorender) -> None:
        async with async_client.folders.with_streaming_response.delete(
            "my8JeLg4tr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderDeleteResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAutorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_no` but received ''"):
            await async_client.folders.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_rename(self, async_client: AsyncAutorender) -> None:
        folder = await async_client.folders.rename(
            folder_no="53855hxPoq",
            name="demo2",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @parametrize
    async def test_raw_response_rename(self, async_client: AsyncAutorender) -> None:
        response = await async_client.folders.with_raw_response.rename(
            folder_no="53855hxPoq",
            name="demo2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @parametrize
    async def test_streaming_response_rename(self, async_client: AsyncAutorender) -> None:
        async with async_client.folders.with_streaming_response.rename(
            folder_no="53855hxPoq",
            name="demo2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rename(self, async_client: AsyncAutorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_no` but received ''"):
            await async_client.folders.with_raw_response.rename(
                folder_no="",
                name="demo2",
            )
