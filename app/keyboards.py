from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)
from app.requests import get_categories, get_item_category
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зарегистрировать нового пользователя🧑‍💼')], 
    [KeyboardButton(text='Расписание игр📅')],
    [KeyboardButton(text='Связаться с нами📲' )],
    [KeyboardButton(text='Наш ТГ-канал📟' )]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите действие:')

# registration_keyboard = ReplyKeyboardMarkup(keyboard=[
    
# ])




# async def categories():
#     all_categories = await get_categories()
#     keyboard = InlineKeyboardBuilder()
#     for category in all_categories:
#         keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
#     keyboard.add(InlineKeyboardButton(text='Main menu', callback_data='to_main'))
#     return keyboard.adjust(2).as_markup()

# async def items(category_id):
#     all_items = await get_item_category(category_id)
#     keyboard = InlineKeyboardBuilder()
#     for item in all_items:
#         keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
#     keyboard.add(InlineKeyboardButton(text='Main menu', callback_data='to_main'))
#     return keyboard.adjust(2).as_markup()