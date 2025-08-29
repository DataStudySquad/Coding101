# Day 9：迴圈進階（while）

## 今日學習目標
- 理解while迴圈的概念和用法
- 學會使用break和continue關鍵字
- 掌握迴圈控制的技巧
- 實作猜數字遊戲

## 1. while迴圈的概念

### for vs while 的差別
想像一下這兩種情況：

**for迴圈**：像是「做10下伏地挺身」
- 明確知道要重複幾次
- 有固定的次數或範圍

**while迴圈**：像是「一直跑步直到累了為止」
- 不確定要重複幾次
- 根據條件決定是否繼續

### while迴圈的特色
```python
while 條件:
    要重複執行的程式碼
```

只要條件為`True`，就會一直執行下去！

## 2. while迴圈基本語法

### 簡單範例
```python
# 倒數計時
count = 5
while count > 0:
    print(f"倒數：{count}")
    count -= 1  # 每次減1，很重要！
print("時間到！")
```

### 重要提醒：避免無限迴圈
```python
# ❌ 危險！無限迴圈
count = 5
while count > 0:
    print(f"倒數：{count}")
    # 忘記減1，count永遠是5，條件永遠為True

# ✅ 正確！記得更新條件變數
count = 5
while count > 0:
    print(f"倒數：{count}")
    count -= 1  # 更新條件變數
```

## 3. while迴圈的實用範例

### 範例1：累加到某個值
```python
total = 0
num = 1
while total < 100:
    total += num
    num += 1
print(f"累加到超過100的總和：{total}")
print(f"用了{num-1}個數字")
```

### 範例2：使用者輸入驗證
```python
password = ""
while password != "python123":
    password = input("請輸入密碼：")
    if password != "python123":
        print("密碼錯誤，請重新輸入")
    else:
        print("密碼正確！歡迎登入")
```

### 範例3：選單系統
```python
choice = ""
while choice != "4":
    print("\n=== 主選單 ===")
    print("1. 查看資料")
    print("2. 新增資料")
    print("3. 刪除資料")
    print("4. 離開")
    
    choice = input("請選擇功能 (1-4): ")
    
    if choice == "1":
        print("查看資料功能")
    elif choice == "2":
        print("新增資料功能")
    elif choice == "3":
        print("刪除資料功能")
    elif choice != "4":
        print("無效的選擇，請重新輸入")

print("感謝使用，再見！")
```

## 4. break語句：強制跳出迴圈

### break的作用
就像是迴圈的「緊急出口」：

```python
# 尋找特定數字
numbers = [1, 3, 7, 12, 8, 15]
target = 12

for num in numbers:
    if num == target:
        print(f"找到了！數字是：{num}")
        break  # 找到就跳出，不用再找了
    print(f"檢查數字：{num}")
```

### break在while迴圈中的應用
```python
# 猜數字遊戲簡化版
secret = 7
attempts = 0
max_attempts = 3

while True:  # 無限迴圈
    attempts += 1
    guess = int(input("猜一個1到10的數字："))
    
    if guess == secret:
        print(f"恭喜！你在第{attempts}次猜對了！")
        break  # 猜對了就跳出
    elif attempts >= max_attempts:
        print(f"遊戲結束！答案是{secret}")
        break  # 超過次數也跳出
    else:
        print("猜錯了，再試一次！")
```

## 5. continue語句：跳過本次執行

### continue的作用
就像是「跳過這一輪，直接進行下一輪」：

```python
# 只印出奇數
for i in range(1, 11):
    if i % 2 == 0:  # 如果是偶數
        continue    # 跳過這次，不執行下面的print
    print(f"奇數：{i}")
```

### continue在while迴圈中的應用
```python
# 只處理正數
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # 偶數跳過
        continue
    print(f"處理奇數：{num}")
```

## 6. 迴圈控制的綜合應用

### 範例：智慧型重試機制
```python
import random

def try_connection():
    """模擬網路連線，隨機成功或失敗"""
    return random.choice([True, False])

max_retries = 5
retry_count = 0

print("嘗試連線...")
while retry_count < max_retries:
    if try_connection():
        print("連線成功！")
        break
    else:
        retry_count += 1
        print(f"連線失敗，重試第{retry_count}次...")
        
        if retry_count >= max_retries:
            print("達到最大重試次數，連線失敗")
            break
        
        # 跳過一些特定情況
        if retry_count == 3:
            print("第3次失敗，稍作休息...")
            continue
```

## 7. 實作項目：猜數字遊戲

讓我們製作一個完整的猜數字遊戲：

```python
import random

def guessing_game():
    # 遊戲設置
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    guessed_numbers = []
    
    print("🎯 歡迎來到猜數字遊戲！")
    print(f"我想了一個1到100之間的數字，你有{max_attempts}次機會猜中它")
    print("提示：輸入'quit'可以隨時退出遊戲")
    
    while attempts < max_attempts:
        # 顯示遊戲狀態
        remaining = max_attempts - attempts
        print(f"\n剩餘機會：{remaining}")
        if guessed_numbers:
            print(f"已猜過的數字：{guessed_numbers}")
        
        # 獲取使用者輸入
        guess_input = input("請輸入你的猜測：")
        
        # 檢查是否要退出
        if guess_input.lower() == 'quit':
            print(f"遊戲結束！答案是：{secret_number}")
            break
        
        # 驗證輸入
        try:
            guess = int(guess_input)
        except ValueError:
            print("請輸入有效的數字！")
            continue  # 跳過這次，重新輸入
        
        if guess < 1 or guess > 100:
            print("請輸入1到100之間的數字！")
            continue  # 跳過這次，重新輸入
        
        if guess in guessed_numbers:
            print("你已經猜過這個數字了！")
            continue  # 跳過這次，重新輸入
        
        # 處理猜測
        attempts += 1
        guessed_numbers.append(guess)
        
        if guess == secret_number:
            print(f"🎉 恭喜！你在第{attempts}次猜中了！答案就是{secret_number}")
            break
        elif guess < secret_number:
            print("太小了！再猜大一點")
        else:
            print("太大了！再猜小一點")
    
    else:
        # while迴圈正常結束（沒有break）
        print(f"😢 遊戲結束！你用完了所有機會，答案是：{secret_number}")

# 執行遊戲
guessing_game()
```

## 8. while True 的使用時機

### 適合用 while True 的情況
```python
# 主程式迴圈
while True:
    user_input = input("輸入命令 (或 'exit' 離開): ")
    
    if user_input == 'exit':
        break
    elif user_input == 'help':
        print("可用命令：help, status, exit")
    elif user_input == 'status':
        print("系統運行正常")
    else:
        print("未知命令，輸入 'help' 查看幫助")
```

### 注意事項
- 一定要有跳出機制（break或return）
- 避免真正的無限迴圈
- 適合不確定執行次數的情況

## 9. 迴圈除錯技巧

### 技巧1：加入計數器防止無限迴圈
```python
safety_counter = 0
while condition and safety_counter < 1000:
    # 你的程式碼
    safety_counter += 1

if safety_counter >= 1000:
    print("警告：可能發生無限迴圈！")
```

### 技巧2：使用print除錯
```python
while condition:
    print(f"Debug: condition = {condition}")  # 除錯輸出
    # 你的程式碼
```

## 10. 實作作業

創建 `while_loop_practice.py`：

```python
# 練習1：數字累加器
print("練習1：數字累加器")
total = 0
while total < 50:
    num = int(input(f"目前總和：{total}，請輸入一個數字："))
    total += num
print(f"總和達到：{total}")

# 練習2：密碼驗證系統
print("\n練習2：密碼驗證")
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("請輸入密碼：")
    if password == correct_password:
        print("登入成功！")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"密碼錯誤！還有{remaining}次機會")
        else:
            print("超過嘗試次數，帳號被鎖定！")

# 練習3：簡單計算機
print("\n練習3：簡單計算機")
while True:
    print("\n可用操作：+, -, *, /, quit")
    operation = input("請選擇操作：")
    
    if operation == 'quit':
        print("計算機已關閉")
        break
    elif operation in ['+', '-', '*', '/']:
        try:
            a = float(input("請輸入第一個數字："))
            b = float(input("請輸入第二個數字："))
            
            if operation == '+':
                result = a + b
            elif operation == '-':
                result = a - b
            elif operation == '*':
                result = a * b
            elif operation == '/':
                if b != 0:
                    result = a / b
                else:
                    print("錯誤：除數不能為零！")
                    continue
            
            print(f"結果：{a} {operation} {b} = {result}")
        except ValueError:
            print("請輸入有效的數字！")
    else:
        print("無效的操作！")
```

## 11. 今日總結

今天你學會了：
- ✅ while迴圈的概念和語法
- ✅ break和continue的使用
- ✅ 避免無限迴圈的技巧
- ✅ 迴圈控制的實際應用
- ✅ 製作完整的猜數字遊戲

## 12. 明日預告

明天我們將學習：
- 什麼是清單（List）
- 如何建立和操作清單
- 清單的常用方法
- 製作待辦事項清單程式

## 13. 重要概念回顧

- **while迴圈**：根據條件重複執行，適合不確定次數的重複
- **break**：立即跳出迴圈
- **continue**：跳過本次執行，進行下一次迴圈
- **無限迴圈**：條件永遠為True的迴圈，要小心避免

記住：**while迴圈給了程式更多彈性，但也需要更小心地控制條件！**