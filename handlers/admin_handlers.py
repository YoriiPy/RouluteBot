from aiogram.fsm.context import FSMContext
from aiogram.types import Message, callback_query, CallbackQuery
from aiogram import Router, F
from aiogram.filters import Command
from keyboards import admin_keyboards as kb
from states import admin_states as st

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer("🤖 В этом боте вы можете создавать конкурсы", reply_markup=kb.admin_start_keyboard())

@router.callback_query(F.data == "back_to_start")
async def back_to_start(callback: CallbackQuery):
    await callback.message.edit_text("🤖 В этом боте вы можете создавать конкурсы", reply_markup=kb.admin_start_keyboard())




@router.callback_query(F.data == "create_contest")
async def create_contest(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("🤖 Что разыгрываем", reply_markup=kb.back_to_start_keyboard())
    await state.set_state(st.Wait.bounty)


@router.message(st.Wait.bounty)
async def dating_contest(message: Message, state: FSMContext):
    global text
    await state.update_data(text=f"🎁 Приз: {message.text}\n")

    await message.edit_text("🤖 Отправьте кол-во победителей", reply_markup=kb.back_to_start_keyboard())
    await state.set_state(st.Wait.wins)

@router.message(st.Wait.wins)
async def dating_contest_counter_users(message: Message, state: FSMContext):
    data = await state.get_data()
    bounty = data.get("text")
    counter = f"👤 Победителей: {message.text}\n"
    text = bounty + counter
    await state.update_data(text=text)
    await message.edit_text("⏳ Отправьте кол-во времени", reply_markup=kb.back_to_start_keyboard())
    await state.set_state(st.Wait.time)

@router.message(st.Wait.time)
async def dating_contest_time(message: Message, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")
    text += f"⏳ Время: {message.text}\n"
    await state.update_data(text=text)
    await message.edit_text("🤖 Вы уверены что хотите выкладывать ?", reply_markup=kb.accept_contest_keyboard())

