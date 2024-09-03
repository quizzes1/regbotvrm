from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Hello!\nYour Id:{message.from_user.id}\nYour name: {message.from_user.first_name}',
                        reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply('Huy tebe a ne pomosh',
                        reply_markup=kb.settings)

@router.message(F.text == "zhopa")
async def zhopa(message: Message):
    await message.answer("zaebis")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID Photo: {message.photo[-1].file_id}')

@router.message(Command('send_photo'))
async def send_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMMZtc6zXyM4F1TkizFoIjLn_9TO5cAAlDkMRsD5bhKdRe45vUz5iEBAAMCAAN5AAM1BA', caption='This is porn')

@router.callback_query(F.data == 'settings')
async def settings(callback: CallbackQuery):
    await callback.answer("degradant poshel nahooy", show_alert=True)
    await callback.message.answer('settings blyat')

@router.message(Command('registration'))
async def registration(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Enter ur name: ')

@router.message(Reg.name)
async def registration_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Enter ur number: ')

@router.message(Reg.number)
async def registration_stop(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Thanks, reg is completed!\nName:{data["name"]}\nPhone:{data["number"]}')
    await state.clear()