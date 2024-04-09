from asyncio import create_task, Task
from typing import Iterable, Type

from app.chat_transport.transpots_data import TransportInitData
from app.configs.logs_config import loguru_logger
from app.simple_bot.simple_business_logic_bot import SimpleBusinessLogicBot


class BotsRunner:
    def __init__(
        self,
        business_logic_bot_class: Type[SimpleBusinessLogicBot],
        transports_data: Iterable[TransportInitData],
    ) -> None:
        self._business_logic_bot_class = business_logic_bot_class
        self._transports_data = transports_data

    async def run_bots_with_transports(self) -> list[Task]:

        tasks_started: list[Task] = []
        for transport_init_data in self._transports_data:
            if transport_init_data.token is None:
                loguru_logger.warning(
                    f"Transport {transport_init_data.class_.__name__} "
                    f"has no token"
                )
                continue
            try:
                transport = transport_init_data.class_(
                    token=transport_init_data.token
                )
            except BaseException as exc:
                loguru_logger.error(
                    f"Error while initializing "
                    f"{transport_init_data.class_.__name__}: {exc}"
                )
                continue

            business_logic_bot = self._business_logic_bot_class(
                transport=transport,
            )
            task_started = create_task(business_logic_bot.run_bot())
            tasks_started.append(task_started)
            loguru_logger.info(
                f"Bot {self._business_logic_bot_class.__name__} "
                f"with transport {transport_init_data.class_.__name__} "
                f"started"
            )
        return tasks_started
