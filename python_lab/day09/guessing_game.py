# 猜數字遊戲 - Day 9主要項目
# 完整的互動式猜數字遊戲

import random

def display_welcome():
    """顯示歡迎畫面"""
    print("🎯" + "="*40 + "🎯")
    print("     歡迎來到終極猜數字遊戲！")
    print("🎯" + "="*40 + "🎯")

def get_difficulty():
    """讓玩家選擇難度"""
    print("\n🎮 請選擇遊戲難度：")
    print("1. 😊 簡單（1-20，8次機會）")
    print("2. 😐 中等（1-50，7次機會）") 
    print("3. 😎 困難（1-100，6次機會）")
    print("4. 🤯 地獄（1-200，5次機會）")
    
    while True:
        choice = input("\n請輸入難度 (1-4): ").strip()
        
        if choice == "1":
            return 1, 20, 8, "簡單"
        elif choice == "2":
            return 1, 50, 7, "中等"
        elif choice == "3":
            return 1, 100, 6, "困難"
        elif choice == "4":
            return 1, 200, 5, "地獄"
        else:
            print("❌ 請輸入1-4之間的數字！")

def get_valid_guess(min_num, max_num, guessed_numbers):
    """取得有效的猜測數字"""
    while True:
        guess_input = input(f"請輸入你的猜測（{min_num}-{max_num}）：").strip()
        
        # 檢查是否要退出
        if guess_input.lower() in ['quit', 'exit', 'q']:
            return 'quit'
        
        # 檢查是否要提示
        if guess_input.lower() in ['hint', 'h']:
            return 'hint'
        
        # 驗證數字輸入
        try:
            guess = int(guess_input)
            
            if guess < min_num or guess > max_num:
                print(f"⚠️ 請輸入{min_num}到{max_num}之間的數字！")
                continue
            
            if guess in guessed_numbers:
                print("⚠️ 你已經猜過這個數字了！")
                continue
            
            return guess
            
        except ValueError:
            print("❌ 請輸入有效的數字！")
            print("💡 提示：輸入 'h' 獲取提示，'q' 退出遊戲")

def give_hint(secret_number, guessed_numbers):
    """提供遊戲提示"""
    hints = []
    
    # 奇偶性提示
    if secret_number % 2 == 0:
        hints.append("是偶數")
    else:
        hints.append("是奇數")
    
    # 範圍提示
    if secret_number <= 10:
        hints.append("≤ 10")
    elif secret_number <= 50:
        hints.append("≤ 50")
    elif secret_number <= 100:
        hints.append("≤ 100")
    else:
        hints.append("> 100")
    
    # 能否被5整除
    if secret_number % 5 == 0:
        hints.append("能被5整除")
    
    # 數字位數
    if secret_number < 10:
        hints.append("個位數")
    elif secret_number < 100:
        hints.append("兩位數")
    else:
        hints.append("三位數")
    
    print("💡 提示：答案", "、".join(hints[:2]))  # 只給前兩個提示

def calculate_score(attempts, max_attempts, difficulty):
    """計算得分"""
    if attempts == 1:
        return 1000 * difficulty  # 一次猜中超高分
    
    remaining_ratio = (max_attempts - attempts) / max_attempts
    base_score = 100 * difficulty
    bonus = base_score * remaining_ratio
    
    return int(base_score + bonus)

def guessing_game():
    """主要遊戲函數"""
    display_welcome()
    
    # 遊戲統計
    total_games = 0
    total_wins = 0
    best_score = 0
    
    while True:
        # 設定遊戲
        min_num, max_num, max_attempts, difficulty_name = get_difficulty()
        secret_number = random.randint(min_num, max_num)
        
        print(f"\n🎲 遊戲開始！【{difficulty_name}模式】")
        print(f"我想了一個{min_num}到{max_num}之間的數字")
        print(f"你有{max_attempts}次機會猜中它")
        print("💡 輸入 'h' 獲取提示，'q' 退出遊戲")
        
        # 遊戲變數
        attempts = 0
        guessed_numbers = []
        hints_used = 0
        
        # 主要遊戲迴圈
        while attempts < max_attempts:
            remaining = max_attempts - attempts
            print(f"\n⏰ 剩餘機會：{remaining}")
            
            if guessed_numbers:
                print(f"📝 已猜過：{sorted(guessed_numbers)}")
            
            # 取得玩家輸入
            guess = get_valid_guess(min_num, max_num, guessed_numbers)
            
            if guess == 'quit':
                print(f"🏳️ 遊戲結束！答案是：{secret_number}")
                break
            elif guess == 'hint':
                if hints_used < 2:
                    give_hint(secret_number, guessed_numbers)
                    hints_used += 1
                    print(f"💡 剩餘提示次數：{2 - hints_used}")
                else:
                    print("❌ 你已經用完所有提示了！")
                continue
            
            # 處理數字猜測
            attempts += 1
            guessed_numbers.append(guess)
            
            if guess == secret_number:
                # 猜中了！
                print("🎊" + "="*30 + "🎊")
                print("🎉 恭喜！你猜中了！ 🎉")
                print(f"🎯 答案：{secret_number}")
                print(f"🎮 嘗試次數：{attempts}")
                
                # 計算得分
                difficulty_multiplier = {"簡單": 1, "中等": 2, "困難": 3, "地獄": 4}[difficulty_name]
                score = calculate_score(attempts, max_attempts, difficulty_multiplier)
                if hints_used > 0:
                    score = score // 2  # 使用提示扣分
                
                print(f"⭐ 得分：{score}")
                
                if score > best_score:
                    best_score = score
                    print("🏆 新的最高分紀錄！")
                
                total_wins += 1
                print("🎊" + "="*30 + "🎊")
                break
                
            else:
                # 給出提示
                if guess < secret_number:
                    difference = secret_number - guess
                    if difference <= 5:
                        print("📈 很接近了！再大一點點")
                    elif difference <= 15:
                        print("📈 太小了！再大一些")
                    else:
                        print("📈 太小了！還差很多")
                else:
                    difference = guess - secret_number
                    if difference <= 5:
                        print("📉 很接近了！再小一點點")
                    elif difference <= 15:
                        print("📉 太大了！再小一些")
                    else:
                        print("📉 太大了！還差很多")
        
        else:
            # while迴圈正常結束（沒有break）
            print("😢" + "="*30 + "😢")
            print("💔 很遺憾！你用完了所有機會")
            print(f"🎯 答案是：{secret_number}")
            print("😢" + "="*30 + "😢")
        
        # 更新統計
        total_games += 1
        
        # 顯示統計資料
        print(f"\n📊 遊戲統計")
        print(f"總遊戲次數：{total_games}")
        print(f"獲勝次數：{total_wins}")
        if total_games > 0:
            win_rate = (total_wins / total_games) * 100
            print(f"勝率：{win_rate:.1f}%")
        if best_score > 0:
            print(f"最高分：{best_score}")
        
        # 詢問是否再玩一次
        while True:
            play_again = input("\n🔄 要再玩一次嗎？(y/n): ").lower().strip()
            if play_again in ['y', 'yes', '是']:
                break
            elif play_again in ['n', 'no', '否']:
                print("👋 感謝遊玩！希望你玩得開心！")
                return
            else:
                print("請輸入 y 或 n")

# 執行遊戲
if __name__ == "__main__":
    try:
        guessing_game()
    except KeyboardInterrupt:
        print("\n\n👋 遊戲被中斷，再見！")