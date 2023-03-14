from aiogram.dispatcher import FSMContext

from constants.quiz_responses_fields import QuizResponsesFields


def set_editing_field(editing_field: QuizResponsesFields, global_state: FSMContext.proxy):
    global_state[QuizResponsesFields.service_data.is_editing] = True
    global_state[QuizResponsesFields.service_data.editing_field] = editing_field
    global_state.pop(editing_field, None)
