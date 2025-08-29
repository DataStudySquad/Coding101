#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 6: 條件判斷（if）範例程式
展示Python中條件判斷的各種使用方法
"""

def basic_if_demo():
    """基本if語句示範"""
    print("=== 基本if語句示範 ===")
    
    age = int(input("請輸入你的年齡："))
    
    if age >= 18:
        print("你已經成年了！可以投票、開車（如果有駕照）。")
    else:
        print(f"你還有{18-age}年就成年了。")
    
    print("程式執行完畢。")

def grade_classifier():
    """成績分類器"""
    print("\n=== 成績分類器 ===")
    
    score = float(input("請輸入分數（0-100）："))
    
    # 檢查分數是否有效
    if score < 0 or score > 100:
        print("錯誤：分數必須在0-100之間！")
        return
    
    if score >= 90:
        grade = "A+"
        comment = "優秀！繼續保持！"
    elif score >= 85:
        grade = "A"
        comment = "很好！"
    elif score >= 80:
        grade = "B+"
        comment = "不錯！"
    elif score >= 75:
        grade = "B"
        comment = "良好。"
    elif score >= 70:
        grade = "C+"
        comment = "還可以。"
    elif score >= 65:
        grade = "C"
        comment = "需要努力。"
    elif score >= 60:
        grade = "D"
        comment = "剛好及格。"
    else:
        grade = "F"
        comment = "不及格，需要重修。"
    
    print(f"分數：{score}")
    print(f"等第：{grade}")
    print(f"評語：{comment}")

def login_system():
    """登入系統示範"""
    print("\n=== 登入系統示範 ===")
    
    # 預設帳號密碼
    valid_users = {
        "admin": "admin123",
        "user": "user123",
        "guest": "guest123"
    }
    
    username = input("請輸入使用者名稱：")
    password = input("請輸入密碼：")
    
    if username in valid_users and valid_users[username] == password:
        print(f"登入成功！歡迎 {username}！")
        
        if username == "admin":
            print("你有管理員權限。")
        elif username == "user":
            print("你有使用者權限。")
        else:
            print("你有訪客權限。")
    else:
        print("帳號或密碼錯誤！")

def weather_advisor():
    """天氣建議系統"""
    print("\n=== 天氣建議系統 ===")
    
    temperature = float(input("請輸入今天的溫度（攝氏）："))
    weather = input("今天天氣如何？(sunny/rainy/cloudy/snowy)：").lower()
    
    print(f"\n今天溫度：{temperature}°C")
    print(f"天氣狀況：{weather}")
    print("建議：")
    
    # 根據溫度給建議
    if temperature > 30:
        print("- 很熱！多喝水，注意防曬")
    elif temperature > 25:
        print("- 溫暖舒適的天氣")
    elif temperature > 15:
        print("- 涼爽，適合戶外活動")
    elif temperature > 5:
        print("- 有點冷，記得保暖")
    else:
        print("- 很冷！穿厚一點")
    
    # 根據天氣給建議
    if weather == "sunny":
        print("- 陽光普照，適合外出")
        if temperature > 25:
            print("- 記得戴帽子和太陽眼鏡")
    elif weather == "rainy":
        print("- 記得帶雨傘！")
        print("- 路面濕滑，小心行走")
    elif weather == "cloudy":
        print("- 多雲天氣，還不錯")
    elif weather == "snowy":
        print("- 下雪天！注意保暖和防滑")
    else:
        print("- 天氣狀況不明")

def bmi_calculator():
    """BMI計算器"""
    print("\n=== BMI計算器 ===")
    
    try:
        weight = float(input("請輸入體重（公斤）："))
        height = float(input("請輸入身高（公尺，例如：1.75）："))
        
        if weight <= 0 or height <= 0:
            print("錯誤：體重和身高必須大於0！")
            return
        
        bmi = weight / (height ** 2)
        
        print(f"\n你的BMI值：{bmi:.2f}")
        
        if bmi < 18.5:
            category = "體重過輕"
            advice = "建議增加營養攝取，適度運動增重"
        elif bmi < 24:
            category = "體重正常"
            advice = "保持良好的生活習慣"
        elif bmi < 27:
            category = "體重過重"
            advice = "建議控制飲食，增加運動"
        elif bmi < 30:
            category = "輕度肥胖"
            advice = "建議諮詢營養師，制定減重計劃"
        elif bmi < 35:
            category = "中度肥胖"
            advice = "建議就醫諮詢，需要專業減重指導"
        else:
            category = "重度肥胖"
            advice = "強烈建議就醫治療"
        
        print(f"分類：{category}")
        print(f"建議：{advice}")
        
    except ValueError:
        print("錯誤：請輸入有效的數字！")

def triangle_classifier():
    """三角形分類器"""
    print("\n=== 三角形分類器 ===")
    
    try:
        a = float(input("請輸入第一邊長："))
        b = float(input("請輸入第二邊長："))
        c = float(input("請輸入第三邊長："))
        
        if a <= 0 or b <= 0 or c <= 0:
            print("錯誤：邊長必須大於0！")
            return
        
        # 檢查是否能構成三角形
        if a + b <= c or a + c <= b or b + c <= a:
            print("這三個邊長無法構成三角形！")
            print("提醒：任意兩邊之和必須大於第三邊")
            return
        
        print("這是一個有效的三角形！")
        
        # 分類三角形
        if a == b == c:
            triangle_type = "等邊三角形"
        elif a == b or b == c or a == c:
            triangle_type = "等腰三角形"
        else:
            triangle_type = "不等邊三角形"
        
        # 檢查是否為直角三角形
        sides = sorted([a, b, c])
        if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 0.0001:
            triangle_type += " (直角三角形)"
        
        print(f"類型：{triangle_type}")
        
        # 計算周長和面積
        perimeter = a + b + c
        s = perimeter / 2  # 半周長
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # 海倫公式
        
        print(f"周長：{perimeter:.2f}")
        print(f"面積：{area:.2f}")
        
    except ValueError:
        print("錯誤：請輸入有效的數字！")

def password_strength_checker():
    """密碼強度檢查器"""
    print("\n=== 密碼強度檢查器 ===")
    
    password = input("請輸入要檢查的密碼：")
    
    score = 0
    feedback = []
    
    # 檢查長度
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
    else:
        feedback.append("密碼長度至少要6個字元，建議12個以上")
    
    # 檢查小寫字母
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("應包含小寫字母")
    
    # 檢查大寫字母
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("應包含大寫字母")
    
    # 檢查數字
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("應包含數字")
    
    # 檢查特殊字元
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 1
    else:
        feedback.append("應包含特殊字元")
    
    # 檢查重複字元
    if len(set(password)) < len(password) * 0.8:
        feedback.append("避免使用太多重複字元")
    else:
        score += 1
    
    # 評估強度
    print(f"\n密碼：{'*' * len(password)}")
    print(f"分數：{score}/8")
    
    if score >= 7:
        strength = "非常強"
        color = "綠色"
    elif score >= 5:
        strength = "強"
        color = "藍色"
    elif score >= 3:
        strength = "中等"
        color = "黃色"
    elif score >= 1:
        strength = "弱"
        color = "橘色"
    else:
        strength = "非常弱"
        color = "紅色"
    
    print(f"強度：{strength} ({color})")
    
    if feedback:
        print("\n改善建議：")
        for i, suggestion in enumerate(feedback, 1):
            print(f"{i}. {suggestion}")
    else:
        print("\n這是一個很棒的密碼！")

def number_guessing_game():
    """數字猜測遊戲"""
    print("\n=== 數字猜測遊戲 ===")
    
    import random
    
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"我想了一個1到100之間的數字")
    print(f"你有{max_attempts}次機會猜中它！")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\n第{attempts + 1}次猜測，請輸入數字："))
            attempts += 1
            
            if guess == secret:
                print(f"🎉 恭喜！你猜中了！答案就是{secret}")
                print(f"你總共用了{attempts}次機會")
                
                if attempts == 1:
                    print("太厲害了！一次就猜中！")
                elif attempts <= 3:
                    print("很棒的直覺！")
                elif attempts <= 5:
                    print("不錯的表現！")
                else:
                    print("終於猜中了！")
                break
                
            elif guess < secret:
                difference = secret - guess
                if difference > 20:
                    hint = "太小了！而且差很多"
                elif difference > 10:
                    hint = "小了一些"
                else:
                    hint = "有點小，很接近了！"
                print(f"❌ {hint}")
                
            else:  # guess > secret
                difference = guess - secret
                if difference > 20:
                    hint = "太大了！而且差很多"
                elif difference > 10:
                    hint = "大了一些"
                else:
                    hint = "有點大，很接近了！"
                print(f"❌ {hint}")
            
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"還有{remaining}次機會")
        
        except ValueError:
            print("請輸入有效的數字！")
    
    if attempts >= max_attempts and guess != secret:
        print(f"\n遊戲結束！正確答案是{secret}")
        print("下次再挑戰吧！")

def main():
    """主程式"""
    print("Day 6: 條件判斷（if）範例程式")
    print("=" * 40)
    
    while True:
        print("\n請選擇功能：")
        print("1. 基本if語句示範")
        print("2. 成績分類器")
        print("3. 登入系統示範")
        print("4. 天氣建議系統")
        print("5. BMI計算器")
        print("6. 三角形分類器")
        print("7. 密碼強度檢查器")
        print("8. 數字猜測遊戲")
        print("0. 結束程式")
        
        choice = input("\n請輸入選項 (0-8)：")
        
        if choice == "1":
            basic_if_demo()
        elif choice == "2":
            grade_classifier()
        elif choice == "3":
            login_system()
        elif choice == "4":
            weather_advisor()
        elif choice == "5":
            bmi_calculator()
        elif choice == "6":
            triangle_classifier()
        elif choice == "7":
            password_strength_checker()
        elif choice == "8":
            number_guessing_game()
        elif choice == "0":
            print("感謝使用，再見！")
            break
        else:
            print("無效的選項，請重新選擇！")

if __name__ == "__main__":
    main()