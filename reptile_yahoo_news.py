import requests
from bs4 import BeautifulSoup

# 定義目標網址
address = 'https://travel.ettoday.net/category/%E9%AB%98%E9%9B%84/?from=travel_MainMenu_PC'

# 發送 HTTP GET 請求並獲得回應
response = requests.get(address)

# 解析回應的 HTML 內容
soup = BeautifulSoup(response.text, "html.parser")

# 尋找所有的新聞標題
titles = soup.find_all("h3", itemprop="headline")

# 逐個輸出新聞標題
for title in titles:
    print(title.a.text.strip())
    print()