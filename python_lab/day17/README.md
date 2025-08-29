# Day 17：內建函數

## 今日學習目標
- 掌握Python常用內建函數的使用
- 學會len()、max()、min()、sum()等基本函數
- 了解map()、filter()、sorted()等進階函數
- 實作統計分析工具程式
- 培養善用內建函數提高效率的習慣

## 1. 什麼是內建函數？

### 1.1 生活中的類比
內建函數就像是**工具箱裡的基本工具**：
- **螺絲起子**：基本且常用（如len()、print()）
- **電鑽**：功能強大（如map()、filter()）
- **測量尺**：精確計算（如max()、min()、sum()）
- 不用自己製作，開箱即用

或者想像內建函數像是**廚房的基本家電**：
- 每個廚房都有，不需要另外購買
- 經過專業設計，效能優化
- 使用簡單，功能可靠

### 1.2 內建函數的優勢
```python
# ❌ 自己寫的函數（比較慢，可能有bug）
def my_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# ✅ 使用內建函數（快速、可靠）
numbers = [3, 7, 2, 9, 1]
max_value = max(numbers)
```

## 2. 基本內建函數

### 2.1 len() - 長度函數
```python
# 字串長度
text = "Hello Python"
print(f"字串長度：{len(text)}")  # 12

# 清單長度
fruits = ["蘋果", "香蕉", "橘子"]
print(f"清單長度：{len(fruits)}")  # 3

# 字典長度
student = {"name": "小明", "age": 18, "grade": "A"}
print(f"字典長度：{len(student)}")  # 3

# 元組長度
coordinates = (10, 20, 30)
print(f"元組長度：{len(coordinates)}")  # 3

# 實用範例：檢查輸入是否為空
def validate_input(user_input):
    if len(user_input.strip()) == 0:
        return False, "輸入不能為空"
    elif len(user_input) > 50:
        return False, "輸入過長（最多50字元）"
    else:
        return True, "輸入有效"

# 測試
print(validate_input(""))        # False, 輸入不能為空
print(validate_input("Hello"))   # True, 輸入有效
```

### 2.2 max() 和 min() - 最大值和最小值
```python
# 數字比較
numbers = [85, 92, 78, 96, 88]
print(f"最高分：{max(numbers)}")  # 96
print(f"最低分：{min(numbers)}")  # 78

# 字串比較（按字母順序）
names = ["Alice", "Bob", "Charlie", "David"]
print(f"字母順序最後：{max(names)}")  # David
print(f"字母順序最前：{min(names)}")  # Alice

# 多個參數
print(f"最大值：{max(10, 25, 3, 47, 8)}")  # 47
print(f"最小值：{min(10, 25, 3, 47, 8)}")  # 3

# 使用 key 參數
students = [
    {"name": "小明", "score": 85},
    {"name": "小美", "score": 92},
    {"name": "小華", "score": 78}
]

# 找出分數最高的學生
best_student = max(students, key=lambda x: x["score"])
print(f"最高分學生：{best_student['name']} - {best_student['score']}")

# 找出姓名最長的學生
longest_name = max(students, key=lambda x: len(x["name"]))
print(f"姓名最長：{longest_name['name']}")

# 實用範例：找出最貴的商品
products = [
    {"name": "筆電", "price": 25000},
    {"name": "手機", "price": 15000},
    {"name": "平板", "price": 8000}
]

most_expensive = max(products, key=lambda p: p["price"])
print(f"最貴商品：{most_expensive['name']} - NT${most_expensive['price']}")
```

### 2.3 sum() - 總和函數
```python
# 基本總和
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(f"總和：{total}")  # 150

# 指定起始值
total_with_bonus = sum(numbers, 100)  # 從100開始加
print(f"加上獎金的總和：{total_with_bonus}")  # 250

# 計算平均值
average = sum(numbers) / len(numbers)
print(f"平均值：{average}")  # 30.0

# 實用範例：計算購物車總價
cart = [
    {"item": "蘋果", "price": 50, "quantity": 3},
    {"item": "香蕉", "price": 30, "quantity": 2},
    {"item": "橘子", "price": 40, "quantity": 1}
]

total_cost = sum(item["price"] * item["quantity"] for item in cart)
print(f"購物車總價：NT${total_cost}")

# 計算成績總分
subjects = {"國文": 85, "英文": 92, "數學": 78, "自然": 88}
total_score = sum(subjects.values())
average_score = total_score / len(subjects)
print(f"總分：{total_score}，平均：{average_score:.1f}")
```

### 2.4 abs() - 絕對值函數
```python
# 基本使用
print(f"|-5| = {abs(-5)}")    # 5
print(f"|3.14| = {abs(3.14)}")  # 3.14
print(f"|0| = {abs(0)}")      # 0

# 實用範例：計算溫度差
temp1 = 25.5
temp2 = 18.3
temp_diff = abs(temp1 - temp2)
print(f"溫度差：{temp_diff}°C")

# 計算距離
def distance_1d(point1, point2):
    """計算一維距離"""
    return abs(point1 - point2)

print(f"距離：{distance_1d(10, 3)}")  # 7
```

### 2.5 round() - 四捨五入函數
```python
# 基本四捨五入
print(f"round(3.7) = {round(3.7)}")     # 4
print(f"round(3.2) = {round(3.2)}")     # 3
print(f"round(3.5) = {round(3.5)}")     # 4

# 指定小數位數
pi = 3.141592653589793
print(f"π ≈ {round(pi, 2)}")          # 3.14
print(f"π ≈ {round(pi, 4)}")          # 3.1416

# 實用範例：貨幣計算
price = 123.456
print(f"價格：NT${round(price, 2)}")

# BMI計算
weight = 70
height = 1.75
bmi = weight / (height ** 2)
print(f"BMI：{round(bmi, 1)}")
```

## 3. 進階內建函數

### 3.1 sorted() - 排序函數
```python
# 基本排序
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sorted(numbers)
print(f"排序後：{sorted_numbers}")

# 反向排序
reverse_sorted = sorted(numbers, reverse=True)
print(f"反向排序：{reverse_sorted}")

# 字串排序
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words)
print(f"字串排序：{sorted_words}")

# 按長度排序
sorted_by_length = sorted(words, key=len)
print(f"按長度排序：{sorted_by_length}")

# 複雜物件排序
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 19, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78}
]

# 按年齡排序
by_age = sorted(students, key=lambda x: x["age"])
print("按年齡排序：")
for student in by_age:
    print(f"  {student['name']}: {student['age']}歲")

# 按成績排序（高到低）
by_grade = sorted(students, key=lambda x: x["grade"], reverse=True)
print("按成績排序（高到低）：")
for student in by_grade:
    print(f"  {student['name']}: {student['grade']}分")
```

### 3.2 reversed() - 反轉函數
```python
# 反轉清單
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(f"反轉清單：{reversed_numbers}")

# 反轉字串
text = "Hello"
reversed_text = ''.join(reversed(text))
print(f"反轉字串：{reversed_text}")

# 實用範例：倒數計時
for i in reversed(range(1, 6)):
    print(f"倒數：{i}")
print("發射！")
```

### 3.3 enumerate() - 枚舉函數
```python
# 基本使用
fruits = ["蘋果", "香蕉", "橘子"]
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# 指定起始數字
for i, fruit in enumerate(fruits, start=1):
    print(f"第{i}個水果：{fruit}")

# 實用範例：製作選單
def display_menu(items):
    print("請選擇：")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

menu_items = ["新增資料", "查看資料", "修改資料", "刪除資料", "離開"]
display_menu(menu_items)
```

### 3.4 zip() - 打包函數
```python
# 基本使用
names = ["小明", "小美", "小華"]
scores = [85, 92, 78]
subjects = ["數學", "英文", "物理"]

# 配對姓名和分數
for name, score in zip(names, scores):
    print(f"{name}：{score}分")

# 三個清單配對
for name, score, subject in zip(names, scores, subjects):
    print(f"{name}的{subject}成績：{score}分")

# 創建字典
grade_dict = dict(zip(names, scores))
print(f"成績字典：{grade_dict}")

# 實用範例：轉置矩陣
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
print("原矩陣：")
for row in matrix:
    print(row)

print("轉置矩陣：")
for row in transposed:
    print(row)
```

### 3.5 map() - 映射函數
```python
# 基本使用
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"平方：{squares}")

# 字串處理
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(f"大寫：{upper_words}")

# 多個可迭代物件
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"相加：{sums}")

# 實用範例：資料轉換
prices_str = ["100", "200", "300", "400"]
prices_int = list(map(int, prices_str))
print(f"轉為整數：{prices_int}")

# 溫度轉換
celsius_temps = [0, 20, 30, 37, 100]
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))
print("攝氏轉華氏：")
for c, f in zip(celsius_temps, fahrenheit_temps):
    print(f"{c}°C = {f}°F")
```

### 3.6 filter() - 過濾函數
```python
# 基本使用
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶數：{evens}")

# 過濾字串
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(f"長度大於5：{long_words}")

# 過濾空值
data = ["", "hello", None, "world", "", "python"]
non_empty = list(filter(None, data))  # None 會過濾掉空值
print(f"非空值：{non_empty}")

# 實用範例：成績篩選
students = [
    {"name": "小明", "score": 85},
    {"name": "小美", "score": 92},
    {"name": "小華", "score": 65},
    {"name": "小李", "score": 78}
]

passed_students = list(filter(lambda s: s["score"] >= 70, students))
print("及格學生：")
for student in passed_students:
    print(f"  {student['name']}: {student['score']}分")
```

### 3.7 any() 和 all() - 邏輯判斷函數
```python
# any() - 任一為真
scores = [65, 78, 45, 82, 90]
has_high_score = any(score >= 90 for score in scores)
print(f"有人達到90分：{has_high_score}")  # True

# all() - 全部為真
all_passed = all(score >= 60 for score in scores)
print(f"全部及格：{all_passed}")  # False（45分不及格）

# 實用範例：表單驗證
def validate_form(data):
    required_fields = ["name", "email", "phone"]
    
    # 檢查是否所有必填欄位都有值
    all_filled = all(field in data and data[field] for field in required_fields)
    
    # 檢查是否有任何欄位包含無效字符
    has_invalid = any("@" in str(value) for key, value in data.items() if key != "email")
    
    return all_filled and not has_invalid

# 測試
form1 = {"name": "張三", "email": "zhang@email.com", "phone": "0912345678"}
form2 = {"name": "", "email": "li@email.com", "phone": "0987654321"}

print(f"表單1有效：{validate_form(form1)}")  # True
print(f"表單2有效：{validate_form(form2)}")  # False（姓名為空）
```

## 4. 實作項目：統計分析工具

### 4.1 功能需求
1. 基本統計：平均值、中位數、眾數
2. 極值分析：最大值、最小值、範圍
3. 分佈分析：標準差、四分位數
4. 資料清理：異常值檢測
5. 視覺化：簡單的文字圖表
6. 報告生成：完整統計報告

### 4.2 完整實作
```python
import math
from collections import Counter

class StatisticalAnalyzer:
    """統計分析工具類別"""
    
    def __init__(self, data=None):
        """初始化分析器"""
        self.data = data if data else []
        self.cleaned_data = []
        self._prepare_data()
    
    def _prepare_data(self):
        """準備和清理資料"""
        if not self.data:
            return
        
        # 過濾非數字資料
        numeric_data = []
        for item in self.data:
            try:
                numeric_data.append(float(item))
            except (ValueError, TypeError):
                continue
        
        self.cleaned_data = numeric_data
    
    def add_data(self, *values):
        """添加資料"""
        self.data.extend(values)
        self._prepare_data()
    
    def basic_statistics(self):
        """基本統計資訊"""
        if not self.cleaned_data:
            return None
        
        data = self.cleaned_data
        n = len(data)
        
        stats = {
            "數據量": n,
            "總和": sum(data),
            "平均值": sum(data) / n,
            "最大值": max(data),
            "最小值": min(data),
            "範圍": max(data) - min(data)
        }
        
        return stats
    
    def median(self):
        """計算中位數"""
        if not self.cleaned_data:
            return None
        
        sorted_data = sorted(self.cleaned_data)
        n = len(sorted_data)
        
        if n % 2 == 0:
            # 偶數個數據，取中間兩數的平均
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            # 奇數個數據，取中間數
            return sorted_data[n//2]
    
    def mode(self):
        """計算眾數"""
        if not self.cleaned_data:
            return None
        
        counter = Counter(self.cleaned_data)
        max_count = max(counter.values())
        
        modes = [value for value, count in counter.items() if count == max_count]
        
        return modes[0] if len(modes) == 1 else modes
    
    def standard_deviation(self):
        """計算標準差"""
        if len(self.cleaned_data) < 2:
            return None
        
        mean = sum(self.cleaned_data) / len(self.cleaned_data)
        variance = sum((x - mean) ** 2 for x in self.cleaned_data) / (len(self.cleaned_data) - 1)
        
        return math.sqrt(variance)
    
    def quartiles(self):
        """計算四分位數"""
        if not self.cleaned_data:
            return None
        
        sorted_data = sorted(self.cleaned_data)
        n = len(sorted_data)
        
        def get_quartile(data, position):
            index = position * (len(data) - 1)
            if index.is_integer():
                return data[int(index)]
            else:
                lower = data[int(index)]
                upper = data[int(index) + 1]
                return lower + (upper - lower) * (index - int(index))
        
        return {
            "Q1": get_quartile(sorted_data, 0.25),
            "Q2": self.median(),  # Q2 就是中位數
            "Q3": get_quartile(sorted_data, 0.75)
        }
    
    def detect_outliers(self, method="iqr"):
        """檢測異常值"""
        if not self.cleaned_data:
            return []
        
        if method == "iqr":
            quartiles = self.quartiles()
            if not quartiles:
                return []
            
            q1, q3 = quartiles["Q1"], quartiles["Q3"]
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            
            outliers = [x for x in self.cleaned_data if x < lower_bound or x > upper_bound]
            return outliers
        
        return []
    
    def frequency_distribution(self, bins=10):
        """頻率分佈"""
        if not self.cleaned_data:
            return {}
        
        min_val, max_val = min(self.cleaned_data), max(self.cleaned_data)
        bin_width = (max_val - min_val) / bins
        
        distribution = {}
        for i in range(bins):
            lower = min_val + i * bin_width
            upper = lower + bin_width
            
            # 計算落在此區間的數據數量
            count = sum(1 for x in self.cleaned_data if lower <= x < upper)
            if i == bins - 1:  # 最後一個區間包含最大值
                count = sum(1 for x in self.cleaned_data if lower <= x <= upper)
            
            distribution[f"{lower:.2f}-{upper:.2f}"] = count
        
        return distribution
    
    def text_histogram(self, bins=10, width=50):
        """文字直方圖"""
        if not self.cleaned_data:
            return "無資料可顯示"
        
        dist = self.frequency_distribution(bins)
        max_count = max(dist.values()) if dist.values() else 1
        
        result = "\n📊 資料分佈直方圖:\n"
        result += "=" * (width + 15) + "\n"
        
        for range_str, count in dist.items():
            # 計算長條圖的長度
            bar_length = int((count / max_count) * width) if max_count > 0 else 0
            bar = "█" * bar_length
            
            result += f"{range_str:>12} │{bar:<{width}} {count}\n"
        
        result += "=" * (width + 15) + "\n"
        return result
    
    def generate_report(self):
        """生成完整統計報告"""
        if not self.cleaned_data:
            return "無有效數據進行分析"
        
        report = "\n" + "=" * 60 + "\n"
        report += "📊 統計分析報告\n"
        report += "=" * 60 + "\n"
        
        # 基本統計
        basic = self.basic_statistics()
        report += "\n📋 基本統計:\n"
        report += "-" * 30 + "\n"
        for key, value in basic.items():
            if isinstance(value, float):
                report += f"{key:>8}: {value:>10.2f}\n"
            else:
                report += f"{key:>8}: {value:>10}\n"
        
        # 中心趨勢
        median_val = self.median()
        mode_val = self.mode()
        report += f"{'中位數':>8}: {median_val:>10.2f}\n"
        if isinstance(mode_val, list):
            report += f"{'眾數':>8}: {str(mode_val):>10}\n"
        else:
            report += f"{'眾數':>8}: {mode_val:>10.2f}\n"
        
        # 變異性指標
        std_dev = self.standard_deviation()
        if std_dev:
            report += f"{'標準差':>8}: {std_dev:>10.2f}\n"
        
        # 四分位數
        quartiles = self.quartiles()
        if quartiles:
            report += "\n📐 四分位數:\n"
            report += "-" * 30 + "\n"
            for q, value in quartiles.items():
                report += f"{q:>8}: {value:>10.2f}\n"
        
        # 異常值
        outliers = self.detect_outliers()
        if outliers:
            report += f"\n⚠️  異常值 ({len(outliers)}個):\n"
            report += "-" * 30 + "\n"
            for i, outlier in enumerate(sorted(outliers)):
                report += f"{i+1:>8}: {outlier:>10.2f}\n"
        else:
            report += "\n✅ 無檢測到異常值\n"
        
        # 分佈圖
        report += self.text_histogram()
        
        # 資料品質評估
        report += "\n🔍 資料品質評估:\n"
        report += "-" * 30 + "\n"
        
        total_data = len(self.data)
        valid_data = len(self.cleaned_data)
        invalid_data = total_data - valid_data
        
        report += f"{'總資料量':>12}: {total_data:>8}\n"
        report += f"{'有效資料':>12}: {valid_data:>8}\n"
        report += f"{'無效資料':>12}: {invalid_data:>8}\n"
        report += f"{'資料完整度':>12}: {(valid_data/total_data*100):>7.1f}%\n"
        
        if std_dev and basic['平均值'] != 0:
            cv = (std_dev / basic['平均值']) * 100
            report += f"{'變異係數':>12}: {cv:>7.1f}%\n"
            
            if cv < 15:
                report += "         → 資料變異性低，相對穩定\n"
            elif cv < 35:
                report += "         → 資料變異性中等\n"
            else:
                report += "         → 資料變異性高，需注意\n"
        
        report += "\n" + "=" * 60 + "\n"
        
        return report

def demo_statistical_functions():
    """示範內建函數在統計中的應用"""
    print("🧮 內建函數在統計分析中的應用示範")
    print("=" * 50)
    
    # 示範資料
    scores = [85, 92, 78, 88, 95, 67, 82, 90, 76, 84, 89, 93, 71, 87, 94]
    
    print(f"原始資料: {scores}")
    print(f"資料數量: {len(scores)}")
    
    # 使用內建函數進行基本分析
    print(f"\n📊 使用內建函數分析:")
    print(f"總分: {sum(scores)}")
    print(f"平均分: {sum(scores) / len(scores):.2f}")
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")
    print(f"分數範圍: {max(scores) - min(scores)}")
    
    # 排序和百分位數
    sorted_scores = sorted(scores)
    print(f"\n排序後: {sorted_scores}")
    
    n = len(sorted_scores)
    median = sorted_scores[n//2] if n % 2 == 1 else (sorted_scores[n//2-1] + sorted_scores[n//2]) / 2
    print(f"中位數: {median}")
    
    # 使用 map 進行資料轉換
    grade_letters = list(map(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'D', scores))
    print(f"\n等第轉換: {grade_letters}")
    
    # 使用 filter 篩選資料
    high_scores = list(filter(lambda x: x >= 90, scores))
    print(f"高分段(>=90): {high_scores}")
    print(f"高分人數: {len(high_scores)}")
    
    # 使用 any 和 all 檢查條件
    print(f"\n邏輯檢查:")
    print(f"有人滿分(100): {any(score == 100 for score in scores)}")
    print(f"全部及格(>=60): {all(score >= 60 for score in scores)}")
    print(f"有人不及格(<60): {any(score < 60 for score in scores)}")

def interactive_analyzer():
    """互動式統計分析器"""
    print("📊 歡迎使用統計分析工具！")
    print("這個工具展示了內建函數的強大功能")
    
    analyzer = StatisticalAnalyzer()
    
    while True:
        print("\n" + "=" * 50)
        print("請選擇功能：")
        print("1. 📝 輸入資料")
        print("2. 📊 基本統計")
        print("3. 📈 進階分析")
        print("4. 📋 完整報告")
        print("5. 🧹 清除資料")
        print("6. 🧪 載入示範資料")
        print("7. 🔧 內建函數示範")
        print("0. 🚪 退出")
        print("=" * 50)
        
        choice = input("請選擇 (0-7): ").strip()
        
        if choice == "0":
            print("感謝使用統計分析工具！")
            break
        elif choice == "1":
            input_data(analyzer)
        elif choice == "2":
            show_basic_stats(analyzer)
        elif choice == "3":
            show_advanced_analysis(analyzer)
        elif choice == "4":
            print(analyzer.generate_report())
        elif choice == "5":
            analyzer.data = []
            analyzer.cleaned_data = []
            print("✅ 資料已清除")
        elif choice == "6":
            load_demo_data(analyzer)
        elif choice == "7":
            demo_statistical_functions()
        else:
            print("❌ 無效選擇")
        
        if choice != "0":
            input("\n按 Enter 繼續...")

def input_data(analyzer):
    """輸入資料介面"""
    print("\n📝 資料輸入")
    print("-" * 20)
    print("請輸入數字資料，每行一個，輸入 'done' 結束：")
    
    count = 0
    while True:
        try:
            data = input(f"資料 #{count + 1}: ").strip()
            if data.lower() == 'done':
                break
            
            # 嘗試轉換為數字
            number = float(data)
            analyzer.add_data(number)
            count += 1
            print(f"✅ 已添加: {number}")
            
        except ValueError:
            print("❌ 請輸入有效數字")
        except KeyboardInterrupt:
            print("\n輸入已取消")
            break
    
    print(f"\n📊 總共輸入了 {count} 個數據")

def show_basic_stats(analyzer):
    """顯示基本統計"""
    if not analyzer.cleaned_data:
        print("❌ 沒有資料可分析")
        return
    
    print("\n📊 基本統計分析")
    print("-" * 30)
    
    stats = analyzer.basic_statistics()
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")
    
    print(f"中位數: {analyzer.median():.2f}")
    
    mode_val = analyzer.mode()
    if isinstance(mode_val, list):
        print(f"眾數: {mode_val}")
    else:
        print(f"眾數: {mode_val:.2f}")

def show_advanced_analysis(analyzer):
    """顯示進階分析"""
    if not analyzer.cleaned_data:
        print("❌ 沒有資料可分析")
        return
    
    print("\n📈 進階統計分析")
    print("-" * 30)
    
    # 標準差
    std_dev = analyzer.standard_deviation()
    if std_dev:
        print(f"標準差: {std_dev:.2f}")
    
    # 四分位數
    quartiles = analyzer.quartiles()
    if quartiles:
        print("\n四分位數:")
        for q, value in quartiles.items():
            print(f"  {q}: {value:.2f}")
    
    # 異常值
    outliers = analyzer.detect_outliers()
    if outliers:
        print(f"\n異常值 ({len(outliers)}個): {[round(x, 2) for x in outliers]}")
    else:
        print("\n✅ 無異常值")
    
    # 簡單分佈圖
    print(analyzer.text_histogram(bins=8, width=30))

def load_demo_data(analyzer):
    """載入示範資料"""
    demo_sets = {
        "1": ("學生成績", [85, 92, 78, 88, 95, 67, 82, 90, 76, 84, 89, 93, 71, 87, 94]),
        "2": ("銷售額", [120, 135, 98, 156, 142, 189, 176, 203, 167, 145, 198, 134, 178]),
        "3": ("溫度記錄", [25.2, 26.8, 24.5, 27.3, 23.9, 28.1, 26.4, 25.7, 29.2, 24.8]),
        "4": ("股票價格", [1250, 1180, 1320, 1290, 1156, 1380, 1420, 1350, 1275, 1195])
    }
    
    print("\n🧪 選擇示範資料集:")
    for key, (name, data) in demo_sets.items():
        print(f"  {key}. {name} ({len(data)}筆資料)")
    
    choice = input("請選擇 (1-4): ").strip()
    
    if choice in demo_sets:
        name, data = demo_sets[choice]
        analyzer.data = data.copy()
        analyzer._prepare_data()
        print(f"✅ 已載入 {name} 資料集")
        print(f"資料: {data}")
    else:
        print("❌ 無效選擇")

if __name__ == "__main__":
    interactive_analyzer()
```

## 5. 內建函數總結表

### 5.1 基本函數
| 函數 | 功能 | 範例 |
|------|------|------|
| `len()` | 計算長度 | `len([1,2,3])` → 3 |
| `max()` | 最大值 | `max([1,3,2])` → 3 |
| `min()` | 最小值 | `min([1,3,2])` → 1 |
| `sum()` | 總和 | `sum([1,2,3])` → 6 |
| `abs()` | 絕對值 | `abs(-5)` → 5 |
| `round()` | 四捨五入 | `round(3.7)` → 4 |

### 5.2 序列函數
| 函數 | 功能 | 範例 |
|------|------|------|
| `sorted()` | 排序 | `sorted([3,1,2])` → [1,2,3] |
| `reversed()` | 反轉 | `list(reversed([1,2,3]))` → [3,2,1] |
| `enumerate()` | 枚舉 | `list(enumerate(['a','b']))` → [(0,'a'),(1,'b')] |
| `zip()` | 打包 | `list(zip([1,2],['a','b']))` → [(1,'a'),(2,'b')] |

### 5.3 高階函數
| 函數 | 功能 | 範例 |
|------|------|------|
| `map()` | 映射 | `list(map(lambda x: x*2, [1,2,3]))` → [2,4,6] |
| `filter()` | 過濾 | `list(filter(lambda x: x>2, [1,2,3,4]))` → [3,4] |
| `any()` | 任一為真 | `any([False, True, False])` → True |
| `all()` | 全部為真 | `all([True, True, False])` → False |

## 6. 今日總結

今天你學會了：
- ✅ Python常用內建函數的使用方法
- ✅ 基本統計函數：len()、max()、min()、sum()等
- ✅ 進階函數：map()、filter()、sorted()等
- ✅ 實作完整的統計分析工具
- ✅ 善用內建函數提高程式效率

**關鍵概念回顧：**
- 內建函數經過優化，效能佳且可靠
- 組合使用多個內建函數可以完成複雜任務
- map()和filter()是函數式程式設計的基礎
- 統計分析是內建函數的絕佳應用場景

**明天預告：**
我們將學習模組和套件的概念，了解如何使用Python的標準函式庫，並實作隨機密碼產生器！

記住：**善用內建函數是Python程式設計的重要技能，它們是你的得力助手！**