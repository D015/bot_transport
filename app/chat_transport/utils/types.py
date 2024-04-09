from typing import runtime_checkable, Protocol, TypeVar

from app.chat_transport.utils.data_classes import MessageData


@runtime_checkable
class EventHandler(Protocol):
    async def __call__(self, msg: MessageData) -> None: ...
