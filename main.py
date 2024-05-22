import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main():
    bot = Bot(token='7025765522:AAHBB1FI4NmvuYlf10mUixEYcjBJJzNDclQ')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())
