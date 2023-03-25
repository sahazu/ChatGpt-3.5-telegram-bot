import asyncio

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import openai

TOKEN = 'YOUR TELEGRAM BOT KEY'
openai.api_key = "YOUR OPEN AI API KEY"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
]

def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет, в этом боте ты можешь использовать <b>GPT 3.5</b>, просто отправь свой запрос", parse_mode=types.ParseMode.HTML)

@dp.message_handler()
async def prompt(message: types.Message):
    if message.text != "start":
        sent_message = await message.answer("<b>ChatGPT генерирует ответ...</b>", parse_mode=types.ParseMode.HTML)
        update(messages, "user", message.text)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
        )
        await bot.delete_message(chat_id=sent_message.chat.id, message_id=sent_message.message_id)
        await message.answer(response['choices'][0]['message']['content'])

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
