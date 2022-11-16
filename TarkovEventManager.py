#https://github.com/JeiKiTinN/Tarkov-EventParser-Telegram
import requests
import time
from bs4 import BeautifulSoup
import threading


def send_msg(text):
    token = "" #telegram bot token
    chat_id = ""

    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text=" +text
    requests.get(url_req)

def parsingHalloween():
    response = requests.get("https://www.escapefromtarkov.com/halloween")
    bs = BeautifulSoup(response.text, "html.parser")
    temp = bs.find('span')
    return temp


def eventHalloween():
    while True:
        temp = parsingHalloween()
        print(temp.text)
        if(int(temp.text) > 620000 and int(temp.text) < 666666):
            send_msg("📍Опасно идти в рейд! Doomed: " + temp.text)
        elif(int(temp.text) == 666666):
            ivent = True
            send_msg("❌❌❌ Начался трешняк! Doomed: " + temp.text + " ❌❌❌")
            while ivent:
                time.sleep(480)
                temp = parsingHalloween()
                if(int(temp.text) == 666666):
                    send_msg("❌❌❌ Треш все еще в процессе! ❌❌❌")
                else:
                    send_msg("✅✅✅Трешняк закончился! Doomed: " + temp.text + " ✅✅✅")
                    ivent=False
        time.sleep(250)


#main body
t = threading.Thread(target = eventHalloween, args=())
t.start()
