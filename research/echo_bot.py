import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types



load_dotenv()
API_TOKEN = os.getenv("TOKEN")
print(API_TOKEN)

logging.basicConfig(level=logging.INFO)

#Initilaize the Bot
bot = Bot(token=API_TOKEN)
dp  =Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message:types.Message):

    await message.reply("Hi!\n I am an Echo Bot! Powered by Aiogram")



@dp.message_handler()
async def echo(message:types.Message):

    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
