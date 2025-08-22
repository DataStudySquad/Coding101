#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 4: 字串處理範例程式
本程式展示各種字串操作的實際應用
"""

# 基本字串操作示範
def basic_string_operations():
    """展示基本字串操作"""
    print("=== 基本字串操作 ===")
    
    # 建立字串
    greeting = "你好"
    name = "Python學習者"
    
    # 字串連接
    welcome_message = greeting + "，" + name + "！"
    print(f"歡迎訊息：{welcome_message}")
    
    # 字串重複
    separator = "-" * 30
    print(separator)
    
    # 字串長度
    print(f"歡迎訊息的字元數：{len(welcome_message)}")
    

def string_methods_demo():
    """展示字串方法"""
    print("\n=== 字串方法示範 ===")
    
    text = "  Hello Python World  "
    print(f"原始文字：'{text}'")
    print(f"去除空白：'{text.strip()}'")
    print(f"轉大寫：'{text.upper()}'")
    print(f"轉小寫：'{text.lower()}'")
    print(f"標題格式：'{text.title()}'")
    
    # 字串替換
    chinese_text = "我喜歡學習程式設計"
    new_text = chinese_text.replace("程式設計", "Python")
    print(f"替換後：{new_text}")
    
    # 字串分割與結合
    fruits = "蘋果,香蕉,橘子,葡萄"
    fruit_list = fruits.split(",")
    print(f"分割後：{fruit_list}")
    
    joined = " | ".join(fruit_list)
    print(f"重新結合：{joined}")


def string_formatting_demo():
    """展示字串格式化"""
    print("\n=== 字串格式化示範 ===")
    
    name = "小明"
    age = 20
    height = 175.5
    
    # f-string 格式化（推薦）
    info1 = f"姓名：{name}，年齡：{age}歲，身高：{height}公分"
    print(f"f-string：{info1}")
    
    # .format() 格式化
    info2 = "姓名：{}，年齡：{}歲，身高：{:.1f}公分".format(name, age, height)
    print(f".format()：{info2}")
    
    # 進階格式化
    price = 1234.5678
    print(f"商品價格：${price:,.2f}")
    print(f"百分比：{0.1234:.2%}")


def text_analyzer():
    """文字分析器"""
    print("\n=== 文字分析器 ===")
    
    text = input("請輸入要分析的文字：")
    
    if not text.strip():
        print("您沒有輸入任何文字！")
        return
    
    print(f"\n分析結果：")
    print(f"總字元數：{len(text)}")
    print(f"去除空白後字元數：{len(text.strip())}")
    print(f"單字數（以空格分隔）：{len(text.split())}")
    print(f"大寫字母數：{sum(1 for c in text if c.isupper())}")
    print(f"小寫字母數：{sum(1 for c in text if c.islower())}")
    print(f"數字字元數：{sum(1 for c in text if c.isdigit())}")
    print(f"包含字母：{'是' if text.isalpha() else '否'}")
    print(f"包含數字：{'是' if any(c.isdigit() for c in text) else '否'}")


def password_generator():
    """簡單的密碼產生器"""
    print("\n=== 密碼產生器 ===")
    
    import random
    import string
    
    name = input("請輸入您的名字：")
    birth_year = input("請輸入您的出生年份：")
    
    # 基本密碼組合
    base_password = name[:2] + birth_year[-2:]
    
    # 添加隨機字符
    symbols = "!@#$%"
    random_symbol = random.choice(symbols)
    random_number = random.randint(10, 99)
    
    # 生成多種密碼選項
    passwords = [
        base_password + str(random_number),
        base_password.upper() + random_symbol + str(random_number),
        base_password.lower() + str(random_number) + random_symbol,
        name.title() + birth_year + random_symbol,
    ]
    
    print("\n建議密碼選項：")
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}. {pwd}")
    
    print("\n密碼安全提醒：")
    print("- 請勿使用過於簡單的個人資訊")
    print("- 定期更換密碼")
    print("- 不同網站使用不同密碼")


def text_art_generator():
    """文字藝術產生器"""
    print("\n=== 文字藝術產生器 ===")
    
    text = input("請輸入要裝飾的文字：")
    
    if not text.strip():
        print("請輸入有效的文字！")
        return
    
    # 不同的裝飾風格
    styles = {
        "1": {"char": "*", "name": "星星框"},
        "2": {"char": "=", "name": "等號框"},
        "3": {"char": "#", "name": "井號框"},
        "4": {"char": "+", "name": "加號框"},
    }
    
    print("\n選擇裝飾風格：")
    for key, style in styles.items():
        print(f"{key}. {style['name']}")
    
    choice = input("請選擇 (1-4)：")
    
    if choice in styles:
        char = styles[choice]["char"]
        width = len(text) + 4
        
        print(f"\n{char * width}")
        print(f"{char} {text} {char}")
        print(f"{char * width}")
    else:
        print("無效的選擇！")


def main():
    """主程式"""
    print("Day 4: 字串處理範例程式")
    print("=" * 40)
    
    while True:
        print("\n請選擇功能：")
        print("1. 基本字串操作示範")
        print("2. 字串方法示範")
        print("3. 字串格式化示範")
        print("4. 文字分析器")
        print("5. 密碼產生器")
        print("6. 文字藝術產生器")
        print("0. 結束程式")
        
        choice = input("\n請輸入選項 (0-6)：")
        
        if choice == "1":
            basic_string_operations()
        elif choice == "2":
            string_methods_demo()
        elif choice == "3":
            string_formatting_demo()
        elif choice == "4":
            text_analyzer()
        elif choice == "5":
            password_generator()
        elif choice == "6":
            text_art_generator()
        elif choice == "0":
            print("感謝使用，再見！")
            break
        else:
            print("無效的選項，請重新選擇！")


if __name__ == "__main__":
    main()