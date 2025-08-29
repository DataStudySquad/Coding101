# Day 13：元組（Tuple）

## 今日學習目標
- 理解元組的概念和特性
- 掌握元組的建立和使用方法
- 了解元組與清單的差異
- 實作座標系統和資料記錄程式

## 1. 什麼是元組？

### 生活中的元組概念
想像一下這些不能改變的事物：
- **身分證字號**：A123456789（一旦發出就不能修改）
- **座標點**：(3, 5)（確定的位置）
- **RGB顏色**：(255, 0, 0)（紅色的固定值）
- **日期**：(2024, 1, 15)（確定的時間點）

### 程式中的元組
元組就像是**不能修改的清單**：
- 有順序的資料集合
- **不可變（Immutable）**：建立後不能修改
- 可以包含不同類型的資料
- 使用小括號 () 表示

```python
# 程式中的元組
point = (3, 5)              # 座標點
color = (255, 0, 0)         # RGB顏色
date = (2024, 1, 15)        # 年月日
person = ("小明", 18, "男")   # 姓名、年齡、性別
```

## 2. 元組與清單的比較

| 比較項目 | 清單 (List) | 元組 (Tuple) |
|---------|-------------|-------------|
| 可變性 | 可變 (Mutable) | 不可變 (Immutable) |
| 符號 | `[1, 2, 3]` | `(1, 2, 3)` |
| 新增元素 | ✅ 可以 | ❌ 不可以 |
| 修改元素 | ✅ 可以 | ❌ 不可以 |
| 刪除元素 | ✅ 可以 | ❌ 不可以 |
| 存取元素 | ✅ 可以 | ✅ 可以 |
| 性能 | 較慢 | 較快 |
| 適用場景 | 需要修改的資料 | 不需修改的固定資料 |

### 為什麼要使用元組？
1. **資料安全**：防止意外修改重要資料
2. **性能優越**：存取速度比清單快
3. **可作為字典鍵**：不可變特性讓它能當字典的鍵
4. **函數回傳多值**：方便函數回傳多個值

## 3. 建立元組

### 方法1：使用小括號
```python
# 空元組
empty_tuple = ()
empty_tuple2 = tuple()

# 有元素的元組
point = (3, 5)
colors = (255, 0, 0)
mixed = ("小明", 18, True, 3.14)

print(type(point))  # <class 'tuple'>
```

### 方法2：直接用逗號
```python
# 不用括號也可以建立元組
point = 3, 5
person = "小明", 18, "男"
single = 42,  # 注意：單一元素需要逗號

print(type(point))   # <class 'tuple'>
print(type(single))  # <class 'tuple'>
```

### 方法3：使用tuple()函數
```python
# 從清單建立元組
list_data = [1, 2, 3, 4, 5]
tuple_data = tuple(list_data)
print(tuple_data)  # (1, 2, 3, 4, 5)

# 從字串建立元組
text_tuple = tuple("Python")
print(text_tuple)  # ('P', 'y', 't', 'h', 'o', 'n')

# 從range建立元組
range_tuple = tuple(range(1, 6))
print(range_tuple)  # (1, 2, 3, 4, 5)
```

### 特別注意：單一元素元組
```python
# 錯誤：這不是元組，而是整數
not_tuple = (42)
print(type(not_tuple))  # <class 'int'>

# 正確：單一元素元組需要逗號
is_tuple = (42,)
print(type(is_tuple))   # <class 'tuple'>

# 或者不用括號
is_tuple2 = 42,
print(type(is_tuple2))  # <class 'tuple'>
```

## 4. 存取元組元素

### 基本索引
```python
point = (10, 20, 30)
print(point[0])   # 10（第一個元素）
print(point[1])   # 20（第二個元素）
print(point[-1])  # 30（最後一個元素）
```

### 切片操作
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers[2:5])    # (2, 3, 4)
print(numbers[:3])     # (0, 1, 2)
print(numbers[5:])     # (5, 6, 7, 8, 9)
print(numbers[::2])    # (0, 2, 4, 6, 8)
print(numbers[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

### 解包（Unpacking）
```python
# 元組解包：將元組元素分配給變數
point = (3, 5)
x, y = point
print(f"x = {x}, y = {y}")  # x = 3, y = 5

# 多元素解包
person = ("小明", 18, "男", "台北")
name, age, gender, city = person
print(f"姓名：{name}, 年齡：{age}, 性別：{gender}, 城市：{city}")

# 部分解包（使用*）
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"第一個：{first}")      # 第一個：1
print(f"中間的：{middle}")     # 中間的：[2, 3, 4]
print(f"最後一個：{last}")     # 最後一個：5
```

### 交換變數值
```python
# 利用元組輕鬆交換變數
a = 10
b = 20
print(f"交換前：a = {a}, b = {b}")

a, b = b, a  # 元組解包的應用
print(f"交換後：a = {a}, b = {b}")
```

## 5. 元組的常用操作

### 5.1 長度和成員檢查
```python
colors = ("紅", "綠", "藍", "黃", "紫")

print(len(colors))         # 5
print("紅" in colors)       # True
print("黑" in colors)       # False
print("黑" not in colors)   # True
```

### 5.2 計數和查找
```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count()：計算元素出現次數
print(numbers.count(2))    # 3
print(numbers.count(6))    # 0

# index()：查找元素第一次出現的位置
print(numbers.index(3))    # 2
print(numbers.index(2))    # 1（找到第一個2的位置）

# 查找不存在的元素會出錯
# print(numbers.index(6))  # ValueError
```

### 5.3 最大值、最小值、總和
```python
scores = (85, 92, 78, 96, 88)

print(max(scores))    # 96
print(min(scores))    # 78
print(sum(scores))    # 439

# 字串元組的比較
words = ("apple", "banana", "cherry")
print(max(words))     # cherry（按字典順序）
print(min(words))     # apple
```

### 5.4 元組連接和重複
```python
# 連接元組
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

# 重複元組
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)

# 注意：原元組不會被修改
print(tuple1)    # (1, 2, 3)
```

## 6. 遍歷元組

### 方法1：直接遍歷
```python
fruits = ("蘋果", "香蕉", "橘子")
for fruit in fruits:
    print(f"我喜歡{fruit}")
```

### 方法2：使用索引
```python
fruits = ("蘋果", "香蕉", "橘子")
for i in range(len(fruits)):
    print(f"第{i+1}個水果：{fruits[i]}")
```

### 方法3：同時取得索引和值
```python
fruits = ("蘋果", "香蕉", "橘子")
for index, fruit in enumerate(fruits):
    print(f"索引{index}：{fruit}")
```

## 7. 巢狀元組

### 什麼是巢狀元組？
元組裡面還有元組，常用於表示複雜的結構化資料：

```python
# 學生成績表（元組的元組）
students = (
    ("小明", 18, (85, 92, 78)),
    ("小美", 19, (96, 88, 91)),
    ("小華", 18, (79, 85, 83))
)

# 座標點集合
points = ((0, 0), (1, 1), (2, 4), (3, 9))

# 公司員工資料
employees = (
    ("資訊部", (
        ("小明", "工程師", 50000),
        ("小美", "設計師", 45000)
    )),
    ("行銷部", (
        ("小華", "企劃", 40000),
        ("小強", "專員", 35000)
    ))
)
```

### 存取巢狀元組
```python
students = (
    ("小明", 18, (85, 92, 78)),
    ("小美", 19, (96, 88, 91)),
    ("小華", 18, (79, 85, 83))
)

# 存取第一個學生的資料
first_student = students[0]
print(first_student)  # ("小明", 18, (85, 92, 78))

# 存取第一個學生的姓名
print(students[0][0])  # 小明

# 存取第一個學生的第一科成績
print(students[0][2][0])  # 85

# 解包巢狀元組
name, age, scores = students[0]
subject1, subject2, subject3 = scores
print(f"{name}的第一科成績是{subject1}")
```

## 8. 元組的實際應用

### 應用1：函數回傳多個值
```python
def get_name_age():
    """函數回傳多個值"""
    return "小明", 18  # 實際上回傳一個元組

def calculate_stats(numbers):
    """計算統計資料"""
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum  # 回傳元組

# 使用
name, age = get_name_age()
print(f"姓名：{name}, 年齡：{age}")

scores = [85, 92, 78, 96, 88]
total, avg, max_score, min_score = calculate_stats(scores)
print(f"總分：{total}, 平均：{avg:.1f}, 最高：{max_score}, 最低：{min_score}")
```

### 應用2：設定和配置
```python
# 遊戲設定（不可修改）
GAME_CONFIG = (
    ("SCREEN_WIDTH", 800),
    ("SCREEN_HEIGHT", 600),
    ("FPS", 60),
    ("TITLE", "Python Game")
)

# 顏色定義
COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0)
}

# 使用配置
for setting, value in GAME_CONFIG:
    print(f"{setting}: {value}")
```

### 應用3：座標和點資料
```python
# 幾何圖形的頂點
triangle = ((0, 0), (3, 0), (1.5, 2.6))
rectangle = ((0, 0), (4, 0), (4, 3), (0, 3))

def calculate_distance(point1, point2):
    """計算兩點間距離"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 計算三角形邊長
for i in range(len(triangle)):
    p1 = triangle[i]
    p2 = triangle[(i + 1) % len(triangle)]
    distance = calculate_distance(p1, p2)
    print(f"邊 {i+1}: {distance:.2f}")
```

## 9. 實作項目：座標系統程式

讓我們建立一個完整的2D座標系統：

```python
import math

class CoordinateSystem:
    def __init__(self):
        self.points = []  # 儲存點的清單
    
    def add_point(self, name, coordinates):
        """新增點"""
        if not isinstance(coordinates, tuple) or len(coordinates) != 2:
            print("❌ 座標必須是包含兩個數值的元組")
            return False
        
        x, y = coordinates
        if not all(isinstance(coord, (int, float)) for coord in coordinates):
            print("❌ 座標值必須是數字")
            return False
        
        point = (name, coordinates)
        self.points.append(point)
        print(f"✅ 已新增點 {name}{coordinates}")
        return True
    
    def display_points(self):
        """顯示所有點"""
        if not self.points:
            print("❌ 目前沒有任何點")
            return
        
        print("\n📍 所有座標點：")
        print(f"{'名稱':<10} {'座標':<15} {'象限':<10}")
        print("-" * 40)
        
        for name, (x, y) in self.points:
            quadrant = self.get_quadrant(x, y)
            print(f"{name:<10} ({x:>5}, {y:>5})     {quadrant:<10}")
    
    def get_quadrant(self, x, y):
        """判斷點所在象限"""
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
    
    def calculate_distance(self, name1, name2):
        """計算兩點間距離"""
        point1 = self.find_point(name1)
        point2 = self.find_point(name2)
        
        if not point1 or not point2:
            print("❌ 找不到指定的點")
            return None
        
        x1, y1 = point1[1]
        x2, y2 = point2[1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        print(f"📏 {name1} 到 {name2} 的距離：{distance:.2f}")
        return distance
    
    def find_point(self, name):
        """尋找指定名稱的點"""
        for point in self.points:
            if point[0] == name:
                return point
        return None
    
    def calculate_midpoint(self, name1, name2):
        """計算兩點的中點"""
        point1 = self.find_point(name1)
        point2 = self.find_point(name2)
        
        if not point1 or not point2:
            print("❌ 找不到指定的點")
            return None
        
        x1, y1 = point1[1]
        x2, y2 = point2[1]
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        midpoint = (mid_x, mid_y)
        print(f"🎯 {name1} 和 {name2} 的中點：({mid_x:.1f}, {mid_y:.1f})")
        return midpoint
    
    def analyze_triangle(self, name1, name2, name3):
        """分析三角形"""
        points = [self.find_point(name) for name in [name1, name2, name3]]
        if not all(points):
            print("❌ 找不到指定的點")
            return
        
        # 提取座標
        coords = [point[1] for point in points]
        (x1, y1), (x2, y2), (x3, y3) = coords
        
        # 計算三邊長
        side_a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        side_b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        side_c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        
        print(f"\n📐 三角形分析（{name1}-{name2}-{name3}）：")
        print(f"邊長：{side_a:.2f}, {side_b:.2f}, {side_c:.2f}")
        
        # 計算周長
        perimeter = side_a + side_b + side_c
        print(f"周長：{perimeter:.2f}")
        
        # 計算面積（海倫公式）
        s = perimeter / 2
        area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        print(f"面積：{area:.2f}")
        
        # 判斷三角形類型
        sides = sorted([side_a, side_b, side_c])
        if abs(sides[0] + sides[1] - sides[2]) < 1e-10:
            triangle_type = "退化三角形"
        elif abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-10:
            triangle_type = "直角三角形"
        elif sides[0] == sides[1] == sides[2]:
            triangle_type = "正三角形"
        elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            triangle_type = "等腰三角形"
        else:
            triangle_type = "一般三角形"
        
        print(f"類型：{triangle_type}")
    
    def run(self):
        """執行主程式"""
        print("📊 2D座標系統")
        print("="*40)
        
        # 預設點
        default_points = [
            ("A", (0, 0)),
            ("B", (3, 4)),
            ("C", (-2, 1)),
            ("D", (1, -2))
        ]
        
        for name, coords in default_points:
            self.add_point(name, coords)
        
        while True:
            print("\n" + "─"*30)
            print("🏠 主選單")
            print("─"*30)
            print("1. 📍 查看所有點")
            print("2. ➕ 新增點")
            print("3. 📏 計算距離")
            print("4. 🎯 計算中點")
            print("5. 📐 分析三角形")
            print("6. 🗺️  繪製簡易圖形")
            print("7. 🚪 離開")
            
            choice = input("\n請選擇功能 (1-7): ").strip()
            
            if choice == "1":
                self.display_points()
            
            elif choice == "2":
                name = input("點的名稱：").strip()
                if not name:
                    print("❌ 名稱不能為空")
                    continue
                
                try:
                    x = float(input("X座標："))
                    y = float(input("Y座標："))
                    self.add_point(name, (x, y))
                except ValueError:
                    print("❌ 座標必須是數字")
            
            elif choice == "3":
                if len(self.points) < 2:
                    print("❌ 至少需要兩個點")
                    continue
                
                print("現有的點：", [point[0] for point in self.points])
                name1 = input("第一個點的名稱：").strip()
                name2 = input("第二個點的名稱：").strip()
                self.calculate_distance(name1, name2)
            
            elif choice == "4":
                if len(self.points) < 2:
                    print("❌ 至少需要兩個點")
                    continue
                
                print("現有的點：", [point[0] for point in self.points])
                name1 = input("第一個點的名稱：").strip()
                name2 = input("第二個點的名稱：").strip()
                self.calculate_midpoint(name1, name2)
            
            elif choice == "5":
                if len(self.points) < 3:
                    print("❌ 至少需要三個點")
                    continue
                
                print("現有的點：", [point[0] for point in self.points])
                name1 = input("第一個點的名稱：").strip()
                name2 = input("第二個點的名稱：").strip()
                name3 = input("第三個點的名稱：").strip()
                self.analyze_triangle(name1, name2, name3)
            
            elif choice == "6":
                self.draw_simple_plot()
            
            elif choice == "7":
                print("👋 感謝使用座標系統程式！")
                break
            
            else:
                print("❌ 無效選擇，請輸入1-7")
            
            input("\n按Enter繼續...")
    
    def draw_simple_plot(self):
        """繪製簡易座標圖"""
        if not self.points:
            print("❌ 沒有點可以繪製")
            return
        
        # 找出座標範圍
        x_coords = [point[1][0] for point in self.points]
        y_coords = [point[1][1] for point in self.points]
        
        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)
        
        # 擴展範圍
        range_x = max_x - min_x or 1
        range_y = max_y - min_y or 1
        margin = 0.2
        
        plot_min_x = min_x - range_x * margin
        plot_max_x = max_x + range_x * margin
        plot_min_y = min_y - range_y * margin
        plot_max_y = max_y + range_y * margin
        
        print(f"\n🗺️ 座標圖（範圍：X[{plot_min_x:.1f}, {plot_max_x:.1f}], Y[{plot_min_y:.1f}, {plot_max_y:.1f}]）")
        print("="*50)
        
        # 簡單的ASCII座標圖
        width, height = 40, 20
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # 座標軸
        center_x = width // 2
        center_y = height // 2
        
        for i in range(width):
            grid[center_y][i] = '-'
        for i in range(height):
            grid[i][center_x] = '|'
        grid[center_y][center_x] = '+'
        
        # 標記點
        for name, (x, y) in self.points:
            # 將實際座標轉換為網格座標
            grid_x = int((x - plot_min_x) / (plot_max_x - plot_min_x) * (width - 1))
            grid_y = int((plot_max_y - y) / (plot_max_y - plot_min_y) * (height - 1))
            
            if 0 <= grid_x < width and 0 <= grid_y < height:
                grid[grid_y][grid_x] = name[0]  # 使用名稱第一個字母
        
        # 輸出網格
        for row in grid:
            print(''.join(row))
        
        # 圖例
        print("\n📝 圖例：")
        for name, (x, y) in self.points:
            print(f"  {name[0]} = {name}({x}, {y})")

# 執行程式
if __name__ == "__main__":
    system = CoordinateSystem()
    system.run()
```

## 10. 常見錯誤與解決

### 錯誤1：嘗試修改元組
```python
# 錯誤：元組不可修改
point = (3, 5)
# point[0] = 10  # TypeError

# 正確：建立新元組
point = (10, 5)
print(point)
```

### 錯誤2：忘記單元素元組的逗號
```python
# 錯誤：不是元組
not_tuple = (42)
print(type(not_tuple))  # <class 'int'>

# 正確：加逗號
is_tuple = (42,)
print(type(is_tuple))   # <class 'tuple'>
```

### 錯誤3：解包數量不匹配
```python
point = (1, 2, 3)

# 錯誤：變數數量不匹配
# x, y = point  # ValueError

# 正確：變數數量要匹配
x, y, z = point
print(x, y, z)

# 或使用*收集剩餘元素
x, *rest = point
print(x, rest)  # 1 [2, 3]
```

## 11. 今日總結

今天你學會了：
- ✅ 元組的概念和不可變特性
- ✅ 建立元組的不同方法
- ✅ 元組的存取、切片、解包操作
- ✅ 元組的常用方法和應用
- ✅ 巢狀元組的使用
- ✅ 製作完整的座標系統程式

## 12. 明日預告

明天我們將進行：
- 第二週學習內容總複習
- 整合所有概念製作學生管理系統
- Week 2 的綜合練習和挑戰

## 13. 作業練習

1. 建立一個儲存RGB顏色的元組字典
2. 實作一個使用元組記錄學生資訊的程式
3. 建立一個幾何計算器，使用元組表示點和形狀
4. 嘗試用元組來儲存不可變的設定資料

記住：**元組雖然簡單，但在需要不可變資料時非常重要。掌握元組的特性能讓你寫出更安全、更高效的程式！**