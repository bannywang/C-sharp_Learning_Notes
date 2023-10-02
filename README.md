# Python_Learning_Notes
這邊放我學習 Python 的筆記

---

# 基礎學習
  
 
## 變數 & 型別
  在 Python 中，不用特別宣告該變數的資料類型，當我賦值時，Python 會自動判斷類型。
  
  ``` python
  A = 5 
      #整數 (int)
  B = 3.14 
      #浮點數 (float) 除了數學寫法也支援科學技術法(1.23456e2)
  C = 'Python' or "Python" 
      #字串，單引或雙引包起來，字串還有(原始字串表示法)、(位元組字串表示法)、(Unicode字串表示法)

  D = True or False
      #布林值

  E = 3+5j
      #複數 例：3+5j，3為實部，5為虛部
  ```

## 變數命名

- 硬性規則：
  - 由字母(廣義的Unicode字元) + 數字 + 下劃線 (開頭不能數字)
  - 大小寫敏感(Apple 與 apple 是不同的變數)
  - 不要與關鍵字 & 保留字衝突

- PEP8 要求：
  - 小寫字母拼寫
  - 受保護的例項屬性用單個下劃線開頭（後面會講到）。
  - 私有的例項屬性用兩個下劃線開頭（後面會講到）。

變數名稱要做到見名知義。

## 變數的使用

``` python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

**可以使用type檢查該變數的型別**

``` python
a = 100
b = 'hello'

print(type(a)) #int
print(type(b)) #str
```

**也可以使用python內建的函式對變數型別進行轉換**

- int()：將一個數值或字串轉換成整數，可以指定進位制。
- float()：將一個字串轉換成浮點數。
- str()：將指定的物件轉換成字串形式，可以指定編碼。
- chr()：將整數轉換成該編碼對應的字串（一個字元）。
- ord()：將字串（一個字元）轉換成對應的編碼（整數）。

``` python 
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))

# %d 整數佔位符
# %f 小數佔位符
# %% 百分號佔位符

# input會獲取使用者輸入的值會回傳 str型態，再用int()包起來改成數字， %d為佔位符，表示整數，將括號中的值替換到佔位符中。
```
## 分支結構

``` python 
#if 的使用
user_name = input('請輸入使用者名稱：')
password = input('請輸入密碼：')

if user_name == 'banny' and password == '123456':
  print('登入成功')
else : 
  print('登入失敗')

# 練習
score = int(input('請輸入成績：'))

if score >= 90:
    grade = 'a'
    note = '90分以上乖寶寶'

elif score >= 80:
    grade = 'b'
    note = '80以上不錯唷'

elif score >= 70:
    grade = 'c'
    note = '有待加強'
else:
    grade = 'd'
    note = '87'

print('你的等級是%s，評價為%s' % (grade, note))
```
## 循環結構

### for in 迴圈
如果明確的知道要執行的次數或要對一個容器進行迭代，推薦使用 for-in迴圈
``` python

# range(stop)：從0開始，到stop-1結束
# range(start, stop) 從 start 開始，到stop-1結束
# range(start, stop, step) step為每次增加的數

# 計算 1+2+3+...+100
sum = 0
for i in range(101):
    sum += i
print(sum)

#計算 1到100的偶數和
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)

#可以加上 if 判斷 
sum = 0
for i in range(2, 101, 2):
    if i % 2 == 0:
        sum += i
print(sum)
```
### while 迴圈
如果不知道具體迴圈次數的的迴圈結構，可以使用 while 迴圈，while透過可以產生bool值來控制，true會繼續迴圈，false會結束迴圈。
``` python
# 引入隨機數產生模組
import random

# 隨機產生1~100的隨機放到answer中
answer = random.randint(1, 100)
counter = 0 #次數預設為0

while True:
    counter += 1  #進到迴圈次數+1
    number = int(input('請輸入: '))
    if number < answer:
        print('大一點')
    elif number > answer:
        print('小一點')
    else:
        print('恭喜你猜對了!')
        break
print('你總共猜了%d次' % counter)
if counter > 7:
    print('你的智商明顯不足')
```
### 99乘法表練習
``` python
for i in range(2, 10):
    for j in range(1, 10):
        print('%d*%d=%d ' % (i, j, i*j), end='\t')
    print()
```

## 函式和模組的使用

### 函數的使用

```python

def function_name(parameters):
  # parameters + ?
  return value

# 例
def hello(name):
  print('hello ' + name)
  return name
```

### 模組的使用

```python

#如果同名時可以放在不同檔案用 import 的方式引入。
```

<!-- - 函式
- 列表、字典
- 模組、套件
- 物件導向程式設計 -->

#實際應用

- 小專案
    1. **網頁爬蟲**：使用 BeautifulSoup 或 Scrapy 來抓取和解析網頁上的數據。
    2. **自動化腳本**：比如自動整理文件、自動發送郵件、或使用 pyautogui 控制滑鼠和鍵盤。
    3. **簡單的 Web 應用**：使用 Flask 或 Django 建立一個個人部落格或任務管理器。
    4. **計算器**：可以從基礎的數學運算擴展到科學或金融計算器。
    5. **遊戲**：如使用 Pygame 創建經典遊戲的複製版，如贪吃蛇、俄羅斯方塊等。
    6. **聊天機器人**：使用 ChatterBot 庫製作簡單的基於規則的聊天機器人。
    7. **圖片編輯器**：使用 PIL 或 OpenCV 進行圖像處理或濾鏡應用。
    8. **音樂播放器**：使用 pygame 或 tkinter 庫製作基本的音樂播放器。
    9. **書籍或文章管理器**：建立一個用於追踪和管理您的書籍或文章的系統。
    10. **費用追踪器**：建立一個費用和預算追踪應用。
    11. **API 接口**：使用 Flask-RESTful 製作自己的 RESTful API。
    12. **文字冒險遊戲**：建立一個基於終端機的文字冒險遊戲。
    13. **天氣應用**：使用公開的天氣 API 來獲取和展示天氣資訊。
    14. **股票市場分析器**：從股票市場 API 抓取數據，進行基本的分析或預測。
    15. **待辦事項應用**：建立一個命令行或 GUI 的待辦事項管理器。

# 資源
- Codecademy
- LeetCode
- Coursera

# 框架與庫
- Django
- Flask
- Pandas
- TensorFlow

# 社群

- 待新增

# 注意事項
本文件僅用於自我學習，如有任何錯誤歡迎告訴作者。