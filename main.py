
import telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler, ConversationHandler# для комангд
from telegram.ext import MessageHandler,Filters# для сообщения

token='870748119:AAHwjuhLx00RrzypTKCsB56N6Ucol2rmUUA'

upd = Updater(token, use_context=True)

def start(update, context):
  chat_id = update.message.chat_id

  context.bot.send_message(chat_id=chat_id, text='список команды:\n/booking(все кабинеты\n/help )')

def help(update, context):
  chat_id = update.message.chat_id

  context.bot.send_message(chat_id=chat_id, text='Чем я могу Вам  помочь?, наши кардинаторы 7777')

def text(update, context):
  chat_id = update.message.chat_id
  text = update.message.text

  context.bot.send_message(chat_id=chat_id, text=f"Ты ввел:{text}")
  
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)
    
def booking(update, context):
  chat_id = update.message.chat_id
  buttons = [[' 1клас"Алтын кол"','2','3','4']]
  a=ReplyKeyboardMarkup(buttons, two_time_keyboard=True)
  context.bot.send_message(chat_id=chat_id, text='Выберите комнату',reply_markup=a)
  return 1

def first(update, context):
  chat_id = update.message.chat_id
  text = update.message.text

  print(text)
  context.bot.send_message(chat_id=chat_id, text='На какое время?')
  return 2

def data(update,context):
  chat_id = update.message.chat_id
  text = update.message.text
  print(text)
  context.bot.send_message(chat_id=chat_id, text='Ok!')
  return ConversationHandler.END


def second(update, context):
  chat_id = update.message.chat_id
  text = update.message.text

  print(text)
  context.bot.send_message(chat_id=chat_id, text='На какое число?')
  return 3

def cancel(update, context):
  chat_id = udpate.message.chat_id
  context.bot.send_message(chat_id=chat_id, text='Ты отменил!')
  return ConversationHandler.END

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
dialog = ConversationHandler(
  entry_points=[CommandHandler('booking', booking)],
  states={
    1:[MessageHandler(Filters.text, first)],
    2:[MessageHandler(Filters.text, second)],
    3:[MessageHandler(Filters.text, data)]
    #4:[MessageHandler(Filter.text,data)
  },
  fallbacks=[CommandHandler('cancel', cancel)]
)
text_handler = MessageHandler(Filters.text, text)

dis = upd.dispatcher
dis.add_handler(start_handler)
dis.add_handler(dialog)
dis.add_handler(text_handler)
dis.add_handler(help_handler)
upd.start_polling()
upd.idle()