#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 5: 數學運算範例程式
展示Python中各種數學運算的使用方法
"""

import math
import random

def basic_math_demo():
    """基本數學運算示範"""
    print("=== 基本數學運算示範 ===")
    
    a = 15
    b = 4
    
    print(f"a = {a}, b = {b}")
    print(f"加法：{a} + {b} = {a + b}")
    print(f"減法：{a} - {b} = {a - b}")
    print(f"乘法：{a} × {b} = {a * b}")
    print(f"除法：{a} ÷ {b} = {a / b:.2f}")
    print(f"整數除法：{a} // {b} = {a // b}")
    print(f"取餘數：{a} % {b} = {a % b}")
    print(f"次方：{a} ^ {b} = {a ** b}")

def math_module_demo():
    """數學模組功能示範"""
    print("\n=== 數學模組功能示範 ===")
    
    number = 25
    
    print(f"數字：{number}")
    print(f"平方根：√{number} = {math.sqrt(number)}")
    print(f"立方根：∛{number} = {number ** (1/3):.2f}")
    print(f"絕對值：|{-number}| = {abs(-number)}")
    
    # 取整函數
    decimal = 3.7
    print(f"\n小數：{decimal}")
    print(f"向上取整：⌈{decimal}⌉ = {math.ceil(decimal)}")
    print(f"向下取整：⌊{decimal}⌋ = {math.floor(decimal)}")
    print(f"四捨五入：round({decimal}) = {round(decimal)}")
    
    # 常數
    print(f"\n數學常數：")
    print(f"圓周率 π = {math.pi:.6f}")
    print(f"自然對數底 e = {math.e:.6f}")

def trigonometry_demo():
    """三角函數示範"""
    print("\n=== 三角函數示範 ===")
    
    angles = [0, 30, 45, 60, 90]
    
    print("角度\t弧度\t\tsin\t\tcos\t\ttan")
    print("-" * 60)
    
    for angle in angles:
        radian = math.radians(angle)
        sin_val = math.sin(radian)
        cos_val = math.cos(radian)
        
        if angle == 90:
            tan_val = "∞"
        else:
            tan_val = f"{math.tan(radian):.4f}"
        
        print(f"{angle}°\t{radian:.4f}\t\t{sin_val:.4f}\t\t{cos_val:.4f}\t\t{tan_val}")

def calculator():
    """簡易計算機"""
    print("\n=== 簡易計算機 ===")
    
    while True:
        try:
            num1 = float(input("請輸入第一個數字："))
            operator = input("請輸入運算子 (+, -, *, /, **, sqrt, quit)：")
            
            if operator.lower() == 'quit':
                break
            
            if operator == 'sqrt':
                if num1 >= 0:
                    result = math.sqrt(num1)
                    print(f"√{num1} = {result}")
                else:
                    print("錯誤：負數不能開平方根")
                continue
            
            num2 = float(input("請輸入第二個數字："))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("錯誤：除數不能為零")
                    continue
            elif operator == '**':
                result = num1 ** num2
            else:
                print("錯誤：不支援的運算子")
                continue
            
            print(f"{num1} {operator} {num2} = {result}")
            
        except ValueError:
            print("錯誤：請輸入有效的數字")
        except Exception as e:
            print(f"發生錯誤：{e}")

def geometry_calculator():
    """幾何計算器"""
    print("\n=== 幾何計算器 ===")
    
    shapes = {
        "1": "圓形",
        "2": "正方形", 
        "3": "長方形",
        "4": "三角形"
    }
    
    print("請選擇形狀：")
    for key, value in shapes.items():
        print(f"{key}. {value}")
    
    choice = input("輸入選項 (1-4)：")
    
    if choice == "1":  # 圓形
        radius = float(input("請輸入半徑："))
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        print(f"圓形面積：{area:.2f}")
        print(f"圓形周長：{circumference:.2f}")
        
    elif choice == "2":  # 正方形
        side = float(input("請輸入邊長："))
        area = side ** 2
        perimeter = 4 * side
        print(f"正方形面積：{area:.2f}")
        print(f"正方形周長：{perimeter:.2f}")
        
    elif choice == "3":  # 長方形
        length = float(input("請輸入長："))
        width = float(input("請輸入寬："))
        area = length * width
        perimeter = 2 * (length + width)
        print(f"長方形面積：{area:.2f}")
        print(f"長方形周長：{perimeter:.2f}")
        
    elif choice == "4":  # 三角形
        base = float(input("請輸入底邊："))
        height = float(input("請輸入高："))
        area = 0.5 * base * height
        print(f"三角形面積：{area:.2f}")
        
    else:
        print("無效的選項")

def number_guessing_game():
    """數字猜測遊戲"""
    print("\n=== 數字猜測遊戲 ===")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"我想了一個1到100之間的數字，你有{max_attempts}次機會猜中它！")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"第{attempts + 1}次猜測，請輸入數字："))
            attempts += 1
            
            if guess == secret_number:
                print(f"恭喜！你在第{attempts}次猜中了數字{secret_number}！")
                break
            elif guess < secret_number:
                print("太小了！")
            else:
                print("太大了！")
            
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"還有{remaining}次機會")
            
        except ValueError:
            print("請輸入有效的數字！")
    
    if attempts >= max_attempts and guess != secret_number:
        print(f"遊戲結束！正確答案是{secret_number}")

def compound_interest_calculator():
    """複利計算器"""
    print("\n=== 複利計算器 ===")
    
    try:
        principal = float(input("請輸入本金："))
        rate = float(input("請輸入年利率（%）：")) / 100
        time = int(input("請輸入投資年數："))
        compounds = int(input("請輸入每年複利次數（例如：1=年複利，12=月複利）："))
        
        # 複利公式：A = P(1 + r/n)^(nt)
        amount = principal * (1 + rate/compounds) ** (compounds * time)
        interest = amount - principal
        
        print(f"\n投資結果：")
        print(f"本金：${principal:,.2f}")
        print(f"年利率：{rate*100:.2f}%")
        print(f"投資期間：{time}年")
        print(f"複利頻率：每年{compounds}次")
        print(f"最終金額：${amount:,.2f}")
        print(f"獲得利息：${interest:,.2f}")
        print(f"總報酬率：{(interest/principal)*100:.2f}%")
        
    except ValueError:
        print("請輸入有效的數字！")

def main():
    """主程式"""
    print("Day 5: 數學運算範例程式")
    print("=" * 40)
    
    while True:
        print("\n請選擇功能：")
        print("1. 基本數學運算示範")
        print("2. 數學模組功能示範")
        print("3. 三角函數示範")
        print("4. 簡易計算機")
        print("5. 幾何計算器")
        print("6. 數字猜測遊戲")
        print("7. 複利計算器")
        print("0. 結束程式")
        
        choice = input("\n請輸入選項 (0-7)：")
        
        if choice == "1":
            basic_math_demo()
        elif choice == "2":
            math_module_demo()
        elif choice == "3":
            trigonometry_demo()
        elif choice == "4":
            calculator()
        elif choice == "5":
            geometry_calculator()
        elif choice == "6":
            number_guessing_game()
        elif choice == "7":
            compound_interest_calculator()
        elif choice == "0":
            print("感謝使用，再見！")
            break
        else:
            print("無效的選項，請重新選擇！")

if __name__ == "__main__":
    main()