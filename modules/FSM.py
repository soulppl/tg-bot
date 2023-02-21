from aiogram import Dispatcher

from handlers import welcome, name, location, interests, who_am_i, travels, default
from handlers.forum import chat
from modules.quiz import Quiz

Quiz.welcome.set()


def register_handlers_client(dp: Dispatcher):
    # dp.register_message_handler: chat.chat_handler(state="*")
    dp.register_message_handler: welcome.send_message
    dp.register_message_handler: name.send_message(state=Quiz.name)
    dp.register_callback_query_handler: location.keyboard_message(state=Quiz.location)
    dp.register_callback_query_handler: interests.keyboard_message(state=Quiz.interests)
    dp.register_callback_query_handler: interests.keyboard_message_travels(state=Quiz.interests)
    dp.register_callback_query_handler: travels.keyboard_message(state=Quiz.travels)
    dp.register_callback_query_handler: who_am_i.keyboard_message(state=Quiz.who_am_i)
    dp.register_message_handler: who_am_i.send_message(state=Quiz.who_am_i)
    dp.register_message_handler: default.answer_to_auth_user


