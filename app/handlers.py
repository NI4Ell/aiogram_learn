from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class Registration(StatesGroup):
    name = State()
    number = State()
    id = State()


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
    await callback.answer('')
    await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())


@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer('Введите ваше имя')


@router.message(Registration.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Registration.id)
    await state.update_data(id = message.from_user.id)
    await state.set_state(Registration.number)
    await message.answer('Предоставьте доступ к номеру', reply_markup= kb.number)


@router.message(Registration.number)
async def reg_final(message: Message, state: FSMContext):
    await state.update_data(number = message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершена!\nИмя: {data["name"]}\nНомер: {data["number"]}\nID: {data["id"]}')
    await state.clear()
