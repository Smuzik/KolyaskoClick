import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

# Токен вашего бота от BotFather
TOKEN = '7445203193:AAGBAALcpZjqnVBLj3Dqc98AUfhzGNjLJKw'
# URL вашего веб-приложения, развернутого на GitHub Pages или другом хостинге
WEBAPP_URL = 'https://github.com/Smuzik/KolyaskoClick'

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    web_app_info = WebAppInfo(url=WEBAPP_URL)
    keyboard.add(InlineKeyboardButton("КоляскоКликер", web_app=web_app_info))
    await message.answer("Запусти КоляскоКликер!", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)