# Day 9: While迴圈練習
# 這個檔案包含各種while迴圈的實用範例

print("=== Day 9: While迴圈練習 ===\n")

# 練習1：數字累加器
print("練習1：數字累加器")
print("目標：輸入數字直到總和超過50")
total = 0
count = 0

while total < 50:
    try:
        num = int(input(f"目前總和：{total}，請輸入一個數字："))
        total += num
        count += 1
    except ValueError:
        print("請輸入有效的數字！")
        continue

print(f"總和達到：{total}，共輸入了{count}個數字")

print("\n" + "="*40 + "\n")

# 練習2：密碼驗證系統
print("練習2：密碼驗證系統")
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("請輸入密碼：")
    if password == correct_password:
        print("✅ 登入成功！歡迎回來")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ 密碼錯誤！還有{remaining}次機會")
        else:
            print("🚫 超過嘗試次數，帳號被鎖定！")

print("\n" + "="*40 + "\n")

# 練習3：簡單計算機
print("練習3：簡單計算機")
print("支援基本四則運算，輸入 'quit' 結束程式")

while True:
    print("\n📱 計算機選單")
    print("可用操作：+（加法）, -（減法）, *（乘法）, /（除法）")
    print("輸入 'quit' 退出計算機")
    
    operation = input("請選擇操作：").strip()
    
    if operation.lower() == 'quit':
        print("👋 計算機已關閉，感謝使用！")
        break
    elif operation in ['+', '-', '*', '/']:
        try:
            a = float(input("請輸入第一個數字："))
            b = float(input("請輸入第二個數字："))
            
            if operation == '+':
                result = a + b
                print(f"🔢 結果：{a} + {b} = {result}")
            elif operation == '-':
                result = a - b
                print(f"🔢 結果：{a} - {b} = {result}")
            elif operation == '*':
                result = a * b
                print(f"🔢 結果：{a} × {b} = {result}")
            elif operation == '/':
                if b != 0:
                    result = a / b
                    print(f"🔢 結果：{a} ÷ {b} = {result:.4f}")
                else:
                    print("❌ 錯誤：除數不能為零！")
                    
        except ValueError:
            print("❌ 請輸入有效的數字！")
    else:
        print("❌ 無效的操作！請輸入 +, -, *, / 或 quit")

print("\n" + "="*40 + "\n")

# 練習4：倒數計時器
print("練習4：倒數計時器")
try:
    start_time = int(input("請設定倒數秒數："))
    if start_time <= 0:
        print("請輸入正整數！")
    else:
        print(f"⏰ {start_time}秒倒數計時開始！")
        
        while start_time > 0:
            if start_time <= 5:
                print(f"⚡ {start_time}！")
            else:
                print(f"⏳ {start_time}")
            
            # 模擬等待1秒（實際應用中可使用time.sleep(1)）
            input("（按Enter模擬1秒經過）")
            start_time -= 1
        
        print("🎉 時間到！")
except ValueError:
    print("請輸入有效的數字！")

print("\n" + "="*40 + "\n")

# 練習5：數字猜謎遊戲（簡化版）
print("練習5：數字猜謎遊戲")
import random

secret = random.randint(1, 20)
max_attempts = 5
attempts = 0
guessed_numbers = []

print("🎯 我想了一個1到20之間的數字")
print(f"你有{max_attempts}次機會猜中它！")

while attempts < max_attempts:
    remaining = max_attempts - attempts
    print(f"\n剩餘機會：{remaining}")
    
    if guessed_numbers:
        print(f"已猜過：{guessed_numbers}")
    
    try:
        guess = int(input("請輸入你的猜測："))
        
        if guess < 1 or guess > 20:
            print("⚠️ 請輸入1到20之間的數字！")
            continue
        
        if guess in guessed_numbers:
            print("⚠️ 你已經猜過這個數字了！")
            continue
        
        attempts += 1
        guessed_numbers.append(guess)
        
        if guess == secret:
            print(f"🎊 恭喜！你在第{attempts}次猜中了！答案就是{secret}")
            break
        elif guess < secret:
            print("📈 太小了！再猜大一點")
        else:
            print("📉 太大了！再猜小一點")
            
    except ValueError:
        print("❌ 請輸入有效的數字！")
        continue

else:
    # while迴圈正常結束（沒有break）
    print(f"😢 遊戲結束！答案是：{secret}")

print("\n" + "="*40 + "\n")

# 練習6：選單導航系統
print("練習6：選單導航系統")
user_data = []

while True:
    print("\n🏠 主選單")
    print("1. 👀 查看資料")
    print("2. ➕ 新增資料")
    print("3. 🗑️  刪除資料")
    print("4. 📊 統計資料")
    print("5. 🚪 離開系統")
    
    choice = input("請選擇功能 (1-5): ").strip()
    
    if choice == "1":
        print("\n👀 查看資料")
        if user_data:
            for i, data in enumerate(user_data, 1):
                print(f"{i}. {data}")
        else:
            print("目前沒有任何資料")
    
    elif choice == "2":
        print("\n➕ 新增資料")
        new_data = input("請輸入要新增的資料：").strip()
        if new_data:
            user_data.append(new_data)
            print(f"已新增：{new_data}")
        else:
            print("❌ 資料不能為空！")
    
    elif choice == "3":
        print("\n🗑️ 刪除資料")
        if user_data:
            print("目前的資料：")
            for i, data in enumerate(user_data, 1):
                print(f"{i}. {data}")
            
            try:
                index = int(input("請輸入要刪除的資料編號：")) - 1
                if 0 <= index < len(user_data):
                    deleted_data = user_data.pop(index)
                    print(f"已刪除：{deleted_data}")
                else:
                    print("❌ 編號無效！")
            except ValueError:
                print("❌ 請輸入有效的編號！")
        else:
            print("目前沒有任何資料可刪除")
    
    elif choice == "4":
        print("\n📊 統計資料")
        print(f"總共有 {len(user_data)} 筆資料")
        if user_data:
            total_chars = sum(len(data) for data in user_data)
            avg_chars = total_chars / len(user_data)
            print(f"平均每筆資料長度：{avg_chars:.1f} 個字元")
    
    elif choice == "5":
        confirm = input("確定要離開嗎？(y/n): ").lower()
        if confirm == 'y':
            print("👋 感謝使用，再見！")
            break
        # 如果不是'y'，則繼續迴圈
    
    else:
        print("❌ 無效的選擇，請輸入1-5")

print("\n程式執行完畢！")