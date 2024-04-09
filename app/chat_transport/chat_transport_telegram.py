from asyncio import get_running_loop

from aiogram import Bot, Dispatcher, types

from app.chat_transport.chat_transport import ChatTransport
from app.chat_transport.utils.data_classes import MessageData
from app.configs.logs_config import loguru_logger


class ChatTransportTelegram(ChatTransport):
    def __init__(self, token: str) -> None:
        super().__init__(token=token)
        self._bot = Bot(token=self._token)
        self._dp = Dispatcher(self._bot)

        @self._dp.message_handler()
        async def message_handler(message: types.Message) -> None:
            await self._message_queue.put(
                MessageData(
                    text=message.text,
                    chat_id=message.chat.id,
                    transport_name=self.__class__.__name__,
                )
            )

    async def send_message(self, msg: MessageData) -> None:
        try:
            await self._bot.send_message(chat_id=msg.chat_id, text=msg.text)
        except BaseException as exc:
            loguru_logger.error(f"Error while sending message: {exc}")

    async def run(self) -> None:
        loop = get_running_loop()
        loop.create_task(self._dp.start_polling())
        await self._process_message()
