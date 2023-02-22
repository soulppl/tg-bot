
from aiogram import types
from aiogram.dispatcher import FSMContext
from constants.message import MESSAGES
from modules.dp import dp, bot
from modules.google_sheet.google_sheet import send_user_info_to_sheets
from modules.quiz import Quiz
from utils.envs import get_forum_id, get_user_info_topic_id, get_rules_info_link
from utils.user_info import get_info_google_doc, get_welcome_topic_text


@dp.message_handler(state=Quiz.who_am_i)
async def send_message(message: types.Message, state=FSMContext):
    forum_id = get_forum_id()
    user_info_topic_id = get_user_info_topic_id()
    invite_link_obj = await bot.create_chat_invite_link(
        chat_id=forum_id,
        member_limit=1
    )
    invite_link = invite_link_obj.invite_link
    async with state.proxy() as quiz_responses:
        who_am_i = message.text
        quiz_responses["who_am_i"] = who_am_i
        quiz_responses["invite_link"] = invite_link
        quiz_responses.pop("_message", None)

        quiz_response_values = list(quiz_responses.values())
        user_info = get_info_google_doc(quiz_response_values)

        await send_user_info_to_sheets(user_info)

        welcome_topic_text = get_welcome_topic_text(quiz_responses)
        await bot.send_message(
            chat_id=forum_id,
            message_thread_id=user_info_topic_id,
            text=welcome_topic_text,
            parse_mode="HTML"
        )

    await message.answer(
        MESSAGES.invite_link.substitute(
            invite_link=invite_link
        )
    )

    await message.delete()
    if message.reply_to_message:
        await message.reply_to_message.delete()
    await state.finish()
