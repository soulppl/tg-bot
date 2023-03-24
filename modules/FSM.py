from aiogram import Dispatcher

from projects.user_quiz.components import preview, location, interests, quiz_send, default, commands, \
    interests_with_skip, quiz_editing
from projects.user_quiz.components import quiz_edit, about
from modules.Quiz import Quiz


# noinspection DuplicatedCode
def register_handlers_client(dp: Dispatcher):
    # referral program
    # default menu
    dp.register_message_handler(
        commands.referral.handler.default,
        commands=[commands.CommandsNames.referral],
        state=None
    )
    # close
    dp.register_callback_query_handler(
        commands.referral.handler.close,
        text=commands.referral.KeyboardText.close,
        state=Quiz.referral
    )
    # show referral list
    dp.register_callback_query_handler(
        commands.referral.handler.show_referral_list,
        text=commands.referral.KeyboardText.get_ref_list,
        state=Quiz.referral
    )
    # back to default menu
    dp.register_callback_query_handler(
        commands.referral.handler.default,
        text=commands.referral.KeyboardText.back,
        state=Quiz.referral
    )

    # user quiz
    dp.register_message_handler(commands.start.handler.default, commands=[commands.CommandsNames.start], state="*")
    dp.register_message_handler(location.handler.default, state=Quiz.location)
    dp.register_callback_query_handler(interests.handler.default, state=Quiz.interests)
    dp.register_callback_query_handler(
        about.handler.default,
        state=Quiz.interests_with_skip,
        text=interests_with_skip.KeyboardText.skip
    )
    dp.register_callback_query_handler(interests_with_skip.handler.default, state=Quiz.interests_with_skip)
    dp.register_message_handler(preview.handler.default, state=Quiz.preview)
    dp.register_callback_query_handler(preview.handler.callback, state=Quiz.preview)
    dp.register_callback_query_handler(
        preview.handler.callback,
        state=Quiz.editing_interests_with_skip,
        text=interests_with_skip.KeyboardText.skip
    )
    dp.register_callback_query_handler(interests_with_skip.handler.default, state=Quiz.editing_interests_with_skip)
    dp.register_callback_query_handler(quiz_send.handler.default, quiz_send.Filter(), state=Quiz.edit_or_send)
    dp.register_callback_query_handler(quiz_edit.handler.default, quiz_edit.Filter(), state=Quiz.edit_or_send)
    dp.register_callback_query_handler(quiz_editing.name_handler, quiz_editing.NameFilter(), state=Quiz.editing)
    dp.register_callback_query_handler(quiz_editing.location_handler, quiz_editing.LocationFilter(), state=Quiz.editing)
    dp.register_callback_query_handler(quiz_editing.interests_handler, quiz_editing.InterestsFIlter(), state=Quiz.editing)
    dp.register_callback_query_handler(quiz_editing.about_handler, quiz_editing.AboutFilter(), state=Quiz.editing)
    dp.register_message_handler(default.handler.default, state='*')

