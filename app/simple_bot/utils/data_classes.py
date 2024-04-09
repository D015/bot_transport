from dataclasses import dataclass
from typing import Iterable

from app.chat_transport.transpots_data import TransportInitData


@dataclass(frozen=True)
class BotInitData:
    class_: object
    transports_init_data: Iterable[TransportInitData]
