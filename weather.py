import requests

city = input("請輸入你的城市：")
API = '4b2eafbb36471d7ce5f4b6da5bb63139'
address = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}"

# 使用 requests.get() 方法發起 HTTP GET 請求
weather_data = requests.get(address)

# 檢查 HTTP 回應狀態碼
if weather_data.status_code == 200:
    data = weather_data.json()
    
    #  參考官方API文件 
       
    # 取得天氣資料
    city_name = data["name"]
    temp = data["main"]["temp"] - 273.15  # 轉換為攝氏度

    # 顯示天氣資料
    print(f"{city_name} 目前的氣溫為 {temp}°C")
    
else:
    # 如果狀態碼不是 200，則打印錯誤信息
    print(f"Failed to retrieve data. HTTP Status Code: {weather_data.status_code}")
