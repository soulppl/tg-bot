from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


message_1 = "WELCOME в travel-семью SOUL people ❤\n\nТут каждого принимают как дома вне зависимости от страны " \
            "проживания, ведь это <b>сообщество друзей, разбросанных по всему миру</b>\n\nЧтобы познакомиться " \
            "поближе," \
            "я задам всего 6 коротких вопросов, ответ на которые займет 3 минуты твоего времени\n\n" \
            "Ну и начнем с главного... 😉\n\n<b>Как я могу к тебе обращаться?</b>"

message_2 = "👯‍♀ Наши люди находятся более чем в 20 странах мира, а в некоторых из них уже открыты базы сообщества, " \
            "куда ты тоже сможешь попасть\n\n<b>Поэтому подскажи, в какой стране ты прямо сейчас?</b>"


# Класс машины состояний
class Questionnaire(StatesGroup):
    name = State()
    location = State()
    interests = State()
    skills = State()


# Старт бота
@dp.message_handler(commands=['start'], state=None)
async def bot_start(message: types.Message):
    await Questionnaire.name.set() # Запускаем машину состояний
    await message.answer(message_1, parse_mode='HTML')


# Ловим имя пользователя
@dp.message_handler(state=Questionnaire.name)
async def add_name(message: types.Message, state=FSMContext):
    await Questionnaire.next() # Переход в слудующее состояние
    async with state.proxy() as data:
        data["name"] = message.text # Сохраняем данные
    await message.answer(f"Отлично, {message.text}\n\n{message_2}", parse_mode='HTML')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'], state=None)
    dp.register_message_handler(add_name, state=Questionnaire.name)
