from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class MessageData:
    text: str
    chat_id: Union[int, str]
    transport_name: str = ""
