from aiogram import executor
from core.dp import dp
from core.FSM import register_handlers_client

register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
