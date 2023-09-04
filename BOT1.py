#!/usr/bin/env python
# -*- coding:h o d e -*-
# ---------------------
# Telegram : @U_OOS
# Coded by WESTON
# ---------------------
import telebot,requests
from telebot import types


bot = telebot.TeleBot("6643322721:AAEzdVsxjrpv-qGvEXnfesb_RjyCWZj0wwg")

@bot.message_handler(commands=['start'])
def start(message):
	mark = types.InlineKeyboardMarkup(row_width=1)
	s1 =types.InlineKeyboardButton("• قناة لبوت •",url =f"https://t.me/TMPHE")
	mark.add(s1)			
	bot.send_message(message.chat.id,"""⟠  بوت تحويل نص الى GIF . 
⟠ يمكن تحويل نص بسهوله الى اكثر من شكل.
⟠ فقط قم بإرسال نص ! .
╌ ╌ ╌ ╌ ╌ ╌ ╌ ╌ ╌ ╌""",reply_markup=mark)
 
 
@bot.message_handler(func=lambda message: True)
def Re(message):
	res = requests.get("https://api.codebazan.ir/image/?type=gif&text="+message.text).json()
	for key in res:
		value = res[key]
		try:
			if "https:" in value:
				bot.send_audio(message.chat.id,value,"• Tele : @U_OOS ")
		except:
			pass


bot.infinity_polling(timeout=10, long_polling_timeout = 5)							