
import random
a = 200
b = 20

# 流程控制 --------------------------------------------------------
# if (a > b):
#     print('A比B大')
# elif (a < b):
#     print('A比B小')
# else:
#     print('一樣大')

# 迴圈 --------------------------------------------------------
# for i in range(100):
#     print(i)

# c = 0
# d = 10
# while c < 10:
#     print(c)
#     c += 1

# 型別 --------------------------------------------------------
# iv = 10
# fv = 12.3
# cv = 3 + 5j
# sv = 'hello python'
# bv = True
# nv = None

# print(type(iv))
# print(type(fv))
# print(type(cv))
# print(type(sv))
# print(type(bv))
# print(nv)
# print(isinstance(sv, str))

# User Input --------------------------------------------------------
# name = input('Hello, what is your name?  ')
# print('Hello, ', name)

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d %% %d = %d' % (a, b, a % b))

# 溫度轉換
# c = float(input('請輸入攝氏溫度：'))
# f = (c * 9/5 +32)
# print('%d 攝氏度 = %d 華氏度'%(c,f))

# 計算周長
# q = float(input('請輸入圓的半徑'))
# a = q * q * 3.14
# c = q * 2 * 3.14
# print('半徑為 %.2f 的面積為 %.2f' % (q,a))
# print('半徑為 %.2f 的周長 = %.2f' % (q,c))

# 閏年計算
# year = int(input('請輸入年份：'))
# if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#     print('%d 年為閏年' % (year))
# else:
#     print('%d 不是閏年' % (year))

# is_leap =  (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# print(is_leap)


# user_name = input('請輸入使用者名稱：')
# password = input('請輸入密碼：')

# if user_name == 'banny' and password == '123456':
#   print('登入成功')
# else :
#   print('登入失敗')

# score = int(input('請輸入成績：'))

# if score >= 90:
#     grade = 'a'
#     note = '90分以上乖寶寶'

# elif score >= 80:
#     grade = 'b'
#     note = '80以上不錯唷'

# elif score >= 70:
#     grade = 'c'
#     note = '有待加強'
# else:
#     grade = 'd'
#     note = '87'

# print('你的等級是%s，評價為%s' % (grade, note))

# sum = 0
# for i in range(2, 101, 2):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# ----------------------------------------------------------------
# 隨機生成一個1到100（包含）的整數作為答案
# answer = random.randint(1, 100)

# # 初始化一個計數器為0，用於記錄玩家猜測的次數
# counter = 0

# # 啟動一個無限循環，直到玩家猜對答案為止
# while True:
#     # 每次進入循環，計數器加1
#     counter += 1

#     # 請求玩家輸入一個猜測的數字
#     number = int(input('請輸入: '))

#     # 判斷玩家猜的數字是否小於答案
#     if number < answer:
#         print('大一點')
#     # 判斷玩家猜的數字是否大於答案
#     elif number > answer:
#         print('小一點')
#     # 如果都不是，那麼玩家猜對了
#     else:
#         print('恭喜你猜對了!')
#         break

# # 輸出玩家總共猜測的次數
# print('你總共猜了%d次' % counter)

# # 如果玩家猜了超過7次，輸出一個玩笑訊息
# if counter > 7:
#     print('你的智商明顯不足')

# 輸出乘法口訣表(九九表)

# for i in range(2, 10):
#     for j in range(1, 10):
#         print('%d*%d=%d ' % (i, j, i*j), end='\t')
#     print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

print(type('hello'))