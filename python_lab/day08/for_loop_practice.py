# Day 8: For迴圈練習
# 這個檔案包含各種for迴圈的實用範例

print("=== Day 8: For迴圈練習 ===\n")

# 練習1：基本for迴圈
print("練習1：印出你的名字5次")
name = input("請輸入你的名字：")
for i in range(5):
    print(f"第{i+1}次：{name}")

print("\n" + "="*30 + "\n")

# 練習2：計算總和
print("練習2：計算1到50的總和")
total = 0
for i in range(1, 51):
    total += i
print(f"1到50的總和：{total}")

print("\n" + "="*30 + "\n")

# 練習3：印出偶數
print("練習3：1到20的偶數")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

print("\n" + "="*30 + "\n")

# 練習4：圖案繪製
print("練習4：愛心圖案")
for i in range(1, 6):
    print("♥" * i)

print("\n" + "="*30 + "\n")

# 練習5：星星三角形
print("練習5：星星三角形")
for i in range(1, 6):
    spaces = " " * (5 - i)  # 前面的空格
    stars = "★" * i        # 星星
    print(spaces + stars)

print("\n" + "="*30 + "\n")

# 練習6：成績處理
print("練習6：成績統計")
scores = [85, 92, 78, 96, 88, 74, 91]
total_score = 0
count = 0

print("所有成績：", end="")
for score in scores:
    print(score, end=" ")
    total_score += score
    count += 1

average = total_score / count
print(f"\n平均成績：{average:.2f}")
print(f"總分：{total_score}")
print(f"科目數：{count}")

print("\n" + "="*30 + "\n")

# 練習7：尋找最大值和最小值
print("練習7：尋找最大值和最小值")
numbers = [45, 23, 89, 12, 67, 91, 34]
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"數字列表：{numbers}")
print(f"最大值：{max_num}")
print(f"最小值：{min_num}")

print("\n" + "="*30 + "\n")

# 練習8：倒數計時
print("練習8：倒數計時")
print("新年倒數計時開始！")
for i in range(10, 0, -1):
    print(f"倒數：{i}")
print("新年快樂！🎉")

print("\n" + "="*30 + "\n")

# 練習9：字串處理
print("練習9：字串分析")
text = "Hello Python Programming"
vowels = "aeiouAEIOU"
vowel_count = 0

print(f"分析文字：{text}")
print("每個字元：")
for i, char in enumerate(text):
    if char in vowels:
        print(f"位置{i}: '{char}' (母音)")
        vowel_count += 1
    else:
        print(f"位置{i}: '{char}'")

print(f"總共有 {vowel_count} 個母音")

print("\n" + "="*30 + "\n")

# 練習10：互動式選單
print("練習10：簡單計算機")
print("選擇運算：")
print("1. 加法表")
print("2. 乘法表") 
print("3. 數字平方表")

choice = input("請選擇 (1-3): ")

if choice == "1":
    print("加法表 (1-10):")
    for i in range(1, 11):
        result = i + 5  # 每個數字加5
        print(f"{i} + 5 = {result}")
elif choice == "2":
    print("乘法表 (1-10):")
    for i in range(1, 11):
        result = i * 3  # 每個數字乘3
        print(f"{i} × 3 = {result}")
elif choice == "3":
    print("數字平方表 (1-10):")
    for i in range(1, 11):
        result = i ** 2  # 每個數字的平方
        print(f"{i}² = {result}")
else:
    print("無效的選擇！")

print("\n程式執行完畢！")