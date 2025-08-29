#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 7: 第一週複習與綜合練習
整合運用第一週學過的所有概念：變數、資料型態、輸入輸出、字串處理、數學運算、條件判斷
"""

import random
import datetime

def knowledge_quiz():
    """第一週知識測驗"""
    print("=== 第一週 Python 知識測驗 ===")
    print("測試你對第一週內容的掌握程度\n")
    
    questions = [
        {
            "question": "Python中用來輸出文字到螢幕的函數是？",
            "options": ["A. input()", "B. print()", "C. output()", "D. display()"],
            "answer": "B",
            "explanation": "print()函數用來將文字或變數值輸出到螢幕上"
        },
        {
            "question": "以下哪個是正確的變數命名？",
            "options": ["A. 2student", "B. student-name", "C. student_name", "D. student name"],
            "answer": "C", 
            "explanation": "變數名稱不能以數字開頭，不能包含空格或連字符，但可以使用底線"
        },
        {
            "question": "Python中 15 // 4 的結果是？",
            "options": ["A. 3.75", "B. 3", "C. 4", "D. 15"],
            "answer": "B",
            "explanation": "// 是整數除法運算子，15除以4等於3餘3，整數部分是3"
        },
        {
            "question": "以下哪個條件判斷的語法是正確的？",
            "options": ["A. if x = 5:", "B. if x == 5:", "C. if x === 5:", "D. if x is 5:"],
            "answer": "B",
            "explanation": "條件判斷使用 == 來比較兩個值是否相等，= 是賦值運算子"
        },
        {
            "question": "字串 'Python'.lower() 的結果是？",
            "options": ["A. PYTHON", "B. Python", "C. python", "D. pYTHON"],
            "answer": "C",
            "explanation": "lower()方法將字串中的所有字母轉換為小寫"
        },
        {
            "question": "如何將字串 '123' 轉換為整數？",
            "options": ["A. str('123')", "B. int('123')", "C. float('123')", "D. number('123')"],
            "answer": "B",
            "explanation": "int()函數用來將字串或浮點數轉換為整數"
        },
        {
            "question": "Python中表示邏輯「且」的運算子是？",
            "options": ["A. &&", "B. and", "C. &", "D. AND"],
            "answer": "B",
            "explanation": "Python使用 and 關鍵字表示邏輯「且」運算"
        }
    ]
    
    score = 0
    total = len(questions)
    wrong_answers = []
    
    for i, q in enumerate(questions, 1):
        print(f"第 {i} 題：{q['question']}")
        for option in q["options"]:
            print(f"  {option}")
        
        user_answer = input("\n請選擇答案 (A/B/C/D)：").upper().strip()
        
        if user_answer == q["answer"]:
            print("✅ 正確！")
            score += 1
        else:
            print(f"❌ 錯誤！正確答案是 {q['answer']}")
            wrong_answers.append((i, q["question"], q["answer"]))
        
        print(f"說明：{q['explanation']}")
        print("-" * 50)
    
    # 顯示成績
    percentage = (score / total) * 100
    print(f"\n=== 測驗結果 ===")
    print(f"答對題數：{score}/{total}")
    print(f"正確率：{percentage:.1f}%")
    
    if percentage >= 90:
        grade = "優秀"
        comment = "太棒了！你完全掌握了第一週的內容！"
    elif percentage >= 70:
        grade = "良好"
        comment = "很好！大部分內容都理解了。"
    elif percentage >= 60:
        grade = "及格"
        comment = "還不錯，建議複習錯誤的題目。"
    else:
        grade = "需要加強"
        comment = "建議重新複習第一週的內容。"
    
    print(f"評級：{grade}")
    print(f"建議：{comment}")
    
    if wrong_answers:
        print(f"\n需要複習的題目：")
        for num, question, correct in wrong_answers:
            print(f"第{num}題：{question}")
            print(f"正確答案：{correct}")

def personal_info_manager():
    """個人資料管理系統"""
    print("\n=== 個人資料管理系統 ===")
    
    # 收集個人基本資料
    name = input("請輸入姓名：").strip()
    
    while True:
        try:
            age = int(input("請輸入年齡："))
            if age > 0:
                break
            else:
                print("年齡必須大於0")
        except ValueError:
            print("請輸入有效的數字")
    
    while True:
        try:
            height = float(input("請輸入身高（公分）："))
            if height > 0:
                break
            else:
                print("身高必須大於0")
        except ValueError:
            print("請輸入有效的數字")
    
    while True:
        try:
            weight = float(input("請輸入體重（公斤）："))
            if weight > 0:
                break
            else:
                print("體重必須大於0")
        except ValueError:
            print("請輸入有效的數字")
    
    # 計算BMI
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    # BMI分類
    if bmi < 18.5:
        bmi_status = "體重過輕"
        bmi_advice = "建議增加營養攝取，適度運動"
    elif bmi < 24:
        bmi_status = "體重正常"
        bmi_advice = "保持良好的生活習慣"
    elif bmi < 27:
        bmi_status = "體重過重"
        bmi_advice = "建議控制飲食，增加運動"
    else:
        bmi_status = "肥胖"
        bmi_advice = "建議諮詢醫生，制定減重計劃"
    
    # 年齡分組
    if age < 18:
        age_group = "青少年"
        age_advice = "注重學習，培養良好習慣"
    elif age < 30:
        age_group = "青年"
        age_advice = "努力發展事業，保持健康"
    elif age < 60:
        age_group = "中年"
        age_advice = "平衡工作與健康，定期檢查"
    else:
        age_group = "長者"
        age_advice = "注重健康保養，享受生活"
    
    # 生成個人化報告
    print(f"\n=== {name} 的個人健康報告 ===")
    print(f"基本資料：")
    print(f"  姓名：{name}")
    print(f"  年齡：{age}歲 ({age_group})")
    print(f"  身高：{height}公分")
    print(f"  體重：{weight}公斤")
    
    print(f"\n健康指標：")
    print(f"  BMI值：{bmi:.2f}")
    print(f"  狀態：{bmi_status}")
    print(f"  建議：{bmi_advice}")
    
    print(f"\n人生階段建議：")
    print(f"  {age_advice}")
    
    # 計算一些有趣的數據
    days_lived = age * 365
    hours_lived = days_lived * 24
    
    print(f"\n有趣統計：")
    print(f"  你已經活了約 {days_lived:,} 天")
    print(f"  相當於約 {hours_lived:,} 小時")
    
    if age < 80:
        remaining_years = 80 - age
        print(f"  如果活到80歲，還有約 {remaining_years} 年")

def simple_calculator():
    """進階計算機"""
    print("\n=== 進階計算機 ===")
    
    while True:
        print("\n計算機選項：")
        print("1. 基本運算 (+, -, *, /)")
        print("2. 進階運算 (平方根, 次方, 百分比)")
        print("3. 幾何計算 (圓形, 矩形面積)")
        print("4. 單位轉換")
        print("0. 返回主選單")
        
        choice = input("請選擇功能 (0-4)：").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            basic_math()
        elif choice == "2":
            advanced_math()
        elif choice == "3":
            geometry_calc()
        elif choice == "4":
            unit_converter()
        else:
            print("無效選擇！")

def basic_math():
    """基本數學運算"""
    print("\n--- 基本運算 ---")
    
    try:
        num1 = float(input("請輸入第一個數字："))
        operator = input("請輸入運算子 (+, -, *, /)：").strip()
        num2 = float(input("請輸入第二個數字："))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("錯誤：除數不能為零！")
                return
        else:
            print("不支援的運算子！")
            return
        
        print(f"結果：{num1} {operator} {num2} = {result}")
        
    except ValueError:
        print("請輸入有效的數字！")

def advanced_math():
    """進階數學運算"""
    print("\n--- 進階運算 ---")
    print("1. 平方根")
    print("2. 次方運算") 
    print("3. 百分比計算")
    
    choice = input("選擇運算類型 (1-3)：").strip()
    
    try:
        if choice == "1":
            num = float(input("請輸入數字："))
            if num >= 0:
                result = num ** 0.5
                print(f"√{num} = {result:.4f}")
            else:
                print("負數不能開平方根！")
        
        elif choice == "2":
            base = float(input("請輸入底數："))
            exponent = float(input("請輸入指數："))
            result = base ** exponent
            print(f"{base}^{exponent} = {result}")
        
        elif choice == "3":
            value = float(input("請輸入數值："))
            total = float(input("請輸入總數："))
            if total != 0:
                percentage = (value / total) * 100
                print(f"{value} 佔 {total} 的 {percentage:.2f}%")
            else:
                print("總數不能為零！")
        
        else:
            print("無效選擇！")
    
    except ValueError:
        print("請輸入有效的數字！")

def geometry_calc():
    """幾何計算"""
    print("\n--- 幾何計算 ---")
    print("1. 圓形面積和周長")
    print("2. 矩形面積和周長")
    print("3. 三角形面積")
    
    choice = input("選擇計算類型 (1-3)：").strip()
    
    try:
        if choice == "1":
            radius = float(input("請輸入圓的半徑："))
            if radius > 0:
                area = 3.14159 * radius ** 2
                circumference = 2 * 3.14159 * radius
                print(f"圓形面積：{area:.2f}")
                print(f"圓形周長：{circumference:.2f}")
            else:
                print("半徑必須大於0！")
        
        elif choice == "2":
            length = float(input("請輸入矩形長度："))
            width = float(input("請輸入矩形寬度："))
            if length > 0 and width > 0:
                area = length * width
                perimeter = 2 * (length + width)
                print(f"矩形面積：{area:.2f}")
                print(f"矩形周長：{perimeter:.2f}")
            else:
                print("長度和寬度都必須大於0！")
        
        elif choice == "3":
            base = float(input("請輸入三角形底邊："))
            height = float(input("請輸入三角形高度："))
            if base > 0 and height > 0:
                area = 0.5 * base * height
                print(f"三角形面積：{area:.2f}")
            else:
                print("底邊和高度都必須大於0！")
        
        else:
            print("無效選擇！")
    
    except ValueError:
        print("請輸入有效的數字！")

def unit_converter():
    """單位轉換器"""
    print("\n--- 單位轉換 ---")
    print("1. 溫度轉換 (攝氏 ↔ 華氏)")
    print("2. 長度轉換 (公尺 ↔ 英尺)")
    print("3. 重量轉換 (公斤 ↔ 磅)")
    
    choice = input("選擇轉換類型 (1-3)：").strip()
    
    try:
        if choice == "1":
            temp_type = input("輸入 'C' 表示攝氏轉華氏，'F' 表示華氏轉攝氏：").upper().strip()
            temp = float(input("請輸入溫度："))
            
            if temp_type == "C":
                fahrenheit = temp * 9/5 + 32
                print(f"{temp}°C = {fahrenheit:.1f}°F")
            elif temp_type == "F":
                celsius = (temp - 32) * 5/9
                print(f"{temp}°F = {celsius:.1f}°C")
            else:
                print("無效輸入！")
        
        elif choice == "2":
            length_type = input("輸入 'M' 表示公尺轉英尺，'F' 表示英尺轉公尺：").upper().strip()
            length = float(input("請輸入長度："))
            
            if length_type == "M":
                feet = length * 3.28084
                print(f"{length}公尺 = {feet:.2f}英尺")
            elif length_type == "F":
                meters = length / 3.28084
                print(f"{length}英尺 = {meters:.2f}公尺")
            else:
                print("無效輸入！")
        
        elif choice == "3":
            weight_type = input("輸入 'K' 表示公斤轉磅，'P' 表示磅轉公斤：").upper().strip()
            weight = float(input("請輸入重量："))
            
            if weight_type == "K":
                pounds = weight * 2.20462
                print(f"{weight}公斤 = {pounds:.2f}磅")
            elif weight_type == "P":
                kilograms = weight / 2.20462
                print(f"{weight}磅 = {kilograms:.2f}公斤")
            else:
                print("無效輸入！")
        
        else:
            print("無效選擇！")
    
    except ValueError:
        print("請輸入有效的數字！")

def text_adventure():
    """文字冒險遊戲"""
    print("\n=== Python 學習冒險 ===")
    
    player_name = input("請輸入你的冒險者名字：").strip()
    health = 100
    knowledge = 0
    
    print(f"\n歡迎，{player_name}！你即將開始一場Python學習冒險。")
    print(f"初始狀態：生命值 {health}，知識點 {knowledge}")
    
    # 第一關：變數村莊
    print(f"\n=== 第一關：變數村莊 ===")
    print("你來到了變數村莊，村民要測試你的變數知識。")
    
    question = "村民問：'如果我想儲存我的年齡25，應該怎麼寫？'"
    print(question)
    print("A. age = '25'")
    print("B. age = 25") 
    print("C. age == 25")
    print("D. 25 = age")
    
    answer = input("請選擇 (A/B/C/D)：").upper().strip()
    
    if answer == "B":
        print("✅ 村民微笑：'很好！你理解變數賦值。'")
        knowledge += 20
        print(f"獲得20點知識！目前知識點：{knowledge}")
    else:
        print("❌ 村民搖頭：'不對，要用 = 來賦值，而且數字不用引號。'")
        health -= 10
        print(f"生命值減少10！目前生命值：{health}")
    
    # 第二關：運算森林
    print(f"\n=== 第二關：運算森林 ===")
    print("你進入運算森林，遇到了數學精靈。")
    
    num1 = random.randint(10, 30)
    num2 = random.randint(5, 15)
    
    print(f"數學精靈問：'{num1} // {num2} 等於多少？'")
    
    try:
        user_answer = int(input("請輸入答案："))
        correct = num1 // num2
        
        if user_answer == correct:
            print("✅ 精靈點頭：'正確！你掌握了整數除法。'")
            knowledge += 25
            print(f"獲得25點知識！目前知識點：{knowledge}")
        else:
            print(f"❌ 精靈說：'錯了，{num1} // {num2} = {correct}'")
            health -= 15
            print(f"生命值減少15！目前生命值：{health}")
    
    except ValueError:
        print("❌ 精靈困惑：'這不是數字！'")
        health -= 10
        print(f"生命值減少10！目前生命值：{health}")
    
    # 檢查是否需要治療
    if health < 50:
        print(f"\n你的生命值過低({health})！")
        use_potion = input("是否使用治療藥水恢復生命值？(yes/no)：").lower().strip()
        
        if use_potion == "yes":
            health += 30
            print(f"使用治療藥水！生命值恢復到 {health}")
        else:
            print("你選擇堅持繼續冒險。")
    
    # 第三關：條件迷宮
    print(f"\n=== 第三關：條件迷宮 ===")
    print("最後一關！智慧守護者出現了。")
    
    print("守護者問：'在Python中，如何表達「年齡大於等於18」這個條件？'")
    print("A. age > 18")
    print("B. age >= 18")
    print("C. age => 18")
    print("D. age = 18")
    
    answer = input("請選擇 (A/B/C/D)：").upper().strip()
    
    if answer == "B":
        print("✅ 守護者讚許：'優秀！你已經掌握了條件判斷。'")
        knowledge += 30
        print(f"獲得30點知識！最終知識點：{knowledge}")
    else:
        print("❌ 守護者說：'應該是 >= 表示大於等於。'")
        health -= 20
        print(f"生命值減少20！最終生命值：{health}")
    
    # 最終評價
    print(f"\n=== 冒險結束 ===")
    print(f"冒險者：{player_name}")
    print(f"最終生命值：{health}")
    print(f"最終知識點：{knowledge}")
    
    if knowledge >= 70 and health >= 60:
        rank = "Python大師"
        comment = "恭喜！你展現了出色的Python基礎能力！"
    elif knowledge >= 50:
        rank = "Python學徒"
        comment = "不錯！你已經掌握了基本概念。"
    elif knowledge >= 30:
        rank = "Python新手"
        comment = "還需要多練習，但開始得不錯。"
    else:
        rank = "需要重新學習"
        comment = "建議重新複習第一週的內容。"
    
    print(f"\n冒險等級：{rank}")
    print(f"評語：{comment}")

def learning_tracker():
    """學習進度追蹤器"""
    print("\n=== 學習進度追蹤器 ===")
    
    learner_name = input("請輸入你的姓名：").strip()
    
    topics = [
        "Day 1: 程式設計基礎概念",
        "Day 2: 變數與資料型態", 
        "Day 3: 輸入與輸出",
        "Day 4: 字串處理",
        "Day 5: 數學運算",
        "Day 6: 條件判斷"
    ]
    
    print(f"\n{learner_name}，請為每個主題的掌握程度評分（1-10分）：")
    
    scores = []
    total_score = 0
    
    for topic in topics:
        while True:
            try:
                score = int(input(f"{topic}: "))
                if 1 <= score <= 10:
                    scores.append(score)
                    total_score += score
                    break
                else:
                    print("請輸入1-10之間的分數！")
            except ValueError:
                print("請輸入有效的數字！")
    
    average = total_score / len(topics)
    
    print(f"\n=== {learner_name} 的學習報告 ===")
    print(f"報告日期：{datetime.datetime.now().strftime('%Y-%m-%d')}")
    print(f"\n各主題評分：")
    
    for i, (topic, score) in enumerate(zip(topics, scores)):
        status = "👑" if score >= 8 else "✅" if score >= 6 else "⚠️" if score >= 4 else "❌"
        print(f"  {status} {topic}: {score}/10")
    
    print(f"\n總體評估：")
    print(f"  平均分數：{average:.1f}/10")
    
    if average >= 8:
        level = "優秀"
        advice = "太棒了！你可以開始第二週的學習。"
    elif average >= 6:
        level = "良好"
        advice = "表現不錯！可以進入下一階段。"
    elif average >= 4:
        level = "普通"
        advice = "需要加強練習，特別是分數較低的主題。"
    else:
        level = "需要改善"
        advice = "建議重新學習第一週內容。"
    
    print(f"  學習等級：{level}")
    print(f"  建議：{advice}")
    
    # 找出需要加強的領域
    weak_areas = [topics[i] for i, score in enumerate(scores) if score < 6]
    if weak_areas:
        print(f"\n需要加強的領域：")
        for area in weak_areas:
            print(f"  - {area}")
    
    # 設定下週目標
    print(f"\n=== 第二週學習目標設定 ===")
    goal1 = input("請設定一個具體的學習目標：").strip()
    goal2 = input("請設定另一個學習挑戰：").strip()
    
    print(f"\n{learner_name} 的第二週目標：")
    print(f"🎯 目標1：{goal1}")
    print(f"🎯 目標2：{goal2}")
    print(f"\n加油！Python學習之旅才剛開始！")

def main():
    """主程式選單"""
    print("🐍 Day 7: 第一週複習與綜合練習")
    print("=" * 50)
    
    while True:
        print(f"\n請選擇活動：")
        print("1. 📝 知識測驗（測試你的理解程度）")
        print("2. 👤 個人資料管理系統") 
        print("3. 🧮 進階計算機")
        print("4. 🎮 Python學習冒險遊戲")
        print("5. 📊 學習進度追蹤器")
        print("0. 結束程式")
        
        choice = input("\n請輸入選項 (0-5)：").strip()
        
        if choice == "1":
            knowledge_quiz()
        elif choice == "2":
            personal_info_manager()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            text_adventure()
        elif choice == "5":
            learning_tracker()
        elif choice == "0":
            print("🎉 恭喜完成第一週的學習！")
            print("準備好迎接第二週的挑戰了嗎？")
            print("下週我們將學習迴圈和資料結構！")
            break
        else:
            print("❌ 無效選項，請重新選擇！")

if __name__ == "__main__":
    main()