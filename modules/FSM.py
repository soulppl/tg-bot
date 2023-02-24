from aiogram import Dispatcher

from handlers import name, location, interests, who_am_i, travels, default, send_quiz, commands, edit_quiz
from modules.quiz import Quiz


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands.restart, commands=['restart'], state="*")
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(name.send_message, state=Quiz.name)
    dp.register_callback_query_handler(location.keyboard_message, state=Quiz.location)
    dp.register_callback_query_handler(interests.keyboard_message, state=Quiz.interests)
    dp.register_callback_query_handler(travels.keyboard_message, state=Quiz.travels)
    dp.register_message_handler(who_am_i.message_handler, state=Quiz.who_am_i)
    dp.register_callback_query_handler(who_am_i.callback_handler, state=Quiz.who_am_i)
    dp.register_callback_query_handler(send_quiz.send_quiz, state=Quiz.send_quiz)
    dp.register_callback_query_handler(edit_quiz, state=Quiz.edit_quiz)
    dp.register_message_handler(default.answer_to_auth_user, state=None)



