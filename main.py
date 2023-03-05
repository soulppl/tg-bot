import os

from aiogram import executor

from components import quiz_send, quiz_edit, quiz_editing
from modules.bot_commands.command_list import set_default_commands
from modules.DP import dp
from modules.FSM import register_handlers_client
from utils.envs import print_envs

print_envs(os)
register_handlers_client(dp)

if __name__ == '__main__':
    dp.bind_filter(quiz_send.Filter)
    dp.bind_filter(quiz_edit.Filter)
    dp.bind_filter(quiz_editing.NameFilter)
    dp.bind_filter(quiz_editing.LocationFilter)
    dp.bind_filter(quiz_editing.AboutFilter)
    executor.start_polling(dp, skip_updates=True, on_startup=set_default_commands)
