from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: Optional[str] = Field(
        default=None,
        description="The token for the Telegram bot. This token is required "
                    "to authenticate the bot with the Telegram API."
    )
    DISCORD_BOT_TOKEN: Optional[str] = Field(
        default=None,
        description="The token for the Discord bot. This token is required "
                    "to authenticate the bot with the Discord API."
    )


    class Config:
        extra = "ignore"
        env_file = '.env'
        env_file_encoding = 'utf-8'
        frozen = True


APP_SETTINGS = AppSettings()
