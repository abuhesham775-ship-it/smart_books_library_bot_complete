from aiogram.fsm.state import State, StatesGroup


class BookSearchState(StatesGroup):
    waiting_query = State()
