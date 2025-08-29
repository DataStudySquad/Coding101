# Day 15：函數概念

## 今日學習目標
- 理解函數的基本概念和重要性
- 學會定義和呼叫函數
- 掌握參數傳遞和回傳值的使用
- 實作溫度轉換器程式

## 1. 什麼是函數？

### 1.1 生活中的類比
想像函數就像是**工廠中的機器**：
- **輸入原料**（參數）→ **機器處理**（函數內容）→ **產出產品**（回傳值）
- 例如：咖啡機接受咖啡豆和水，經過處理後產出咖啡

或者想像函數像是**食譜**：
- 有明確的**材料清單**（參數）
- 有詳細的**製作步驟**（函數內容）
- 最終產出**美味料理**（回傳值）

### 1.2 程式中的函數
函數是一段**可重複使用的程式碼**，具有以下特點：
- **封裝性**：將相關程式碼組織在一起
- **重複使用**：寫一次，多次呼叫
- **模組化**：將大問題分解成小問題
- **可讀性**：讓程式更容易理解和維護

```python
# 沒有使用函數的程式碼（重複且難維護）
print("計算第一個圓的面積")
radius1 = 5
area1 = 3.14159 * radius1 * radius1
print(f"圓的面積：{area1}")

print("計算第二個圓的面積")
radius2 = 3
area2 = 3.14159 * radius2 * radius2
print(f"圓的面積：{area2}")

print("計算第三個圓的面積")
radius3 = 7
area3 = 3.14159 * radius3 * radius3
print(f"圓的面積：{area3}")
```

```python
# 使用函數的程式碼（簡潔且易維護）
def calculate_circle_area(radius):
    """計算圓的面積"""
    area = 3.14159 * radius * radius
    return area

# 使用函數
print("計算第一個圓的面積")
area1 = calculate_circle_area(5)
print(f"圓的面積：{area1}")

print("計算第二個圓的面積")
area2 = calculate_circle_area(3)
print(f"圓的面積：{area2}")

print("計算第三個圓的面積")
area3 = calculate_circle_area(7)
print(f"圓的面積：{area3}")
```

## 2. 函數的基本語法

### 2.1 函數定義
```python
def 函數名稱(參數1, 參數2, ...):
    """函數說明文件"""
    # 函數內容
    # 處理邏輯
    return 回傳值  # 可選
```

**語法說明：**
- `def`：定義函數的關鍵字
- `函數名稱`：遵循變數命名規則，建議使用動詞
- `參數`：函數接收的輸入（可選）
- `"""`：函數說明文件（建議加上）
- `return`：回傳結果（可選）

### 2.2 函數呼叫
```python
# 呼叫函數
結果 = 函數名稱(參數1, 參數2, ...)

# 或者直接使用
print(函數名稱(參數1, 參數2, ...))
```

### 2.3 基本範例
```python
# 定義一個簡單的打招呼函數
def greet():
    """打招呼函數"""
    print("你好！歡迎來到Python世界！")

# 呼叫函數
greet()  # 輸出：你好！歡迎來到Python世界！

# 定義一個有參數的函數
def greet_person(name):
    """個人化打招呼函數"""
    print(f"你好，{name}！")

# 呼叫函數
greet_person("小明")  # 輸出：你好，小明！
greet_person("小美")  # 輸出：你好，小美！

# 定義一個有回傳值的函數
def add_numbers(a, b):
    """加法函數"""
    result = a + b
    return result

# 呼叫函數並使用回傳值
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")  # 輸出：5 + 3 = 8
```

## 3. 參數（Parameters）詳解

### 3.1 必需參數
```python
def introduce_person(name, age):
    """介紹一個人"""
    print(f"這是{name}，今年{age}歲")

# 必須提供所有參數
introduce_person("張三", 25)  # 正確
# introduce_person("張三")    # 錯誤：缺少參數
```

### 3.2 位置參數與關鍵字參數
```python
def calculate_rectangle_area(length, width):
    """計算長方形面積"""
    area = length * width
    return area

# 位置參數：按照順序傳遞
area1 = calculate_rectangle_area(5, 3)  # length=5, width=3

# 關鍵字參數：指定參數名稱
area2 = calculate_rectangle_area(width=3, length=5)  # 順序可以改變

# 混合使用（位置參數必須在前）
area3 = calculate_rectangle_area(5, width=3)  # length=5, width=3
```

### 3.3 參數傳遞的概念
```python
def modify_value(x):
    """嘗試修改數值"""
    x = x + 10
    print(f"函數內的x: {x}")
    return x

# 測試參數傳遞
original = 5
result = modify_value(original)
print(f"原始值: {original}")  # 原始值: 5（沒有改變）
print(f"回傳值: {result}")    # 回傳值: 15

def modify_list(my_list):
    """修改清單"""
    my_list.append("新項目")
    print(f"函數內的清單: {my_list}")

# 測試清單傳遞
original_list = ["A", "B", "C"]
modify_list(original_list)
print(f"原始清單: {original_list}")  # 原始清單: ['A', 'B', 'C', '新項目']（已改變）
```

## 4. 回傳值（Return Values）詳解

### 4.1 單一回傳值
```python
def calculate_square(number):
    """計算平方"""
    return number ** 2

result = calculate_square(4)
print(result)  # 16
```

### 4.2 多重回傳值
```python
def calculate_rectangle_info(length, width):
    """計算長方形的周長和面積"""
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area  # 回傳元組

# 接收多重回傳值
p, a = calculate_rectangle_info(5, 3)
print(f"周長: {p}, 面積: {a}")

# 或者接收為元組
result = calculate_rectangle_info(5, 3)
print(f"結果: {result}")  # 結果: (16, 15)
```

### 4.3 條件回傳
```python
def check_grade(score):
    """檢查成績等第"""
    if score >= 90:
        return "優秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "及格"
    else:
        return "不及格"

grade = check_grade(85)
print(f"成績等第: {grade}")  # 成績等第: 良好
```

### 4.4 沒有回傳值的函數
```python
def print_report(name, score):
    """列印報告（沒有明確的return）"""
    print("=" * 30)
    print(f"學生姓名: {name}")
    print(f"成績: {score}")
    print("=" * 30)
    # 沒有return語句，會自動回傳None

result = print_report("小明", 85)
print(f"函數回傳值: {result}")  # 函數回傳值: None
```

## 5. 函數的好處與應用場景

### 5.1 程式碼重複使用
```python
def format_currency(amount):
    """格式化貨幣顯示"""
    return f"NT$ {amount:,.2f}"

# 重複使用同一個函數
print(f"商品價格: {format_currency(1500)}")
print(f"折扣金額: {format_currency(300)}")
print(f"實付金額: {format_currency(1200)}")
```

### 5.2 程式碼模組化
```python
def get_user_input():
    """獲取使用者輸入"""
    name = input("請輸入姓名: ")
    age = int(input("請輸入年齡: "))
    return name, age

def validate_age(age):
    """驗證年齡"""
    return 0 <= age <= 120

def display_result(name, age, is_valid):
    """顯示結果"""
    if is_valid:
        print(f"{name}，你的年齡是{age}歲，資料有效。")
    else:
        print(f"{name}，年齡{age}不在有效範圍內。")

# 主程式
def main():
    name, age = get_user_input()
    is_valid = validate_age(age)
    display_result(name, age, is_valid)

# 執行主程式
main()
```

### 5.3 降低程式複雜度
```python
def calculate_tax(income):
    """計算所得稅"""
    if income <= 540000:
        return income * 0.05
    elif income <= 1210000:
        return income * 0.12 - 37800
    else:
        return income * 0.2 - 134600

def calculate_net_income(gross_income):
    """計算淨收入"""
    tax = calculate_tax(gross_income)
    net_income = gross_income - tax
    return net_income, tax

# 使用函數讓邏輯更清晰
gross = 800000
net, tax = calculate_net_income(gross)
print(f"總收入: {gross}")
print(f"所得稅: {tax}")
print(f"淨收入: {net}")
```

## 6. 實作項目：溫度轉換器

讓我們應用所學的函數概念，建立一個實用的溫度轉換器：

### 6.1 功能需求
1. 攝氏轉華氏
2. 華氏轉攝氏
3. 攝氏轉克氏（Kelvin）
4. 克氏轉攝氏
5. 溫度有效性檢查
6. 友好的使用者界面

### 6.2 設計思路
```python
# 溫度轉換公式：
# 攝氏轉華氏：F = C × 9/5 + 32
# 華氏轉攝氏：C = (F - 32) × 5/9
# 攝氏轉克氏：K = C + 273.15
# 克氏轉攝氏：C = K - 273.15
```

### 6.3 完整實作
```python
def celsius_to_fahrenheit(celsius):
    """攝氏轉華氏"""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """華氏轉攝氏"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    """攝氏轉克氏"""
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    """克氏轉攝氏"""
    celsius = kelvin - 273.15
    return celsius

def validate_temperature(temp, scale):
    """驗證溫度是否在合理範圍內"""
    if scale.upper() == 'C':
        # 攝氏：絕對零度 -273.15°C 到太陽表面 5500°C
        return -273.15 <= temp <= 10000
    elif scale.upper() == 'F':
        # 華氏：絕對零度 -459.67°F 到合理上限
        return -459.67 <= temp <= 18000
    elif scale.upper() == 'K':
        # 克氏：絕對零度 0K 到合理上限
        return 0 <= temp <= 10273.15
    return False

def format_temperature(temp, scale):
    """格式化溫度顯示"""
    scale_symbols = {'C': '°C', 'F': '°F', 'K': 'K'}
    symbol = scale_symbols.get(scale.upper(), '°')
    return f"{temp:.2f}{symbol}"

def display_conversion_result(original_temp, original_scale, converted_temp, converted_scale):
    """顯示轉換結果"""
    original_formatted = format_temperature(original_temp, original_scale)
    converted_formatted = format_temperature(converted_temp, converted_scale)
    print(f"\n🌡️  轉換結果：{original_formatted} = {converted_formatted}")

def get_temperature_input():
    """獲取溫度輸入"""
    while True:
        try:
            temp_str = input("\n請輸入溫度數值: ").strip()
            temp = float(temp_str)
            return temp
        except ValueError:
            print("❌ 請輸入有效的數字！")

def get_scale_input(prompt):
    """獲取溫度單位輸入"""
    while True:
        scale = input(prompt).strip().upper()
        if scale in ['C', 'F', 'K']:
            return scale
        print("❌ 請輸入 C（攝氏）、F（華氏）或 K（克氏）！")

def display_menu():
    """顯示主選單"""
    print("\n" + "="*50)
    print("🌡️           溫度轉換器           🌡️")
    print("="*50)
    print("1. 攝氏 → 華氏 (C → F)")
    print("2. 華氏 → 攝氏 (F → C)")
    print("3. 攝氏 → 克氏 (C → K)")
    print("4. 克氏 → 攝氏 (K → C)")
    print("5. 自訂轉換")
    print("6. 溫度對照表")
    print("0. 離開程式")
    print("-"*50)

def show_temperature_reference():
    """顯示溫度對照表"""
    print("\n🌡️ 常見溫度對照表")
    print("="*60)
    
    # 常見溫度點
    reference_points = [
        ("絕對零度", -273.15, "C"),
        ("水結冰點", 0, "C"),
        ("室溫", 25, "C"),
        ("人體體溫", 37, "C"),
        ("水沸點", 100, "C"),
        ("烤箱溫度", 200, "C")
    ]
    
    print(f"{'項目':<12} {'攝氏(°C)':<10} {'華氏(°F)':<10} {'克氏(K)':<10}")
    print("-"*60)
    
    for name, temp_c, scale in reference_points:
        temp_f = celsius_to_fahrenheit(temp_c)
        temp_k = celsius_to_kelvin(temp_c)
        print(f"{name:<12} {temp_c:<10.2f} {temp_f:<10.2f} {temp_k:<10.2f}")

def custom_conversion():
    """自訂轉換功能"""
    print("\n🔄 自訂溫度轉換")
    
    # 獲取原始溫度和單位
    temp = get_temperature_input()
    from_scale = get_scale_input("請輸入原始溫度單位 (C/F/K): ")
    
    # 驗證溫度
    if not validate_temperature(temp, from_scale):
        print(f"❌ 溫度 {temp}°{from_scale} 超出合理範圍！")
        return
    
    # 獲取目標單位
    to_scale = get_scale_input("請輸入目標溫度單位 (C/F/K): ")
    
    if from_scale == to_scale:
        print("⚠️  相同的溫度單位不需要轉換！")
        return
    
    # 執行轉換
    converted_temp = convert_temperature(temp, from_scale, to_scale)
    if converted_temp is not None:
        display_conversion_result(temp, from_scale, converted_temp, to_scale)

def convert_temperature(temp, from_scale, to_scale):
    """通用溫度轉換函數"""
    # 先轉換為攝氏度作為中間值
    if from_scale == 'C':
        celsius = temp
    elif from_scale == 'F':
        celsius = fahrenheit_to_celsius(temp)
    elif from_scale == 'K':
        celsius = kelvin_to_celsius(temp)
    else:
        return None
    
    # 從攝氏度轉換為目標單位
    if to_scale == 'C':
        return celsius
    elif to_scale == 'F':
        return celsius_to_fahrenheit(celsius)
    elif to_scale == 'K':
        return celsius_to_kelvin(celsius)
    else:
        return None

def temperature_converter():
    """主程式"""
    print("🎉 歡迎使用溫度轉換器！")
    
    while True:
        display_menu()
        choice = input("請選擇功能 (0-6): ").strip()
        
        if choice == "1":
            # 攝氏轉華氏
            temp_c = get_temperature_input()
            if validate_temperature(temp_c, 'C'):
                temp_f = celsius_to_fahrenheit(temp_c)
                display_conversion_result(temp_c, 'C', temp_f, 'F')
            else:
                print("❌ 攝氏溫度超出合理範圍！")
                
        elif choice == "2":
            # 華氏轉攝氏
            temp_f = get_temperature_input()
            if validate_temperature(temp_f, 'F'):
                temp_c = fahrenheit_to_celsius(temp_f)
                display_conversion_result(temp_f, 'F', temp_c, 'C')
            else:
                print("❌ 華氏溫度超出合理範圍！")
                
        elif choice == "3":
            # 攝氏轉克氏
            temp_c = get_temperature_input()
            if validate_temperature(temp_c, 'C'):
                temp_k = celsius_to_kelvin(temp_c)
                display_conversion_result(temp_c, 'C', temp_k, 'K')
            else:
                print("❌ 攝氏溫度超出合理範圍！")
                
        elif choice == "4":
            # 克氏轉攝氏
            temp_k = get_temperature_input()
            if validate_temperature(temp_k, 'K'):
                temp_c = kelvin_to_celsius(temp_k)
                display_conversion_result(temp_k, 'K', temp_c, 'C')
            else:
                print("❌ 克氏溫度超出合理範圍！")
                
        elif choice == "5":
            # 自訂轉換
            custom_conversion()
            
        elif choice == "6":
            # 溫度對照表
            show_temperature_reference()
            
        elif choice == "0":
            print("\n👋 感謝使用溫度轉換器！")
            break
            
        else:
            print("❌ 無效選擇！請輸入 0-6 之間的數字。")
        
        # 暫停讓使用者查看結果
        if choice != "0":
            input("\n按 Enter 鍵繼續...")

# 程式入口點
if __name__ == "__main__":
    temperature_converter()
```

## 7. 程式設計最佳實踐

### 7.1 函數命名規範
```python
# 好的函數名稱（動詞 + 名詞）
def calculate_area()           # 計算面積
def validate_email()           # 驗證電子郵件
def convert_temperature()      # 轉換溫度
def display_menu()            # 顯示選單

# 不好的函數名稱
def area()                    # 不夠明確
def check()                   # 檢查什麼？
def process()                 # 處理什麼？
def func1()                   # 無意義名稱
```

### 7.2 函數文檔字串
```python
def calculate_compound_interest(principal, rate, time, compound_frequency=12):
    """
    計算複利
    
    參數:
        principal (float): 本金
        rate (float): 年利率（以小數表示，如0.05表示5%）
        time (int): 投資年數
        compound_frequency (int): 每年複利次數，預設為12（月複利）
    
    回傳:
        float: 複利計算後的總金額
    
    範例:
        >>> calculate_compound_interest(10000, 0.05, 2)
        11049.41
    """
    amount = principal * (1 + rate/compound_frequency) ** (compound_frequency * time)
    return round(amount, 2)
```

### 7.3 函數設計原則
1. **單一職責**：每個函數只做一件事
2. **簡短明確**：函數長度不宜過長
3. **參數合理**：參數數量不宜過多
4. **有意義的命名**：函數和參數名稱要有意義
5. **適當的回傳值**：回傳有用的資訊

```python
# 好的函數設計
def calculate_bmi(weight, height):
    """計算BMI指數"""
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def classify_bmi(bmi):
    """分類BMI等級"""
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "正常範圍"
    elif bmi < 27:
        return "過重"
    else:
        return "肥胖"

def get_bmi_advice(classification):
    """根據BMI分類給予建議"""
    advice = {
        "體重過輕": "建議增加營養攝取，適度運動增加肌肉量",
        "正常範圍": "維持目前的健康生活方式",
        "過重": "建議控制飲食，增加運動量",
        "肥胖": "建議諮詢醫師，制定減重計劃"
    }
    return advice.get(classification, "請諮詢專業醫師")

# 整合使用
def bmi_analyzer(weight, height):
    """BMI分析器"""
    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)
    advice = get_bmi_advice(classification)
    
    return {
        "bmi": bmi,
        "classification": classification,
        "advice": advice
    }
```

## 8. 實作練習

### 8.1 基礎練習
```python
# 練習1：創建一個計算圓形周長的函數
def calculate_circle_circumference(radius):
    """完成這個函數"""
    pass

# 練習2：創建一個判斷偶數的函數
def is_even(number):
    """完成這個函數"""
    pass

# 練習3：創建一個字串反轉函數
def reverse_string(text):
    """完成這個函數"""
    pass
```

### 8.2 進階練習
```python
# 練習4：創建一個密碼強度檢查函數
def check_password_strength(password):
    """
    檢查密碼強度
    規則：
    - 長度至少8個字符
    - 包含大寫字母
    - 包含小寫字母
    - 包含數字
    - 包含特殊字符
    回傳強度等級：弱、中、強
    """
    pass

# 練習5：創建一個成績分析函數
def analyze_grades(scores):
    """
    分析成績列表
    回傳：平均分、最高分、最低分、及格人數
    """
    pass
```

## 9. 常見錯誤與除錯

### 9.1 常見錯誤
```python
# 錯誤1：忘記呼叫函數
def greet():
    print("Hello!")

greet  # 錯誤：沒有括號，不會執行函數
greet()  # 正確：有括號，會執行函數

# 錯誤2：參數數量不匹配
def add(a, b):
    return a + b

result = add(5)  # 錯誤：缺少參數
result = add(5, 3, 2)  # 錯誤：參數過多
result = add(5, 3)  # 正確

# 錯誤3：忘記回傳值
def calculate(x):
    result = x * 2
    # 忘記return，函數會回傳None

def calculate(x):
    result = x * 2
    return result  # 正確
```

### 9.2 除錯技巧
```python
def debug_function(a, b):
    """示範除錯技巧"""
    print(f"函數開始執行，參數：a={a}, b={b}")  # 除錯訊息
    
    result = a + b
    print(f"計算結果：{result}")  # 除錯訊息
    
    return result

# 使用除錯
result = debug_function(3, 5)
print(f"最終結果：{result}")
```

## 10. 今日總結

今天你學會了：
- ✅ 函數的基本概念和語法
- ✅ 參數傳遞和回傳值的使用
- ✅ 函數的設計原則和最佳實踐
- ✅ 實作溫度轉換器應用程式

**關鍵概念回顧：**
- 函數是可重複使用的程式碼塊
- 參數讓函數更加靈活
- 回傳值讓函數能夠產出結果
- 良好的函數設計讓程式更易維護

**明天預告：**
我們將學習函數的進階概念，包括預設參數、變數作用域等，並實作密碼強度檢查器！

記住：**函數是程式設計的基石，掌握了函數就掌握了程式模組化的精髓！**