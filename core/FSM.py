from aiogram import Dispatcher

from handlers import welcome, name, location, interests, who_am_i, travels
from modules.quiz import Quiz


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler: welcome.send_message
    dp.register_message_handler: name.send_message(state=Quiz.name)
    dp.register_callback_query_handler: location.keyboard_message(state=Quiz.location)
    dp.register_callback_query_handler: interests.keyboard_message(state=Quiz.interests)
    dp.register_callback_query_handler: interests.keyboard_message_travels(state=Quiz.interests)
    dp.register_callback_query_handler: travels.keyboard_message(state=Quiz.travels)
    dp.register_message_handler: who_am_i.send_message(state=Quiz.who_am_i)

