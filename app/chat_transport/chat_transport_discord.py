from asyncio import get_running_loop

import discord

from app.chat_transport.chat_transport import ChatTransport
from app.chat_transport.utils.data_classes import MessageData
from app.configs.logs_config import loguru_logger


class ChatTransportDiscord(ChatTransport):
    def __init__(self, token: str) -> None:
        super().__init__(token=token)

        intents = discord.Intents.default()
        intents.messages = True
        intents.guild_messages = True
        intents.dm_messages = True
        self._bot = discord.Client(intents=intents)

        @self._bot.event
        async def on_message(message: discord.Message) -> None:
            if message.author == self._bot.user:
                return
            await self._message_queue.put(
                MessageData(
                    text=message.content,
                    chat_id=message.channel.id,
                    transport_name=self.__class__.__name__,
                )
            )

    async def send_message(self, msg: MessageData) -> None:
        try:
            channel = await self._bot.fetch_channel(msg.chat_id)
            if channel:
                await channel.send(msg.text)
        except BaseException as exc:
            loguru_logger.error(f"Error while sending message: {exc}")

    async def _run(self) -> None:
        loop = get_running_loop()
        loop.create_task(self._bot.start(self._token))
