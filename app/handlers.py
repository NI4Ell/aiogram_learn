from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет! {message.from_user.first_name}!\nПодпишись на меня!', reply_markup=kb.main)

@router.message(Command('help'))
async def command_help(message: Message):
    await message.answer('Команда помощи /help')

@router.message(F.text =="Как дела?" )
async def how_are_you(message: Message):
    await message.answer("Отлично!") 

@router.message(F.text == "Бубусик")
async def get(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMNZh7Ssp2A54tKu3j8Vv6jjQABlNMlAAIb2jEbigrxSKlK-OxA61ToAQADAgADeQADNAQ',
                        caption="Мой бубусик")

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.message.answer('Привет!')