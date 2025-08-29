# Day 14：第二週複習與綜合練習

## 今日學習目標
- 複習第二週所有學習內容
- 整合迴圈、清單、字典、元組的應用
- 實作完整的學生管理系統
- 培養綜合解決問題的能力

## 1. 第二週學習回顧

### Day 8：for迴圈
**核心概念：**
- 重複執行指定次數的程式碼
- range()函數的使用
- 巢狀迴圈的應用

**關鍵語法：**
```python
for i in range(10):
    print(i)

for item in items:
    process(item)

for i, value in enumerate(items):
    print(f"{i}: {value}")
```

### Day 9：while迴圈
**核心概念：**
- 根據條件重複執行程式碼
- break和continue的使用
- 無限迴圈的避免

**關鍵語法：**
```python
while condition:
    do_something()
    update_condition()

while True:
    if exit_condition:
        break
    continue
```

### Day 10：清單（List）
**核心概念：**
- 有序的可變資料集合
- 索引存取和切片操作
- 常用方法：append(), remove(), sort()等

**關鍵語法：**
```python
my_list = [1, 2, 3]
my_list.append(4)
my_list[0] = 10
for item in my_list:
    print(item)
```

### Day 11：清單進階操作
**核心概念：**
- 清單切片：[start:end:step]
- 清單推導式：[expression for item in iterable if condition]
- 多維清單和巢狀結構

**關鍵語法：**
```python
# 切片
numbers[2:5]
numbers[::-1]

# 推導式
squares = [x**2 for x in range(10) if x % 2 == 0]

# 多維清單
matrix = [[1, 2], [3, 4]]
```

### Day 12：字典（Dictionary）
**核心概念：**
- 鍵值對的資料結構
- 快速查詢和存取
- 常用方法：keys(), values(), items()

**關鍵語法：**
```python
my_dict = {"key": "value"}
my_dict["new_key"] = "new_value"
for key, value in my_dict.items():
    print(key, value)
```

### Day 13：元組（Tuple）
**核心概念：**
- 不可變的有序資料集合
- 元組解包和多值回傳
- 適用於固定資料和配置

**關鍵語法：**
```python
my_tuple = (1, 2, 3)
x, y, z = my_tuple
coordinates = (10, 20)
```

## 2. 綜合應用模式

### 模式1：資料處理流程
```python
# 1. 收集資料（清單）
data = []

# 2. 處理資料（迴圈 + 條件）
for item in raw_data:
    if meets_condition(item):
        processed = process_item(item)
        data.append(processed)

# 3. 分析資料（字典統計）
statistics = {}
for item in data:
    category = get_category(item)
    statistics[category] = statistics.get(category, 0) + 1

# 4. 輸出結果（格式化顯示）
for category, count in statistics.items():
    print(f"{category}: {count}")
```

### 模式2：選單驅動程式
```python
def main():
    data = initialize_data()
    
    while True:
        display_menu()
        choice = input("請選擇: ")
        
        if choice == "1":
            add_data(data)
        elif choice == "2":
            view_data(data)
        elif choice == "3":
            search_data(data)
        elif choice == "0":
            break
        else:
            print("無效選擇")
```

### 模式3：多層資料結構
```python
# 組合使用不同資料結構
school = {
    "name": "Python高中",
    "classes": [
        {
            "class_name": "一年一班",
            "students": [
                ("小明", 16, {"數學": 85, "英文": 92}),
                ("小美", 16, {"數學": 78, "英文": 88})
            ]
        }
    ]
}
```

## 3. 常見程式設計模式

### 3.1 輸入驗證模式
```python
def get_valid_input(prompt, validator, error_msg):
    """通用輸入驗證函數"""
    while True:
        user_input = input(prompt).strip()
        if validator(user_input):
            return user_input
        print(error_msg)

# 使用範例
age = int(get_valid_input(
    "請輸入年齡: ",
    lambda x: x.isdigit() and 0 < int(x) < 120,
    "請輸入有效年齡（1-119）"
))
```

### 3.2 資料查找模式
```python
def find_item(data_list, key, value):
    """在清單中查找符合條件的項目"""
    for item in data_list:
        if item.get(key) == value:
            return item
    return None

def find_items(data_list, condition):
    """查找所有符合條件的項目"""
    return [item for item in data_list if condition(item)]
```

### 3.3 統計分析模式
```python
def analyze_data(data, key_func):
    """分析資料並產生統計"""
    stats = {}
    for item in data:
        key = key_func(item)
        stats[key] = stats.get(key, 0) + 1
    return stats

def calculate_stats(numbers):
    """計算數字統計"""
    return {
        "總數": len(numbers),
        "總和": sum(numbers),
        "平均": sum(numbers) / len(numbers) if numbers else 0,
        "最大值": max(numbers) if numbers else 0,
        "最小值": min(numbers) if numbers else 0
    }
```

## 4. 實作項目：學生管理系統

讓我們整合所有學習內容，建立一個完整的學生管理系統：

### 系統功能需求
1. **學生資料管理**：新增、查看、修改、刪除
2. **成績管理**：記錄各科成績、計算統計
3. **班級管理**：班級資訊、學生分組
4. **資料分析**：成績分析、排名統計
5. **資料持久化**：儲存和載入資料

### 資料結構設計
```python
# 學生資料結構
student = {
    "student_id": "S001",
    "name": "張小明",
    "age": 16,
    "gender": "男",
    "class": "一年一班",
    "contact": {
        "phone": "0912345678",
        "email": "ming@school.edu",
        "address": "台北市信義區"
    },
    "grades": {
        "國文": [85, 92, 78],
        "英文": [88, 85, 90],
        "數學": [92, 88, 85]
    },
    "activities": ["籃球社", "學生會"]
}

# 班級資料結構
class_info = {
    "class_id": "C001",
    "class_name": "一年一班",
    "teacher": "王老師",
    "student_count": 30,
    "subjects": ["國文", "英文", "數學", "自然", "社會"]
}
```

## 5. 完整實作程式

```python
import json
import os
from datetime import datetime
import statistics

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.classes = {}
        self.subjects = ["國文", "英文", "數學", "自然", "社會"]
        self.data_file = "student_data.json"
        self.load_data()
    
    def save_data(self):
        """儲存資料到檔案"""
        try:
            data = {
                "students": self.students,
                "classes": self.classes,
                "subjects": self.subjects,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"儲存失敗：{e}")
    
    def load_data(self):
        """從檔案載入資料"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.students = data.get("students", [])
                    self.classes = data.get("classes", {})
                    self.subjects = data.get("subjects", self.subjects)
            else:
                self.initialize_sample_data()
        except Exception as e:
            print(f"載入失敗：{e}")
            self.initialize_sample_data()
    
    def initialize_sample_data(self):
        """初始化範例資料"""
        # 範例學生資料
        sample_students = [
            {
                "student_id": "S001",
                "name": "張小明",
                "age": 16,
                "gender": "男",
                "class": "一年一班",
                "contact": {
                    "phone": "0912345678",
                    "email": "ming@school.edu",
                    "address": "台北市信義區"
                },
                "grades": {
                    "國文": [85, 92, 78],
                    "英文": [88, 85, 90], 
                    "數學": [92, 88, 85],
                    "自然": [79, 83, 87],
                    "社會": [91, 89, 93]
                },
                "activities": ["籃球社", "學生會"]
            },
            {
                "student_id": "S002",
                "name": "李小美",
                "age": 16,
                "gender": "女",
                "class": "一年一班",
                "contact": {
                    "phone": "0987654321",
                    "email": "mei@school.edu",
                    "address": "台北市大安區"
                },
                "grades": {
                    "國文": [92, 88, 91],
                    "英文": [85, 89, 87],
                    "數學": [78, 82, 80],
                    "自然": [88, 91, 85],
                    "社會": [94, 90, 92]
                },
                "activities": ["合唱團", "志工社"]
            }
        ]
        
        self.students = sample_students
        
        # 範例班級資料
        self.classes = {
            "一年一班": {
                "class_id": "C001",
                "teacher": "王老師",
                "room": "101教室",
                "student_count": len([s for s in self.students if s["class"] == "一年一班"])
            }
        }
    
    def display_header(self):
        """顯示系統標題"""
        print("\n" + "="*60)
        print("🎓              學生管理系統              🎓")
        print("="*60)
        print(f"📅 當前時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"👥 學生總數：{len(self.students)}")
        print(f"🏫 班級數量：{len(self.classes)}")
    
    def display_main_menu(self):
        """顯示主選單"""
        print("\n" + "─"*40)
        print("🏠 主選單")
        print("─"*40)
        print("1. 👤 學生資料管理")
        print("2. 📊 成績管理")  
        print("3. 🏫 班級管理")
        print("4. 📈 資料分析")
        print("5. 🔍 搜尋功能")
        print("6. 💾 資料管理")
        print("0. 🚪 離開系統")
        print("─"*40)
    
    def student_management_menu(self):
        """學生資料管理選單"""
        while True:
            print("\n" + "─"*30)
            print("👤 學生資料管理")
            print("─"*30)
            print("1. 查看所有學生")
            print("2. 新增學生")
            print("3. 修改學生資料")
            print("4. 刪除學生")
            print("5. 學生詳細資料")
            print("0. 回到主選單")
            
            choice = input("\n請選擇功能: ").strip()
            
            if choice == "1":
                self.view_all_students()
            elif choice == "2":
                self.add_student()
            elif choice == "3":
                self.modify_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.view_student_details()
            elif choice == "0":
                break
            else:
                print("無效選擇！")
            
            if choice != "0":
                input("\n按Enter繼續...")
    
    def view_all_students(self):
        """查看所有學生"""
        if not self.students:
            print("目前沒有學生資料！")
            return
        
        print(f"\n👥 學生清單（共{len(self.students)}人）")
        print("="*80)
        print(f"{'學號':<8} {'姓名':<10} {'年齡':<4} {'性別':<4} {'班級':<12} {'平均成績':<8}")
        print("-" * 80)
        
        for student in self.students:
            avg_grade = self.calculate_student_average(student)
            print(f"{student['student_id']:<8} {student['name']:<10} "
                  f"{student['age']:<4} {student['gender']:<4} "
                  f"{student['class']:<12} {avg_grade:<8.1f}")
    
    def calculate_student_average(self, student):
        """計算學生平均成績"""
        all_grades = []
        for subject, grades in student['grades'].items():
            if grades:
                all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def add_student(self):
        """新增學生"""
        print("\n➕ 新增學生")
        print("─"*15)
        
        # 生成學號
        student_ids = [s['student_id'] for s in self.students]
        next_id = f"S{len(self.students) + 1:03d}"
        while next_id in student_ids:
            next_id = f"S{len(self.students) + len(student_ids) + 1:03d}"
        
        print(f"學號：{next_id}")
        
        # 輸入基本資料
        name = input("姓名：").strip()
        if not name:
            print("姓名不能為空！")
            return
        
        try:
            age = int(input("年齡："))
            if not 10 <= age <= 25:
                print("年齡必須在10-25之間！")
                return
        except ValueError:
            print("請輸入有效年齡！")
            return
        
        gender = input("性別（男/女）：").strip()
        if gender not in ["男", "女"]:
            print("性別必須是'男'或'女'！")
            return
        
        # 選擇班級
        print("\n可選班級：")
        for class_name in self.classes.keys():
            print(f"  - {class_name}")
        
        class_name = input("班級：").strip()
        if class_name not in self.classes:
            # 如果班級不存在，建立新班級
            create_class = input(f"班級'{class_name}'不存在，是否建立？(y/N): ")
            if create_class.lower() == 'y':
                teacher = input("導師：").strip() or "未設定"
                room = input("教室：").strip() or "未設定"
                self.classes[class_name] = {
                    "class_id": f"C{len(self.classes) + 1:03d}",
                    "teacher": teacher,
                    "room": room,
                    "student_count": 0
                }
            else:
                print("取消新增學生！")
                return
        
        # 聯絡資訊
        phone = input("電話（選填）：").strip()
        email = input("Email（選填）：").strip()
        address = input("地址（選填）：").strip()
        
        # 建立學生資料
        new_student = {
            "student_id": next_id,
            "name": name,
            "age": age,
            "gender": gender,
            "class": class_name,
            "contact": {
                "phone": phone,
                "email": email,
                "address": address
            },
            "grades": {subject: [] for subject in self.subjects},
            "activities": []
        }
        
        self.students.append(new_student)
        
        # 更新班級人數
        self.classes[class_name]["student_count"] = len([
            s for s in self.students if s["class"] == class_name
        ])
        
        self.save_data()
        print(f"✅ 成功新增學生：{name}（學號：{next_id}）")
    
    def run(self):
        """執行主程式"""
        self.display_header()
        print("🎉 歡迎使用學生管理系統！")
        
        while True:
            self.display_main_menu()
            choice = input("\n請選擇功能: ").strip()
            
            if choice == "1":
                self.student_management_menu()
            elif choice == "2":
                self.grade_management_menu()
            elif choice == "3":
                self.class_management_menu()
            elif choice == "4":
                self.data_analysis_menu()
            elif choice == "5":
                self.search_menu()
            elif choice == "6":
                self.data_management_menu()
            elif choice == "0":
                self.save_data()
                print("\n👋 感謝使用學生管理系統！")
                print("💾 資料已自動儲存")
                break
            else:
                print("無效選擇！")

# 程式入口點
if __name__ == "__main__":
    system = StudentManagementSystem()
    try:
        system.run()
    except KeyboardInterrupt:
        print("\n\n程式被中斷，資料已儲存！")
        system.save_data()
```

## 6. 學習成效檢驗

### 6.1 程式設計思維檢驗
能夠回答以下問題：
1. 何時使用for迴圈，何時使用while迴圈？
2. 清單和元組的差異及應用場景？
3. 字典的優勢和使用時機？
4. 如何選擇適當的資料結構？

### 6.2 實作能力檢驗
能夠獨立完成：
1. 設計多層選單系統
2. 實作資料的增刪改查功能
3. 進行資料統計和分析
4. 處理檔案儲存和載入

### 6.3 問題解決能力檢驗
面對新需求時能夠：
1. 分析問題並拆解成小步驟
2. 選擇合適的程式結構
3. 整合已學概念解決問題
4. 除錯和優化程式

## 7. 第二週重要概念總結

### 資料結構選擇指南
- **清單（List）**：需要修改、有序序列
- **元組（Tuple）**：不需修改、固定資料
- **字典（Dict）**：鍵值對應、快速查詢
- **組合使用**：複雜資料結構

### 迴圈使用指南
- **for迴圈**：已知次數、遍歷序列
- **while迴圈**：未知次數、條件控制
- **break/continue**：迴圈控制
- **巢狀迴圈**：多維處理

### 程式設計原則
1. **可讀性**：程式碼要清晰易懂
2. **模組化**：功能分離、重複利用
3. **資料驗證**：確保輸入有效性
4. **錯誤處理**：優雅處理異常情況

## 8. 後續學習方向

### 第三週預告：函數與模組
- 函數的定義和使用
- 參數傳遞和回傳值
- 模組化程式設計
- 標準函式庫的使用

### 進階學習建議
1. **深入資料結構**：集合（Set）、更多清單操作
2. **檔案處理**：CSV、JSON、文字檔案
3. **錯誤處理**：try-except機制
4. **物件導向**：類別和物件概念

## 9. 作業與挑戶

### 基礎作業
1. 完成學生管理系統的基本功能
2. 新增成績分析和排名功能
3. 實作資料匯出功能

### 進階挑戰
1. 新增圖形化介面（tkinter）
2. 實作資料備份和還原
3. 新增學生選課系統
4. 建立教師評價系統

### 創意專案
根據個人興趣，結合所學概念創作：
- 個人記帳系統
- 讀書計劃管理器
- 社團活動管理系統
- 小遊戲（如文字冒險遊戲）

## 10. 今日總結

今天你完成了：
- ✅ 第二週所有概念的整合複習
- ✅ 學習了程式設計的常見模式
- ✅ 實作了完整的學生管理系統
- ✅ 培養了系統性思考能力

**恭喜你完成了Python程式設計的第二週學習！**

你已經掌握了：
- 迴圈控制結構
- 基本資料結構（清單、字典、元組）
- 資料處理和分析技巧
- 綜合系統開發能力

這些技能為你打下了堅實的程式設計基礎，接下來我們將學習更進階的概念，讓你的程式設計能力更上一層樓！

記住：**程式設計是一個持續學習和實作的過程，保持練習和好奇心是成功的關鍵！**