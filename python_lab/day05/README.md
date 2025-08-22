# Day 5: 數學運算

## 學習目標
- 掌握Python中的基本數學運算子
- 了解數學運算的優先順序
- 學會使用Python的數學模組
- 練習數學運算在實際問題中的應用

## 理論說明

### 數學運算的重要性
就像日常生活中我們需要計算購物費用、計算時間、測量距離一樣，程式設計也經常需要進行各種數學運算。Python提供了豐富的數學運算功能，就像一個超強的計算機！

### 想像數學運算
想像Python就像一個萬能的計算機：
- **基本運算**：就像小學數學課學的加減乘除
- **進階運算**：就像科學計算機的各種函數
- **數學模組**：就像專業的數學工具箱

## 程式範例

### 1. 基本運算子
```python
# 基本四則運算
a = 10
b = 3

print(f"{a} + {b} = {a + b}")    # 加法：10 + 3 = 13
print(f"{a} - {b} = {a - b}")    # 減法：10 - 3 = 7
print(f"{a} * {b} = {a * b}")    # 乘法：10 * 3 = 30
print(f"{a} / {b} = {a / b}")    # 除法：10 / 3 = 3.333...

# 特殊運算子
print(f"{a} // {b} = {a // b}")  # 整數除法：10 // 3 = 3
print(f"{a} % {b} = {a % b}")    # 取餘數：10 % 3 = 1
print(f"{a} ** {b} = {a ** b}")  # 次方：10 ** 3 = 1000
```

### 2. 運算優先順序
```python
# 運算優先順序（由高到低）
# 1. 括號 ()
# 2. 次方 **
# 3. 乘法 *、除法 /、整數除法 //、取餘數 %
# 4. 加法 +、減法 -

result1 = 2 + 3 * 4        # 2 + (3 * 4) = 14
result2 = (2 + 3) * 4      # (2 + 3) * 4 = 20
result3 = 2 ** 3 * 4       # (2 ** 3) * 4 = 32
result4 = 10 - 6 / 2       # 10 - (6 / 2) = 7.0

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")
print(f"2 ** 3 * 4 = {result3}")
print(f"10 - 6 / 2 = {result4}")
```

### 3. 數學模組的使用
```python
import math

# 常用數學函數
number = 16

print(f"平方根 √{number} = {math.sqrt(number)}")
print(f"絕對值 |{-number}| = {math.fabs(-number)}")
print(f"向上取整 ⌈{3.2}⌉ = {math.ceil(3.2)}")
print(f"向下取整 ⌊{3.8}⌋ = {math.floor(3.8)}")
print(f"四捨五入 round({3.7}) = {round(3.7)}")

# 三角函數（使用弧度）
angle_degrees = 45
angle_radians = math.radians(angle_degrees)

print(f"\n{angle_degrees}度 = {angle_radians}弧度")
print(f"sin({angle_degrees}°) = {math.sin(angle_radians):.4f}")
print(f"cos({angle_degrees}°) = {math.cos(angle_radians):.4f}")
print(f"tan({angle_degrees}°) = {math.tan(angle_radians):.4f}")

# 對數和指數
print(f"\ne的值 = {math.e:.6f}")
print(f"π的值 = {math.pi:.6f}")
print(f"e^2 = {math.exp(2):.4f}")
print(f"ln(10) = {math.log(10):.4f}")
print(f"log₁₀(100) = {math.log10(100)}")
```

### 4. 複合指定運算子
```python
# 複合指定運算子讓程式碼更簡潔
x = 10

print(f"原始值：x = {x}")

x += 5    # 等同於 x = x + 5
print(f"x += 5 後：x = {x}")

x -= 3    # 等同於 x = x - 3
print(f"x -= 3 後：x = {x}")

x *= 2    # 等同於 x = x * 2
print(f"x *= 2 後：x = {x}")

x /= 4    # 等同於 x = x / 4
print(f"x /= 4 後：x = {x}")

x **= 2   # 等同於 x = x ** 2
print(f"x **= 2 後：x = {x}")
```

### 5. 數字型別轉換
```python
# 整數、浮點數、字串之間的轉換
integer_num = 42
float_num = 3.14159
string_num = "123"

print("原始值：")
print(f"整數：{integer_num} (型別：{type(integer_num)})")
print(f"浮點數：{float_num} (型別：{type(float_num)})")
print(f"字串：{string_num} (型別：{type(string_num)})")

print("\n轉換後：")
print(f"整數→浮點數：{float(integer_num)}")
print(f"浮點數→整數：{int(float_num)}")
print(f"字串→整數：{int(string_num)}")
print(f"字串→浮點數：{float(string_num)}")
print(f"數字→字串：'{str(integer_num)}'")
```

## 實作練習

### 練習1：智慧計算機
```python
def smart_calculator():
    """製作一個智慧計算機"""
    print("=== 智慧計算機 ===")
    
    while True:
        try:
            expression = input("請輸入數學運算式（或輸入'quit'結束）：")
            
            if expression.lower() == 'quit':
                print("感謝使用！")
                break
            
            # 安全評估數學運算式
            # 注意：在實際應用中需要更嚴格的安全檢查
            result = eval(expression)
            print(f"結果：{expression} = {result}")
            
        except Exception as e:
            print(f"計算錯誤：{e}")
            print("請輸入有效的數學運算式")

# 呼叫函數
# smart_calculator()  # 取消註解來執行
```

### 練習2：幾何計算器
```python
import math

def circle_calculator():
    """圓形計算器"""
    print("=== 圓形計算器 ===")
    radius = float(input("請輸入圓的半徑："))
    
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    
    print(f"半徑：{radius}")
    print(f"面積：{area:.2f}")
    print(f"周長：{circumference:.2f}")

def triangle_calculator():
    """三角形計算器"""
    print("\n=== 三角形計算器 ===")
    base = float(input("請輸入三角形的底邊長："))
    height = float(input("請輸入三角形的高："))
    
    area = 0.5 * base * height
    
    print(f"底邊長：{base}")
    print(f"高：{height}")
    print(f"面積：{area:.2f}")

def rectangle_calculator():
    """矩形計算器"""
    print("\n=== 矩形計算器 ===")
    length = float(input("請輸入矩形的長："))
    width = float(input("請輸入矩形的寬："))
    
    area = length * width
    perimeter = 2 * (length + width)
    
    print(f"長：{length}")
    print(f"寬：{width}")
    print(f"面積：{area:.2f}")
    print(f"周長：{perimeter:.2f}")

# 執行幾何計算
circle_calculator()
triangle_calculator()
rectangle_calculator()
```

### 練習3：單位轉換器
```python
def temperature_converter():
    """溫度轉換器"""
    print("=== 溫度轉換器 ===")
    
    celsius = float(input("請輸入攝氏溫度："))
    
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    
    print(f"{celsius}°C = {fahrenheit:.1f}°F")
    print(f"{celsius}°C = {kelvin:.2f}K")

def length_converter():
    """長度轉換器"""
    print("\n=== 長度轉換器 ===")
    
    meters = float(input("請輸入公尺數："))
    
    centimeters = meters * 100
    feet = meters * 3.28084
    inches = meters * 39.3701
    
    print(f"{meters}公尺 = {centimeters}公分")
    print(f"{meters}公尺 = {feet:.2f}英尺")
    print(f"{meters}公尺 = {inches:.2f}英寸")

def weight_converter():
    """重量轉換器"""
    print("\n=== 重量轉換器 ===")
    
    kg = float(input("請輸入公斤數："))
    
    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274
    
    print(f"{kg}公斤 = {grams}公克")
    print(f"{kg}公斤 = {pounds:.2f}磅")
    print(f"{kg}公斤 = {ounces:.2f}盎司")

# 執行單位轉換
temperature_converter()
length_converter()
weight_converter()
```

## 實際應用範例

### 貸款計算器
```python
import math

def loan_calculator():
    """貸款計算器"""
    print("=== 貸款計算器 ===")
    
    principal = float(input("請輸入貸款本金："))
    annual_rate = float(input("請輸入年利率（%）：")) / 100
    years = int(input("請輸入貸款年數："))
    
    # 月利率和總月數
    monthly_rate = annual_rate / 12
    total_months = years * 12
    
    # 月付金計算公式
    if monthly_rate > 0:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**total_months) / \
                         ((1 + monthly_rate)**total_months - 1)
    else:
        monthly_payment = principal / total_months
    
    total_payment = monthly_payment * total_months
    total_interest = total_payment - principal
    
    print(f"\n貸款詳情：")
    print(f"本金：${principal:,.2f}")
    print(f"年利率：{annual_rate*100:.2f}%")
    print(f"貸款期間：{years}年（{total_months}個月）")
    print(f"月付金：${monthly_payment:,.2f}")
    print(f"總付款：${total_payment:,.2f}")
    print(f"總利息：${total_interest:,.2f}")

# loan_calculator()  # 取消註解來執行
```

### 統計計算器
```python
def statistics_calculator():
    """統計計算器"""
    print("=== 統計計算器 ===")
    
    # 輸入數據
    data_str = input("請輸入數字（用逗號分隔）：")
    numbers = [float(x.strip()) for x in data_str.split(',')]
    
    # 計算統計值
    count = len(numbers)
    total = sum(numbers)
    mean = total / count
    
    # 排序後計算中位數
    sorted_numbers = sorted(numbers)
    if count % 2 == 0:
        median = (sorted_numbers[count//2 - 1] + sorted_numbers[count//2]) / 2
    else:
        median = sorted_numbers[count//2]
    
    # 計算變異數和標準差
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    
    # 最大值和最小值
    maximum = max(numbers)
    minimum = min(numbers)
    
    print(f"\n統計結果：")
    print(f"數據個數：{count}")
    print(f"總和：{total:.2f}")
    print(f"平均數：{mean:.2f}")
    print(f"中位數：{median:.2f}")
    print(f"最大值：{maximum:.2f}")
    print(f"最小值：{minimum:.2f}")
    print(f"標準差：{std_dev:.2f}")
    print(f"變異數：{variance:.2f}")

# statistics_calculator()  # 取消註解來執行
```

## 重點整理
1. **基本運算**：+, -, *, /, //, %, **
2. **運算優先順序**：括號 > 次方 > 乘除 > 加減
3. **數學模組**：import math，提供豐富的數學函數
4. **複合運算子**：+=, -=, *=, /=, **=
5. **型別轉換**：int(), float(), str()

## 作業
1. 建立一個「數學遊戲」程式：
   - 隨機產生兩個數字
   - 讓使用者選擇運算（加減乘除）
   - 計算正確答案並檢查使用者的回答
   - 記錄分數

2. 設計一個「科學計算機」：
   - 支援基本四則運算
   - 支援開根號、次方、對數
   - 支援三角函數計算
   - 能夠處理複雜的數學運算式

3. 製作一個「投資報酬率計算器」：
   - 計算複利成長
   - 計算投資回本時間
   - 比較不同投資方案

## 下一步預告
明天我們將學習條件判斷（if語句），這是程式設計中的重要概念，讓程式能夠根據不同的情況做出不同的決定，就像人類的思考過程一樣！