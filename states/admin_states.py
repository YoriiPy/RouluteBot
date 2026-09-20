from aiogram.fsm.state import StatesGroup, State


class Wait(StatesGroup):
    bounty = State()
    wins = State()
    time = State()
    

