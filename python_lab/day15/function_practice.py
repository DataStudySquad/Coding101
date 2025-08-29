"""
Day 15: 函數基礎練習
這個檔案包含各種函數練習題，幫助熟悉函數的定義和使用
"""

# ============== 基礎函數練習 ==============

def greet():
    """最簡單的函數：不接受參數，不回傳值"""
    print("Hello, Python!")

def greet_person(name):
    """接受一個參數的函數"""
    print(f"Hello, {name}!")

def add_two_numbers(a, b):
    """接受兩個參數，回傳計算結果"""
    result = a + b
    return result

def get_full_name(first_name, last_name):
    """組合名字函數"""
    full_name = f"{first_name} {last_name}"
    return full_name

# ============== 數學運算函數 ==============

def calculate_rectangle_area(length, width):
    """計算長方形面積"""
    area = length * width
    return area

def calculate_rectangle_perimeter(length, width):
    """計算長方形周長"""
    perimeter = 2 * (length + width)
    return perimeter

def calculate_circle_area(radius):
    """計算圓形面積"""
    pi = 3.14159
    area = pi * radius * radius
    return area

def calculate_circle_circumference(radius):
    """計算圓形周長"""
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

# ============== 條件判斷函數 ==============

def is_even(number):
    """判斷是否為偶數"""
    return number % 2 == 0

def is_positive(number):
    """判斷是否為正數"""
    return number > 0

def get_grade_letter(score):
    """根據分數返回等第"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def classify_age(age):
    """年齡分類"""
    if age < 13:
        return "兒童"
    elif age < 20:
        return "青少年"
    elif age < 65:
        return "成年人"
    else:
        return "長者"

# ============== 字串處理函數 ==============

def count_words(text):
    """計算字串中的單字數量"""
    words = text.split()
    return len(words)

def reverse_string(text):
    """反轉字串"""
    return text[::-1]

def capitalize_words(text):
    """將每個單字的首字母大寫"""
    return text.title()

def remove_spaces(text):
    """移除所有空格"""
    return text.replace(" ", "")

# ============== 清單處理函數 ==============

def find_maximum(numbers):
    """找出清單中的最大值"""
    if not numbers:  # 空清單檢查
        return None
    return max(numbers)

def find_minimum(numbers):
    """找出清單中的最小值"""
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    """計算平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def count_positive_numbers(numbers):
    """計算正數的數量"""
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

# ============== 進階函數練習 ==============

def calculate_bmi(weight, height):
    """計算BMI值"""
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def classify_bmi(bmi):
    """BMI分類"""
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "正常範圍"
    elif bmi < 27:
        return "過重"
    else:
        return "肥胖"

def seconds_to_time(seconds):
    """將秒數轉換為時:分:秒格式"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def calculate_compound_interest(principal, rate, time):
    """計算複利"""
    amount = principal * (1 + rate) ** time
    return round(amount, 2)

# ============== 實用工具函數 ==============

def format_currency(amount):
    """格式化貨幣顯示"""
    return f"NT$ {amount:,.2f}"

def generate_email(first_name, last_name, domain="example.com"):
    """產生電子郵件地址"""
    username = f"{first_name.lower()}.{last_name.lower()}"
    return f"{username}@{domain}"

def validate_phone(phone):
    """簡單的電話號碼驗證"""
    # 移除所有非數字字符
    digits = ''.join(filter(str.isdigit, phone))
    # 檢查是否為10位數
    return len(digits) == 10

def create_password_hint(password):
    """創建密碼提示（只顯示第一個和最後一個字符）"""
    if len(password) < 2:
        return "*"
    return f"{password[0]}{'*' * (len(password) - 2)}{password[-1]}"

# ============== 測試函數功能 ==============

def test_basic_functions():
    """測試基礎函數"""
    print("=== 基礎函數測試 ===")
    
    # 測試打招呼函數
    greet()
    greet_person("小明")
    
    # 測試數學函數
    print(f"5 + 3 = {add_two_numbers(5, 3)}")
    print(f"全名：{get_full_name('張', '小明')}")
    
    print()

def test_math_functions():
    """測試數學函數"""
    print("=== 數學函數測試 ===")
    
    # 測試幾何計算
    print(f"長方形面積 (5x3): {calculate_rectangle_area(5, 3)}")
    print(f"長方形周長 (5x3): {calculate_rectangle_perimeter(5, 3)}")
    print(f"圓形面積 (半徑5): {calculate_circle_area(5):.2f}")
    print(f"圓形周長 (半徑5): {calculate_circle_circumference(5):.2f}")
    
    print()

def test_condition_functions():
    """測試條件判斷函數"""
    print("=== 條件判斷函數測試 ===")
    
    # 測試數字判斷
    print(f"6是偶數：{is_even(6)}")
    print(f"7是偶數：{is_even(7)}")
    print(f"-5是正數：{is_positive(-5)}")
    print(f"10是正數：{is_positive(10)}")
    
    # 測試等第判斷
    print(f"85分等第：{get_grade_letter(85)}")
    print(f"65分等第：{get_grade_letter(65)}")
    
    # 測試年齡分類
    print(f"15歲分類：{classify_age(15)}")
    print(f"25歲分類：{classify_age(25)}")
    
    print()

def test_string_functions():
    """測試字串函數"""
    print("=== 字串函數測試 ===")
    
    text = "hello python world"
    print(f"原文：{text}")
    print(f"單字數：{count_words(text)}")
    print(f"反轉：{reverse_string(text)}")
    print(f"首字母大寫：{capitalize_words(text)}")
    print(f"移除空格：{remove_spaces(text)}")
    
    print()

def test_list_functions():
    """測試清單函數"""
    print("=== 清單函數測試 ===")
    
    numbers = [10, -5, 8, 3, -2, 15]
    print(f"數字清單：{numbers}")
    print(f"最大值：{find_maximum(numbers)}")
    print(f"最小值：{find_minimum(numbers)}")
    print(f"平均值：{calculate_average(numbers):.2f}")
    print(f"正數數量：{count_positive_numbers(numbers)}")
    
    print()

def test_advanced_functions():
    """測試進階函數"""
    print("=== 進階函數測試 ===")
    
    # BMI計算
    weight = 70  # 公斤
    height = 1.75  # 公尺
    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)
    print(f"BMI計算：體重{weight}kg, 身高{height}m")
    print(f"BMI值：{bmi}, 分類：{classification}")
    
    # 時間轉換
    print(f"3661秒 = {seconds_to_time(3661)}")
    
    # 複利計算
    principal = 10000  # 本金
    rate = 0.05  # 年利率5%
    time = 3  # 3年
    amount = calculate_compound_interest(principal, rate, time)
    print(f"複利計算：本金{principal}, 年利率{rate*100}%, {time}年後為 {amount}")
    
    print()

def test_utility_functions():
    """測試實用工具函數"""
    print("=== 實用工具函數測試 ===")
    
    # 貨幣格式化
    print(f"格式化金額：{format_currency(123456.789)}")
    
    # 電子郵件生成
    email = generate_email("小明", "張")
    print(f"生成Email：{email}")
    
    # 電話號碼驗證
    phone1 = "0912-345-678"
    phone2 = "123456"
    print(f"{phone1} 驗證結果：{validate_phone(phone1)}")
    print(f"{phone2} 驗證結果：{validate_phone(phone2)}")
    
    # 密碼提示
    password = "mypassword123"
    hint = create_password_hint(password)
    print(f"密碼提示：{hint}")
    
    print()

def interactive_function_demo():
    """互動式函數示範"""
    print("=== 互動式函數示範 ===")
    print("讓我們來試試一些實用的函數！")
    
    while True:
        print("\n請選擇要測試的功能：")
        print("1. BMI計算")
        print("2. 溫度轉換")
        print("3. 字串處理")
        print("4. 數學計算")
        print("0. 返回")
        
        choice = input("請選擇 (0-4): ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            demo_bmi_calculator()
        elif choice == "2":
            demo_temperature_converter()
        elif choice == "3":
            demo_string_processor()
        elif choice == "4":
            demo_math_calculator()
        else:
            print("無效選擇！")

def demo_bmi_calculator():
    """示範BMI計算"""
    print("\n--- BMI計算器 ---")
    try:
        weight = float(input("請輸入體重（公斤）: "))
        height = float(input("請輸入身高（公尺）: "))
        
        bmi = calculate_bmi(weight, height)
        classification = classify_bmi(bmi)
        
        print(f"你的BMI值是：{bmi}")
        print(f"分類：{classification}")
        
    except ValueError:
        print("請輸入有效的數字！")

def demo_temperature_converter():
    """示範溫度轉換"""
    print("\n--- 簡易溫度轉換 ---")
    try:
        celsius = float(input("請輸入攝氏溫度: "))
        fahrenheit = celsius * 9/5 + 32
        kelvin = celsius + 273.15
        
        print(f"{celsius}°C = {fahrenheit:.1f}°F = {kelvin:.1f}K")
        
    except ValueError:
        print("請輸入有效的數字！")

def demo_string_processor():
    """示範字串處理"""
    print("\n--- 字串處理器 ---")
    text = input("請輸入一段文字: ")
    
    print(f"原文：{text}")
    print(f"字數：{count_words(text)}")
    print(f"反轉：{reverse_string(text)}")
    print(f"首字母大寫：{capitalize_words(text)}")
    print(f"移除空格：{remove_spaces(text)}")

def demo_math_calculator():
    """示範數學計算"""
    print("\n--- 數學計算器 ---")
    print("計算長方形的面積和周長")
    
    try:
        length = float(input("請輸入長度: "))
        width = float(input("請輸入寬度: "))
        
        area = calculate_rectangle_area(length, width)
        perimeter = calculate_rectangle_perimeter(length, width)
        
        print(f"面積：{area}")
        print(f"周長：{perimeter}")
        
    except ValueError:
        print("請輸入有效的數字！")

def main():
    """主程式"""
    print("🎉 歡迎來到函數練習！")
    print("這個程式展示了各種函數的使用方式")
    
    while True:
        print("\n" + "="*40)
        print("請選擇測試類型：")
        print("1. 基礎函數測試")
        print("2. 數學函數測試")
        print("3. 條件判斷函數測試")
        print("4. 字串函數測試")
        print("5. 清單函數測試")
        print("6. 進階函數測試")
        print("7. 實用工具函數測試")
        print("8. 互動式示範")
        print("9. 執行所有測試")
        print("0. 離開")
        print("="*40)
        
        choice = input("請選擇 (0-9): ").strip()
        
        if choice == "0":
            print("感謝使用函數練習程式！")
            break
        elif choice == "1":
            test_basic_functions()
        elif choice == "2":
            test_math_functions()
        elif choice == "3":
            test_condition_functions()
        elif choice == "4":
            test_string_functions()
        elif choice == "5":
            test_list_functions()
        elif choice == "6":
            test_advanced_functions()
        elif choice == "7":
            test_utility_functions()
        elif choice == "8":
            interactive_function_demo()
        elif choice == "9":
            print("執行所有測試...")
            test_basic_functions()
            test_math_functions()
            test_condition_functions()
            test_string_functions()
            test_list_functions()
            test_advanced_functions()
            test_utility_functions()
            print("所有測試完成！")
        else:
            print("無效選擇！")
        
        if choice != "0":
            input("\n按Enter繼續...")

if __name__ == "__main__":
    main()