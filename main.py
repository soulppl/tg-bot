import os

from aiogram import executor

from handlers.native_buttons.command_list import set_default_commands
from modules.dp import dp
from modules.FSM import register_handlers_client
from utils.envs import print_envs

print_envs(os)
register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_default_commands)
