# Day 14: 第二週複習練習
# 整合第二週所有學習內容的綜合練習

print("=== Day 14: 第二週複習練習 ===\n")

# 練習1：迴圈綜合應用
print("練習1：迴圈綜合應用")
print("使用for和while迴圈解決不同問題")

# for迴圈：九九乘法表
print("\n📊 九九乘法表（for迴圈）：")
for i in range(1, 4):
    print(f"{i}的乘法：", end="")
    for j in range(1, 10):
        print(f"{i}×{j}={i*j:2d}", end="  ")
    print()

# while迴圈：猜數字遊戲簡化版
print(f"\n🎯 猜數字遊戲（while迴圈）：")
import random
secret = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("我想了一個1-10的數字，你有3次機會")
while attempts < max_attempts:
    try:
        guess = int(input(f"第{attempts + 1}次猜測："))
        attempts += 1
        
        if guess == secret:
            print(f"🎉 恭喜！你猜對了！答案是{secret}")
            break
        elif guess < secret:
            print("太小了！")
        else:
            print("太大了！")
    except ValueError:
        print("請輸入數字！")
        attempts -= 1  # 無效輸入不計次數
else:
    print(f"💔 遊戲結束！答案是{secret}")

print("\n" + "="*50 + "\n")

# 練習2：清單操作綜合
print("練習2：清單操作綜合")
print("結合基礎操作、切片、推導式")

# 基礎清單操作
students = ["小明", "小美", "小華", "小強", "小雅"]
scores = [85, 92, 78, 96, 88]

print(f"學生清單：{students}")
print(f"成績清單：{scores}")

# 清單組合和處理
student_scores = list(zip(students, scores))
print(f"學生成績配對：{student_scores}")

# 清單切片應用
print(f"前三名學生：{students[:3]}")
print(f"後兩個成績：{scores[-2:]}")
print(f"每隔一個學生：{students[::2]}")

# 清單推導式
high_scores = [score for score in scores if score >= 90]
print(f"高分成績（≥90）：{high_scores}")

excellent_students = [name for name, score in student_scores if score >= 90]
print(f"優秀學生：{excellent_students}")

# 成績統計
print(f"\n📊 成績統計：")
print(f"總人數：{len(scores)}")
print(f"總分：{sum(scores)}")
print(f"平均分：{sum(scores) / len(scores):.1f}")
print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")

# 排名計算
ranked_students = sorted(student_scores, key=lambda x: x[1], reverse=True)
print(f"成績排名：")
for i, (name, score) in enumerate(ranked_students, 1):
    print(f"  第{i}名：{name} ({score}分)")

print("\n" + "="*50 + "\n")

# 練習3：字典應用綜合
print("練習3：字典應用綜合")
print("學生資料管理和統計分析")

# 建立學生資料庫
student_database = {
    "S001": {
        "name": "張小明",
        "age": 16,
        "class": "一年一班",
        "subjects": {"國文": 85, "英文": 92, "數學": 78},
        "activities": ["籃球社", "學生會"]
    },
    "S002": {
        "name": "李小美", 
        "age": 16,
        "class": "一年一班",
        "subjects": {"國文": 92, "英文": 88, "數學": 94},
        "activities": ["合唱團", "志工社"]
    },
    "S003": {
        "name": "王小華",
        "age": 17,
        "class": "二年二班", 
        "subjects": {"國文": 78, "英文": 85, "數學": 82},
        "activities": ["資訊社"]
    }
}

print("🎓 學生資料庫")
print("-" * 60)
for student_id, info in student_database.items():
    name = info["name"]
    class_name = info["class"]
    avg_score = sum(info["subjects"].values()) / len(info["subjects"])
    activities = ", ".join(info["activities"])
    
    print(f"{student_id}: {name} ({class_name}) 平均:{avg_score:.1f} 社團:[{activities}]")

# 資料統計分析
print(f"\n📊 統計分析：")

# 年齡分布
age_distribution = {}
for info in student_database.values():
    age = info["age"]
    age_distribution[age] = age_distribution.get(age, 0) + 1

print(f"年齡分布：")
for age, count in age_distribution.items():
    print(f"  {age}歲：{count}人")

# 班級分布
class_distribution = {}
for info in student_database.values():
    class_name = info["class"]
    class_distribution[class_name] = class_distribution.get(class_name, 0) + 1

print(f"班級分布：")
for class_name, count in class_distribution.items():
    print(f"  {class_name}：{count}人")

# 科目平均成績
subject_totals = {}
subject_counts = {}
for info in student_database.values():
    for subject, score in info["subjects"].items():
        subject_totals[subject] = subject_totals.get(subject, 0) + score
        subject_counts[subject] = subject_counts.get(subject, 0) + 1

print(f"各科平均成績：")
for subject in subject_totals:
    avg = subject_totals[subject] / subject_counts[subject]
    print(f"  {subject}：{avg:.1f}")

# 社團參與統計
activity_participation = {}
for info in student_database.values():
    for activity in info["activities"]:
        activity_participation[activity] = activity_participation.get(activity, 0) + 1

print(f"社團參與統計：")
for activity, count in activity_participation.items():
    print(f"  {activity}：{count}人")

print("\n" + "="*50 + "\n")

# 練習4：元組應用綜合
print("練習4：元組應用綜合")
print("座標系統和不可變資料處理")

# 座標點資料（使用元組確保不被修改）
coordinate_points = (
    ("原點", (0, 0)),
    ("A", (3, 4)),
    ("B", (-2, 1)),
    ("C", (5, -3)),
    ("D", (1, 2))
)

print("📍 座標點資料：")
for name, (x, y) in coordinate_points:
    # 計算距離原點的距離
    distance = (x ** 2 + y ** 2) ** 0.5
    # 判斷象限
    if x > 0 and y > 0:
        quadrant = "第一象限"
    elif x < 0 and y > 0:
        quadrant = "第二象限"
    elif x < 0 and y < 0:
        quadrant = "第三象限"
    elif x > 0 and y < 0:
        quadrant = "第四象限"
    else:
        quadrant = "軸上"
    
    print(f"  {name}: ({x:>3}, {y:>3}) 距原點:{distance:>5.2f} {quadrant}")

# 計算點對距離
print(f"\n📏 點對距離計算：")
import math
for i in range(len(coordinate_points)):
    for j in range(i + 1, len(coordinate_points)):
        name1, (x1, y1) = coordinate_points[i]
        name2, (x2, y2) = coordinate_points[j]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(f"  {name1} 到 {name2}: {distance:.2f}")

# 學生成績元組（不可變成績記錄）
grade_records = (
    ("小明", ("2024-01", (85, 92, 78, 88, 91))),
    ("小美", ("2024-01", (96, 88, 91, 94, 89))),
    ("小華", ("2024-01", (79, 85, 83, 87, 82)))
)

subjects = ("國文", "英文", "數學", "自然", "社會")

print(f"\n📚 成績記錄（不可變）：")
for name, (period, grades) in grade_records:
    total = sum(grades)
    average = total / len(grades)
    print(f"{name} ({period}): 總分{total} 平均{average:.1f}")
    
    # 解包成績顯示各科
    chinese, english, math, science, social = grades
    print(f"  各科: 國文{chinese} 英文{english} 數學{math} 自然{science} 社會{social}")

print("\n" + "="*50 + "\n")

# 練習5：資料結構組合應用
print("練習5：資料結構組合應用")
print("多層資料結構的綜合運用")

# 複雜的學校資料結構
school_data = {
    "school_name": "Python高中",
    "principal": "陳校長",
    "classes": {
        "一年一班": {
            "teacher": "王老師",
            "students": [
                {
                    "name": "小明",
                    "grades": {"國文": [85, 88, 92], "數學": [78, 82, 85]},
                    "activities": ("籃球社", "學生會")
                },
                {
                    "name": "小美", 
                    "grades": {"國文": [92, 89, 94], "數學": [88, 91, 87]},
                    "activities": ("合唱團", "志工社")
                }
            ]
        },
        "二年一班": {
            "teacher": "李老師",
            "students": [
                {
                    "name": "小華",
                    "grades": {"國文": [79, 83, 86], "數學": [85, 88, 82]},
                    "activities": ("資訊社",)
                }
            ]
        }
    }
}

print(f"🏫 {school_data['school_name']} 資料分析")
print(f"校長：{school_data['principal']}")
print("-" * 50)

total_students = 0
all_grades = []
all_activities = []

# 遍歷所有班級和學生
for class_name, class_info in school_data["classes"].items():
    print(f"\n📚 {class_name} (導師: {class_info['teacher']})")
    students = class_info["students"]
    total_students += len(students)
    
    for student in students:
        name = student["name"]
        
        # 計算學生總平均
        student_total = 0
        student_count = 0
        for subject, scores in student["grades"].items():
            subject_avg = sum(scores) / len(scores)
            student_total += subject_avg
            student_count += 1
            all_grades.extend(scores)  # 收集所有成績
        
        student_avg = student_total / student_count
        activities = ", ".join(student["activities"])
        
        print(f"  👤 {name}: 平均{student_avg:.1f} 社團:[{activities}]")
        
        # 收集社團資料
        all_activities.extend(student["activities"])

# 全校統計
print(f"\n🎯 全校統計:")
print(f"總學生數: {total_students}")
print(f"平均成績: {sum(all_grades) / len(all_grades):.1f}")
print(f"最高成績: {max(all_grades)}")
print(f"最低成績: {min(all_grades)}")

# 社團統計
activity_count = {}
for activity in all_activities:
    activity_count[activity] = activity_count.get(activity, 0) + 1

print(f"\n🎭 社團參與統計:")
for activity, count in sorted(activity_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {activity}: {count}人")

print("\n" + "="*50 + "\n")

# 練習6：綜合問題解決
print("練習6：綜合問題解決")
print("模擬實際應用場景的問題解決")

# 問題：圖書館管理系統簡化版
library_books = [
    {"id": "B001", "title": "Python程式設計", "author": "張三", "category": "程式設計", "borrowed": False},
    {"id": "B002", "title": "資料結構", "author": "李四", "category": "電腦科學", "borrowed": True},
    {"id": "B003", "title": "演算法導論", "author": "王五", "category": "電腦科學", "borrowed": False},
    {"id": "B004", "title": "機器學習", "author": "趙六", "category": "AI", "borrowed": True},
    {"id": "B005", "title": "深度學習", "author": "錢七", "category": "AI", "borrowed": False}
]

# 借閱記錄（使用元組確保記錄不被修改）
borrow_records = (
    ("2024-01-15", "B002", "小明", "借出"),
    ("2024-01-18", "B004", "小美", "借出"),
    ("2024-01-20", "B001", "小華", "借出"),
    ("2024-01-20", "B001", "小華", "歸還")
)

print("📚 圖書館管理系統")
print("-" * 40)

# 統計圖書狀態
available_books = [book for book in library_books if not book["borrowed"]]
borrowed_books = [book for book in library_books if book["borrowed"]]

print(f"📖 可借閱圖書 ({len(available_books)}本):")
for book in available_books:
    print(f"  {book['id']}: {book['title']} - {book['author']} ({book['category']})")

print(f"\n📕 已借出圖書 ({len(borrowed_books)}本):")
for book in borrowed_books:
    print(f"  {book['id']}: {book['title']} - {book['author']} ({book['category']})")

# 分類統計
category_stats = {}
for book in library_books:
    category = book["category"]
    if category not in category_stats:
        category_stats[category] = {"total": 0, "available": 0, "borrowed": 0}
    
    category_stats[category]["total"] += 1
    if book["borrowed"]:
        category_stats[category]["borrowed"] += 1
    else:
        category_stats[category]["available"] += 1

print(f"\n📊 分類統計:")
for category, stats in category_stats.items():
    print(f"  {category}: 總共{stats['total']}本, 可借{stats['available']}本, 已借{stats['borrowed']}本")

# 借閱歷史分析
print(f"\n📋 借閱歷史:")
borrower_stats = {}
for date, book_id, borrower, action in borrow_records:
    if borrower not in borrower_stats:
        borrower_stats[borrower] = {"borrow": 0, "return": 0}
    
    if action == "借出":
        borrower_stats[borrower]["borrow"] += 1
    elif action == "歸還":
        borrower_stats[borrower]["return"] += 1
    
    # 找出書名
    book_title = "未知"
    for book in library_books:
        if book["id"] == book_id:
            book_title = book["title"]
            break
    
    print(f"  {date}: {borrower} {action} 《{book_title}》")

print(f"\n👥 借閱者統計:")
for borrower, stats in borrower_stats.items():
    print(f"  {borrower}: 借出{stats['borrow']}次, 歸還{stats['return']}次")

print("\n" + "="*50 + "\n")

# 練習7：效能比較和最佳實務
print("練習7：效能比較和最佳實務")
print("不同資料結構和演算法的效能比較")

import time

# 準備測試資料
test_data = list(range(1000))
search_targets = [100, 500, 900]

print("🔍 搜尋效能比較 (1000筆資料):")

# 清單搜尋 vs 字典搜尋
print("\n清單 vs 字典搜尋效能:")

# 清單搜尋
list_search_times = []
for target in search_targets:
    start_time = time.time()
    result = target in test_data
    end_time = time.time()
    search_time = (end_time - start_time) * 1000  # 轉為毫秒
    list_search_times.append(search_time)
    print(f"  清單搜尋 {target}: {search_time:.4f}ms")

# 字典搜尋（將清單轉為字典）
test_dict = {value: True for value in test_data}
dict_search_times = []
for target in search_targets:
    start_time = time.time()
    result = target in test_dict
    end_time = time.time()
    search_time = (end_time - start_time) * 1000
    dict_search_times.append(search_time)
    print(f"  字典搜尋 {target}: {search_time:.4f}ms")

# 不同迴圈方式的效能比較
print(f"\n🔄 迴圈效能比較:")
test_list = list(range(10000))

# 傳統for迴圈
start_time = time.time()
result1 = []
for i in range(len(test_list)):
    if test_list[i] % 2 == 0:
        result1.append(test_list[i] ** 2)
time1 = (time.time() - start_time) * 1000

# for-in迴圈
start_time = time.time()
result2 = []
for item in test_list:
    if item % 2 == 0:
        result2.append(item ** 2)
time2 = (time.time() - start_time) * 1000

# 清單推導式
start_time = time.time()
result3 = [item ** 2 for item in test_list if item % 2 == 0]
time3 = (time.time() - start_time) * 1000

print(f"  傳統for迴圈: {time1:.4f}ms")
print(f"  for-in迴圈: {time2:.4f}ms")
print(f"  清單推導式: {time3:.4f}ms")

# 最佳實務建議
print(f"\n💡 最佳實務建議:")
print("1. 需要快速查找 → 使用字典")
print("2. 需要保持順序且可變 → 使用清單")
print("3. 需要不可變資料 → 使用元組")
print("4. 簡單的清單處理 → 使用推導式")
print("5. 複雜的邏輯處理 → 使用傳統迴圈")

print("\n程式執行完畢！")
print("\n🎉 恭喜完成第二週的所有學習內容！")
print("你已經掌握了：")
print("- ✅ for和while迴圈的使用")
print("- ✅ 清單的基礎和進階操作")
print("- ✅ 字典的應用和資料管理")
print("- ✅ 元組的特性和使用場景")
print("- ✅ 綜合資料結構的整合應用")
print("\n準備迎接第三週的挑戰吧！🚀")