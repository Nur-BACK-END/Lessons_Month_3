# import random
# from aiogram import types
# from config import bot
#

# async def game(message: types.Message):
#     dice_random = random.choice(['⚽', '🎰', '🏀', '🎯', '🎳', '🎲'])
#     await bot.send_dice(chat_id=message.from_user.id, emoji=dice_random)


# def register_echo_handlers(dp: Dispatcher):
#     dp.register_message_handler(game, commands=['game'])
#     dp.register_message_handler(echo_handler)

