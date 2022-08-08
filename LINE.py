token="aPNtA9CoV1zm0DTi80qSjNdAEkGBUjc4mubX7ssQmZ6"
url="https://notify-api.line.me/api/notify"
from bs4 import BeautifulSoup
import requests

tenki_url="https://weather.yahoo.co.jp/weather/jp/22/5040.html"

#　天気取得
def Weather(AreaCode):
    url = "https://weather.yahoo.co.jp/weather/jp/22/" + str(AreaCode) + ".html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rs = soup.find(class_='forecastCity')
    rs = [i.strip() for i in rs.text.splitlines()]
    rs = [i for i in rs if i != ""]
    print(rs[0] + "の天気は" + rs[1] + "、明日の天気は" + rs[19] + "です。")
    return "岐阜 "+str(rs[0]) + "の天気は" + str(rs[1]) + "、明日の天気は" + str(rs[2]) + "です。"

message=str(Weather(5040))

# 名言取得
def saying_text():
    url = 'http://www.meigensyu.com/quotations/view/random'
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    saying = soup.find('div',class_='text')
    saying = [i.strip() for i in saying.text.splitlines()]
    saying = [i for i in saying if i != ""]
    return saying

qwe2=str(saying_text())

auth={"Authorization":"Bearer "+token}
content={"message":message+"\r\n""今日の名言"+"\r\n"+qwe2}

requests.post(url, headers=auth, data=content)


