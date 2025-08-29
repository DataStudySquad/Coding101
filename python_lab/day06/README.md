# Day 6：條件判斷（if）

## 今日學習目標
- 理解程式的決策能力概念
- 掌握if, elif, else的使用方法
- 學會各種比較運算子
- 實作成績等第判斷系統

## 1. 什麼是條件判斷？

想像條件判斷就像是**人生中的選擇題**：

- **日常例子**：如果下雨，就帶雨傘；否則就不帶
- **程式例子**：如果分數>=90，就顯示"優等"；否則顯示其他等第

### 生活中的條件判斷
```
如果 天氣下雨：
    帶雨傘
否則：
    不帶雨傘

如果 錢包有錢：
    可以買東西
否則：
    不能買東西
```

## 2. Python的條件判斷語法

### 基本if語法
```python
if 條件:
    要執行的程式碼
```

### if-else語法
```python
if 條件:
    條件為真時執行
else:
    條件為假時執行
```

### if-elif-else語法
```python
if 條件1:
    條件1為真時執行
elif 條件2:
    條件2為真時執行
else:
    所有條件都不符合時執行
```

## 3. 比較運算子

| 運算子 | 意義 | 範例 | 結果 |
|--------|------|------|------|
| == | 等於 | 5 == 5 | True |
| != | 不等於 | 5 != 3 | True |
| > | 大於 | 5 > 3 | True |
| < | 小於 | 3 < 5 | True |
| >= | 大於等於 | 5 >= 5 | True |
| <= | 小於等於 | 3 <= 5 | True |

### 重要提醒
- **賦值** 用 `=`：`x = 5`（把5放進x）
- **比較** 用 `==`：`x == 5`（檢查x是否等於5）

## 4. 程式範例

### 範例1：簡單條件判斷
```python
age = int(input("請輸入你的年齡："))

if age >= 18:
    print("你已經成年了！")
else:
    print("你還是未成年。")
```

### 範例2：多重條件判斷
```python
score = int(input("請輸入你的分數："))

if score >= 90:
    print("優等！恭喜你！")
elif score >= 80:
    print("甲等，很棒！")
elif score >= 70:
    print("乙等，還不錯！")
elif score >= 60:
    print("丙等，及格了。")
else:
    print("不及格，要加油喔！")
```

### 範例3：複合條件
```python
username = input("請輸入使用者名稱：")
password = input("請輸入密碼：")

if username == "admin" and password == "12345":
    print("登入成功！歡迎管理員！")
elif username == "user" and password == "password":
    print("登入成功！歡迎使用者！")
else:
    print("帳號或密碼錯誤！")
```

## 5. 邏輯運算子

| 運算子 | 意義 | 範例 |
|--------|------|------|
| and | 且（兩個條件都要成立） | age >= 18 and score >= 60 |
| or | 或（至少一個條件成立） | day == "Saturday" or day == "Sunday" |
| not | 非（相反條件） | not is_raining |

### 邏輯運算子範例
```python
age = int(input("請輸入年齡："))
has_license = input("有駕照嗎？(yes/no)：").lower() == "yes"

# 使用 and
if age >= 18 and has_license:
    print("可以開車！")
else:
    print("不能開車。")

# 使用 or
day = input("今天是什麼日子？").lower()
if day == "saturday" or day == "sunday":
    print("今天是週末！")
else:
    print("今天是平日。")

# 使用 not
is_raining = input("現在下雨嗎？(yes/no)：").lower() == "yes"
if not is_raining:
    print("天氣不錯，適合出門！")
else:
    print("在下雨，記得帶雨傘！")
```

## 6. 巢狀條件判斷

```python
weather = input("今天天氣如何？(sunny/rainy/cloudy)：").lower()
temperature = int(input("今天溫度幾度？："))

if weather == "sunny":
    if temperature > 25:
        print("太陽很大又很熱，記得防曬和多喝水！")
    else:
        print("陽光普照，是個好天氣！")
elif weather == "rainy":
    if temperature < 15:
        print("又冷又下雨，記得保暖和帶雨傘！")
    else:
        print("下雨天，記得帶雨傘！")
else:  # cloudy
    print("多雲的天氣，還算不錯。")
```

## 7. 實作練習

### 練習1：BMI計算器
```python
def calculate_bmi():
    print("=== BMI計算器 ===")
    
    height = float(input("請輸入身高（公尺）："))
    weight = float(input("請輸入體重（公斤）："))
    
    bmi = weight / (height ** 2)
    
    print(f"你的BMI值是：{bmi:.2f}")
    
    if bmi < 18.5:
        print("體重過輕")
    elif bmi < 24:
        print("體重正常")
    elif bmi < 27:
        print("體重過重")
    elif bmi < 30:
        print("輕度肥胖")
    elif bmi < 35:
        print("中度肥胖")
    else:
        print("重度肥胖")

calculate_bmi()
```

### 練習2：簡單計算機
```python
def simple_calculator():
    print("=== 簡單計算機 ===")
    
    num1 = float(input("請輸入第一個數字："))
    operator = input("請輸入運算子 (+, -, *, /)：")
    num2 = float(input("請輸入第二個數字："))
    
    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} × {num2} = {result}")
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} ÷ {num2} = {result}")
        else:
            print("錯誤：除數不能為零！")
    else:
        print("錯誤：不支援的運算子！")

simple_calculator()
```

### 練習3：密碼強度檢查器
```python
def check_password_strength():
    print("=== 密碼強度檢查器 ===")
    
    password = input("請輸入密碼：")
    strength_score = 0
    feedback = []
    
    # 檢查長度
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("密碼長度至少要8個字元")
    
    # 檢查是否包含數字
    has_digit = any(char.isdigit() for char in password)
    if has_digit:
        strength_score += 1
    else:
        feedback.append("密碼應包含數字")
    
    # 檢查是否包含大寫字母
    has_upper = any(char.isupper() for char in password)
    if has_upper:
        strength_score += 1
    else:
        feedback.append("密碼應包含大寫字母")
    
    # 檢查是否包含小寫字母
    has_lower = any(char.islower() for char in password)
    if has_lower:
        strength_score += 1
    else:
        feedback.append("密碼應包含小寫字母")
    
    # 檢查是否包含特殊字元
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(char in special_chars for char in password)
    if has_special:
        strength_score += 1
    else:
        feedback.append("密碼應包含特殊字元")
    
    # 評估強度
    if strength_score >= 4:
        print("密碼強度：強")
    elif strength_score >= 3:
        print("密碼強度：中等")
    elif strength_score >= 2:
        print("密碼強度：弱")
    else:
        print("密碼強度：非常弱")
    
    # 顯示改善建議
    if feedback:
        print("改善建議：")
        for suggestion in feedback:
            print(f"- {suggestion}")

check_password_strength()
```

## 8. 常見錯誤

### 錯誤1：使用賦值運算子
```python
# 錯誤
x = 5
if x = 5:  # 這是錯誤的！
    print("x等於5")

# 正確
x = 5
if x == 5:  # 這是正確的！
    print("x等於5")
```

### 錯誤2：忘記冒號
```python
# 錯誤
if age >= 18  # 忘記冒號
    print("成年了")

# 正確
if age >= 18:  # 記得加冒號
    print("成年了")
```

### 錯誤3：縮排錯誤
```python
# 錯誤
if score >= 60:
print("及格")  # 沒有縮排

# 正確
if score >= 60:
    print("及格")  # 正確縮排
```

## 9. 除錯小技巧

1. **列印變數值**：不確定變數內容時，先印出來看看
```python
score = int(input("請輸入分數："))
print(f"debug: score = {score}")  # 除錯用

if score >= 60:
    print("及格")
```

2. **分步驟測試**：複雜條件分開測試
```python
age = int(input("年齡："))
has_license = input("有駕照嗎？").lower() == "yes"

print(f"age >= 18: {age >= 18}")
print(f"has_license: {has_license}")

if age >= 18 and has_license:
    print("可以開車")
```

## 10. 實際應用：成績管理系統

```python
def grade_management_system():
    """成績管理系統"""
    print("=== 學生成績管理系統 ===")
    
    student_name = input("請輸入學生姓名：")
    
    # 輸入各科成績
    chinese = float(input("請輸入國文成績："))
    english = float(input("請輸入英文成績："))
    math = float(input("請輸入數學成績："))
    
    # 計算平均
    average = (chinese + english + math) / 3
    
    # 判斷等第
    if average >= 90:
        grade = "優等"
        comment = "表現優異！"
    elif average >= 80:
        grade = "甲等"
        comment = "表現良好！"
    elif average >= 70:
        grade = "乙等"
        comment = "表現尚可。"
    elif average >= 60:
        grade = "丙等"
        comment = "需要努力。"
    else:
        grade = "不及格"
        comment = "需要加強！"
    
    # 檢查是否有單科不及格
    failed_subjects = []
    if chinese < 60:
        failed_subjects.append("國文")
    if english < 60:
        failed_subjects.append("英文")
    if math < 60:
        failed_subjects.append("數學")
    
    # 輸出結果
    print(f"\n=== {student_name} 的成績單 ===")
    print(f"國文：{chinese}分")
    print(f"英文：{english}分")
    print(f"數學：{math}分")
    print(f"平均：{average:.2f}分")
    print(f"等第：{grade}")
    print(f"評語：{comment}")
    
    if failed_subjects:
        print(f"單科不及格：{', '.join(failed_subjects)}")
        print("建議：針對不及格科目加強復習。")
    else:
        print("所有科目都及格！")

grade_management_system()
```

## 11. 重點整理

1. **if語句**：程式的決策工具
2. **比較運算子**：==, !=, >, <, >=, <=
3. **邏輯運算子**：and, or, not
4. **語法重點**：記得冒號和縮排
5. **常見錯誤**：混淆 = 和 ==

## 12. 作業

1. **製作一個「人生建議程式」**：
   - 根據使用者的年齡給予不同建議
   - 18歲以下：專心讀書
   - 18-30歲：努力學習技能
   - 30-50歲：專注事業發展
   - 50歲以上：享受人生

2. **設計一個「餐廳點餐系統」**：
   - 顯示菜單和價格
   - 讓使用者選擇餐點
   - 根據金額給予折扣（滿500打9折，滿1000打8折）
   - 計算總金額

3. **建立一個「天氣穿搭建議」**：
   - 根據溫度和天氣狀況建議穿著
   - 考慮是否下雨、溫度高低
   - 給予具體的穿搭建議

## 13. 明日預告

明天是第一週的複習日，我們將：
- 整合本週所學的概念
- 製作一個綜合性的問答遊戲
- 練習所有學過的語法
- 為下週的學習做準備

記住：**條件判斷讓程式變得聰明，能夠根據不同情況做出不同的反應！**