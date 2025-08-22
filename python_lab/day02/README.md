# Day 2：變數與資料型態

## 今日學習目標
- 理解什麼是變數
- 學習Python的基本資料型態
- 掌握變數命名規則
- 實作個人資料卡程式

## 1. 什麼是變數？

變數就像是**標籤貼紙**或**儲物盒**：

### 生活中的比喻：
- **標籤貼紙**：你把便利貼貼在不同的東西上，寫上名字
- **儲物盒**：你有很多盒子，每個盒子裝不同的東西，並貼上標籤

```python
# 變數就像給資料取名字
name = "小明"        # name 這個標籤指向 "小明"
age = 20            # age 這個標籤指向 20
height = 175.5      # height 這個標籤指向 175.5
```

## 2. Python的基本資料型態

### 2.1 字串（String）- 文字資料
```python
name = "張三"
hobby = "看電影"
message = "Hello World"

# 用單引號或雙引號都可以
city = '台北'
country = "台灣"
```

### 2.2 整數（Integer）- 整數
```python
age = 25
score = 95
temperature = -5
```

### 2.3 浮點數（Float）- 小數
```python
height = 170.5
weight = 65.2
pi = 3.14159
```

### 2.4 布林值（Boolean）- 真假值
```python
is_student = True    # 真
is_married = False   # 假
```

## 3. 變數命名規則

### 3.1 合法的命名
```python
name = "小王"          # ✅ 簡單明瞭
user_age = 30         # ✅ 用底線分隔
firstName = "李"       # ✅ 駝峰命名法
score1 = 85           # ✅ 可以包含數字
```

### 3.2 不合法的命名
```python
2age = 30            # ❌ 不能以數字開頭
user-name = "小李"    # ❌ 不能使用減號
class = "A班"         # ❌ 不能使用Python關鍵字
```

### 3.3 命名建議
- **有意義的名字**：`age` 比 `a` 好
- **英文命名**：雖然可以用中文，但建議用英文
- **一致性**：選定一種風格就持續使用

## 4. 查看變數型態

```python
name = "小明"
age = 20
height = 175.5
is_student = True

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student)) # <class 'bool'>
```

## 5. 變數的使用

### 5.1 印出變數
```python
name = "小華"
age = 22

print(name)
print(age)
print("姓名：", name)
print("年齡：", age)
```

### 5.2 變數可以改變
```python
score = 80
print("原本成績：", score)

score = 95  # 改變變數的值
print("新成績：", score)
```

## 6. 實作練習

創建 `personal_info.py`：

```python
# 個人資料卡程式
print("=== 個人資料卡 ===")

# 請修改下面的變數內容
name = "你的姓名"
age = 0
height = 0.0
weight = 0.0
hobby = "你的興趣"
is_student = True

# 顯示資料
print("姓名：", name)
print("年齡：", age, "歲")
print("身高：", height, "公分")
print("體重：", weight, "公斤")
print("興趣：", hobby)
print("是否為學生：", is_student)

print("=== 資料卡結束 ===")
```

## 7. 進階概念

### 7.1 多個變數賦值
```python
# 同時給多個變數賦值
x, y, z = 1, 2, 3
print(x, y, z)  # 輸出：1 2 3

# 交換變數值
a = 10
b = 20
a, b = b, a  # 交換
print(a, b)  # 輸出：20 10
```

### 7.2 變數命名慣例
```python
# 常數（不會改變的值）用全大寫
PI = 3.14159
MAX_SCORE = 100

# 私有變數（進階概念）用底線開頭
_private_var = "內部使用"
```

## 8. 常見錯誤與解決

### 8.1 使用未定義的變數
```python
# 錯誤示例
print(username)  # NameError: name 'username' is not defined

# 正確做法
username = "小明"
print(username)
```

### 8.2 型態不匹配
```python
# 這樣可能會有問題
age = "20"  # 這是字串，不是數字
next_age = age + 1  # 錯誤！不能將字串和數字相加
```

## 9. 今日總結

今天你學會了：
- ✅ 變數的概念（像標籤或儲物盒）
- ✅ 四種基本資料型態：字串、整數、浮點數、布林值
- ✅ 變數命名規則和建議
- ✅ 如何查看和使用變數

## 10. 明日預告

明天我們將學習：
- 如何讓程式與使用者互動
- input() 和 print() 的進階用法
- 製作簡單的對話程式

## 11. 作業

1. 完成 `personal_info.py` 程式，填入你的真實資料
2. 嘗試創建更多變數，練習不同的資料型態
3. 實驗變數賦值和修改
4. 思考：變數在日常生活中有什麼對應的例子？

記住：**變數是程式設計的基礎，就像寫文章需要先學會字彙一樣！**