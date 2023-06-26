from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import text
import stickers
import enchant
import kb

router = Router()
dictionary = enchant.Dict("en_US")


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer_sticker(stickers.STICKER_HELLO, reply_markup=kb.create_markup(types))
    await msg.answer(f'Привет, {msg.from_user.first_name}! {text.GREENENG}\n\n{text.RULES} "A"')


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
