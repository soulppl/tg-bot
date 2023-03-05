from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from components.about.handler import tell_about_yourself
from components.location.handler import ask_location
from utils import say_welcome


async def name_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        globalState["is_editing"] = True
        globalState["editing_field"] = "name"
    await say_welcome(call.message, state)


async def location_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        globalState["is_editing"] = True
        globalState["editing_field"] = "location"
    await ask_location(call.message, state)


async def about_handler(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as globalState:
        globalState["is_editing"] = True
        globalState["editing_field"] = "who_am_i"
    await tell_about_yourself(call.message, state)
