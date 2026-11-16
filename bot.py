
import telebot
import json

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

bot = telebot.TeleBot(config["BOT_TOKEN"])

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.row("🖥 Управление ПК")
    keyboard.row("📸 Скриншоты", "🎵 Музыка")
    keyboard.row("⚙️ Настройки")

    bot.send_message(
        message.chat.id,
        "PC Helper запущен!\nВыбери раздел:",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == "🖥 Управление ПК":
        bot.send_message(message.chat.id, "Раздел управления ПК")
    elif message.text == "📸 Скриншоты":
        bot.send_message(message.chat.id, "Раздел скриншотов")
    elif message.text == "🎵 Музыка":
        bot.send_message(message.chat.id, "Раздел музыки")
    elif message.text == "⚙️ Настройки":
        bot.send_message(message.chat.id, "Настройки PC Helper")

bot.infinity_polling()

