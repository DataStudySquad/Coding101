"""
Day 17: 內建函數練習
練習各種Python內建函數的使用方法
"""

import random
import string

# =============== 基本內建函數練習 ===============

def basic_functions_demo():
    """基本內建函數示範"""
    print("🔧 基本內建函數示範")
    print("=" * 40)
    
    # len() - 長度函數
    print("📏 len() 函數:")
    text = "Python程式設計"
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    student = {"name": "小明", "age": 18, "grade": "A"}
    
    print(f"  字串長度: len('{text}') = {len(text)}")
    print(f"  清單長度: len({numbers}) = {len(numbers)}")
    print(f"  字典長度: len({student}) = {len(student)}")
    
    # max() 和 min() - 最大值和最小值
    print(f"\n📊 max() 和 min() 函數:")
    scores = [85, 92, 78, 96, 88, 67, 94]
    print(f"  成績: {scores}")
    print(f"  最高分: max({scores}) = {max(scores)}")
    print(f"  最低分: min({scores}) = {min(scores)}")
    
    # 字串比較
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"  水果: {fruits}")
    print(f"  字母順序最後: max({fruits}) = {max(fruits)}")
    print(f"  字母順序最前: min({fruits}) = {min(fruits)}")
    
    # sum() - 總和函數
    print(f"\n🧮 sum() 函數:")
    print(f"  總分: sum({scores}) = {sum(scores)}")
    print(f"  平均分: sum({scores}) / len({scores}) = {sum(scores) / len(scores):.1f}")
    
    # 加上起始值
    bonus_total = sum(scores, 100)
    print(f"  加上獎金100分: sum({scores}, 100) = {bonus_total}")
    
    # abs() - 絕對值函數
    print(f"\n📐 abs() 函數:")
    temperatures = [-5, 3.2, -18.7, 0, 25.6]
    print(f"  溫度: {temperatures}")
    abs_temps = [abs(temp) for temp in temperatures]
    print(f"  絕對值: {abs_temps}")
    
    # round() - 四捨五入函數
    print(f"\n🔢 round() 函數:")
    pi = 3.141592653589793
    print(f"  π = {pi}")
    print(f"  round(π) = {round(pi)}")
    print(f"  round(π, 2) = {round(pi, 2)}")
    print(f"  round(π, 4) = {round(pi, 4)}")

def sequence_functions_demo():
    """序列函數示範"""
    print("\n🔗 序列函數示範")
    print("=" * 40)
    
    # sorted() - 排序函數
    print("📈 sorted() 函數:")
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"  原始: {numbers}")
    print(f"  升序: {sorted(numbers)}")
    print(f"  降序: {sorted(numbers, reverse=True)}")
    
    # 字串排序
    words = ["python", "java", "javascript", "go", "rust"]
    print(f"  單字: {words}")
    print(f"  字母排序: {sorted(words)}")
    print(f"  長度排序: {sorted(words, key=len)}")
    print(f"  長度排序(降序): {sorted(words, key=len, reverse=True)}")
    
    # reversed() - 反轉函數
    print(f"\n🔄 reversed() 函數:")
    original = [1, 2, 3, 4, 5]
    reversed_list = list(reversed(original))
    print(f"  原始: {original}")
    print(f"  反轉: {reversed_list}")
    
    # 字串反轉
    text = "Hello World"
    reversed_text = ''.join(reversed(text))
    print(f"  字串: '{text}' → '{reversed_text}'")
    
    # enumerate() - 枚舉函數
    print(f"\n📋 enumerate() 函數:")
    fruits = ["蘋果", "香蕉", "橘子", "葡萄"]
    print("  水果清單:")
    for index, fruit in enumerate(fruits):
        print(f"    {index}: {fruit}")
    
    print("  從1開始編號:")
    for i, fruit in enumerate(fruits, start=1):
        print(f"    {i}. {fruit}")
    
    # zip() - 打包函數
    print(f"\n🔗 zip() 函數:")
    names = ["小明", "小美", "小華"]
    ages = [18, 19, 17]
    grades = ["A", "B+", "A-"]
    
    print("  學生資料配對:")
    for name, age, grade in zip(names, ages, grades):
        print(f"    {name}: {age}歲, 成績{grade}")
    
    # 建立字典
    student_dict = dict(zip(names, ages))
    print(f"  建立字典: {student_dict}")

def higher_order_functions_demo():
    """高階函數示範"""
    print("\n⚡ 高階函數示範")
    print("=" * 40)
    
    # map() - 映射函數
    print("🔄 map() 函數:")
    numbers = [1, 2, 3, 4, 5]
    
    # 計算平方
    squares = list(map(lambda x: x**2, numbers))
    print(f"  原數字: {numbers}")
    print(f"  平方: {squares}")
    
    # 字串處理
    words = ["hello", "world", "python"]
    upper_words = list(map(str.upper, words))
    print(f"  原字串: {words}")
    print(f"  大寫: {upper_words}")
    
    # 溫度轉換
    celsius = [0, 20, 30, 37, 100]
    fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
    print(f"  攝氏: {celsius}")
    print(f"  華氏: {fahrenheit}")
    
    # filter() - 過濾函數
    print(f"\n🔍 filter() 函數:")
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 篩選偶數
    evens = list(filter(lambda x: x % 2 == 0, test_numbers))
    print(f"  原數字: {test_numbers}")
    print(f"  偶數: {evens}")
    
    # 篩選長單字
    test_words = ["a", "hello", "hi", "python", "programming", "go"]
    long_words = list(filter(lambda w: len(w) > 3, test_words))
    print(f"  原單字: {test_words}")
    print(f"  長單字(>3字元): {long_words}")
    
    # 篩選及格分數
    all_scores = [45, 78, 92, 56, 88, 34, 95, 67]
    passed_scores = list(filter(lambda s: s >= 60, all_scores))
    print(f"  所有分數: {all_scores}")
    print(f"  及格分數: {passed_scores}")
    
    # any() 和 all() - 邏輯判斷函數
    print(f"\n✅ any() 和 all() 函數:")
    test_scores = [85, 92, 78, 96, 88]
    
    print(f"  成績: {test_scores}")
    print(f"  有人達到90分: {any(score >= 90 for score in test_scores)}")
    print(f"  全部都及格(>=60): {all(score >= 60 for score in test_scores)}")
    print(f"  有人不及格: {any(score < 60 for score in test_scores)}")
    print(f"  全部都優秀(>=95): {all(score >= 95 for score in test_scores)}")

def practical_applications():
    """實際應用範例"""
    print("\n💼 實際應用範例")
    print("=" * 40)
    
    # 範例1: 購物車計算
    print("🛒 購物車計算:")
    shopping_cart = [
        {"item": "蘋果", "price": 50, "quantity": 3},
        {"item": "香蕉", "price": 30, "quantity": 5},
        {"item": "橘子", "price": 40, "quantity": 2},
        {"item": "牛奶", "price": 65, "quantity": 1}
    ]
    
    # 計算總價
    total_cost = sum(item["price"] * item["quantity"] for item in shopping_cart)
    print(f"  購物車總價: NT${total_cost}")
    
    # 找出最貴的商品
    most_expensive = max(shopping_cart, key=lambda x: x["price"])
    print(f"  最貴商品: {most_expensive['item']} - NT${most_expensive['price']}")
    
    # 計算平均商品價格
    avg_price = sum(item["price"] for item in shopping_cart) / len(shopping_cart)
    print(f"  平均商品價格: NT${avg_price:.1f}")
    
    # 範例2: 成績分析
    print(f"\n📊 成績分析:")
    class_scores = {
        "數學": [85, 92, 78, 96, 88, 67, 94, 82, 90, 76],
        "英文": [88, 85, 90, 82, 95, 70, 87, 89, 92, 78],
        "物理": [75, 88, 82, 90, 79, 65, 91, 77, 85, 80]
    }
    
    print("  各科統計:")
    for subject, scores in class_scores.items():
        avg = sum(scores) / len(scores)
        highest = max(scores)
        lowest = min(scores)
        print(f"    {subject}: 平均{avg:.1f}, 最高{highest}, 最低{lowest}")
    
    # 找出每個學生的總分和排名
    student_totals = []
    for i in range(len(class_scores["數學"])):
        total = sum(scores[i] for scores in class_scores.values())
        student_totals.append(total)
    
    print(f"\n  學生總分: {student_totals}")
    ranked_totals = sorted(student_totals, reverse=True)
    print(f"  總分排名: {ranked_totals}")
    
    # 範例3: 資料清理
    print(f"\n🧹 資料清理:")
    messy_data = ["123", "456.7", "", "abc", "789", None, "0", "NaN", "100.5", "def"]
    
    print(f"  原始資料: {messy_data}")
    
    # 過濾出有效的數字
    def is_valid_number(value):
        if value is None or value == "":
            return False
        try:
            float(str(value))
            return True
        except (ValueError, TypeError):
            return False
    
    clean_numbers = list(filter(is_valid_number, messy_data))
    numeric_values = list(map(float, clean_numbers))
    
    print(f"  清理後數字: {numeric_values}")
    print(f"  數字統計: 總數{len(numeric_values)}, 總和{sum(numeric_values)}, 平均{sum(numeric_values)/len(numeric_values):.2f}")

def string_operations_with_builtins():
    """字串操作與內建函數"""
    print("\n📝 字串操作與內建函數")
    print("=" * 40)
    
    # 字串分析
    text = "Python is a powerful programming language. Python is easy to learn."
    words = text.split()
    
    print(f"文本: {text}")
    print(f"單字數量: {len(words)}")
    print(f"字符數量: {len(text)}")
    
    # 使用 map 處理單字
    word_lengths = list(map(len, words))
    print(f"單字長度: {word_lengths}")
    print(f"最長單字長度: {max(word_lengths)}")
    print(f"最短單字長度: {min(word_lengths)}")
    
    # 使用 filter 篩選長單字
    long_words = list(filter(lambda w: len(w) > 5, words))
    print(f"長單字(>5字元): {long_words}")
    
    # 字母頻率統計
    letters = [char.lower() for char in text if char.isalpha()]
    print(f"字母總數: {len(letters)}")
    
    # 使用 any 和 all 檢查條件
    print(f"包含大寫字母: {any(c.isupper() for c in text)}")
    print(f"全部是字母: {all(c.isalpha() for c in text.replace(' ', '').replace('.', ''))}")

def mathematical_operations():
    """數學運算應用"""
    print("\n🧮 數學運算應用")
    print("=" * 40)
    
    # 數列運算
    numbers = list(range(1, 11))  # 1到10的數字
    print(f"數列: {numbers}")
    
    # 各種統計
    print(f"總和: {sum(numbers)}")
    print(f"平均: {sum(numbers) / len(numbers)}")
    print(f"最大值: {max(numbers)}")
    print(f"最小值: {min(numbers)}")
    
    # 使用 map 進行數學運算
    squares = list(map(lambda x: x**2, numbers))
    cubes = list(map(lambda x: x**3, numbers))
    
    print(f"平方: {squares}")
    print(f"立方: {cubes}")
    
    # 篩選特定條件的數字
    even_squares = list(filter(lambda x: x % 2 == 0, squares))
    print(f"偶數平方: {even_squares}")
    
    # 複雜計算組合
    # 計算平方和
    sum_of_squares = sum(map(lambda x: x**2, numbers))
    print(f"平方和: {sum_of_squares}")
    
    # 計算平方根（需要導入math模組，這裡用簡化版）
    square_roots = list(map(lambda x: x**0.5, numbers))
    print(f"平方根: {[round(x, 2) for x in square_roots]}")

def interactive_builtin_functions():
    """互動式內建函數練習"""
    print("\n🎮 互動式內建函數練習")
    print("歡迎來到內建函數練習場！")
    
    while True:
        print("\n" + "=" * 50)
        print("選擇練習項目：")
        print("1. 📏 基本函數 (len, max, min, sum)")
        print("2. 🔗 序列函數 (sorted, reversed, enumerate, zip)")
        print("3. ⚡ 高階函數 (map, filter, any, all)")
        print("4. 💼 實際應用範例")
        print("5. 📝 字串操作")
        print("6. 🧮 數學運算")
        print("7. 🎯 自定義練習")
        print("8. 🧪 綜合測試")
        print("0. 🚪 退出")
        print("=" * 50)
        
        choice = input("請選擇 (0-8): ").strip()
        
        if choice == "0":
            print("感謝使用內建函數練習！")
            break
        elif choice == "1":
            basic_functions_demo()
        elif choice == "2":
            sequence_functions_demo()
        elif choice == "3":
            higher_order_functions_demo()
        elif choice == "4":
            practical_applications()
        elif choice == "5":
            string_operations_with_builtins()
        elif choice == "6":
            mathematical_operations()
        elif choice == "7":
            custom_practice()
        elif choice == "8":
            comprehensive_test()
        else:
            print("❌ 無效選擇")
        
        if choice != "0":
            input("\n按 Enter 繼續...")

def custom_practice():
    """自定義練習"""
    print("\n🎯 自定義練習")
    print("-" * 30)
    
    print("輸入一些數字來練習內建函數（空格分隔）:")
    try:
        numbers_input = input("數字: ").strip()
        if not numbers_input:
            print("❌ 沒有輸入任何數字")
            return
        
        numbers = list(map(float, numbers_input.split()))
        print(f"✅ 輸入的數字: {numbers}")
        
        # 應用各種內建函數
        print(f"\n📊 統計分析:")
        print(f"  數量: len() = {len(numbers)}")
        print(f"  總和: sum() = {sum(numbers)}")
        print(f"  平均: sum()/len() = {sum(numbers)/len(numbers):.2f}")
        print(f"  最大值: max() = {max(numbers)}")
        print(f"  最小值: min() = {min(numbers)}")
        print(f"  排序: sorted() = {sorted(numbers)}")
        
        # 進階處理
        evens = list(filter(lambda x: x % 2 == 0, numbers))
        squares = list(map(lambda x: x**2, numbers))
        
        print(f"\n🔍 進階分析:")
        print(f"  偶數: filter() = {evens}")
        print(f"  平方: map() = {squares}")
        print(f"  有負數: any() = {any(x < 0 for x in numbers)}")
        print(f"  全為正數: all() = {all(x > 0 for x in numbers)}")
        
    except ValueError:
        print("❌ 請輸入有效的數字")

def comprehensive_test():
    """綜合測試"""
    print("\n🧪 內建函數綜合測試")
    print("-" * 40)
    
    # 生成隨機測試資料
    test_data = [random.randint(1, 100) for _ in range(10)]
    print(f"測試資料: {test_data}")
    
    print(f"\n📊 請計算以下問題的答案:")
    
    # 問題1
    correct_len = len(test_data)
    user_len = input(f"1. 資料長度 len(): ")
    try:
        if int(user_len) == correct_len:
            print("   ✅ 正確！")
        else:
            print(f"   ❌ 錯誤，正確答案是 {correct_len}")
    except ValueError:
        print(f"   ❌ 請輸入數字，正確答案是 {correct_len}")
    
    # 問題2
    correct_max = max(test_data)
    user_max = input(f"2. 最大值 max(): ")
    try:
        if int(user_max) == correct_max:
            print("   ✅ 正確！")
        else:
            print(f"   ❌ 錯誤，正確答案是 {correct_max}")
    except ValueError:
        print(f"   ❌ 請輸入數字，正確答案是 {correct_max}")
    
    # 問題3
    correct_sum = sum(test_data)
    user_sum = input(f"3. 總和 sum(): ")
    try:
        if int(user_sum) == correct_sum:
            print("   ✅ 正確！")
        else:
            print(f"   ❌ 錯誤，正確答案是 {correct_sum}")
    except ValueError:
        print(f"   ❌ 請輸入數字，正確答案是 {correct_sum}")
    
    # 展示正確答案
    print(f"\n📋 完整解答:")
    print(f"  長度: {len(test_data)}")
    print(f"  最大值: {max(test_data)}")
    print(f"  最小值: {min(test_data)}")
    print(f"  總和: {sum(test_data)}")
    print(f"  平均: {sum(test_data)/len(test_data):.2f}")
    print(f"  排序: {sorted(test_data)}")
    print(f"  反轉: {sorted(test_data, reverse=True)}")
    
    # 進階分析
    evens = list(filter(lambda x: x % 2 == 0, test_data))
    odds = list(filter(lambda x: x % 2 == 1, test_data))
    
    print(f"\n🔍 進階分析:")
    print(f"  偶數: {evens} (共{len(evens)}個)")
    print(f"  奇數: {odds} (共{len(odds)}個)")
    print(f"  有大於50的數: {any(x > 50 for x in test_data)}")
    print(f"  全部都大於0: {all(x > 0 for x in test_data)}")

if __name__ == "__main__":
    print("🐍 Python 內建函數練習場")
    print("=" * 50)
    print("歡迎來到內建函數的世界！")
    print("這裡有豐富的練習等著您探索")
    
    interactive_builtin_functions()