# Day 12: 字典練習
# 這個檔案包含各種字典操作的實用範例

print("=== Day 12: 字典練習 ===\n")

# 練習1：基本字典操作
print("練習1：基本字典操作")
student = {
    "姓名": "小明",
    "年齡": 18,
    "科系": "資工系",
    "學號": "A001"
}

print(f"學生資料：{student}")
print(f"姓名：{student['姓名']}")
print(f"年齡：{student.get('年齡')}")
print(f"電話：{student.get('電話', '未提供')}")

# 新增和修改
student["電話"] = "0912-345-678"
student["年齡"] = 19
print(f"更新後：{student}")

# 檢查鍵是否存在
print(f"有電話資料：{'電話' in student}")
print(f"有地址資料：{'地址' in student}")

print("\n" + "="*50 + "\n")

# 練習2：字典方法練習
print("練習2：字典方法練習")
fruits = {
    "蘋果": 30,
    "香蕉": 25,
    "橘子": 35,
    "芒果": 45,
    "草莓": 80
}

print(f"水果價格表：{fruits}")
print(f"所有水果：{list(fruits.keys())}")
print(f"所有價格：{list(fruits.values())}")
print(f"鍵值對：{list(fruits.items())}")

# 價格分析
print(f"\n價格分析：")
print(f"最貴的水果價格：{max(fruits.values())}元")
print(f"最便宜的水果價格：{min(fruits.values())}元")
print(f"平均價格：{sum(fruits.values()) / len(fruits):.1f}元")

# 找出最貴的水果
most_expensive = max(fruits, key=fruits.get)
print(f"最貴的水果：{most_expensive}（{fruits[most_expensive]}元）")

# 價格篩選
expensive_fruits = {name: price for name, price in fruits.items() if price > 40}
print(f"高價水果（>40元）：{expensive_fruits}")

print("\n" + "="*50 + "\n")

# 練習3：字典計數應用
print("練習3：字典計數應用")
text = "Python是一種高階程式語言Python非常適合初學者學習程式設計"
print(f"原文：{text}")

# 字元計數
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print(f"\n字元統計（前10個）：")
sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
for char, count in sorted_chars[:10]:
    if char != ' ':  # 跳過空格
        print(f"'{char}'：{count}次")

# 詞語計數
words = text.replace("程式語言", " 程式語言 ").replace("程式設計", " 程式設計 ").split()
word_count = {}
for word in words:
    if len(word) > 1:  # 只計算長度>1的詞
        word_count[word] = word_count.get(word, 0) + 1

print(f"\n詞語統計：")
for word, count in word_count.items():
    print(f"{word}：{count}次")

print("\n" + "="*50 + "\n")

# 練習4：學生成績管理系統
print("練習4：學生成績管理系統")
class_grades = {
    "小明": {"國文": 85, "英文": 92, "數學": 78, "自然": 88},
    "小美": {"國文": 96, "英文": 88, "數學": 91, "自然": 94},
    "小華": {"國文": 79, "英文": 85, "數學": 83, "自然": 87},
    "小強": {"國文": 88, "英文": 91, "數學": 85, "自然": 90}
}

print("📊 班級成績總表")
print(f"{'姓名':<6} {'國文':<4} {'英文':<4} {'數學':<4} {'自然':<4} {'總分':<4} {'平均':<6}")
print("-" * 50)

student_totals = {}
for name, grades in class_grades.items():
    total = sum(grades.values())
    average = total / len(grades)
    student_totals[name] = total
    
    print(f"{name:<6} ", end="")
    for subject in ["國文", "英文", "數學", "自然"]:
        print(f"{grades[subject]:<4} ", end="")
    print(f"{total:<4} {average:<6.1f}")

# 科目統計
print(f"\n📚 各科平均分：")
subjects = ["國文", "英文", "數學", "自然"]
for subject in subjects:
    scores = [grades[subject] for grades in class_grades.values()]
    avg = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    print(f"{subject}：平均{avg:.1f}，最高{max_score}，最低{min_score}")

# 個人排名
print(f"\n🏆 總分排名：")
ranked_students = sorted(student_totals.items(), key=lambda x: x[1], reverse=True)
for rank, (name, total) in enumerate(ranked_students, 1):
    print(f"第{rank}名：{name}（{total}分）")

print("\n" + "="*50 + "\n")

# 練習5：商品庫存管理
print("練習5：商品庫存管理系統")
inventory = {
    "iPhone 14": {"價格": 30000, "庫存": 15, "類別": "手機"},
    "iPad Air": {"價格": 18000, "庫存": 8, "類別": "平板"},
    "MacBook Pro": {"價格": 60000, "庫存": 5, "類別": "筆電"},
    "AirPods": {"價格": 6000, "庫存": 25, "類別": "耳機"},
    "Apple Watch": {"價格": 12000, "庫存": 12, "類別": "手錶"}
}

print("📦 庫存管理系統")
print(f"{'商品名稱':<15} {'價格':<8} {'庫存':<6} {'類別':<6} {'庫存價值':<10}")
print("-" * 55)

total_value = 0
low_stock_items = []

for product, info in inventory.items():
    stock_value = info["價格"] * info["庫存"]
    total_value += stock_value
    
    print(f"{product:<15} ${info['價格']:<7,} {info['庫存']:<6} {info['類別']:<6} ${stock_value:<9,}")
    
    if info["庫存"] < 10:
        low_stock_items.append(product)

print(f"\n💰 總庫存價值：${total_value:,}")

if low_stock_items:
    print(f"\n⚠️  低庫存商品（<10件）：")
    for item in low_stock_items:
        print(f"  {item}：{inventory[item]['庫存']}件")

# 按類別分組
print(f"\n📊 按類別統計：")
categories = {}
for product, info in inventory.items():
    category = info["類別"]
    if category not in categories:
        categories[category] = {"數量": 0, "總價值": 0}
    categories[category]["數量"] += info["庫存"]
    categories[category]["總價值"] += info["價格"] * info["庫存"]

for category, stats in categories.items():
    print(f"{category}：{stats['數量']}件，價值${stats['總價值']:,}")

print("\n" + "="*50 + "\n")

# 練習6：巢狀字典操作
print("練習6：巢狀字典操作")
company = {
    "資訊部": {
        "經理": {"姓名": "張經理", "薪資": 80000, "年資": 5},
        "員工": {
            "小明": {"薪資": 45000, "年資": 2, "技能": ["Python", "Java"]},
            "小美": {"薪資": 50000, "年資": 3, "技能": ["JavaScript", "React"]},
            "小華": {"薪資": 42000, "年資": 1, "技能": ["Python", "Django"]}
        }
    },
    "行銷部": {
        "經理": {"姓名": "李經理", "薪資": 75000, "年資": 4},
        "員工": {
            "小強": {"薪資": 38000, "年資": 2, "技能": ["文案", "設計"]},
            "小雅": {"薪資": 40000, "年資": 3, "技能": ["社群", "廣告"]}
        }
    }
}

print("🏢 公司組織架構分析")

total_salary = 0
total_employees = 0
all_skills = {}

for dept_name, dept_info in company.items():
    print(f"\n📊 {dept_name}：")
    
    # 經理資訊
    manager = dept_info["經理"]
    print(f"  經理：{manager['姓名']}，薪資${manager['薪資']:,}，年資{manager['年資']}年")
    total_salary += manager["薪資"]
    total_employees += 1
    
    # 員工資訊
    employees = dept_info["員工"]
    dept_salary = manager["薪資"]
    
    print(f"  員工：")
    for emp_name, emp_info in employees.items():
        print(f"    {emp_name}：薪資${emp_info['薪資']:,}，年資{emp_info['年資']}年")
        print(f"      技能：{', '.join(emp_info['技能'])}")
        
        dept_salary += emp_info["薪資"]
        total_salary += emp_info["薪資"]
        total_employees += 1
        
        # 統計技能
        for skill in emp_info["技能"]:
            all_skills[skill] = all_skills.get(skill, 0) + 1
    
    print(f"  部門總薪資：${dept_salary:,}")
    print(f"  部門人數：{len(employees) + 1}人")

print(f"\n💼 公司總覽：")
print(f"總員工數：{total_employees}人")
print(f"總薪資支出：${total_salary:,}")
print(f"平均薪資：${total_salary // total_employees:,}")

print(f"\n🛠️ 技能統計：")
for skill, count in sorted(all_skills.items(), key=lambda x: x[1], reverse=True):
    print(f"{skill}：{count}人掌握")

print("\n" + "="*50 + "\n")

# 練習7：資料轉換與處理
print("練習7：資料轉換與處理")

# CSV格式資料轉字典
csv_data = """姓名,年齡,城市,職業
小明,25,台北,工程師
小美,28,台中,設計師
小華,22,高雄,學生
小強,30,台南,老師"""

print("📄 CSV資料轉換：")
lines = csv_data.strip().split('\n')
headers = lines[0].split(',')
people = []

for line in lines[1:]:
    values = line.split(',')
    person = {headers[i]: values[i] for i in range(len(headers))}
    people.append(person)

print(f"轉換後的資料：")
for person in people:
    print(f"  {person}")

# 按城市分組
print(f"\n🏙️ 按城市分組：")
by_city = {}
for person in people:
    city = person["城市"]
    if city not in by_city:
        by_city[city] = []
    by_city[city].append(person["姓名"])

for city, names in by_city.items():
    print(f"{city}：{', '.join(names)}")

# 年齡統計
ages = [int(person["年齡"]) for person in people]
print(f"\n👥 年齡統計：")
print(f"平均年齡：{sum(ages) / len(ages):.1f}歲")
print(f"最大年齡：{max(ages)}歲")
print(f"最小年齡：{min(ages)}歲")

print("\n" + "="*50 + "\n")

# 練習8：互動式字典操作
print("練習8：互動式餐廳菜單")
menu = {
    "主餐": {
        "牛肉麵": 120,
        "雞腿飯": 100,
        "魚香茄子": 90,
        "宮保雞丁": 110
    },
    "小食": {
        "滷蛋": 15,
        "豆干": 20,
        "海帶": 15,
        "小菜": 25
    },
    "飲品": {
        "紅茶": 25,
        "綠茶": 25,
        "咖啡": 35,
        "果汁": 40
    }
}

print("🍽️ 歡迎光臨Python餐廳！")
print("\n📋 今日菜單：")
for category, items in menu.items():
    print(f"\n【{category}】")
    for dish, price in items.items():
        print(f"  {dish}：${price}")

# 模擬點餐
order = {}
total_cost = 0

print(f"\n🛒 點餐系統（輸入菜名，輸入'結帳'完成）：")
while True:
    dish_name = input("請點餐：").strip()
    
    if dish_name == "結帳":
        break
    
    # 搜尋菜品
    found = False
    for category, items in menu.items():
        if dish_name in items:
            price = items[dish_name]
            order[dish_name] = order.get(dish_name, 0) + 1
            total_cost += price
            print(f"✅ 已加入：{dish_name} ${price} (共{order[dish_name]}份)")
            found = True
            break
    
    if not found:
        print("❌ 抱歉，沒有這道菜")

# 顯示訂單
if order:
    print(f"\n🧾 您的訂單：")
    print("-" * 30)
    for dish, quantity in order.items():
        # 找到價格
        price = 0
        for category, items in menu.items():
            if dish in items:
                price = items[dish]
                break
        
        subtotal = price * quantity
        print(f"{dish} x{quantity} = ${subtotal}")
    
    print("-" * 30)
    print(f"總計：${total_cost}")
    print("感謝光臨！")
else:
    print("沒有點餐項目")

print("\n程式執行完畢！")