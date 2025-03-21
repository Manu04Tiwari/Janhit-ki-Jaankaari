# 1. Enable Logging
# we want to know about the activities(warning,errors) in a systematic manner
# thats why we need logging
import logging
from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update, ReplyKeyboardMarkup
from utils import get_reply, fetch_news, topics_keyboard

# logger object will help us create the logs in this program
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


TOKEN = "1701925941:AAHNOV5z5z6S100tno5eqO1fMnytLfnHq74"


app=Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    """webhook view which receives updates from telegram"""
    # create update object from json-format request data
    update = Update.de_json(request.get_json(), bot)
    # process update
    dp.process_update(update)
    return "ok"


# CommandHandlers
# def start(bot, update):
#     print(update)
#     author=update.message.from_user.first_name
#     # msg=update.message.text
#     reply="Hi! {}",format(author)
#     bot.send_message(chat_id=update.message.chat_id, text=reply)
def start(update, context):
   print(update)
   author=update.message.from_user.first_name
   reply="Hi! {}".format(author)
   context.bot.sendMessage(chat_id=update.message.chat_id, text=reply)

def _help(update, context):
    help_text="Hey! This is a help text."
    context.bot.send_message(chat_id=update.message.chat_id, text=help_text)

def news(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Choose a catagory",
                reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard, one_time_keyboard=True))

def reply_text(update, context):
    """callback function for text message handler"""
    intent, reply = get_reply(update.message.text, update.message.chat_id)
    if intent == "get_news":
        articles = fetch_news(reply)
        for article in articles:
            context.bot.send_message(chat_id=update.message.chat_id, text=article['link'])
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text=reply)


def echo_sticker(update, context):
    context.bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)
def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update, update.error)

    # this will try to recieve updates for the bot

# this will keep on handling the updates

# def main():

bot = Bot(TOKEN)
try:
    bot.set_webhook("https://ancient-caverns-72036.herokuapp.com/" + TOKEN)
    time.sleep(5)
except Exception as e:
    print(e)

dp = Dispatcher(bot, None)
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", _help))
dp.add_handler(CommandHandler("news", news))
dp.add_handler(MessageHandler(Filters.text, reply_text))
dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
dp.add_error_handler(error)

if __name__=="__main__":

    app.run(port=8443)
