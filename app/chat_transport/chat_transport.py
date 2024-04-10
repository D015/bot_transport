from abc import ABC, abstractmethod
from asyncio import Queue

from app.chat_transport.utils.data_classes import MessageData
from app.chat_transport.utils.types import EventHandler
from app.configs.logs_config import loguru_logger


class ChatTransport(ABC):
    @abstractmethod
    def __init__(self, token: str) -> None:
        self._token = token
        self.handlers: list[EventHandler] = []
        self._message_queue: Queue[MessageData] = Queue()

    def add_handler(self, event: callable) -> None:
        self.handlers.append(event)

    @abstractmethod
    async def send_message(self, msg: MessageData) -> None:
        # Send a message through the transport
        pass

    @abstractmethod
    async def _run(self) -> None:
        # Run the transport for receiving messages
        pass

    @abstractmethod
    async def _put_message_queue(self) -> None:
        # Put a message to the queue
        pass

    async def run(self) -> None:
        await self._run()
        await self._put_message_queue()
        await self._process_message()

    async def _process_message(self) -> None:
        while True:
            msg = await self._message_queue.get()
            if isinstance(msg, MessageData):
                await self._handle_message(msg)
            else:
                loguru_logger.error(f"Received message is not a MessageData")

    async def _handle_message(self, msg: MessageData) -> None:
        for handler in self.handlers:
            await handler(msg=msg)
