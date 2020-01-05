import requests
from bs4 import BeautifulSoup as bs

class ifunny_bot:
    def __init__(self):
        self.hour = 0
        self.minutes = 0
        self.second = 0
    
    def get_countdown():
        html_response = bs(requests.get('https://ifunny.co/').content, "lxml")
        coutdown_timer = (html_response.body.find('div', attrs = {'class' : 'digitchanger js-countdown-mainCounter'}).text)
        coutdown_timer = coutdown_timer.replace(" ", "")
        if __debug__:
            print("Hours", coutdown_timer[0:2])
            print("Minutes", coutdown_timer[3:5])
            print("Seconds", coutdown_timer[6:8])
            hour = int(coutdown_timer[0:2])
            minutes = int(coutdown_timer[3:5])
            second = int(coutdown_timer[6:8])
        else:
            hour = int(coutdown_timer[0:2])
            minutes = int(coutdown_timer[3:5])
            second = int(coutdown_timer[6:8])

    def get_features(number_features):
        html_response = bs(requests.get('https://ifunny.co/').content, "lxml")
        feed = (html_response.body.find('div', attrs = {'data-test' : 'feed'}).text)
        user = bs(feed, "lxml").find('a', attes = {'href' : ''}).text
        print(bs(feed, "lxml"))

print(ifunny_bot.get_features(1))