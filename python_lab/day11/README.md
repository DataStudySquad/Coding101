# Day 11：清單進階操作

## 今日學習目標
- 掌握清單切片（Slicing）技術
- 學會清單推導式（List Comprehension）
- 理解多維清單的概念
- 實作成績統計分析程式

## 1. 清單切片（Slicing）

### 什麼是切片？
想像清單是一條吐司麵包，切片就是**把麵包切成你想要的部分**：
- 可以切前幾片
- 可以切中間幾片
- 可以切後幾片
- 甚至可以間隔著切

### 基本切片語法
```python
list[開始:結束:步進]
```

### 基本範例
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0  1  2  3  4  5  6  7  8  9   (正向索引)
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1   (反向索引)

print(numbers[2:5])    # [2, 3, 4] (從索引2到4)
print(numbers[2:])     # [2, 3, 4, 5, 6, 7, 8, 9] (從索引2到最後)
print(numbers[:5])     # [0, 1, 2, 3, 4] (從開頭到索引4)
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (整個清單)
```

### 使用步進
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[::2])    # [0, 2, 4, 6, 8] (每隔一個取一個)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (從索引1開始，每隔一個)
print(numbers[2:8:2])  # [2, 4, 6] (從索引2到7，每隔一個)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (反向)
```

### 負數索引切片
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[-3:])    # [7, 8, 9] (最後3個)
print(numbers[:-3])    # [0, 1, 2, 3, 4, 5, 6] (除了最後3個)
print(numbers[-5:-2])  # [5, 6, 7] (倒數第5到倒數第3)
```

## 2. 切片的實用應用

### 應用1：字串處理
```python
text = "Hello, World!"
print(text[7:])      # "World!"
print(text[:5])      # "Hello"
print(text[::2])     # "Hlo ol!"
print(text[::-1])    # "!dlroW ,olleH"
```

### 應用2：清單複製
```python
original = [1, 2, 3, 4, 5]
copy1 = original[:]         # 淺複製
copy2 = original.copy()     # 另一種方式
copy3 = list(original)      # 第三種方式

print(f"原清單：{original}")
print(f"複製1：{copy1}")
```

### 應用3：清單分割
```python
students = ["小明", "小美", "小華", "小強", "小雅", "小杰"]
first_half = students[:3]   # 前半部
second_half = students[3:]  # 後半部

print(f"前半組：{first_half}")
print(f"後半組：{second_half}")
```

### 應用4：取樣和過濾
```python
data = list(range(1, 21))   # [1, 2, 3, ..., 20]
every_third = data[::3]     # 每三個取一個
middle_portion = data[5:15] # 中間部分
last_five = data[-5:]       # 最後5個

print(f"每三個：{every_third}")
print(f"中間部分：{middle_portion}")
print(f"最後五個：{last_five}")
```

## 3. 清單推導式（List Comprehension）

### 什麼是清單推導式？
清單推導式是Python的**超能力**，可以用一行程式碼建立複雜的清單。

就像是「**告訴電腦你要什麼樣的清單，電腦立刻幫你做出來**」。

### 基本語法
```python
[表達式 for 項目 in 序列]
```

### 基本範例
```python
# 傳統方式：建立1-10的平方
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)

# 清單推導式：一行搞定
squares = [i ** 2 for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 帶條件的推導式
```python
# 語法：[表達式 for 項目 in 序列 if 條件]

# 只要1-20中的偶數
evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 只要1-10中能被3整除的數字的平方
divisible_by_3_squares = [i ** 2 for i in range(1, 11) if i % 3 == 0]
print(divisible_by_3_squares)  # [9, 36, 81]
```

### 字串處理的推導式
```python
words = ["hello", "world", "python", "programming"]

# 轉成大寫
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']

# 只要長度超過5的單字
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['python', 'programming']

# 每個單字的長度
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 5, 6, 11]
```

### 複雜的推導式
```python
# 建立座標點
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 乘法表
multiplication_table = [f"{i}x{j}={i*j}" for i in range(1, 4) for j in range(1, 4)]
print(multiplication_table)
# ['1x1=1', '1x2=2', '1x3=3', '2x1=2', '2x2=4', '2x3=6', '3x1=3', '3x2=6', '3x3=9']
```

## 4. 多維清單

### 什麼是多維清單？
想像清單裡面還有清單，就像是**盒子裡面還有小盒子**：

```python
# 一維清單（一排盒子）
simple_list = [1, 2, 3, 4, 5]

# 二維清單（像表格）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### 建立二維清單
```python
# 方法1：直接建立
grades = [
    ["小明", 85, 92, 78],
    ["小美", 96, 88, 91],
    ["小華", 79, 85, 83]
]

# 方法2：使用推導式
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 方法3：初始化零矩陣
rows, cols = 3, 4
zero_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(zero_matrix)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

### 存取二維清單
```python
grades = [
    ["小明", 85, 92, 78],
    ["小美", 96, 88, 91],
    ["小華", 79, 85, 83]
]

print(grades[0])        # ['小明', 85, 92, 78] (第一個學生)
print(grades[0][0])     # 小明 (第一個學生的名字)
print(grades[1][2])     # 91 (第二個學生的第二科成績)

# 修改資料
grades[2][1] = 90       # 修改小華的第一科成績
print(grades[2])        # ['小華', 90, 85, 83]
```

### 遍歷二維清單
```python
grades = [
    ["小明", 85, 92, 78],
    ["小美", 96, 88, 91],
    ["小華", 79, 85, 83]
]

# 方法1：雙重迴圈
for row in grades:
    for item in row:
        print(item, end=" ")
    print()  # 換行

# 方法2：帶索引的遍歷
for i, student in enumerate(grades):
    print(f"學生{i+1}：{student[0]}")
    for j, score in enumerate(student[1:], 1):
        print(f"  科目{j}：{score}")
```

## 5. 實用的清單操作技巧

### 技巧1：快速交換元素
```python
numbers = [1, 2, 3, 4, 5]
# 交換第0個和第4個元素
numbers[0], numbers[4] = numbers[4], numbers[0]
print(numbers)  # [5, 2, 3, 4, 1]
```

### 技巧2：清單去重
```python
# 保持原順序的去重
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

numbers = [1, 2, 3, 2, 4, 1, 5]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # [1, 2, 3, 4, 5]

# 使用set去重（不保證順序）
unique_set = list(set(numbers))
print(unique_set)
```

### 技巧3：清單扁平化
```python
# 將二維清單變成一維
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 方法1：傳統方式
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 方法2：推導式
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 技巧4：清單分組
```python
def chunk_list(lst, chunk_size):
    """將清單分成指定大小的子清單"""
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunked = chunk_list(numbers, 3)
print(chunked)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
```

## 6. 實作項目：成績統計分析程式

```python
def grade_analyzer():
    """完整的成績分析程式"""
    
    # 學生成績資料（二維清單）
    students_data = [
        ["小明", 85, 92, 78, 88, 91],
        ["小美", 96, 88, 91, 94, 89],
        ["小華", 79, 85, 83, 87, 82],
        ["小強", 88, 91, 85, 90, 87],
        ["小雅", 92, 87, 89, 85, 91]
    ]
    
    subjects = ["國文", "英文", "數學", "自然", "社會"]
    
    print("📊 學生成績統計分析系統")
    print("="*50)
    
    # 1. 顯示原始資料
    print("\n📋 原始成績資料：")
    print(f"{'姓名':<6} {'國文':<4} {'英文':<4} {'數學':<4} {'自然':<4} {'社會':<4} {'總分':<4} {'平均':<6}")
    print("-"*50)
    
    for student in students_data:
        name = student[0]
        scores = student[1:]
        total = sum(scores)
        average = total / len(scores)
        print(f"{name:<6} {scores[0]:<4} {scores[1]:<4} {scores[2]:<4} {scores[3]:<4} {scores[4]:<4} {total:<4} {average:<6.1f}")
    
    # 2. 計算每個學生的統計
    print("\n👨‍🎓 個人成績分析：")
    for student in students_data:
        name = student[0]
        scores = student[1:]
        
        total = sum(scores)
        average = total / len(scores)
        highest = max(scores)
        lowest = min(scores)
        
        # 找出最強和最弱科目
        best_subject = subjects[scores.index(highest)]
        worst_subject = subjects[scores.index(lowest)]
        
        print(f"\n{name}的成績分析：")
        print(f"  總分：{total} | 平均：{average:.1f}")
        print(f"  最高分：{highest}（{best_subject}） | 最低分：{lowest}（{worst_subject}）")
        print(f"  成績分佈：{scores}")
    
    # 3. 計算科目統計
    print("\n📚 科目成績分析：")
    for i, subject in enumerate(subjects):
        # 使用清單推導式提取該科目所有學生的成績
        subject_scores = [student[i+1] for student in students_data]
        
        avg_score = sum(subject_scores) / len(subject_scores)
        max_score = max(subject_scores)
        min_score = min(subject_scores)
        
        # 找出該科目最高分的學生
        max_student_index = subject_scores.index(max_score)
        max_student_name = students_data[max_student_index][0]
        
        print(f"\n{subject}：")
        print(f"  平均分：{avg_score:.1f}")
        print(f"  最高分：{max_score}（{max_student_name}）")
        print(f"  最低分：{min_score}")
        print(f"  成績分佈：{sorted(subject_scores, reverse=True)}")
    
    # 4. 排名分析
    print("\n🏆 學生排名：")
    
    # 計算總分並排序
    student_totals = []
    for student in students_data:
        name = student[0]
        total = sum(student[1:])
        average = total / len(student[1:])
        student_totals.append((name, total, average))
    
    # 按總分排序
    student_totals.sort(key=lambda x: x[1], reverse=True)
    
    print("按總分排名：")
    for rank, (name, total, average) in enumerate(student_totals, 1):
        print(f"  第{rank}名：{name:<6} 總分{total} 平均{average:.1f}")
    
    # 5. 等第分析
    print("\n📈 等第分析：")
    all_scores = []
    for student in students_data:
        all_scores.extend(student[1:])  # 將所有成績加入清單
    
    excellent = [score for score in all_scores if score >= 90]
    good = [score for score in all_scores if 80 <= score < 90]
    fair = [score for score in all_scores if 70 <= score < 80]
    poor = [score for score in all_scores if score < 70]
    
    total_scores = len(all_scores)
    print(f"總成績數：{total_scores}")
    print(f"優秀（90+）：{len(excellent)} 項（{len(excellent)/total_scores*100:.1f}%）")
    print(f"良好（80-89）：{len(good)} 項（{len(good)/total_scores*100:.1f}%）")
    print(f"普通（70-79）：{len(fair)} 項（{len(fair)/total_scores*100:.1f}%）")
    print(f"待加強（<70）：{len(poor)} 項（{len(poor)/total_scores*100:.1f}%）")
    
    # 6. 進階分析
    print("\n🔍 進階分析：")
    
    # 找出進步空間最大的學生
    improvement_potential = []
    for student in students_data:
        name = student[0]
        scores = student[1:]
        highest = max(scores)
        lowest = min(scores)
        potential = highest - lowest
        improvement_potential.append((name, potential, lowest, highest))
    
    improvement_potential.sort(key=lambda x: x[1], reverse=True)
    top_potential = improvement_potential[0]
    
    print(f"最有進步潛力：{top_potential[0]}（分差{top_potential[1]}分）")
    print(f"  最低分：{top_potential[2]} | 最高分：{top_potential[3]}")
    
    # 找出最穩定的學生（分數差異最小）
    most_stable = min(improvement_potential, key=lambda x: x[1])
    print(f"成績最穩定：{most_stable[0]}（分差僅{most_stable[1]}分）")

# 執行分析
if __name__ == "__main__":
    grade_analyzer()
```

## 7. 今日總結

今天你學會了：
- ✅ 清單切片的各種用法
- ✅ 清單推導式的強大功能
- ✅ 多維清單的概念和操作
- ✅ 各種清單處理技巧
- ✅ 製作完整的成績分析程式

## 8. 明日預告

明天我們將學習：
- 字典（Dictionary）的概念
- 鍵值對的使用方法
- 字典的常用操作
- 製作通訊錄程式

## 9. 作業練習

1. 使用切片操作處理一個長字串
2. 用推導式建立一個複雜的數字清單
3. 建立一個二維清單來表示課程表
4. 實作一個簡單的資料分析功能

記住：**掌握清單的進階操作，是成為Python高手的重要一步！**