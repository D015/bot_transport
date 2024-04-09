from asyncio import run, sleep, CancelledError
from app.chat_transport.transpots_data import transports_data
from app.simple_bot.bot_runner import BotsRunner
from app.simple_bot.simple_business_logic_bot import SimpleBusinessLogicBot


async def main():
    tasks_started = await BotsRunner(
            business_logic_bot_class=SimpleBusinessLogicBot,
            transports_data=transports_data,
    ).run_bots_with_transports()

    try:
        while True:
            await sleep(3600)
    except BaseException:
        for task in tasks_started:
            task.cancel()
            try:
                await task
            except CancelledError:
                pass


if __name__ == "__main__":
    run(main())
