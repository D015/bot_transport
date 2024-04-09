from dataclasses import dataclass
from typing import Optional, Type

from app.chat_transport.chat_transport_discord import ChatTransportDiscord
from app.chat_transport.chat_transport import ChatTransport
from app.chat_transport.chat_transport_telegram import ChatTransportTelegram
from app.configs.settings import APP_SETTINGS


@dataclass(frozen=True)
class TransportInitData:
    class_: Type[ChatTransport]
    token: Optional[str]


transports_data = frozenset(
    {
        TransportInitData(
            class_=ChatTransportTelegram,
            token=APP_SETTINGS.TELEGRAM_BOT_TOKEN
        ),
        TransportInitData(
            class_=ChatTransportDiscord,
            token=APP_SETTINGS.DISCORD_BOT_TOKEN
        )
    }
)