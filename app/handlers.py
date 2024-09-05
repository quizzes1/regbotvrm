from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.requests as rq
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f'Nice to meet you! Welcome to our sneakers shop!',
                        reply_markup=kb.main)

@router.message(F.text == 'Catalogue')
async def catalog(message: Message):
    await message.answer('Choose the category', reply_markup=await kb.categories())
    
@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('You have chosen the category')
    await callback.message.answer('Choose the item by category', reply_markup=await kb.items(callback.data.split('_')[1]))
    
@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    await callback.answer('You have chosen the item')
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.message.answer(f'Name: {item_data.name}\nDescription: {item_data.description}\nPrice: {item_data.price}$', reply_markup=await kb.items(callback.data.split('_')[1]))
    