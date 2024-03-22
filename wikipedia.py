import telebot
import requests
from wikisearchh import searchwikipedia
from bs4 import BeautifulSoup
token="1814931675:AAEBYefSTm3k9T0Z20LgFUHb2j7sem53p-4"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start','hi','Hi','hello','Start'])
def handle_st(message):
    wel="Hey hi"
    bot.reply_to(message,wel,parse_mode='Markdown')
@bot.message_handler(func=lambda message:True)
def handel_all_messages(message):
    try:
        searched=searchwikipedia(message.text)
        response=requests.get(searched)
        soup=BeautifulSoup(response.text,"html.parser")
        result=""
        title = soup.find('title').text
        info = soup.find('table')
        born1 = soup.findAll('th', class_="infobox-label")
        born = info.findAll('td', class_=["infobox-data", "infobox-data role"])
        pic=soup.find('td',class_="infobox-image")
        piclink=pic.img['src']
        message_text = f"{title}🔍\n{piclink}"
        bot.reply_to(message, message_text)
        for i in range(len(born1)):
            if born[i].text=="Full list":
              continue
            string = born[i].text
            result+="\n"+"🌟 "+born1[i].text + " : " + string+"\n"
        bot.reply_to(message,result,parse_mode='Markdown')
    except:
        bot.reply_to(message,f"Check your query and Try again!!")

bot.polling()


