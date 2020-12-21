import telebot
from telebot import types
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TOKEN")
PFAD = os.getenv("PFAD")
print(TOKEN)
print(PFAD)
bot = telebot.TeleBot(TOKEN)

# query.query == "Text der nach @JoergenBot eingegeben muss, 
# damit die Liste getriggert wird
@bot.inline_handler(lambda query: query.query == "samples")
def query_text(inline_query):
    r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
    r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
    r3 = types.InlineQueryResultAudio('3', PFAD, "yeet")
    bot.answer_inline_query(inline_query.id, [r, r2, r3])
    print("inline triggered")

print("Bot lüppt")
bot.polling()
