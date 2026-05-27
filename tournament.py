import telebot
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Replace this with your actual BotFather token
TOKEN = "8448397148:AAGcZn9K--yop72HJycJrGXJazA0tTUOQhs"

bot = telebot.TeleBot(TOKEN)

def get_main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("🎮 የቀጥታ ውድድር ፈልግ (Find Match)"))
    markup.row(KeyboardButton("👤 የእኔ አካውንት"), KeyboardButton("📊 የአሸናፊዎች ሰሌዳ"))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "🏆 እንኳን በደህና መጡ ወደ ቶርናመንት መድረክ! 🏆", reply_markup=get_main_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if "👤 የእኔ አካውንት" in message.text:
        bot.send_message(message.chat.id, "👤 ይህ የእርስዎ መገለጫ ነው።")
    elif "📊 የአሸናፊዎች ሰሌዳ" in message.text:
        bot.send_message(message.chat.id, "📊 አሁን በውድድር ላይ ያሉ ምርጥ ተጫዋቾች ዝርዝር...")
    elif "🎮 የቀጥታ ውድድር ፈልግ" in message.text:
        bot.send_message(message.chat.id, "📡 ተወዳዳሪ በመፈለግ ላይ... እባክዎን ይጠብቁ።")
    else:
        bot.send_message(message.chat.id, "እባክዎን ከታች ካሉት አማራጮች አንዱን ይምረጡ።")

if __name__ == '__main__':
    print("Bot is starting...")
    bot.infinity_polling()