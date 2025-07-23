import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
import os

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_1 = os.getenv("ADMIN_1")
ADMIN_2 = os.getenv("ADMIN_2")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

admins = [ADMIN_1, ADMIN_2]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Tilni tanlang:\nВыберите язык:", reply_markup=language_keyboard())

def language_keyboard():
    buttons = [
        types.KeyboardButton(text="🇺🇿 O‘zbekcha"),
        types.KeyboardButton(text="🇷🇺 Русский"),
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
