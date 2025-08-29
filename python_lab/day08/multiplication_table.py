# 九九乘法表程式
# 這是Day 8的主要實作項目

print("🔢 九九乘法表生成器 🔢")
print("=" * 50)

def print_single_table(num):
    """印出單一數字的乘法表"""
    print(f"\n📊 {num} 的乘法表：")
    print("-" * 20)
    for i in range(1, 10):
        result = num * i
        print(f"{num} × {i} = {result:2d}")

def print_full_table():
    """印出完整的九九乘法表"""
    print("\n📚 完整九九乘法表：")
    print("=" * 70)
    
    # 表頭
    print("   ", end="")
    for i in range(1, 10):
        print(f" {i:2d} ", end="")
    print("\n" + "=" * 70)
    
    # 乘法表內容
    for i in range(1, 10):
        print(f"{i} |", end="")
        for j in range(1, 10):
            result = i * j
            print(f" {result:2d} ", end="")
        print()  # 換行

def print_triangle_table():
    """印出三角形排列的乘法表"""
    print("\n🔺 三角形乘法表：")
    print("=" * 40)
    
    for i in range(1, 10):
        for j in range(1, i + 1):
            result = i * j
            print(f"{i}×{j}={result:2d}", end="  ")
        print()  # 每行結束換行

# 主程式
while True:
    print("\n請選擇要顯示的乘法表類型：")
    print("1. 單一數字乘法表")
    print("2. 完整九九乘法表")
    print("3. 三角形乘法表")
    print("4. 離開程式")
    
    choice = input("\n請輸入選項 (1-4): ")
    
    if choice == "1":
        try:
            num = int(input("請輸入要查看的數字 (1-9): "))
            if 1 <= num <= 9:
                print_single_table(num)
            else:
                print("請輸入1到9之間的數字！")
        except ValueError:
            print("請輸入有效的數字！")
    
    elif choice == "2":
        print_full_table()
    
    elif choice == "3":
        print_triangle_table()
    
    elif choice == "4":
        print("👋 感謝使用九九乘法表程式，再見！")
        break
    
    else:
        print("❌ 無效的選項，請重新選擇！")
    
    # 詢問是否繼續
    if choice in ["1", "2", "3"]:
        continue_choice = input("\n按Enter繼續，或輸入 'q' 離開: ")
        if continue_choice.lower() == 'q':
            print("👋 感謝使用九九乘法表程式，再見！")
            break

# 額外功能：乘法練習
print("\n🎯 想要練習乘法嗎？")
practice = input("輸入 'y' 開始練習，其他任意鍵跳過: ")

if practice.lower() == 'y':
    import random
    score = 0
    total_questions = 5
    
    print(f"\n開始乘法練習！共 {total_questions} 題")
    print("-" * 30)
    
    for question in range(1, total_questions + 1):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        correct_answer = num1 * num2
        
        try:
            user_answer = int(input(f"第{question}題: {num1} × {num2} = "))
            if user_answer == correct_answer:
                print("✅ 正確！")
                score += 1
            else:
                print(f"❌ 錯誤！正確答案是 {correct_answer}")
        except ValueError:
            print(f"❌ 請輸入數字！正確答案是 {correct_answer}")
    
    print(f"\n🏆 練習結束！")
    print(f"你答對了 {score}/{total_questions} 題")
    percentage = (score / total_questions) * 100
    print(f"正確率：{percentage:.1f}%")
    
    if percentage >= 80:
        print("🌟 太棒了！你已經熟練掌握乘法了！")
    elif percentage >= 60:
        print("👍 不錯！再多練習一下會更好！")
    else:
        print("💪 繼續努力，多練習乘法表吧！")