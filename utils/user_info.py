from aiogram.dispatcher.storage import FSMContextProxy
from aiogram.types import Chat

from components.about import KeyboardText
from constants.message import MESSAGES
from constants.quiz_responses_fields import QuizResponsesFields


def get_info_google_doc(quiz_responses: FSMContextProxy):
    quiz_responses_copy = dict(quiz_responses)
    quiz_responses_copy[QuizResponsesFields.interests] = ', '.join(quiz_responses_copy[QuizResponsesFields.interests])
    chat = Chat.get_current()
    user_id = chat.id
    username = chat.username
    user_url_id = f"tg://user?id={user_id}"
    user_url_name = f"t.me/{username}"

    quiz_response_values = [
        quiz_responses[QuizResponsesFields.name],
        quiz_responses[QuizResponsesFields.location],
        ', '.join(quiz_responses[QuizResponsesFields.interests]),
        quiz_responses[QuizResponsesFields.about],
        quiz_responses[QuizResponsesFields.invite_link]
    ]

    return [username, user_id, user_url_name, user_url_id] + quiz_response_values


def get_welcome_topic_text(quiz_response):
    answers_preview = get_answers_preview(quiz_response)

    return MESSAGES.welcome_topic_text.substitute(
        answers_preview=answers_preview,
    )


def get_preview_text(quiz_response):
    answers_preview = get_answers_preview(quiz_response)

    return MESSAGES.quiz_preview.substitute(
        answers_preview=answers_preview,
    )


def get_answers_preview(quiz_response):
    chat = Chat.get_current()
    mention = chat.mention
    username = chat.username
    user_id = chat.id
    if not username:
        mention = f"tg://user?id={user_id}"
    name = quiz_response[QuizResponsesFields.name]
    location = quiz_response[QuizResponsesFields.location]
    interests = '\n'.join(quiz_response[QuizResponsesFields.interests])
    about = quiz_response[QuizResponsesFields.about]
    skip_about = about == KeyboardText.skip
    about_preview = "" if skip_about else MESSAGES.about_preview.substitute(about=about)
    answers_preview = (
        MESSAGES.name_preview.substitute(name=name, mention=mention) +
        MESSAGES.location_preview.substitute(location=location) +
        MESSAGES.interests_preview.substitute(interests=interests) +
        about_preview
    )

    return answers_preview
