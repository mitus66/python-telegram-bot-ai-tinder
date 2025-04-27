# DAY 1
# from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
#
# from gpt import *
# from util import *
#
# # тут будемо писати наш код :)
# TOKEN = ""
#
# async def start(update, context):
#     # await send_photo(update, context, "avatar_main")
#     # await send_text(update, context, "Hallo, user")
#     msg = load_message("main")
#     await send_text(update, context, msg)
#
# async def hello(update,context):
#     # await send_text(update,context, "Hello" + update.message.text)
#     await send_text_buttons(update, context, "Hello" + update.message.text, {
#         "start": "START",
#         "stop": "STOP",
#     })
#
# async def buttons_handler(update, context):
#     query = update.callback_query.data
#     if query == "start":
#         await send_text(update, context, "Started")
#     elif query == "stop":
#         await send_text(update, context, "Stopped")
#
# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
# app.add_handler(CallbackQueryHandler(buttons_handler))
# app.run_polling()
# __________________________________________________________________________

# DAY 2
# from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
#
# from gpt import *
# from util import *
#
# # тут будемо писати наш код :)
# TOKEN = ""
#
# async def start(update, context):
#     msg = load_message("main")
#     await send_photo(update, context, "main")
#     await send_text(update, context, msg)
#     await show_main_menu(update, context, {
#         "start": "Main menu",
#         "profile": "Tinder-profile generation \uD830\uDE0E",
#         "opener": "Dating message \uD83E\uDD70",
#         "message": "Correspondence on your behalf \uD83D\uDE08",
#         "date": "Communicating with the stars \uD83D\uDD25",
#         "gpt": "Ask a question ChatGPT \uD83E\uDDE0",
#     })
#
# async def gpt(update, context):
#     dialog.mode = "gpt"
#     await send_photo(update, context, "gpt")
#     msg = load_message("gpt")
#     await send_text(update, context, msg)
#
# async def gpt_dialog(update, context):
#     text = update.message.text
#     prompt = load_prompt("gpt")
#     answer = await chatgpt.send_question(prompt, text)
#     await send_text(update, context, answer)
#
# async def hello(update,context):
#     if dialog.mode == "gpt":
#         await gpt_dialog(update, context)
#
# #
# dialog = Dialog()
# dialog.mode = None
#
# chatgpt = ChatGptService(token="")
#
# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("gpt", gpt))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
# # app.add_handler(CallbackQueryHandler(buttons_handler))
# app.run_polling()
# __________________________________________________________________________

# DAY 3
# from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
#
# from gpt import *
# from util import *
#
# TOKEN = ""
#
# # тут будемо писати наш код :)
#
# async def start(update, context):
#     msg = load_message("main")
#     await send_photo(update, context, "main")
#     await send_text(update, context, msg)
#     await show_main_menu(update, context, {
#         "start": "Main menu",
#         "profile": "Tinder-profile generation \uD830\uDE0E",
#         "opener": "Dating message \uD83E\uDD70",
#         "message": "Correspondence on your behalf \uD83D\uDE08",
#         "date": "Communicating with the stars \uD83D\uDD25",
#         "gpt": "Ask a question ChatGPT \uD83E\uDDE0",
#     })
#
#
# async def gpt(update, context):
#     dialog.mode = "gpt"
#     await send_photo(update, context, "gpt")
#     msg = load_message("gpt")
#     await send_text(update, context, msg)
#
#
# async def gpt_dialog(update, context):
#     text = update.message.text
#     prompt = load_prompt("gpt")
#     answer = await chatgpt.send_question(prompt, text)
#     await send_text(update, context, answer)
#
#
# async def date(update, context):
#     dialog.mode = "date"
#     msg = load_message("date")
#     await send_photo(update, context, "date")
#     await send_text_buttons(update, context, msg, {
#         "date_grande": "Аріана Гранде",
#         "date_robbie": " Марго Роббі",
#         "date_zendaya": "Зендея",
#         "date_gosling": "Райан Гослінг",
#         "date_hardy": "Том Харді",
#     })
#
#
# async def date_button(update, context):
#     query = update.callback_query.data
#     await update.callback_query.answer()
#     await send_photo(update, context, query)
#     await send_text(update, context, "Гарний вибір. \uD83D\uDE05 Ваша задача запросити дівчину/хлопця на побачення за 5 повідомлень! \uFE0F")
#     prompt = load_prompt(query)
#     chatgpt.set_prompt(prompt)
#
#
# async def date_dialog(update, context):
#     text = update.message.text
#     my_message = await send_text(update, context, "type answer...")
#     answer = await chatgpt.add_message(text)
#     await my_message.edit_text(answer)
#
#
# async def message(update, context):
#     dialog.mode = "massage"
#     msg = load_message("message")
#     await send_photo(update, context, "message")
#     await send_text_buttons(update, context, msg, {
#         "message_next": "Написати повідомлення",
#         "message_date": "Запросити на побачення",
#     })
#     dialog.list.clear()
#
#
# async def message_dialog(update, context):
#     text = update.message.text
#     dialog.list.append(text)
#
#
# async def message_button(update, context):
#     query = update.callback_query.data
#     await update.callback_query.answer()
#
#     prompt = load_prompt(query)
#     user_chat_history = "\n\n".join(dialog.list)
#
#     my_message = await send_text(update, context, "Думаю над варіантами...")
#     answer = await chatgpt.send_question(prompt, user_chat_history)
#     await my_message.edit_text(answer)
#
#
# async def hello(update,context):
#     if dialog.mode == "gpt":
#         await gpt_dialog(update, context)
#     elif dialog.mode == "date":
#         await date_dialog(update, context)
#     elif dialog.mode == "message":
#         await message_dialog(update, context)
#
# #
# dialog = Dialog()
# dialog.mode = None
# dialog.list = []
#
# chatgpt = ChatGptService(token="")
#
# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("gpt", gpt))
# app.add_handler(CommandHandler("date", date))
# app.add_handler(CommandHandler("message", message))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
# app.add_handler(CallbackQueryHandler(date_button, pattern="^date_.*"))
# app.add_handler(CallbackQueryHandler(message_button, pattern="^message_.*"))
# app.run_polling()
# __________________________________________________________________________

# DAY 4
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

TOKEN = ""

# тут будемо писати наш код :)

async def start(update, context):
    msg = load_message("main")
    await send_photo(update, context, "main")
    await send_text(update, context, msg)
    await show_main_menu(update, context, {
        "start": "Main menu",
        "profile": "Tinder-profile generation \uD830\uDE0E",
        "opener": "Dating message \uD83E\uDD70",
        "message": "Correspondence on your behalf \uD83D\uDE08",
        "date": "Communicating with the stars \uD83D\uDD25",
        "gpt": "Ask a question ChatGPT \uD83E\uDDE0",
    })


async def gpt(update, context):
    dialog.mode = "gpt"
    await send_photo(update, context, "gpt")
    msg = load_message("gpt")
    await send_text(update, context, msg)


async def gpt_dialog(update, context):
    text = update.message.text
    prompt = load_prompt("gpt")
    answer = await chatgpt.send_question(prompt, text)
    await send_text(update, context, answer)


async def date(update, context):
    dialog.mode = "date"
    msg = load_message("date")
    await send_photo(update, context, "date")
    await send_text_buttons(update, context, msg, {
        "date_grande": "Аріана Гранде",
        "date_robbie": " Марго Роббі",
        "date_zendaya": "Зендея",
        "date_gosling": "Райан Гослінг",
        "date_hardy": "Том Харді",
    })


async def date_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()
    await send_photo(update, context, query)
    await send_text(update, context, "Гарний вибір. \uD83D\uDE05 Ваша задача запросити дівчину/хлопця на побачення за 5 повідомлень! \uFE0F")
    prompt = load_prompt(query)
    chatgpt.set_prompt(prompt)


async def date_dialog(update, context):
    text = update.message.text
    my_message = await send_text(update, context, "type answer...")
    answer = await chatgpt.add_message(text)
    await my_message.edit_text(answer)


async def message(update, context):
    dialog.mode = "massage"
    msg = load_message("message")
    await send_photo(update, context, "message")
    await send_text_buttons(update, context, msg, {
        "message_next": "Написати повідомлення",
        "message_date": "Запросити на побачення",
    })
    dialog.list.clear()


async def message_dialog(update, context):
    text = update.message.text
    dialog.list.append(text)


async def message_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()

    prompt = load_prompt(query)
    user_chat_history = "\n\n".join(dialog.list)

    my_message = await send_text(update, context, "Думаю над варіантами...")
    answer = await chatgpt.send_question(prompt, user_chat_history)
    await my_message.edit_text(answer)


async def profile(update, context):
    dialog.mode = "profile"
    msg = load_message("profile")
    await send_photo(update, context, "profile")
    await send_text(update, context, msg)

    dialog.user.clear()
    dialog.counter = 0
    await send_text(update, context, "Скільки вам років?")


async def profile_dialog(update, context):
    text = update.message.text
    dialog.counter += 1

    if dialog.counter == 1:
        dialog.user["age"] = text
        await send_text(update, context, "Ким ви працюєте?")
    if dialog.counter == 2:
        dialog.user["occupation"] = text
        await send_text(update, context, "Які ваши хобі?")
    if dialog.counter == 3:
        dialog.user["hobby"] = text
        await send_text(update, context, "Що вам НЕ подобається в людях?")
    if dialog.counter == 4:
        dialog.user["annoys"] = text
        await send_text(update, context, "Мета знайомства?")
    if dialog.counter == 5:
        dialog.user["goals"] = text
        prompt = load_prompt("profile")
        user_info = dialog_user_info_to_str(dialog.user)

        my_message = await send_text(update, context, "ChatGPT генерує ваш профіль. Зачекайте декілька секунд...")
        answer = await chatgpt.send_question(prompt, user_info)
        await  my_message.edit_text(answer)


async def opener(update, context):
    dialog.mode = "opener"
    msg = load_message("opener")
    await send_photo(update, context, "opener")
    await send_text(update, context, msg)

    dialog.user.clear()
    dialog.counter = 0
    await send_text(update, context, "Ім'я партнера?")

async def opener_dialog(update, context):
    text = update.message.text
    dialog.counter += 1

    if dialog.counter == 1:
        dialog.user["name"] = text
        await send_text(update, context, "Скільки років партнеру?")
    if dialog.counter == 2:
        dialog.user["age"] = text
        await send_text(update, context, "Оцінить зовнішність: 1-10?")
    if dialog.counter == 3:
        dialog.user["handsome"] = text
        await send_text(update, context, "Ким вона працює?")
    if dialog.counter == 4:
        dialog.user["occupation"] = text
        await send_text(update, context, "Мета знайомства?")
    if dialog.counter == 5:
        dialog.user["goals"] = text

        prompt = load_prompt("opener")
        user_info = dialog_user_info_to_str(dialog.user)

        my_message = await send_text(update, context, "ChatGPT генерує ваше повідомлення. Зачекайте декілька секунд...")
        answer = await chatgpt.send_question(prompt, user_info)
        await  my_message.edit_text(answer)


async def hello(update,context):
    if dialog.mode == "gpt":
        await gpt_dialog(update, context)
    elif dialog.mode == "date":
        await date_dialog(update, context)
    elif dialog.mode == "message":
        await message_dialog(update, context)
    elif dialog.mode == "profile":
        await profile_dialog(update, context)
    elif dialog.mode == "opener":
        await opener_dialog(update, context)

#
dialog = Dialog()
dialog.mode = None
dialog.list = []
dialog.user = {}
dialog.counter = 0

chatgpt = ChatGptService(token="")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gpt", gpt))
app.add_handler(CommandHandler("date", date))
app.add_handler(CommandHandler("message", message))
app.add_handler(CommandHandler("profile", profile))
app.add_handler(CommandHandler("opener", opener))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
app.add_handler(CallbackQueryHandler(date_button, pattern="^date_.*"))
app.add_handler(CallbackQueryHandler(message_button, pattern="^message_.*"))
app.run_polling()