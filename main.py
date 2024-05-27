from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN_API = '7429575332:AAHa7x5o6u6LfkcPDOeMLbG6Yl3Bt64LZJc'
bot = Bot(token = TOKEN_API)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Команда для того,чтобы включить бота'),
        types.BotCommand(command='/help', description='Команда для того,чтобы помочь с вашей проблемой')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands="start")
async def start(message: types.message):
    await message.reply('Привет,я твой бот')

@dp.message_handler(commands="help")
async def start(message: types.message):
    await message.answer('С чем тебе помочь')


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)
