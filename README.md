<h1 align="center">ChatGpt 3.5 telegram bot </h1>

<p>В этом боте ты можешь использовать <b>GPT 3.5</b>, для начала работы нужно изменить задать токен бота и openai api ключ</p>



<h2>Инструкция по использованию</h2>

<p>1. Создаем бота и получаем его токен в телеграм боте https://t.me/BotFather</p>
<p>2. Получаем open ai api ключ по ссылке https://platform.openai.com/account/api-keys</p>
<p>3. Открываем файл с ботом и в 6 строчке в переменную TOKEN в ковечках вставляем токен бота</p>
<p>4. Вставляем в ковычки наш токен и в следующей строчке api ключ</p>

```python
TOKEN = ''
openai.api_key = ''
```

<p>5. Устанавливаем python</p>
<p>6. Устанавливаем зависимости</p>

```
pip install openai  
pip install aiogram
```

<p>7. Запускаем бота</p>

```
python bot.py
```
