from app.chat_transport.chat_transport import ChatTransport
from app.chat_transport.utils.data_classes import MessageData
from app.configs.text_templates import TextTemplates


class SimpleBusinessLogicBot:
    def __init__(self, transport: ChatTransport) -> None:
        self._transport = transport

        handlers = [
            self._print_message_info,
            self._reply_to_message,
        ]

        for handler in handlers:
            self._transport.add_handler(handler)

    async def run_bot(self) -> None:
        await self._transport.run()

    async def _reply_to_message(self, msg: MessageData) -> None:
        reply_message = MessageData(
            text=TextTemplates.GREETING_TO_MESSAGE(msg_text=msg.text),
            chat_id=msg.chat_id,
            transport_name=self.__class__.__name__,
        )
        await self._transport.send_message(reply_message)

    @staticmethod
    async def _print_message_info(msg: MessageData) -> None:
        message_info_text = TextTemplates.MESSAGE_INFO(
            msg_text=msg.text,
            msg_chat_id=msg.chat_id,
            transport_name=msg.transport_name,
        )
        print(message_info_text)
