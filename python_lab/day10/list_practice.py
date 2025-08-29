# Day 10: 清單練習
# 這個檔案包含各種清單操作的實用範例

print("=== Day 10: 清單練習 ===\n")

# 練習1：基本清單操作
print("練習1：基本清單操作")
print("建立和操作水果清單")

fruits = ["蘋果", "香蕉", "橘子"]
print(f"原始清單：{fruits}")

# 新增元素
fruits.append("芒果")
print(f"新增芒果後：{fruits}")

fruits.insert(1, "草莓")
print(f"在位置1插入草莓：{fruits}")

# 修改元素
fruits[0] = "大蘋果"
print(f"修改第一個元素：{fruits}")

# 刪除元素
removed_fruit = fruits.pop(2)
print(f"移除位置2的元素({removed_fruit})：{fruits}")

print("\n" + "="*40 + "\n")

# 練習2：清單方法練習
print("練習2：清單方法練習")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"原始數字清單：{numbers}")

print(f"清單長度：{len(numbers)}")
print(f"最大值：{max(numbers)}")
print(f"最小值：{min(numbers)}")
print(f"總和：{sum(numbers)}")
print(f"平均值：{sum(numbers)/len(numbers):.2f}")

print(f"數字1出現次數：{numbers.count(1)}")
print(f"數字5的位置：{numbers.index(5)}")
print(f"數字7是否在清單中：{7 in numbers}")

# 排序
numbers_copy = numbers.copy()  # 複製一份
numbers_copy.sort()
print(f"升序排列：{numbers_copy}")

numbers_copy.sort(reverse=True)
print(f"降序排列：{numbers_copy}")

print("\n" + "="*40 + "\n")

# 練習3：學生成績管理
print("練習3：學生成績管理系統")
students = []
scores = []

# 模擬輸入學生資料
student_data = [
    ("小明", 85),
    ("小美", 92),
    ("小華", 78),
    ("小強", 96),
    ("小雅", 88)
]

for name, score in student_data:
    students.append(name)
    scores.append(score)

print(f"學生名單：{students}")
print(f"成績清單：{scores}")

# 成績分析
print(f"\n📊 成績統計：")
print(f"班級人數：{len(students)}人")
print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")
print(f"平均分：{sum(scores)/len(scores):.2f}")

# 找出最高分學生
max_score = max(scores)
top_student_index = scores.index(max_score)
print(f"最高分學生：{students[top_student_index]}（{max_score}分）")

# 成績排名
print(f"\n📈 成績排名：")
# 創建學生和成績的配對清單
student_score_pairs = []
for i in range(len(students)):
    student_score_pairs.append((students[i], scores[i]))

# 按成績排序
student_score_pairs.sort(key=lambda x: x[1], reverse=True)

for rank, (name, score) in enumerate(student_score_pairs, 1):
    print(f"第{rank}名：{name} - {score}分")

print("\n" + "="*40 + "\n")

# 練習4：購物清單管理
print("練習4：購物清單模擬")
shopping_list = []
prices = []

print("模擬購物過程...")

# 模擬添加商品
items_to_add = [
    ("牛奶", 45),
    ("麵包", 25),
    ("雞蛋", 60),
    ("蘋果", 80),
    ("香蕉", 30)
]

for item, price in items_to_add:
    shopping_list.append(item)
    prices.append(price)
    print(f"✅ 已加入：{item} - ${price}")

print(f"\n🛒 購物清單：")
total_cost = 0
for i in range(len(shopping_list)):
    print(f"{i+1}. {shopping_list[i]} - ${prices[i]}")
    total_cost += prices[i]

print(f"\n💰 總金額：${total_cost}")

# 移除最貴的商品
max_price = max(prices)
expensive_item_index = prices.index(max_price)
removed_item = shopping_list.pop(expensive_item_index)
removed_price = prices.pop(expensive_item_index)

print(f"❌ 移除最貴商品：{removed_item}（${removed_price}）")
print(f"💰 新總金額：${sum(prices)}")

print("\n" + "="*40 + "\n")

# 練習5：文字分析
print("練習5：文字分析")
text = "Python is a powerful programming language. Python is easy to learn."
print(f"原始文字：{text}")

# 將文字分割成單字清單
words = text.replace(".", "").replace(",", "").lower().split()
print(f"單字清單：{words}")
print(f"總單字數：{len(words)}")

# 統計每個單字出現次數
word_counts = {}
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)
        count = words.count(word)
        word_counts[word] = count

print(f"不重複單字：{unique_words}")
print(f"單字出現次數：")
for word in unique_words:
    count = words.count(word)
    print(f"  {word}: {count}次")

# 找出最常出現的單字
max_count = 0
most_common_word = ""
for word in unique_words:
    count = words.count(word)
    if count > max_count:
        max_count = count
        most_common_word = word

print(f"最常出現的單字：{most_common_word}（{max_count}次）")

print("\n" + "="*40 + "\n")

# 練習6：數字處理
print("練習6：數字清單處理")
numbers = list(range(1, 21))  # 1到20的數字
print(f"原始數字：{numbers}")

# 篩選偶數
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"偶數：{even_numbers}")

# 篩選奇數
odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)
print(f"奇數：{odd_numbers}")

# 計算平方
squares = []
for num in numbers[:10]:  # 只取前10個
    squares.append(num ** 2)
print(f"前10個數字的平方：{squares}")

# 篩選大於10的數字
greater_than_10 = []
for num in numbers:
    if num > 10:
        greater_than_10.append(num)
print(f"大於10的數字：{greater_than_10}")

print("\n" + "="*40 + "\n")

# 練習7：清單合併與分割
print("練習7：清單合併與分割")

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]

print(f"清單1：{list1}")
print(f"清單2：{list2}")
print(f"清單3：{list3}")

# 合併清單
combined = list1 + list2 + list3
print(f"合併後：{combined}")

# 使用extend
list1_copy = list1.copy()
list1_copy.extend(list2)
list1_copy.extend(list3)
print(f"使用extend合併：{list1_copy}")

# 分割清單
mid = len(combined) // 2
first_half = combined[:mid]
second_half = combined[mid:]
print(f"前半部：{first_half}")
print(f"後半部：{second_half}")

# 每3個一組
groups = []
for i in range(0, len(combined), 3):
    group = combined[i:i+3]
    groups.append(group)
print(f"每3個一組：{groups}")

print("\n" + "="*40 + "\n")

# 練習8：互動式清單操作
print("練習8：互動式數字清單")
my_numbers = []

print("請輸入一些數字（輸入0結束）：")
while True:
    try:
        num = int(input("輸入數字："))
        if num == 0:
            break
        my_numbers.append(num)
        print(f"目前清單：{my_numbers}")
    except ValueError:
        print("請輸入有效的數字！")

if my_numbers:
    print(f"\n🔢 最終清單：{my_numbers}")
    print(f"📊 統計資料：")
    print(f"  數量：{len(my_numbers)}")
    print(f"  最大值：{max(my_numbers)}")
    print(f"  最小值：{min(my_numbers)}")
    print(f"  總和：{sum(my_numbers)}")
    print(f"  平均值：{sum(my_numbers)/len(my_numbers):.2f}")
    
    # 排序選項
    sort_choice = input("\n要看排序結果嗎？(y/n): ").lower()
    if sort_choice == 'y':
        sorted_asc = sorted(my_numbers)
        sorted_desc = sorted(my_numbers, reverse=True)
        print(f"升序：{sorted_asc}")
        print(f"降序：{sorted_desc}")
else:
    print("沒有輸入任何數字")

print("\n程式執行完畢！")