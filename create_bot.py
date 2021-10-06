from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher

from config import TOKEN

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)