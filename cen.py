#!/usr/bin/python
# -*- coding: utf-8 -*-
import discord
import random

tfile = open('token.txt', 'r')
TOKEN = tfile.read()
client = discord.Client()
euromess = [
'I am confused...',
'Je suis confus...',
'Ich bin verwirrt...',
'Ik ben in de war...',
'Estoy confundido...',
'Sono confuso...',
'Jam i hutuar...',
'Ja sam zbunjen...',
'Jeg er forvirret...',
'Ma olen segaduses...',
'Olen hämilläni...',
'Eímai berdeménos...',
'Ég er ringlaður...',
'Esmu apjukusi...',
'Aš sutrikęs...',
'Ech sinn duercherneen...',
'Jas sum zbunet...',
'Jiena konfuż...',
'Ya zbentezhenyy...',
'Jestem zdezorientowany...',
'Estou confuso...',
'Sunt confuz...',
'Ya zaputalsya...',
'Zbunjen sam...',
'Som zmätený...',
'Zmeden sem...',
'Jsem zmatený...',
'Ya zasmuchany...',
'Jag är förvirrad...'
]

helpmsg = '*confused european noises*\n \
©MKE 2020\n\n \
Each function of this bot is preceded by "cen?" or "€?". Typing only this will bring up a short sentence in European.\n\n \
Functions:\n \
\thelp\n \
- Show this explanation.\n \
\t(number) F\n \
- Convert the (number) in degrees Celsius to degrees Fahrenheit.\n \
\t(number) C\n \
- Convert the (number) in degrees Fahrenheit to degrees Celsius.\n \
\t(number) ft\n \
- Convert the (number) in feet to meters.\n \
\t(number) m\n \
- Convert the (number) in meters to feet.'

mpft = 0.3048

def ftoc(f):
	return ((f - 32) * 5.0 / 9.0)

def ctof(c):
	return ((c * 9.0 / 5.0) + 32)

def	alldigits(str):
	try:
		float(str)
		return True
	except ValueError:
		return False

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('cen?') or message.content.startswith("€?"):
		msglist = message.content.split()
		print(msglist)
		msg = '`' + euromess[random.randrange(len(euromess))] + '`'
		print(msg)
		if (len(msglist) == 3):
			if (alldigits(msglist[1])):
				prec = 0
				if ('.' in msglist[1]):
					prec = len(msglist[1]) - msglist[1].find('.') - 1
				num = float(msglist[1])
				if (msglist[2] == 'F'):
					msg = '`%.*f °F = %.*f °C`' % (prec, num, prec, ftoc(num))
				if (msglist[2] == 'C'):
					msg = '`%.*f °C = %.*f °F`' % (prec, num, prec, ctof(num))
				if (msglist[2] == 'ft'):
					msg = '`%.*f ft = %.*f m`' % (prec, num, prec, mpft * num)
				if (msglist[2] == 'm'):
					msg = '`%.*f m = %.*f ft`' % (prec, num, prec, num / mpft)
		elif (len(msglist) == 2) and (msglist[1] == 'help'):
			msg = '```' + helpmsg + '```'
		await message.channel.send(msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)