from aiogram.fsm.context import FSMContext
from aiogram.types import Message, callback_query, CallbackQuery
from aiogram import Router, F, Bot
from aiogram.filters import Command
from keyboards import admin_keyboards as kb
from states import admin_states as st
from database import requests as rq

router = Router()

@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await message.answer("🤖 В этом боте вы можете создавать конкурсы", reply_markup=kb.admin_start_keyboard())
    await state.update_data(message=message)

@router.callback_query(F.data == "back_to_start")
async def back_to_start(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await callback.message.edit_text("🤖 В этом боте вы можете создавать конкурсы", reply_markup=kb.admin_start_keyboard())

@router.message(F.data == "my_contest")
async def my_contest(callback: CallbackQuery, state: FSMContext):
    my_contest = await rq.get_roulette(user_id=str(callback.from_user.id))
    await callback.message.edit_text("⬇️ Ваши конкурсы", reply_markup=await rq.get_roulette_keyboard(user_id=str(callback.from_user.id)))








@router.callback_query(F.data == "create_contest")
async def create_contest(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("🤖 Что разыгрываем", reply_markup=kb.back_to_start_keyboard())
    await state.set_state(st.Wait.bounty)
    await state.update_data(message=callback.message)


@router.message(st.Wait.bounty)
async def dating_contest(message: Message, state: FSMContext):
    global text
    await state.update_data(text=f"🎁 Приз: {message.text}\n")
    try:
        await message.delete()
        data = await state.get_data()
        messages = data.get("roulette")

    except Exception:
        pass


    await message.answer("🤖 Отправьте кол-во победителей", reply_markup=kb.back_to_start_keyboard())
    await state.update_data(message=message)
    await state.set_state(st.Wait.wins)

@router.message(st.Wait.wins)
async def dating_contest_counter_users(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    bounty = data.get("roulette")
    counter = f"👤 Победителей: {message.text}\n"
    text = bounty + counter

    await state.update_data(roulette=text)

    data = await state.get_data()
    messages = data.get("roulette")
    try:
        await message.delete()
        await bot.delete_message(chat_id=messages.chat.id, message_id=messages.message_id)
    except Exception:
        pass

    await state.update_data(message=message)


    await message.answer("⏳ Отправьте кол-во времени", reply_markup=kb.back_to_start_keyboard())
    await state.set_state(st.Wait.time)

@router.message(st.Wait.time)
async def dating_contest_time(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    text = data.get("roulette")
    text += f"⏳ Время: {message.text}\n"
    await state.update_data(roulette=text)

    messages = data.get("roulette")
    await bot.delete_message(chat_id=messages.chat.id, message_id=messages.message_id)

    await message.answer("🤖 Вы уверены что хотите выкладывать ?", reply_markup=kb.accept_contest_keyboard())

@router.callback_query(F.data == "accept_contest")
async def accept_contest(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    roulette = data.get("roulette")
    await bot.send_message(chat_id=callback.from_user.id, text=str(roulette))
    messages = callback.message
    await rq.add_roulette(
                        user_id=str(callback.from_user.id),
                        username=str(callback.from_user.username),
                        roulette=str(roulette),
                        roulette_message_id=str(messages.message_id),
                        roulette_chat_id=str(messages.chat.id)
                        )
    await callback.message.edit_text("✅ Успешно выложено")

