from aiogram.fsm.state import State, StatesGroup


class RegistrationState(StatesGroup):
    waiting_full_name = State()


class EditProfileState(StatesGroup):
    waiting_new_name = State()


class CreateTestState(StatesGroup):
    waiting_title = State()
    waiting_answer_key = State()
    waiting_confirm = State()


class SubmitAnswerState(StatesGroup):
    waiting_code_or_full = State()
    waiting_answers = State()
