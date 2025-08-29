# Day 7：第一週複習與綜合練習

## 今日學習目標
- 複習第一週學過的所有概念
- 整合運用變數、資料型態、輸入輸出、字串處理、數學運算、條件判斷
- 製作一個綜合性的問答遊戲
- 檢視學習成果，為第二週做準備

## 第一週學習回顧

### Day 1: 程式設計基礎
- ✅ 理解程式設計概念
- ✅ 認識Python特色
- ✅ 安裝開發環境
- ✅ 第一個Hello World程式

### Day 2: 變數與資料型態
- ✅ 變數的概念和命名規則
- ✅ 基本資料型態：int, float, str, bool
- ✅ 型態轉換：int(), float(), str()
- ✅ 實作：個人資料卡

### Day 3: 輸入與輸出
- ✅ input()函數：接收使用者輸入
- ✅ print()函數：顯示輸出結果
- ✅ 格式化輸出：f-string
- ✅ 實作：對話程式

### Day 4: 字串處理
- ✅ 字串操作：連接、重複、分割
- ✅ 常用字串方法：upper(), lower(), strip()
- ✅ 字串格式化
- ✅ 實作：個人化問候語

### Day 5: 數學運算
- ✅ 基本運算子：+, -, *, /, //, %, **
- ✅ 運算優先順序
- ✅ 數學模組：math
- ✅ 實作：計算機和單位轉換

### Day 6: 條件判斷
- ✅ if, elif, else語句
- ✅ 比較運算子：==, !=, >, <, >=, <=
- ✅ 邏輯運算子：and, or, not
- ✅ 實作：成績分類和BMI計算

## 知識點整合測驗

### 測驗1：基本概念
```python
# 請回答以下問題：

# 1. Python中如何輸出 "Hello World"？
print("Hello World")

# 2. 如何宣告一個名為name的變數，值為"Alice"？
name = "Alice"

# 3. 如何將字串"123"轉換為整數？
number = int("123")

# 4. f-string的基本語法是什麼？
age = 25
message = f"我今年{age}歲"
```

### 測驗2：運算和判斷
```python
# 請寫出執行結果：

a = 10
b = 3

print(a + b)      # 結果：13
print(a // b)     # 結果：3
print(a % b)      # 結果：1
print(a ** b)     # 結果：1000

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(grade)      # 結果：B
```

## 綜合練習項目

### 練習1：個人資料處理系統
```python
def personal_info_system():
    """個人資料處理系統"""
    print("=== 個人資料處理系統 ===")
    
    # 收集基本資料
    name = input("請輸入姓名：")
    age = int(input("請輸入年齡："))
    height = float(input("請輸入身高（公分）："))
    weight = float(input("請輸入體重（公斤）："))
    
    # 計算BMI
    height_m = height / 100  # 轉換為公尺
    bmi = weight / (height_m ** 2)
    
    # BMI分類
    if bmi < 18.5:
        bmi_category = "體重過輕"
    elif bmi < 24:
        bmi_category = "體重正常"
    elif bmi < 27:
        bmi_category = "體重過重"
    else:
        bmi_category = "肥胖"
    
    # 年齡分類
    if age < 18:
        age_group = "青少年"
    elif age < 65:
        age_group = "成年人"
    else:
        age_group = "長者"
    
    # 生成報告
    print(f"\n=== {name}的健康報告 ===")
    print(f"基本資料：")
    print(f"  姓名：{name}")
    print(f"  年齡：{age}歲 ({age_group})")
    print(f"  身高：{height}公分")
    print(f"  體重：{weight}公斤")
    print(f"\n健康指標：")
    print(f"  BMI：{bmi:.2f}")
    print(f"  分類：{bmi_category}")
    
    # 個人化建議
    if age_group == "青少年":
        print(f"\n建議：多運動，均衡飲食，充足睡眠")
    elif age_group == "成年人":
        print(f"\n建議：保持規律運動，定期健康檢查")
    else:
        print(f"\n建議：適度運動，注意營養，定期就醫")

personal_info_system()
```

### 練習2：簡易購物系統
```python
def simple_shopping_system():
    """簡易購物系統"""
    print("=== 歡迎來到小小商店 ===")
    
    # 商品清單和價格
    products = {
        "1": ("蘋果", 30),
        "2": ("香蕉", 25),
        "3": ("橘子", 35),
        "4": ("牛奶", 45),
        "5": ("麵包", 40)
    }
    
    # 顯示商品
    print("\n商品清單：")
    for code, (name, price) in products.items():
        print(f"{code}. {name} - ${price}")
    
    total_amount = 0
    cart = []
    
    while True:
        choice = input("\n請選擇商品編號（1-5），或輸入'done'結帳：")
        
        if choice.lower() == 'done':
            break
        
        if choice in products:
            name, price = products[choice]
            quantity = int(input(f"請輸入{name}的數量："))
            
            subtotal = price * quantity
            total_amount += subtotal
            cart.append((name, quantity, price, subtotal))
            
            print(f"已添加：{name} x {quantity} = ${subtotal}")
        else:
            print("無效的商品編號！")
    
    # 結帳
    if cart:
        print(f"\n=== 購物清單 ===")
        for name, quantity, price, subtotal in cart:
            print(f"{name} x {quantity} @ ${price} = ${subtotal}")
        
        print(f"\n小計：${total_amount}")
        
        # 折扣計算
        discount = 0
        if total_amount >= 200:
            discount = total_amount * 0.1  # 9折
            print(f"滿200元享9折優惠：-${discount:.0f}")
        elif total_amount >= 100:
            discount = total_amount * 0.05  # 95折
            print(f"滿100元享95折優惠：-${discount:.0f}")
        
        final_amount = total_amount - discount
        print(f"最終金額：${final_amount:.0f}")
        
        # 付款
        while True:
            try:
                payment = float(input(f"\n請付款${final_amount:.0f}，您支付：$"))
                if payment >= final_amount:
                    change = payment - final_amount
                    print(f"付款成功！找零：${change:.0f}")
                    print("謝謝光臨！")
                    break
                else:
                    shortage = final_amount - payment
                    print(f"金額不足，還需要${shortage:.0f}")
            except ValueError:
                print("請輸入有效的金額！")
    else:
        print("沒有購買任何商品。")

simple_shopping_system()
```

### 練習3：智慧問答遊戲
```python
def quiz_game():
    """智慧問答遊戲"""
    print("=== 第一週Python知識問答 ===")
    
    questions = [
        {
            "question": "Python中用來輸出的函數是？",
            "options": ["A. input()", "B. print()", "C. output()", "D. show()"],
            "answer": "B",
            "explanation": "print()函數用來顯示輸出結果"
        },
        {
            "question": "以下哪個是正確的變數命名？",
            "options": ["A. 2name", "B. my-name", "C. my_name", "D. my name"],
            "answer": "C",
            "explanation": "變數名稱不能以數字開頭，不能包含空格和連字符"
        },
        {
            "question": "Python中 10 // 3 的結果是？",
            "options": ["A. 3.33", "B. 3", "C. 4", "D. 1"],
            "answer": "B",
            "explanation": "//是整數除法運算子，會捨去小數部分"
        },
        {
            "question": "以下哪個條件判斷語法是正確的？",
            "options": ["A. if x = 5:", "B. if x == 5:", "C. if x === 5:", "D. if (x = 5):"],
            "answer": "B",
            "explanation": "條件判斷使用==比較，=是賦值運算子"
        },
        {
            "question": "字串'hello'.upper()的結果是？",
            "options": ["A. hello", "B. HELLO", "C. Hello", "D. hELLO"],
            "answer": "B",
            "explanation": "upper()方法將字串轉換為大寫"
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    for i, q in enumerate(questions, 1):
        print(f"\n問題 {i}/{total_questions}:")
        print(q["question"])
        
        for option in q["options"]:
            print(f"  {option}")
        
        user_answer = input("\n請輸入答案 (A/B/C/D)：").upper()
        
        if user_answer == q["answer"]:
            print("✅ 正確！")
            score += 1
        else:
            print(f"❌ 錯誤！正確答案是 {q['answer']}")
        
        print(f"解釋：{q['explanation']}")
        input("按 Enter 繼續下一題...")
    
    # 計算成績
    percentage = (score / total_questions) * 100
    
    print(f"\n=== 遊戲結束 ===")
    print(f"總題數：{total_questions}")
    print(f"答對：{score}題")
    print(f"分數：{percentage:.1f}分")
    
    if percentage >= 90:
        grade = "優秀"
        comment = "太棒了！你完全掌握了第一週的內容！"
    elif percentage >= 70:
        grade = "良好"
        comment = "很好！大部分內容都掌握了，繼續努力！"
    elif percentage >= 60:
        grade = "及格"
        comment = "還不錯，建議再複習一下錯誤的部分。"
    else:
        grade = "需要加強"
        comment = "建議重新複習第一週的內容，多做練習。"
    
    print(f"評級：{grade}")
    print(f"建議：{comment}")

quiz_game()
```

## 第一週總結項目：個人學習記錄系統

```python
def learning_record_system():
    """個人學習記錄系統 - 第一週總結"""
    import datetime
    
    print("=== Python學習記錄系統 ===")
    print("第一週學習總結")
    
    # 記錄學習者資訊
    learner_name = input("請輸入你的姓名：")
    start_date = input("請輸入開始學習日期 (例如：2024-01-01)：")
    
    print(f"\n{learner_name}，讓我們來總結你第一週的學習成果！")
    
    # 各天學習情況調查
    days_content = {
        "Day 1": "程式設計基礎概念",
        "Day 2": "變數與資料型態", 
        "Day 3": "輸入與輸出",
        "Day 4": "字串處理",
        "Day 5": "數學運算",
        "Day 6": "條件判斷"
    }
    
    understanding_scores = {}
    total_score = 0
    
    print("\n請為每天的學習內容打分（1-10分，10分表示完全理解）：")
    
    for day, content in days_content.items():
        while True:
            try:
                score = int(input(f"{day} - {content}: "))
                if 1 <= score <= 10:
                    understanding_scores[day] = score
                    total_score += score
                    break
                else:
                    print("請輸入1-10之間的分數")
            except ValueError:
                print("請輸入有效的數字")
    
    # 計算平均分和評級
    average_score = total_score / len(days_content)
    
    if average_score >= 8:
        level = "優秀"
        suggestion = "你的學習狀況很好！可以開始準備第二週的內容。"
    elif average_score >= 6:
        level = "良好"
        suggestion = "學習進度不錯，建議加強理解較弱的部分。"
    elif average_score >= 4:
        level = "普通"
        suggestion = "需要多花時間複習，特別是分數較低的章節。"
    else:
        level = "需要加強"
        suggestion = "建議重新學習第一週內容，多做練習。"
    
    # 找出最需要加強的部分
    min_score = min(understanding_scores.values())
    weak_areas = [day for day, score in understanding_scores.items() if score == min_score]
    
    # 生成學習報告
    print(f"\n=== {learner_name} 的第一週學習報告 ===")
    print(f"學習開始日期：{start_date}")
    print(f"報告生成日期：{datetime.datetime.now().strftime('%Y-%m-%d')}")
    print(f"\n各日學習評分：")
    
    for day, score in understanding_scores.items():
        print(f"  {day}: {score}/10 - {days_content[day]}")
    
    print(f"\n總體評估：")
    print(f"  平均分數：{average_score:.1f}/10")
    print(f"  學習等級：{level}")
    print(f"  建議：{suggestion}")
    
    if weak_areas:
        print(f"\n需要加強的部分：")
        for area in weak_areas:
            print(f"  - {area}: {days_content[area]}")
    
    # 設定第二週學習目標
    print(f"\n=== 第二週學習目標設定 ===")
    goal1 = input("請設定一個具體的學習目標：")
    goal2 = input("請設定另一個學習目標：")
    
    print(f"\n你的第二週學習目標：")
    print(f"1. {goal1}")
    print(f"2. {goal2}")
    print(f"\n加油！繼續你的Python學習之旅！")

learning_record_system()
```

## 實戰挑戦：文字冒險遊戲

```python
def text_adventure_game():
    """文字冒險遊戲 - 運用第一週所學"""
    import random
    
    print("=== Python學習冒險 ===")
    print("歡迎來到程式世界！你是一個剛開始學習Python的新手。")
    
    # 玩家屬性
    player_name = input("請輸入你的姓名：")
    health = 100
    knowledge = 0
    items = []
    
    print(f"\n{player_name}，你的冒險開始了！")
    print(f"生命值：{health}")
    print(f"知識點：{knowledge}")
    
    # 第一關：變數迷宮
    print(f"\n=== 第一關：變數迷宮 ===")
    print("你遇到了變數迷宮，需要正確宣告變數才能通過。")
    
    question = "創建一個變數name，值為你的姓名，正確的語法是？"
    options = ["A. name = input()", f"B. name = '{player_name}'", "C. name == input()", "D. name := input()"]
    
    print(question)
    for option in options:
        print(option)
    
    answer = input("請選擇 (A/B/C/D)：").upper()
    
    if answer == "B":
        print("✅ 正確！你獲得了『變數精通』徽章！")
        knowledge += 20
        items.append("變數精通徽章")
    else:
        print("❌ 錯誤！你被困在迷宮中，損失10點生命值。")
        health -= 10
        print("正確答案是B。記住：變數賦值使用 = 符號。")
    
    # 第二關：運算挑戰
    print(f"\n=== 第二關：運算挑戰 ===")
    print(f"目前狀態 - 生命值：{health}, 知識點：{knowledge}")
    
    num1 = random.randint(10, 50)
    num2 = random.randint(5, 15)
    
    print(f"數學精靈出現了！它出了一道題：{num1} // {num2} = ?")
    
    try:
        user_answer = int(input("請輸入答案："))
        correct_answer = num1 // num2
        
        if user_answer == correct_answer:
            print("✅ 正確！你獲得了『運算大師』稱號！")
            knowledge += 25
            items.append("運算大師稱號")
        else:
            print(f"❌ 錯誤！正確答案是{correct_answer}")
            print("//是整數除法，會捨去小數部分。")
            health -= 15
    
    except ValueError:
        print("❌ 輸入格式錯誤！損失10點生命值。")
        health -= 10
    
    # 第三關：條件迷題
    print(f"\n=== 第三關：條件迷題 ===")
    print(f"目前狀態 - 生命值：{health}, 知識點：{knowledge}")
    
    if health <= 50:
        print("你的生命值過低！是否要使用治療藥水？")
        use_potion = input("輸入 yes 使用，其他任意鍵跳過：").lower()
        
        if use_potion == "yes":
            health += 30
            print(f"使用治療藥水！生命值恢復到{health}")
        else:
            print("你選擇繼續冒險。")
    
    print("智慧老人出現：「年輕的程式設計師，回答我的問題。」")
    print("「在Python中，如何檢查變數x是否等於10？」")
    
    options = ["A. x = 10", "B. x == 10", "C. x === 10", "D. x is 10"]
    for option in options:
        print(option)
    
    answer = input("請選擇 (A/B/C/D)：").upper()
    
    if answer == "B":
        print("✅「很好！你已經理解了條件判斷。」")
        knowledge += 30
        items.append("智慧老人的祝福")
    else:
        print("❌「還需要多學習啊。」條件比較使用 == 符號。")
        health -= 20
    
    # 最終結果
    print(f"\n=== 冒險結束 ===")
    print(f"冒險者：{player_name}")
    print(f"最終生命值：{health}")
    print(f"獲得知識點：{knowledge}")
    
    print(f"\n獲得物品：")
    if items:
        for item in items:
            print(f"  - {item}")
    else:
        print("  無")
    
    # 評價
    if knowledge >= 70 and health >= 50:
        rating = "Python新星"
        message = "恭喜！你展現了出色的Python基礎！"
    elif knowledge >= 50:
        rating = "程式新手"
        message = "不錯的開始！繼續學習會更好。"
    elif health > 0:
        rating = "勇敢探索者"
        message = "雖然遇到困難，但勇氣可嘉！"
    else:
        rating = "需要重新學習"
        message = "建議複習第一週內容後再次挑戰。"
    
    print(f"\n最終評級：{rating}")
    print(f"評語：{message}")

text_adventure_game()
```

## 學習檢查清單

### 必須掌握的概念 ✅
- [ ] 能夠使用print()輸出內容
- [ ] 理解變數的概念和命名規則
- [ ] 掌握基本資料型態：int, float, str, bool
- [ ] 會使用input()接收使用者輸入
- [ ] 能夠進行型態轉換
- [ ] 掌握字串的基本操作
- [ ] 理解數學運算子和優先順序
- [ ] 會使用if, elif, else條件判斷
- [ ] 理解比較運算子和邏輯運算子

### 實作能力檢核 ✅
- [ ] 能寫出接收輸入並處理的程式
- [ ] 能製作簡單的計算程式
- [ ] 能使用條件判斷處理不同情況
- [ ] 能組合多個概念完成複雜任務
- [ ] 能找出並修正常見的程式錯誤

## 第二週預習

下週我們將學習：

### Day 8-9: 迴圈（for & while）
- 重複執行程式碼的方法
- for迴圈遍歷序列
- while迴圈條件控制
- 實作：九九乘法表、猜數字遊戲

### Day 10-13: 資料結構
- 清單（List）：存儲多個項目
- 字典（Dictionary）：鍵值對資料
- 元組（Tuple）：不可變序列
- 實作：學生管理系統

### Day 14: 第二週綜合練習
- 整合迴圈和資料結構
- 製作更複雜的程式

## 鼓勵話語

🎉 **恭喜你完成了Python學習的第一週！**

你已經掌握了程式設計的基礎概念，這是一個很好的開始。記住：
- **每個程式設計師都是從這些基礎開始的**
- **不要害怕犯錯，錯誤是學習最好的老師**
- **多動手實作，理論結合實踐才能真正掌握**
- **保持好奇心，嘗試修改程式碼看看會發生什麼**

準備好迎接下一週更精彩的內容了嗎？讓我們繼續這趟Python學習之旅！

---

**下一步：開始第二週學習 - 迴圈與資料結構**