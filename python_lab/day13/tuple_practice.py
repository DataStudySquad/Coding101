# Day 13: 元組練習
# 這個檔案包含各種元組操作的實用範例

print("=== Day 13: 元組練習 ===\n")

# 練習1：基本元組操作
print("練習1：基本元組操作")
point = (3, 5)
color = (255, 0, 0)  # RGB紅色
person = ("小明", 18, "男", "台北")

print(f"座標點：{point}")
print(f"顏色值：{color}")
print(f"個人資料：{person}")

# 存取元組元素
print(f"X座標：{point[0]}")
print(f"Y座標：{point[1]}")
print(f"紅色值：{color[0]}")
print(f"姓名：{person[0]}")
print(f"年齡：{person[1]}")

# 元組解包
x, y = point
r, g, b = color
name, age, gender, city = person

print(f"解包後 - 座標：({x}, {y})")
print(f"解包後 - RGB：R={r}, G={g}, B={b}")
print(f"解包後 - 個人：{name}, {age}歲, {gender}, 住{city}")

print("\n" + "="*50 + "\n")

# 練習2：元組的不可變性
print("練習2：元組的不可變性")
original_tuple = (1, 2, 3, 4, 5)
print(f"原始元組：{original_tuple}")

# 嘗試模擬修改（實際上是建立新元組）
modified_tuple = original_tuple + (6,)
print(f"添加元素後：{modified_tuple}")

doubled_tuple = original_tuple * 2
print(f"重複兩次：{doubled_tuple}")

sliced_tuple = original_tuple[1:4]
print(f"切片[1:4]：{sliced_tuple}")

reversed_tuple = original_tuple[::-1]
print(f"反轉：{reversed_tuple}")

print(f"原元組未改變：{original_tuple}")

print("\n" + "="*50 + "\n")

# 練習3：元組方法和函數
print("練習3：元組方法和函數")
numbers = (1, 2, 3, 2, 4, 2, 5, 6, 2)
print(f"數字元組：{numbers}")

print(f"長度：{len(numbers)}")
print(f"數字2的次數：{numbers.count(2)}")
print(f"數字3的位置：{numbers.index(3)}")
print(f"最大值：{max(numbers)}")
print(f"最小值：{min(numbers)}")
print(f"總和：{sum(numbers)}")

# 成員檢查
print(f"包含數字5：{5 in numbers}")
print(f"包含數字10：{10 in numbers}")

# 字串元組
words = ("python", "java", "javascript", "c++")
print(f"\n程式語言：{words}")
print(f"按字典順序最大：{max(words)}")
print(f"按字典順序最小：{min(words)}")
print(f"按長度排序：{tuple(sorted(words, key=len))}")

print("\n" + "="*50 + "\n")

# 練習4：元組解包進階
print("練習4：元組解包進階")

# 基本解包
student = ("小明", 20, "資工系", "台北", "0912345678")
name, age, major, city, phone = student
print(f"學生：{name}, {age}歲, {major}, 來自{city}, 電話{phone}")

# 部分解包（使用*）
scores = (85, 92, 78, 96, 88, 74, 91)
first, second, *others, last = scores
print(f"\n成績分析：")
print(f"最高分：{first}")
print(f"第二高：{second}")
print(f"中間成績：{others}")
print(f"最低分：{last}")

# 忽略某些值（使用_）
rgb_colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255))
for r, g, b in rgb_colors:
    print(f"RGB({r:3d}, {g:3d}, {b:3d})")

# 函數回傳多值
def get_statistics(data):
    return len(data), max(data), min(data), sum(data)/len(data)

numbers = [85, 92, 78, 96, 88]
count, maximum, minimum, average = get_statistics(numbers)
print(f"\n統計結果：")
print(f"數量：{count}, 最大：{maximum}, 最小：{minimum}, 平均：{average:.1f}")

# 變數交換
a, b = 10, 20
print(f"\n交換前：a={a}, b={b}")
a, b = b, a
print(f"交換後：a={a}, b={b}")

print("\n" + "="*50 + "\n")

# 練習5：巢狀元組
print("練習5：巢狀元組")

# 學生成績表
students = (
    ("小明", "男", (85, 92, 78, 88, 91)),
    ("小美", "女", (96, 88, 91, 94, 89)),
    ("小華", "男", (79, 85, 83, 87, 82)),
    ("小強", "男", (88, 91, 85, 90, 87)),
    ("小雅", "女", (92, 87, 89, 85, 91))
)

subjects = ("國文", "英文", "數學", "自然", "社會")

print("📊 學生成績表")
print(f"{'姓名':<6} {'性別':<4} {'國文':<4} {'英文':<4} {'數學':<4} {'自然':<4} {'社會':<4} {'總分':<4} {'平均':<6}")
print("-" * 70)

for name, gender, scores in students:
    total = sum(scores)
    average = total / len(scores)
    print(f"{name:<6} {gender:<4} ", end="")
    for score in scores:
        print(f"{score:<4} ", end="")
    print(f"{total:<4} {average:<6.1f}")

# 分析每科平均
print(f"\n📚 科目統計：")
for i, subject in enumerate(subjects):
    subject_scores = tuple(student[2][i] for student in students)
    avg = sum(subject_scores) / len(subject_scores)
    max_score = max(subject_scores)
    min_score = min(subject_scores)
    print(f"{subject}：平均{avg:.1f}, 最高{max_score}, 最低{min_score}")

print("\n" + "="*50 + "\n")

# 練習6：座標系統應用
print("練習6：座標系統應用")
import math

# 定義一些幾何圖形的頂點
triangle = ((0, 0), (3, 0), (1.5, 2.6))
rectangle = ((0, 0), (4, 0), (4, 3), (0, 3))
pentagon = ((0, 2), (1.9, 0.6), (1.2, -1.6), (-1.2, -1.6), (-1.9, 0.6))

def calculate_distance(point1, point2):
    """計算兩點間的距離"""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_perimeter(vertices):
    """計算多邊形周長"""
    perimeter = 0
    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]
        perimeter += calculate_distance(p1, p2)
    return perimeter

def get_centroid(vertices):
    """計算多邊形重心"""
    x_sum = sum(point[0] for point in vertices)
    y_sum = sum(point[1] for point in vertices)
    n = len(vertices)
    return (x_sum / n, y_sum / n)

print("🔺 三角形分析：")
print(f"頂點：{triangle}")
perimeter = calculate_perimeter(triangle)
centroid = get_centroid(triangle)
print(f"周長：{perimeter:.2f}")
print(f"重心：({centroid[0]:.2f}, {centroid[1]:.2f})")

print(f"\n⬜ 矩形分析：")
print(f"頂點：{rectangle}")
perimeter = calculate_perimeter(rectangle)
centroid = get_centroid(rectangle)
print(f"周長：{perimeter:.2f}")
print(f"重心：({centroid[0]:.2f}, {centroid[1]:.2f})")

print(f"\n⭐ 五邊形分析：")
print(f"頂點：{pentagon}")
perimeter = calculate_perimeter(pentagon)
centroid = get_centroid(pentagon)
print(f"周長：{perimeter:.2f}")
print(f"重心：({centroid[0]:.2f}, {centroid[1]:.2f})")

print("\n" + "="*50 + "\n")

# 練習7：資料記錄與處理
print("練習7：資料記錄與處理")

# 員工資料（使用元組確保不被意外修改）
employees = (
    ("E001", "張小明", "工程師", "資訊部", 50000, (1990, 5, 15)),
    ("E002", "李小美", "設計師", "設計部", 45000, (1992, 8, 20)),
    ("E003", "王小華", "專員", "行銷部", 40000, (1988, 12, 3)),
    ("E004", "陳小強", "經理", "業務部", 60000, (1985, 3, 10)),
    ("E005", "林小雅", "分析師", "資訊部", 48000, (1991, 7, 25))
)

print("👥 員工資料庫")
print(f"{'編號':<6} {'姓名':<8} {'職位':<8} {'部門':<8} {'薪資':<8} {'生日':<12}")
print("-" * 65)

total_salary = 0
departments = {}
ages = []

for emp_id, name, position, dept, salary, (year, month, day) in employees:
    birthday = f"{year}-{month:02d}-{day:02d}"
    print(f"{emp_id:<6} {name:<8} {position:<8} {dept:<8} ${salary:<7,} {birthday:<12}")
    
    total_salary += salary
    departments[dept] = departments.get(dept, 0) + 1
    
    # 計算年齡（簡化版）
    current_year = 2024
    age = current_year - year
    ages.append(age)

print(f"\n💰 薪資統計：")
print(f"總薪資：${total_salary:,}")
print(f"平均薪資：${total_salary // len(employees):,}")

print(f"\n🏢 部門分佈：")
for dept, count in departments.items():
    print(f"{dept}：{count}人")

print(f"\n👴 年齡統計：")
print(f"平均年齡：{sum(ages) / len(ages):.1f}歲")
print(f"最大年齡：{max(ages)}歲")
print(f"最小年齡：{min(ages)}歲")

print("\n" + "="*50 + "\n")

# 練習8：設定和配置管理
print("練習8：設定和配置管理")

# 遊戲設定（不可變）
GAME_SETTINGS = (
    ("WINDOW_WIDTH", 800),
    ("WINDOW_HEIGHT", 600),
    ("FPS", 60),
    ("MAX_PLAYERS", 4),
    ("DIFFICULTY", "NORMAL"),
    ("SOUND_ENABLED", True)
)

# 顏色配置
COLOR_PALETTE = {
    "PRIMARY": (52, 152, 219),    # 藍色
    "SUCCESS": (46, 204, 113),    # 綠色
    "WARNING": (241, 196, 15),    # 黃色
    "DANGER": (231, 76, 60),      # 紅色
    "INFO": (155, 89, 182),       # 紫色
    "LIGHT": (236, 240, 241),     # 淺灰色
    "DARK": (52, 73, 94)          # 深灰色
}

# 關卡配置
LEVEL_CONFIG = (
    ("LEVEL_1", {"enemies": 5, "time_limit": 60, "bonus_points": 100}),
    ("LEVEL_2", {"enemies": 8, "time_limit": 90, "bonus_points": 200}),
    ("LEVEL_3", {"enemies": 12, "time_limit": 120, "bonus_points": 300}),
    ("LEVEL_4", {"enemies": 15, "time_limit": 150, "bonus_points": 500}),
    ("LEVEL_5", {"enemies": 20, "time_limit": 180, "bonus_points": 1000})
)

print("🎮 遊戲配置")
print("─" * 30)
print("基本設定：")
for setting, value in GAME_SETTINGS:
    print(f"  {setting}: {value}")

print(f"\n🎨 顏色配置：")
for color_name, (r, g, b) in COLOR_PALETTE.items():
    print(f"  {color_name}: RGB({r}, {g}, {b})")

print(f"\n🏆 關卡設定：")
for level_name, config in LEVEL_CONFIG:
    enemies = config["enemies"]
    time_limit = config["time_limit"]
    bonus = config["bonus_points"]
    print(f"  {level_name}: {enemies}個敵人, {time_limit}秒, 獎勵{bonus}分")

# 設定查詢功能
def get_setting(name):
    """取得設定值"""
    for setting, value in GAME_SETTINGS:
        if setting == name:
            return value
    return None

def get_color(name):
    """取得顏色值"""
    return COLOR_PALETTE.get(name)

def get_level_config(level):
    """取得關卡配置"""
    for level_name, config in LEVEL_CONFIG:
        if level_name == level:
            return config
    return None

# 測試設定查詢
print(f"\n🔍 設定查詢測試：")
print(f"視窗寬度：{get_setting('WINDOW_WIDTH')}")
print(f"主要顏色：{get_color('PRIMARY')}")
print(f"第3關配置：{get_level_config('LEVEL_3')}")

print("\n" + "="*50 + "\n")

# 練習9：互動式座標計算
print("練習9：互動式座標計算")

# 預定義一些座標點
points = (
    ("原點", (0, 0)),
    ("A", (3, 4)),
    ("B", (-2, 1)),
    ("C", (5, -3)),
    ("D", (-1, -2))
)

def display_points(points_tuple):
    """顯示所有點"""
    print("📍 座標點列表：")
    for name, (x, y) in points_tuple:
        quadrant = get_quadrant(x, y)
        print(f"  {name}: ({x:>3}, {y:>3}) - {quadrant}")

def get_quadrant(x, y):
    """判斷象限"""
    if x > 0 and y > 0:
        return "第一象限"
    elif x < 0 and y > 0:
        return "第二象限"
    elif x < 0 and y < 0:
        return "第三象限"
    elif x > 0 and y < 0:
        return "第四象限"
    elif x == 0 and y == 0:
        return "原點"
    elif x == 0:
        return "Y軸上"
    else:
        return "X軸上"

def calculate_distances(points_tuple):
    """計算所有點對的距離"""
    print("\n📏 點對距離：")
    for i in range(len(points_tuple)):
        for j in range(i + 1, len(points_tuple)):
            name1, (x1, y1) = points_tuple[i]
            name2, (x2, y2) = points_tuple[j]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            print(f"  {name1} 到 {name2}: {distance:.2f}")

display_points(points)
calculate_distances(points)

# 找出距離原點最近和最遠的點
origin = (0, 0)
distances_from_origin = []

for name, (x, y) in points:
    if (x, y) != origin:  # 排除原點本身
        distance = math.sqrt(x ** 2 + y ** 2)
        distances_from_origin.append((name, distance))

if distances_from_origin:
    closest = min(distances_from_origin, key=lambda x: x[1])
    farthest = max(distances_from_origin, key=lambda x: x[1])
    
    print(f"\n🎯 相對原點：")
    print(f"最近的點：{closest[0]} (距離: {closest[1]:.2f})")
    print(f"最遠的點：{farthest[0]} (距離: {farthest[1]:.2f})")

print("\n程式執行完畢！")