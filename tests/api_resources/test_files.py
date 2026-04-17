# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from autorender import Autorender, AsyncAutorender
from tests.utils import assert_matches_type
from autorender.types import (
    FileObject,
    FileListResponse,
    FileDeleteResponse,
    FileRenameResponse,
    FileUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Autorender) -> None:
        file = client.files.retrieve(
            "2353377462",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Autorender) -> None:
        response = client.files.with_raw_response.retrieve(
            "2353377462",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Autorender) -> None:
        with client.files.with_streaming_response.retrieve(
            "2353377462",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Autorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_no` but received ''"):
            client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Autorender) -> None:
        file = client.files.update(
            file_no="2353377462",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Autorender) -> None:
        file = client.files.update(
            file_no="2353377462",
            add_tags=["string"],
            metadata={"foo": "bar"},
            remove_tags=["string"],
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Autorender) -> None:
        response = client.files.with_raw_response.update(
            file_no="2353377462",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Autorender) -> None:
        with client.files.with_streaming_response.update(
            file_no="2353377462",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUpdateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Autorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_no` but received ''"):
            client.files.with_raw_response.update(
                file_no="",
            )

    @parametrize
    def test_method_list(self, client: Autorender) -> None:
        file = client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Autorender) -> None:
        file = client.files.list(
            folder_no="folder_no",
            limit=0,
            name="name",
            page=0,
            path="path",
            sort_field="file_size",
            sort_order="asc",
            tags="tags",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Autorender) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Autorender) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Autorender) -> None:
        file = client.files.delete(
            "2353377462",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Autorender) -> None:
        response = client.files.with_raw_response.delete(
            "2353377462",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Autorender) -> None:
        with client.files.with_streaming_response.delete(
            "2353377462",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Autorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_no` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_rename(self, client: Autorender) -> None:
        file = client.files.rename(
            file_no="2353377462",
            name="name",
        )
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @parametrize
    def test_raw_response_rename(self, client: Autorender) -> None:
        response = client.files.with_raw_response.rename(
            file_no="2353377462",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_rename(self, client: Autorender) -> None:
        with client.files.with_streaming_response.rename(
            file_no="2353377462",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileRenameResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rename(self, client: Autorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_no` but received ''"):
            client.files.with_raw_response.rename(
                file_no="",
                name="name",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAutorender) -> None:
        file = await async_client.files.retrieve(
            "2353377462",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAutorender) -> None:
        response = await async_client.files.with_raw_response.retrieve(
            "2353377462",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAutorender) -> None:
        async with async_client.files.with_streaming_response.retrieve(
            "2353377462",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAutorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_no` but received ''"):
            await async_client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncAutorender) -> None:
        file = await async_client.files.update(
            file_no="2353377462",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAutorender) -> None:
        file = await async_client.files.update(
            file_no="2353377462",
            add_tags=["string"],
            metadata={"foo": "bar"},
            remove_tags=["string"],
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAutorender) -> None:
        response = await async_client.files.with_raw_response.update(
            file_no="2353377462",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAutorender) -> None:
        async with async_client.files.with_streaming_response.update(
            file_no="2353377462",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUpdateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAutorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_no` but received ''"):
            await async_client.files.with_raw_response.update(
                file_no="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAutorender) -> None:
        file = await async_client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAutorender) -> None:
        file = await async_client.files.list(
            folder_no="folder_no",
            limit=0,
            name="name",
            page=0,
            path="path",
            sort_field="file_size",
            sort_order="asc",
            tags="tags",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAutorender) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAutorender) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAutorender) -> None:
        file = await async_client.files.delete(
            "2353377462",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAutorender) -> None:
        response = await async_client.files.with_raw_response.delete(
            "2353377462",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAutorender) -> None:
        async with async_client.files.with_streaming_response.delete(
            "2353377462",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAutorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_no` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_rename(self, async_client: AsyncAutorender) -> None:
        file = await async_client.files.rename(
            file_no="2353377462",
            name="name",
        )
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_rename(self, async_client: AsyncAutorender) -> None:
        response = await async_client.files.with_raw_response.rename(
            file_no="2353377462",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_rename(self, async_client: AsyncAutorender) -> None:
        async with async_client.files.with_streaming_response.rename(
            file_no="2353377462",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileRenameResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rename(self, async_client: AsyncAutorender) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_no` but received ''"):
            await async_client.files.with_raw_response.rename(
                file_no="",
                name="name",
            )
