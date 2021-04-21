import telegram

telgm_token = '1659964894:AAFMh8xKTpLkKHjVyX47PF9NE_7Pwm606pM'
bot = telegram.Bot(token = telgm_token)
updates = bot.getUpdates()
bot.sendMessage(chat_id ='1668191285', text="모두들 벼락부자되세요")
print(updates)
for i in updates:
    print(i)
print('start telegram chat bot')
    
    