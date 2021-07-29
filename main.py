# from pyrogram import Client
# from pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
#     InlineKeyboardButton, CallbackQuery
#
# # api_id = 3319961
# # api_hash = '4b29dfcc07e782dcc4a03366d74b19a8'
# # bot_token = '1665126021:AAEOgJrigY8eLpr49gk8c8b6a-Mrd1YHA-E'
# # app = Client(session_name='mybot', bot_token=bot_token,
# #                 api_id=api_id, api_hash=api_hash)
#
# # add config.ini and delete this config.ini
#
#
# app = Client('mybot')
# data = []
#
# class MyUser:
#     def __init__(self,user_id):
#         self.id = user_id
#         self.state = 0
#         self.age = None
#         self.name = None
#
#
# def check_user(user_id):
#
#     for user in data:
#         if user_id == user.id:
#             return user
#
#     new_user = MyUser(user_id)
#     data.append(new_user)
#     return new_user
#
# def IKM(data):
#
#     return InlineKeyboardMarkup([[InlineKeyboardButton(text,cd) for text,cd in data]])
#
#
# @app.on_message()
# def my_handler(client: Client,message: Message):
#     # print(message)
#
#     # if message["text"]:
#     #     client.send_message(chat_id=message["chat"]["id"],text=message["text"],reply_markup=ReplyKeyboardMarkup([["salme","khodahfez"],["back"]],resize_keyboard=True))
#     # elif message["voice"]:
#     #     print(message)
#     #     client.send_voice(chat_id=message.chat.id,voice=message.voice.file_id)
#     # elif message["document"]:
#     #     client.send_document(chat_id=message.chat.id, document=message.document.file_id)
#     # else:
#     #     print(message)
#
#     """
#     part 2
#     """
#     # user = check_user(message.from_user.id)
#     # if message.chat.type != 'private':
#     #     return
#     # if message.text:
#     #     if message.text == '/start':
#     #         client.send_message(user.id,'welcome',reply_markup=ReplyKeyboardMarkup([['set name','set age'],['about']],resize_keyboard=True))
#     #
#     #     elif message.text == 'set name':
#     #         user.state = 1
#     #         client.send_message(user.id,'enter your name: ', reply_markup=ReplyKeyboardRemove())
#     #
#     #     elif message.text == 'set age':
#     #         user.state = 2
#     #         client.send_message(user.id,'enter your age: ', reply_markup=ReplyKeyboardRemove())
#     #
#     #     elif message.text == 'about':
#     #         client.send_message(user.id,f'name:{user.name}\nAge:{user.age}')
#     #
#     #     elif user.state == 1:
#     #         user.name = message.text
#     #         user.state = 0
#     #         client.send_message(user.id,'your name saved',reply_markup=ReplyKeyboardMarkup([['set name','set age'],['about']],resize_keyboard=True))
#     #
#     #     elif user.state == 2:
#     #
#     #         user.age = message.text
#     #         user.state = 0
#     #         client.send_message(user.id, 'your age saved',
#     #                             reply_markup=ReplyKeyboardMarkup([['set name', 'set age'], ['about']],
#     #                                                              resize_keyboard=True))
#     """
#     part 3
#     """
#     user = check_user(message.from_user.id)
#     if message.chat.type != 'private':
#         return
#     if message.text:
#         if message.text == '/start':
#             user.state = 0
#             client.send_message(user.id,'welcome',reply_markup=IKM([('dr keshrkaran',)]))
#
# @app.on_callback_query()
# def handle_callback_query(bot: Client,query:CallbackQuery):
#     print(query.data)
#     bot.answer_callback_query(query.id,f'got{query.data}!!',show_alert=True)
#
# app.run()
#

"""part 4 inlinekeybort"""
from pyrogram import Client
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery


def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])


client = Client('mybot')

data = []
MAIN_KEYBOARD = ReplyKeyboardMarkup([['set name', 'set age'], ['my profile']], resize_keyboard=True)
TEACHERS_INLINEKB = IKM([('Dr Keshtkaran', 'TCH0'), ('Dr Hamze', 'TCH1'), ('Dr Sami', 'TCH2')])


class MyUser:
    def __init__(self, user_id):
        self.id = user_id
        self.state = 0
        self.name = None
        self.age = None


def check_user(user_id):
    for user in data:
        if user_id == user.id:
            return user
    new_user = MyUser(user_id)
    data.append(new_user)
    return new_user


@client.on_message()
def handle_message(bot: Client, message: Message):
    user = check_user(message.from_user.id)
    if message.chat.type != 'private':
        return
    if message.text:
        if message.text == '/start':
            user.state = 0
            bot.send_message(user.id, 'welcome', reply_markup=TEACHERS_INLINEKB)


teachers = ['دکتر کشتکاران', 'دکتر حمزه', 'دکتر سامی']


@client.on_callback_query()
def handle_callback_query(bot: Client, query: CallbackQuery):
    if query.data.startswith('TCH'):
        i = int(query.data[3:])
        bot.edit_message_text(query.message.chat.id, query.message.message_id, teachers[i],
                              reply_markup=TEACHERS_INLINEKB)


client.run()