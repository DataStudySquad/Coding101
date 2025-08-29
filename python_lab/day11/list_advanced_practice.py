# Day 11: 清單進階操作練習
# 這個檔案包含切片、推導式、多維清單的實用範例

print("=== Day 11: 清單進階操作練習 ===\n")

# 練習1：清單切片操作
print("練習1：清單切片操作")
numbers = list(range(0, 20))  # [0, 1, 2, ..., 19]
print(f"原始清單：{numbers}")

print(f"前5個元素：{numbers[:5]}")
print(f"後5個元素：{numbers[-5:]}")
print(f"中間10個元素：{numbers[5:15]}")
print(f"每隔2個取一個：{numbers[::2]}")
print(f"每隔3個取一個，從索引1開始：{numbers[1::3]}")
print(f"反向清單：{numbers[::-1]}")
print(f"反向每隔2個：{numbers[::-2]}")

# 字串切片
text = "Python Programming"
print(f"\n字串：{text}")
print(f"前6個字元：{text[:6]}")
print(f"後11個字元：{text[-11:]}")
print(f"每隔2個字元：{text[::2]}")
print(f"反向字串：{text[::-1]}")

print("\n" + "="*50 + "\n")

# 練習2：清單推導式基礎
print("練習2：清單推導式基礎")

# 基本推導式
squares = [x**2 for x in range(1, 11)]
print(f"1-10的平方：{squares}")

cubes = [x**3 for x in range(1, 6)]
print(f"1-5的立方：{cubes}")

# 帶條件的推導式
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"1-20的偶數：{evens}")

odds_squared = [x**2 for x in range(1, 11) if x % 2 == 1]
print(f"1-10奇數的平方：{odds_squared}")

# 字串處理推導式
words = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"原始單字：{words}")

upper_words = [word.upper() for word in words]
print(f"大寫單字：{upper_words}")

long_words = [word for word in words if len(word) > 5]
print(f"長度>5的單字：{long_words}")

word_lengths = [len(word) for word in words]
print(f"單字長度：{word_lengths}")

first_letters = [word[0] for word in words]
print(f"首字母：{first_letters}")

print("\n" + "="*50 + "\n")

# 練習3：進階推導式
print("練習3：進階推導式")

# 巢狀推導式
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("3x3乘法矩陣：")
for row in matrix:
    print(row)

# 座標生成
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"\n3x3座標點：{coordinates}")

# 條件表達式推導式
numbers = range(-5, 6)
abs_or_zero = [x if x >= 0 else -x for x in numbers]
print(f"絕對值轉換：{list(numbers)} -> {abs_or_zero}")

# 分類推導式
grades = [85, 92, 78, 96, 88, 74, 91, 83, 95, 79]
grade_categories = ["優秀" if g >= 90 else "良好" if g >= 80 else "普通" if g >= 70 else "待加強" for g in grades]
print(f"成績分類：")
for i, (grade, category) in enumerate(zip(grades, grade_categories)):
    print(f"  {grade}分 -> {category}")

print("\n" + "="*50 + "\n")

# 練習4：多維清單操作
print("練習4：多維清單操作")

# 建立學生成績表
students = [
    ["小明", "男", 85, 92, 78],
    ["小美", "女", 96, 88, 91],
    ["小華", "男", 79, 85, 83],
    ["小雅", "女", 92, 87, 89],
    ["小強", "男", 88, 91, 85]
]

subjects = ["國文", "英文", "數學"]

print("📊 學生成績表：")
print(f"{'姓名':<6} {'性別':<4} {'國文':<4} {'英文':<4} {'數學':<4} {'總分':<4} {'平均':<6}")
print("-" * 45)

for student in students:
    name, gender = student[0], student[1]
    scores = student[2:]
    total = sum(scores)
    average = total / len(scores)
    print(f"{name:<6} {gender:<4} {scores[0]:<4} {scores[1]:<4} {scores[2]:<4} {total:<4} {average:<6.1f}")

# 科目統計
print(f"\n📚 各科目統計：")
for i, subject in enumerate(subjects):
    subject_scores = [student[i+2] for student in students]
    avg = sum(subject_scores) / len(subject_scores)
    max_score = max(subject_scores)
    min_score = min(subject_scores)
    
    print(f"{subject}：平均{avg:.1f}，最高{max_score}，最低{min_score}")

# 性別統計
print(f"\n👥 性別統計：")
male_students = [s for s in students if s[1] == "男"]
female_students = [s for s in students if s[1] == "女"]

male_avg = sum([sum(s[2:]) for s in male_students]) / (len(male_students) * 3)
female_avg = sum([sum(s[2:]) for s in female_students]) / (len(female_students) * 3)

print(f"男學生：{len(male_students)}人，平均成績{male_avg:.1f}")
print(f"女學生：{len(female_students)}人，平均成績{female_avg:.1f}")

print("\n" + "="*50 + "\n")

# 練習5：資料處理綜合應用
print("練習5：資料處理綜合應用")

# 模擬銷售數據（產品名稱、類別、價格、銷量）
sales_data = [
    ["iPhone 14", "手機", 30000, 150],
    ["iPad Air", "平板", 18000, 89],
    ["MacBook Pro", "筆電", 60000, 45],
    ["AirPods", "耳機", 6000, 200],
    ["Apple Watch", "手錶", 12000, 120],
    ["Mac Studio", "電腦", 80000, 25],
    ["iPhone SE", "手機", 15000, 95],
    ["iPad Pro", "平板", 35000, 60]
]

print("💰 銷售數據分析：")
print(f"{'產品名稱':<15} {'類別':<6} {'價格':<8} {'銷量':<6} {'營收':<10}")
print("-" * 55)

total_revenue = 0
for product in sales_data:
    name, category, price, quantity = product
    revenue = price * quantity
    total_revenue += revenue
    print(f"{name:<15} {category:<6} ${price:<7,} {quantity:<6} ${revenue:<9,}")

print(f"\n總營收：${total_revenue:,}")

# 類別分析
categories = list(set([product[1] for product in sales_data]))
print(f"\n📊 類別分析：")
for category in categories:
    category_products = [p for p in sales_data if p[1] == category]
    category_revenue = sum([p[2] * p[3] for p in category_products])
    category_quantity = sum([p[3] for p in category_products])
    
    print(f"{category}：{len(category_products)}項產品，營收${category_revenue:,}，銷量{category_quantity}")

# 找出最佳銷售
best_revenue_product = max(sales_data, key=lambda x: x[2] * x[3])
best_quantity_product = max(sales_data, key=lambda x: x[3])

print(f"\n🏆 最佳表現：")
print(f"最高營收：{best_revenue_product[0]}（${best_revenue_product[2] * best_revenue_product[3]:,}）")
print(f"最高銷量：{best_quantity_product[0]}（{best_quantity_product[3]}件）")

# 價格區間分析
high_end = [p for p in sales_data if p[2] >= 30000]
mid_range = [p for p in sales_data if 10000 <= p[2] < 30000]
budget = [p for p in sales_data if p[2] < 10000]

print(f"\n💎 價格區間分析：")
print(f"高端產品（≥3萬）：{len(high_end)}項")
print(f"中端產品（1-3萬）：{len(mid_range)}項")
print(f"平價產品（<1萬）：{len(budget)}項")

print("\n" + "="*50 + "\n")

# 練習6：文字分析進階
print("練習6：文字分析進階")

text = """
Python是一種高階程式語言，由Guido van Rossum在1989年發明。
Python的設計哲學強調程式碼的可讀性和簡潔的語法。
Python支援多種程式設計範式，包括物件導向、命令式、函數式和程序式編程。
Python擁有動態型別系統和垃圾回收功能。
"""

# 清理文字
text = text.replace("\n", " ").strip()
print(f"原文：{text[:100]}...")

# 分割成句子
sentences = [s.strip() for s in text.split("。") if s.strip()]
print(f"\n句子數量：{len(sentences)}")

# 分割成單字
words = []
for sentence in sentences:
    # 移除標點符號
    clean_sentence = sentence.replace("，", " ").replace("。", " ").replace("、", " ")
    words.extend(clean_sentence.split())

print(f"總單字數：{len(words)}")

# 找出包含"Python"的句子
python_sentences = [s for s in sentences if "Python" in s]
print(f"提到Python的句子：{len(python_sentences)}句")
for i, sentence in enumerate(python_sentences, 1):
    print(f"  {i}. {sentence}。")

# 統計單字頻率（簡化版）
word_freq = {}
for word in words:
    if len(word) > 1:  # 只計算長度>1的字
        word_freq[word] = word_freq.get(word, 0) + 1

# 找出最常出現的前5個單字
frequent_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
print(f"\n🔤 最常出現的單字：")
for word, count in frequent_words:
    print(f"  {word}：{count}次")

print("\n" + "="*50 + "\n")

# 練習7：互動式矩陣操作
print("練習7：互動式矩陣操作")

def create_matrix():
    """建立矩陣"""
    try:
        rows = int(input("請輸入矩陣行數："))
        cols = int(input("請輸入矩陣列數："))
        
        print("請選擇矩陣類型：")
        print("1. 零矩陣")
        print("2. 單位矩陣")
        print("3. 隨機數字矩陣")
        print("4. 自定義輸入")
        
        choice = input("選擇 (1-4): ").strip()
        
        if choice == "1":
            matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        elif choice == "2" and rows == cols:
            matrix = [[1 if i == j else 0 for j in range(cols)] for i in range(rows)]
        elif choice == "3":
            import random
            matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
        elif choice == "4":
            matrix = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    value = int(input(f"輸入位置({i+1},{j+1})的值："))
                    row.append(value)
                matrix.append(row)
        else:
            print("無效選擇或矩陣不是方陣，建立零矩陣")
            matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        
        return matrix
    except ValueError:
        print("輸入錯誤，建立2x2零矩陣")
        return [[0, 0], [0, 0]]

def display_matrix(matrix, title="矩陣"):
    """顯示矩陣"""
    print(f"\n{title}：")
    for row in matrix:
        print("  ", end="")
        for item in row:
            print(f"{item:4}", end="")
        print()

# 建立示例矩陣
sample_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
display_matrix(sample_matrix, "示例3x3矩陣")

# 矩陣操作示例
print("\n🔢 矩陣操作示例：")

# 轉置矩陣
transposed = [[sample_matrix[j][i] for j in range(len(sample_matrix))] for i in range(len(sample_matrix[0]))]
display_matrix(transposed, "轉置矩陣")

# 每個元素乘以2
doubled = [[item * 2 for item in row] for row in sample_matrix]
display_matrix(doubled, "每元素乘2")

# 對角線元素
diagonal = [sample_matrix[i][i] for i in range(len(sample_matrix))]
print(f"\n對角線元素：{diagonal}")

# 邊框元素
border_elements = []
rows, cols = len(sample_matrix), len(sample_matrix[0])
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            border_elements.append(sample_matrix[i][j])
print(f"邊框元素：{border_elements}")

print("\n程式執行完畢！")