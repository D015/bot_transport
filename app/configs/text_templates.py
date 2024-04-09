from app.utils.str_base_enum import StrBaseEnum


class TextTemplates(StrBaseEnum):
    MESSAGE_INFO = "New message: {msg_text} from transport: " \
                   "{transport_name} chat: {msg_chat_id}"
    GREETING_TO_MESSAGE = "Hi! Your message was received: {msg_text}"
