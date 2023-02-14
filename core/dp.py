import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Configure logging
logging.basicConfig(level=logging.INFO)

API_TOKEN = "6129587666:AAF922W5WGJS1_f-IXxfcz9VlJPs_73t4nE"

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

print("Auth bot")
