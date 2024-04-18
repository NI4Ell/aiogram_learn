from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts'), InlineKeyboardButton(text='Корзина', callback_data='basket')],
    
])

number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Предоставить доступ', request_contact=True)]

])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/kirusha_zaidal')]

])
cars = ['Tesla', 'BMW', 'Mersedes']
async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car}'))
    return keyboard.adjust(2).as_markup()