from aiogram.types import Chat

from constants.message import MESSAGES


def get_info_google_doc(quiz_response_values):
    chat = Chat.get_current()
    user_id = chat.id
    username = chat.username
    user_url_id = f"tg://user?id={user_id}"
    user_url_name = f"t.me/{username}"

    return [username, user_id, user_url_name, user_url_id] + quiz_response_values


def get_welcome_topic_text(quiz_response):
    chat = Chat.get_current()
    mention = chat.mention
    username = chat.username
    user_id = chat.id
    if not username:
        mention = f"tg://user?id={user_id}"
    name = quiz_response["name"]
    location = quiz_response["location"]
    interests = '\n'.join(quiz_response["interests"].split(", "))
    who_am_i = quiz_response["who_am_i"]
    return MESSAGES.welcome_topic_text.substitute(
        name=name,
        mention=mention,
        location=location,
        interests=interests,
        who_am_i=who_am_i
    )
