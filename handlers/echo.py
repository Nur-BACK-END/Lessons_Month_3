# echo.py
from aiogram import types, Dispatcher
from config import bot
import random


async def echo_handler(message: types.Message):
    await message.answer("Я не понимаю твое сообщение")
    await message.delete()


async def game(message: types.Message):
    dice_random = random.choice(['⚽', '🎰', '🏀', '🎯', '🎳', '🎲'])
    await bot.send_dice(chat_id=message.from_user.id, emoji=dice_random)


def register_echo_handlers(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(echo_handler)
