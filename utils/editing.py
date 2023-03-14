from aiogram.dispatcher import FSMContext

from constants.quiz_responses import QuizResponses


def set_editing_field(editing_field: QuizResponses, global_state: FSMContext.proxy):
    global_state[QuizResponses.service_data.is_editing] = True
    global_state[QuizResponses.service_data.editing_field] = editing_field
    global_state.pop(editing_field, None)
