# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/services/block/v1/block.proto, tendermint/services/block/v1/block_service.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from typing import TYPE_CHECKING, AsyncIterator, Dict, Optional

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .... import types as ___types__

if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class GetByHeightRequest(betterproto.Message):
    height: int = betterproto.int64_field(1)
    """
    The height of the block requested. If set to 0, the latest height will be returned.
    """


@dataclass(eq=False, repr=False)
class GetByHeightResponse(betterproto.Message):
    block_id: "___types__.BlockId" = betterproto.message_field(1)
    block: "___types__.Block" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GetLatestRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetLatestResponse(betterproto.Message):
    block_id: "___types__.BlockId" = betterproto.message_field(1)
    block: "___types__.Block" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GetLatestHeightRequest(betterproto.Message):
    """GetLatestHeightRequest - empty message since no parameter is required"""

    pass


@dataclass(eq=False, repr=False)
class GetLatestHeightResponse(betterproto.Message):
    """GetLatestHeightResponse provides the height of the latest committed block."""

    height: int = betterproto.int64_field(1)
    """
    The height of the latest committed block. Will be 0 if no data has been
    committed yet.
    """


class BlockServiceStub(betterproto.ServiceStub):
    async def get_by_height(
        self,
        get_by_height_request: "GetByHeightRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GetByHeightResponse":
        return await self._unary_unary(
            "/tendermint.services.block.v1.BlockService/GetByHeight",
            get_by_height_request,
            GetByHeightResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_latest(
        self,
        get_latest_request: "GetLatestRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GetLatestResponse":
        return await self._unary_unary(
            "/tendermint.services.block.v1.BlockService/GetLatest",
            get_latest_request,
            GetLatestResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_latest_height(
        self,
        get_latest_height_request: "GetLatestHeightRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["GetLatestHeightResponse"]:
        async for response in self._unary_stream(
            "/tendermint.services.block.v1.BlockService/GetLatestHeight",
            get_latest_height_request,
            GetLatestHeightResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class BlockServiceBase(ServiceBase):
    async def get_by_height(self, get_by_height_request: "GetByHeightRequest") -> "GetByHeightResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_latest(self, get_latest_request: "GetLatestRequest") -> "GetLatestResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_latest_height(
        self, get_latest_height_request: "GetLatestHeightRequest"
    ) -> AsyncIterator["GetLatestHeightResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)
        yield GetLatestHeightResponse()

    async def __rpc_get_by_height(
        self, stream: "grpclib.server.Stream[GetByHeightRequest, GetByHeightResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_by_height(request)
        await stream.send_message(response)

    async def __rpc_get_latest(self, stream: "grpclib.server.Stream[GetLatestRequest, GetLatestResponse]") -> None:
        request = await stream.recv_message()
        response = await self.get_latest(request)
        await stream.send_message(response)

    async def __rpc_get_latest_height(
        self,
        stream: "grpclib.server.Stream[GetLatestHeightRequest, GetLatestHeightResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.get_latest_height,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/tendermint.services.block.v1.BlockService/GetByHeight": grpclib.const.Handler(
                self.__rpc_get_by_height,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetByHeightRequest,
                GetByHeightResponse,
            ),
            "/tendermint.services.block.v1.BlockService/GetLatest": grpclib.const.Handler(
                self.__rpc_get_latest,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetLatestRequest,
                GetLatestResponse,
            ),
            "/tendermint.services.block.v1.BlockService/GetLatestHeight": grpclib.const.Handler(
                self.__rpc_get_latest_height,
                grpclib.const.Cardinality.UNARY_STREAM,
                GetLatestHeightRequest,
                GetLatestHeightResponse,
            ),
        }
