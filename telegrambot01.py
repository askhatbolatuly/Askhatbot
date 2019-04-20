import telegram
from telegram import Bot
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, Filters

token = "878689008:AAGr6QALc6jNhy4lMI1Ct-Wv56yE126SgSI"

admin = Bot("893384171:AAGpcZlLtoI4KiiNVM-2Es_hI9iZcCEh-lQ")


def start(update, context):
  chat_id = update.message.chat_id
  text = update.message.text
  print(chat_id)

  context.bot.send_message(chat_id=chat_id, text='Hello!\nThis is Beaty Bot!'
  )

def prefer(update, context):
  chat_id = update.message.chat_id
  text = update.message.text
  
  buttons = [['Косметика', 'Парфюм']]
  m = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)

  context.bot.send_message(chat_id=chat_id,
    text='Выбери тип товара',
    reply_markup=m)
  return 1

def first(update, context):
  chat_id = update.message.chat_id
  text = update.message.text

  user_data = context.user_data
  user_data['type'] = text

  context.bot.send_message(chat_id=chat_id,
    text='Укажи название товара')
  return 2

def second(update, context):
  chat_id = update.message.chat_id
  text = update.message.text

  user_data = context.user_data
  user_data['item'] = text

  context.bot.send_message(chat_id=chat_id,
    text='Укажи адрес')
  return 3

def third(update, context):
  chat_id = update.message.chat_id
  text = update.message.text

  user_data = context.user_data
  user_data['address'] = text

  context.bot.send_message(chat_id=chat_id,
    text='Спасибо! Заказ принят!')
  admin.send_message(chat_id=389337650,
    text=f'Новый заказ:\n{user_data}')
  return ConversationHandler.END

def cancel(update, context):
  chat_id = update.message.chat_id
  text = update.message.text

  context.bot.send_message(chat_id=chat_id,
    text='Ты отменил!')
  return ConversationHandler.END

updater = Updater(token, use_context=True)

disp = updater.dispatcher

start_handler = CommandHandler('start', start)

dialog_handler = ConversationHandler(
  entry_points=[CommandHandler('prefer', prefer)],
  states={
    1: [MessageHandler(Filters.text, first, pass_user_data=True)],
    2: [MessageHandler(Filters.text, second, pass_user_data=True)],
    3: [MessageHandler(Filters.text, third, pass_user_data=True)]
  },
  fallbacks=[CommandHandler('cancel', cancel, pass_user_data=True)]
)

disp.add_handler(start_handler)
disp.add_handler(dialog_handler)

updater.start_polling()
updater.idle()