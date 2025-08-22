# Day 3：輸入與輸出

## 今日學習目標
- 掌握 input() 函數讓程式接收使用者輸入
- 學習 print() 函數的進階用法
- 了解格式化輸出的方式
- 製作互動式對話程式

## 1. 讓程式與使用者對話

到目前為止，我們的程式就像**自言自語**，今天要學會**對話**！

### 1.1 input() - 接收使用者輸入
```python
name = input("請輸入你的姓名：")
print("你好，", name)
```

### 類比理解
- **input()** 就像問問題，等對方回答
- 就像問卷調查，程式問問題，使用者填答案

## 2. input() 的使用方式

### 2.1 基本語法
```python
變數名稱 = input("提示訊息")
```

### 2.2 實際範例
```python
# 詢問基本資料
name = input("你的姓名是？")
age = input("你幾歲？")
city = input("你住在哪個城市？")

print("姓名：", name)
print("年齡：", age)
print("城市：", city)
```

### 2.3 重要概念：input() 永遠回傳字串
```python
age = input("你幾歲？")  # 即使輸入20，age的型態是字串"20"
print(type(age))  # <class 'str'>
```

## 3. 字串轉換為數字

### 3.1 轉換為整數
```python
age_str = input("你幾歲？")  # 輸入 "25"
age_int = int(age_str)      # 轉換為整數 25
print("明年你", age_int + 1, "歲")
```

### 3.2 轉換為浮點數
```python
height_str = input("你的身高(公分)？")  # 輸入 "170.5"
height_float = float(height_str)       # 轉換為浮點數 170.5
print("你的身高是", height_float, "公分")
```

### 3.3 一行完成轉換
```python
age = int(input("你幾歲？"))
height = float(input("你的身高？"))
```

## 4. print() 的進階用法

### 4.1 基本輸出
```python
print("Hello")
print("World")
# 輸出：
# Hello
# World
```

### 4.2 同一行輸出多個內容
```python
name = "小明"
age = 20
print("姓名：", name, "年齡：", age)
# 輸出：姓名： 小明 年齡： 20
```

### 4.3 改變分隔符號
```python
print("蘋果", "香蕉", "橘子", sep="-")
# 輸出：蘋果-香蕉-橘子

print("A", "B", "C", sep="")
# 輸出：ABC
```

### 4.4 控制結尾字元
```python
print("第一行", end="")
print("第二行")
# 輸出：第一行第二行

print("讀取中", end="...")
# 輸出：讀取中...
```

## 5. 格式化輸出

### 5.1 使用 f-string（推薦方式）
```python
name = "小華"
age = 22
score = 85.7

print(f"姓名：{name}")
print(f"年齡：{age}歲")
print(f"成績：{score}分")
print(f"{name}今年{age}歲，考了{score}分")
```

### 5.2 format() 方法
```python
name = "小美"
age = 21

print("姓名：{}".format(name))
print("{}今年{}歲".format(name, age))
```

### 5.3 % 格式化（舊方式）
```python
name = "小強"
age = 23

print("姓名：%s" % name)
print("%s今年%d歲" % (name, age))
```

## 6. 實作練習

創建 `interactive_chat.py`：

```python
# 互動式對話程式
print("=== 歡迎使用個人助理 ===")
print("我想更認識你！")

# 收集使用者資料
name = input("請告訴我你的姓名：")
age = int(input("你幾歲了？"))
hobby = input("你的興趣是什麼？")
city = input("你住在哪個城市？")

# 計算一些有趣的資料
birth_year = 2024 - age
next_age = age + 1

# 友善的回應
print(f"\n很高興認識你，{name}！")
print(f"原來你是{birth_year}年出生的")
print(f"明年你就{next_age}歲了")
print(f"住在{city}很不錯呢！")
print(f"我也喜歡{hobby}，我們真有緣")

print("\n感謝你跟我分享這些資訊！")
```

## 7. 錯誤處理基礎

### 7.1 常見錯誤
```python
# 錯誤：輸入非數字時轉換會失敗
age = int(input("年齡？"))  # 如果輸入"abc"會出錯
```

### 7.2 簡單的防錯方式
```python
# 給使用者清楚的指示
age_str = input("請輸入你的年齡（只能輸入數字）：")
age = int(age_str)
```

## 8. 實用範例

### 8.1 簡單計算機
```python
print("=== 簡單加法計算機 ===")
num1 = float(input("請輸入第一個數字："))
num2 = float(input("請輸入第二個數字："))
result = num1 + num2
print(f"{num1} + {num2} = {result}")
```

### 8.2 個人BMI計算器
```python
print("=== BMI計算器 ===")
name = input("姓名：")
weight = float(input("體重(公斤)："))
height = float(input("身高(公分)："))

height_m = height / 100  # 轉換為公尺
bmi = weight / (height_m ** 2)

print(f"\n{name}的BMI計算結果：")
print(f"身高：{height}公分")
print(f"體重：{weight}公斤")
print(f"BMI：{bmi:.2f}")  # 保留兩位小數
```

## 9. 今日總結

今天你學會了：
- ✅ 使用 input() 接收使用者輸入
- ✅ 字串轉換為數字（int(), float()）
- ✅ print() 的進階用法
- ✅ f-string 格式化輸出
- ✅ 製作互動式程式

## 10. 明日預告

明天我們將學習：
- 字串的各種操作方法
- 文字處理技巧
- 製作更實用的文字程式

## 11. 作業

1. 完成 `interactive_chat.py` 程式
2. 製作一個「自我介紹產生器」，詢問使用者各種資料，然後產生完整的自我介紹
3. 嘗試製作一個單位轉換程式（如：公分轉公尺、攝氏轉華氏）
4. 練習不同的 print() 格式化方法

記住：**互動是程式有趣的開始，讓程式能與人對話就像學會聊天一樣重要！**