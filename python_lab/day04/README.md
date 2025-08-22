# Day 4: 字串處理

## 學習目標
- 了解字串的基本概念和特性
- 學會字串的基本操作方法
- 掌握字串格式化的技巧
- 練習字串在實際應用中的使用

## 理論說明

### 字串是什麼？
想像字串就像是一串珠子，每顆珠子代表一個字元（字母、數字、符號等）。在Python中，字串是用來儲存和處理文字資料的資料型別。

就像你寫日記時會用到各種文字一樣，程式也需要處理文字資料：
- 使用者的姓名
- 商品的描述
- 錯誤訊息
- 網頁內容

### 字串的特性
1. **不可變性**：一旦建立就不能修改，就像印刷好的書籍不能改變內容
2. **有順序性**：每個字元都有固定的位置，從0開始編號
3. **可重複**：同一個字元可以出現多次

## 程式範例

### 1. 基本字串操作
```python
# 建立字串
name = "小明"
message = '歡迎來到Python世界！'
long_text = """這是一段
很長的文字，
可以跨越多行。"""

# 字串連接
greeting = "你好，" + name + "！"
print(greeting)  # 輸出：你好，小明！

# 字串重複
stars = "*" * 10
print(stars)  # 輸出：**********
```

### 2. 字串索引和切片
```python
text = "Python程式設計"

# 取得單一字元（索引從0開始）
print(text[0])    # P
print(text[6])    # 程
print(text[-1])   # 計（負數從後面算起）

# 字串切片
print(text[0:6])   # Python
print(text[6:])    # 程式設計
print(text[:6])    # Python
print(text[::2])   # Pto程設（每隔一個字元取一個）
```

### 3. 常用字串方法
```python
text = "  Hello Python World  "

# 去除空白
print(text.strip())     # "Hello Python World"
print(text.lstrip())    # "Hello Python World  "
print(text.rstrip())    # "  Hello Python World"

# 大小寫轉換
print(text.upper())     # "  HELLO PYTHON WORLD  "
print(text.lower())     # "  hello python world  "
print(text.title())     # "  Hello Python World  "

# 替換
new_text = text.replace("Python", "程式")
print(new_text)         # "  Hello 程式 World  "

# 分割
words = "蘋果,香蕉,橘子".split(",")
print(words)           # ['蘋果', '香蕉', '橘子']

# 結合
fruits = ["蘋果", "香蕉", "橘子"]
result = ",".join(fruits)
print(result)          # "蘋果,香蕉,橘子"
```

### 4. 字串格式化
```python
name = "小華"
age = 25
score = 87.5

# 方法1：使用f-string（推薦）
message1 = f"我的名字是{name}，今年{age}歲，成績是{score}分"
print(message1)

# 方法2：使用.format()
message2 = "我的名字是{}，今年{}歲，成績是{}分".format(name, age, score)
print(message2)

# 方法3：使用%格式化（較舊的方式）
message3 = "我的名字是%s，今年%d歲，成績是%.1f分" % (name, age, score)
print(message3)

# 進階格式化
price = 1234.5678
formatted_price = f"商品價格：${price:,.2f}"
print(formatted_price)  # 商品價格：$1,234.57
```

## 實作練習

### 練習1：個人資料處理器
```python
# 建立一個簡單的個人資料處理程式
first_name = input("請輸入您的姓：")
last_name = input("請輸入您的名：")
age = int(input("請輸入您的年齡："))

# 處理輸入資料
full_name = first_name.strip() + last_name.strip()
formatted_name = full_name.title()

print(f"您好，{formatted_name}先生/小姐")
print(f"您今年{age}歲")
print(f"您的全名有{len(full_name)}個字元")
```

### 練習2：文字美化器
```python
# 建立文字美化功能
text = input("請輸入要美化的文字：")

# 不同的美化風格
print("=" * 50)
print("原始文字：", text)
print("=" * 50)
print("大寫版本：", text.upper())
print("小寫版本：", text.lower())
print("標題格式：", text.title())
print("反轉文字：", text[::-1])
print("加上裝飾：", f"★ {text} ★")
print("=" * 50)
```

### 練習3：簡單的文字統計
```python
# 文字統計分析器
text = """Python是一種廣泛使用的程式語言。
它簡單易學，功能強大。
非常適合初學者學習程式設計。"""

print("文字統計報告")
print("-" * 30)
print(f"總字數：{len(text)}")
print(f"行數：{text.count(chr(10)) + 1}")  # chr(10)是換行符號
print(f"Python出現次數：{text.count('Python')}")
print(f"程式出現次數：{text.count('程式')}")

# 字元頻率統計（簡化版）
text_clean = text.replace('\n', '').replace('，', '').replace('。', '')
unique_chars = set(text_clean)
print(f"不同字元數：{len(unique_chars)}")
```

## 實際應用範例

### 密碼強度檢查器
```python
def check_password_strength(password):
    """簡單的密碼強度檢查"""
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("密碼應至少8個字元")
    
    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("應包含大寫字母")
    
    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("應包含小寫字母")
    
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("應包含數字")
    
    # 回傳結果
    levels = ["很弱", "弱", "中等", "強", "很強"]
    return levels[strength], feedback

# 測試密碼
password = input("請輸入密碼：")
level, suggestions = check_password_strength(password)

print(f"密碼強度：{level}")
if suggestions:
    print("建議改進：")
    for suggestion in suggestions:
        print(f"- {suggestion}")
```

## 重點整理
1. **字串建立**：使用單引號、雙引號或三引號
2. **字串連接**：使用+號或join()方法
3. **字串切片**：使用[start:end:step]語法
4. **常用方法**：strip(), upper(), lower(), replace(), split()
5. **格式化**：推薦使用f-string，語法是f"文字{變數}"

## 作業
1. 建立一個程式，要求使用者輸入一句話，然後：
   - 計算總字數和字元數
   - 將每個單字的第一個字母大寫
   - 移除所有空白字元
   - 反轉整個句子

2. 設計一個「文字加密器」，將使用者輸入的文字中的每個字元替換成ASCII碼值+3的字元（簡單的凱撒密碼）

3. 製作一個「文字藝術產生器」，將輸入的文字用不同的符號圍繞起來，創造出美觀的文字框

## 下一步預告
明天我們將學習數學運算，了解Python如何處理各種數學計算，包括基本運算、數學函數等。這將為我們後續的程式設計奠定堅實的數學基礎！