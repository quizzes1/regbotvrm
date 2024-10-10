from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.requests as rq
import app.keyboards as kb


router = Router()


class Registration(StatesGroup):
    nickname = State()
    email = State()
    password = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f'VRM приветствует вас! Что вы хотите сделать?👾',
                        reply_markup=kb.main)


@router.message(F.text == 'Зарегистрировать нового пользователя🧑‍💼')
async def catalog(message: Message):
    await message.answer('Регистрируем...')


@router.message(F.text == 'Расписание игр📅')
async def catalog(message: Message):
    await message.answer('Расписываем игры...')


@router.message(F.text == 'Связаться с нами📲')
async def catalog(message: Message):
    await message.answer('До связи...')


@router.message(F.text == 'Наш ТГ-канал📟')
async def catalog(message: Message):
    await message.answer('TG channel')
