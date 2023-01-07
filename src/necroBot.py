import logging
from pathlib import Path
from aiogram import Bot, Dispatcher, executor, types

TG_BOT_TOKEN = Path('telegram-bot.token').read_text()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher(bot)
username = 'NecronWasTaken'


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # smth
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # smth
    await message.answer(message.text)


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
