import asyncio
import logging
import sys
from os import getenv
import wikipedia
import requests
import json
from uzwords import words
from difflib import get_close_matches
from CheckWord import checkWord, notMatches, mavjud
from difflib import get_close_matches


from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

bot = Bot(token='7065448388:AAEdosm8jYko3g03olNhNAK4mcKvaQHnNbA')
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply(f"Салом {message.from_user.full_name}, WordFixer ботга хуш келибсиз!")


@dp.message(Command('help'))
async def help_user(message: types.message) -> None:
    await message.reply("Бу ботдан фойдаланиш учун сўз юборинг(фақат кирилча)")


@dp.message()
async def checkImlo(message: types.Message):
    input_str = message.text
    if len(input_str) == 1:
        mavjud(input_str)

    else:
        counter = input_str.split()
        print(counter)
        for i in counter:
            await message.answer(f'{mavjud(i)}')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
