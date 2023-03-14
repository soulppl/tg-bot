import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv, find_dotenv


# Configure logging
logging.basicConfig(level=logging.INFO)

load_dotenv(find_dotenv())
API_TOKEN = os.getenv("BOT_API_TOKEN")

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

