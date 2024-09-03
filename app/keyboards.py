from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='hey')], 
    [KeyboardButton(text='idi nahooy'), KeyboardButton(text='zhopa')]
],
                           resize_keyboard=True,
                           input_field_placeholder='choose the point of the menu')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='settings', callback_data='settings')],
    [InlineKeyboardButton(text='check your mother', callback_data='checkmom')]
])