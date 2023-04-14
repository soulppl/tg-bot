import os

from aiogram import executor

from projects.user_quiz.components import quiz_edit, quiz_send, quiz_editing
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
    dp.bind_filter(quiz_editing.InterestsFIlter)
    dp.bind_filter(quiz_editing.AboutFilter)
    executor.start_polling(dp, allowed_updates=["chat_member", "message", "callback_query"])
