import requests
from bs4 import BeautifulSoup

# 定義目標網址
address = 'https://www.kcg.gov.tw/News.aspx?n=F29A02A9D36C47F0&sms=19902EF36D6B551D'

# 發送 HTTP GET 請求以獲得網頁內容
response = requests.get(address)

# 使用 BeautifulSoup 解析網頁內容
soup = BeautifulSoup(response.text, "html.parser")

# 找到所有的新聞資訊
news_list = soup.select('tbody tr')

# 遍歷每一條新聞資訊
for news in news_list:
    # 獲取新聞標題
    title = news.select_one('td:nth-child(1) p a').get_text(strip=True)
    # 獲取新聞發布機關
    agency = news.select_one('td:nth-child(2) p').get_text(strip=True)
    # 獲取新聞發布日期
    date = news.select_one('td:nth-child(3) p').get_text(strip=True)
    
    # 印出新聞資訊
    print(f"標題: {title}")
    print(f"發布機關: {agency}")
    print(f"發布日期: {date}")
    print('-' * 50)
