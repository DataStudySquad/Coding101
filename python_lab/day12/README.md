# Day 12：字典（Dictionary）

## 今日學習目標
- 理解字典的概念和重要性
- 掌握字典的建立、存取、修改方法
- 學會字典的常用方法和操作
- 實作通訊錄管理程式

## 1. 什麼是字典？

### 生活中的字典概念
想像一下這些日常場景：
- **英文字典**：查「apple」→「蘋果」
- **電話簿**：查「小明」→「0912-345-678」
- **學號對照**：查「A001」→「張小明」
- **商品價格**：查「蘋果」→「30元/斤」

### 程式中的字典
字典就像是一本**智慧型查詢手冊**：
- 有「鍵」（Key）和「值」（Value）
- 透過鍵來找到對應的值
- 查詢速度非常快
- 資料之間沒有固定順序（但有對應關係）

```python
# 程式中的字典
student_info = {
    "姓名": "小明",
    "年齡": 18,
    "科系": "資工系",
    "學號": "A001"
}

phone_book = {
    "小明": "0912-345-678",
    "小美": "0987-654-321",
    "小華": "0923-456-789"
}
```

## 2. 字典與清單的比較

| 比較項目 | 清單 (List) | 字典 (Dictionary) |
|---------|-------------|------------------|
| 索引方式 | 數字索引 [0, 1, 2...] | 鍵值索引 ["name", "age"...] |
| 順序性 | 有順序 | 無固定順序（Python 3.7+保持插入順序） |
| 查詢方式 | `list[0]` | `dict["key"]` |
| 適用場景 | 序列資料 | 對應關係資料 |
| 範例 | `["小明", "小美", "小華"]` | `{"小明": "0912-345-678"}` |

## 3. 建立字典

### 方法1：直接建立
```python
# 空字典
empty_dict = {}
empty_dict2 = dict()

# 有內容的字典
student = {
    "姓名": "小明",
    "年齡": 18,
    "科系": "資工系"
}

# 混合資料類型
mixed_dict = {
    "name": "Python",
    "version": 3.9,
    "features": ["簡潔", "強大", "易學"],
    "is_popular": True
}
```

### 方法2：使用dict()函數
```python
# 從關鍵字參數建立
person = dict(name="小美", age=20, city="台北")
print(person)  # {'name': '小美', 'age': 20, 'city': '台北'}

# 從元組清單建立
data = [("apple", "蘋果"), ("banana", "香蕉"), ("orange", "橘子")]
fruit_dict = dict(data)
print(fruit_dict)  # {'apple': '蘋果', 'banana': '香蕉', 'orange': '橘子'}
```

### 方法3：字典推導式
```python
# 建立平方字典
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 從清單建立字典
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```

## 4. 存取字典元素

### 基本存取
```python
student = {
    "姓名": "小明",
    "年齡": 18,
    "科系": "資工系",
    "成績": [85, 92, 78]
}

# 存取值
print(student["姓名"])    # 小明
print(student["年齡"])    # 18
print(student["成績"][0]) # 85 (存取清單中的第一個元素)
```

### 安全存取：get()方法
```python
student = {"姓名": "小明", "年齡": 18}

# 如果鍵不存在會出錯
# print(student["電話"])  # KeyError!

# 安全的存取方式
phone = student.get("電話")
print(phone)  # None

# 設定預設值
phone = student.get("電話", "未提供")
print(phone)  # 未提供
```

### 檢查鍵是否存在
```python
student = {"姓名": "小明", "年齡": 18}

print("姓名" in student)    # True
print("電話" in student)    # False
print("電話" not in student) # True
```

## 5. 修改字典

### 新增和修改元素
```python
student = {"姓名": "小明", "年齡": 18}

# 新增元素
student["科系"] = "資工系"
student["電話"] = "0912-345-678"

# 修改元素
student["年齡"] = 19

print(student)
# {'姓名': '小明', '年齡': 19, '科系': '資工系', '電話': '0912-345-678'}
```

### 批量更新：update()
```python
student = {"姓名": "小明", "年齡": 18}

# 用另一個字典更新
new_info = {"科系": "資工系", "年級": "大一", "年齡": 19}
student.update(new_info)

print(student)
# {'姓名': '小明', '年齡': 19, '科系': '資工系', '年級': '大一'}
```

## 6. 字典的常用方法

### 6.1 取得鍵、值、項目

```python
student = {
    "姓名": "小明",
    "年齡": 18,
    "科系": "資工系"
}

# 取得所有鍵
keys = student.keys()
print(list(keys))  # ['姓名', '年齡', '科系']

# 取得所有值
values = student.values()
print(list(values))  # ['小明', 18, '資工系']

# 取得所有鍵值對
items = student.items()
print(list(items))  # [('姓名', '小明'), ('年齡', 18), ('科系', '資工系')]
```

### 6.2 刪除元素

```python
student = {
    "姓名": "小明",
    "年齡": 18,
    "科系": "資工系",
    "電話": "0912-345-678"
}

# pop()：刪除指定鍵並返回值
phone = student.pop("電話")
print(f"刪除的電話：{phone}")  # 刪除的電話：0912-345-678

# pop()設定預設值
email = student.pop("email", "無")
print(f"email：{email}")  # email：無

# del：刪除指定鍵
del student["科系"]

# popitem()：刪除並返回最後一個鍵值對
last_item = student.popitem()
print(f"刪除的項目：{last_item}")

# clear()：清空字典
student.clear()
print(student)  # {}
```

### 6.3 複製字典

```python
original = {"a": 1, "b": 2, "c": 3}

# 淺複製
copy1 = original.copy()
copy2 = dict(original)

# 修改複製品不會影響原本
copy1["d"] = 4
print(f"原字典：{original}")  # 原字典：{'a': 1, 'b': 2, 'c': 3}
print(f"複製品：{copy1}")     # 複製品：{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## 7. 遍歷字典

### 方法1：遍歷鍵
```python
student = {"姓名": "小明", "年齡": 18, "科系": "資工系"}

for key in student:
    print(f"{key}: {student[key]}")

# 或者明確使用keys()
for key in student.keys():
    print(f"{key}: {student[key]}")
```

### 方法2：遍歷值
```python
student = {"姓名": "小明", "年齡": 18, "科系": "資工系"}

for value in student.values():
    print(value)
```

### 方法3：同時遍歷鍵和值
```python
student = {"姓名": "小明", "年齡": 18, "科系": "資工系"}

for key, value in student.items():
    print(f"{key}: {value}")
```

## 8. 巢狀字典

### 什麼是巢狀字典？
字典裡面還有字典，就像是**文件夾裡面還有子文件夾**：

```python
# 班級資料
class_data = {
    "班級": "資工一A",
    "導師": "王教授",
    "學生": {
        "A001": {
            "姓名": "小明",
            "年齡": 18,
            "成績": {"國文": 85, "英文": 92, "數學": 78}
        },
        "A002": {
            "姓名": "小美",
            "年齡": 19,
            "成績": {"國文": 96, "英文": 88, "數學": 91}
        }
    }
}

# 存取巢狀資料
print(class_data["班級"])                    # 資工一A
print(class_data["學生"]["A001"]["姓名"])    # 小明
print(class_data["學生"]["A001"]["成績"]["數學"])  # 78
```

### 修改巢狀字典
```python
# 修改學生成績
class_data["學生"]["A001"]["成績"]["數學"] = 85

# 新增學生
class_data["學生"]["A003"] = {
    "姓名": "小華",
    "年齡": 18,
    "成績": {"國文": 79, "英文": 85, "數學": 83}
}
```

### 遍歷巢狀字典
```python
for student_id, student_info in class_data["學生"].items():
    print(f"\n學號：{student_id}")
    print(f"姓名：{student_info['姓名']}")
    print(f"年齡：{student_info['年齡']}")
    print("成績：")
    for subject, score in student_info["成績"].items():
        print(f"  {subject}：{score}")
```

## 9. 字典的實用應用

### 應用1：計數器
```python
text = "hello world"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# 更簡潔的方式
char_count2 = {}
for char in text:
    char_count2[char] = char_count2.get(char, 0) + 1
```

### 應用2：分組資料
```python
students = [
    {"姓名": "小明", "性別": "男", "年級": "一年級"},
    {"姓名": "小美", "性別": "女", "年級": "一年級"},
    {"姓名": "小華", "性別": "男", "年級": "二年級"},
    {"姓名": "小雅", "性別": "女", "年級": "二年級"}
]

# 按性別分組
by_gender = {}
for student in students:
    gender = student["性別"]
    if gender not in by_gender:
        by_gender[gender] = []
    by_gender[gender].append(student["姓名"])

print(by_gender)
# {'男': ['小明', '小華'], '女': ['小美', '小雅']}
```

### 應用3：查詢表
```python
# 成績等第查詢表
grade_scale = {
    (90, 100): "A",
    (80, 89): "B",
    (70, 79): "C",
    (60, 69): "D",
    (0, 59): "F"
}

def get_grade(score):
    for (min_score, max_score), letter in grade_scale.items():
        if min_score <= score <= max_score:
            return letter
    return "無效分數"

print(get_grade(85))  # B
print(get_grade(92))  # A
```

## 10. 實作項目：通訊錄管理程式

讓我們建立一個完整的通訊錄管理系統：

```python
def display_menu():
    print("\n📞 通訊錄管理系統")
    print("1. 📋 查看所有聯絡人")
    print("2. ➕ 新增聯絡人")
    print("3. 🔍 搜尋聯絡人")
    print("4. 📝 修改聯絡人")
    print("5. ❌ 刪除聯絡人")
    print("6. 📊 統計資料")
    print("7. 🚪 離開程式")

def main():
    contacts = {
        "小明": {
            "電話": "0912-345-678",
            "email": "xiaoming@example.com",
            "地址": "台北市信義區",
            "生日": "1990-05-15",
            "分類": "朋友"
        },
        "小美": {
            "電話": "0987-654-321", 
            "email": "xiaomei@example.com",
            "地址": "台中市西區",
            "生日": "1992-08-20",
            "分類": "同事"
        }
    }
    
    while True:
        display_menu()
        choice = input("\n請選擇功能 (1-7): ")
        
        if choice == "1":
            # 查看所有聯絡人
            if contacts:
                print(f"\n📋 通訊錄（共{len(contacts)}位聯絡人）")
                print("="*50)
                for name, info in contacts.items():
                    print(f"\n👤 {name} ({info['分類']})")
                    print(f"📞 電話：{info['電話']}")
                    print(f"📧 Email：{info['email']}")
                    print(f"🏠 地址：{info['地址']}")
                    print(f"🎂 生日：{info['生日']}")
            else:
                print("\n❌ 通訊錄是空的！")
        
        elif choice == "2":
            # 新增聯絡人
            print("\n➕ 新增聯絡人")
            name = input("姓名：").strip()
            
            if not name:
                print("❌ 姓名不能為空！")
                continue
            
            if name in contacts:
                print("❌ 此聯絡人已存在！")
                continue
            
            phone = input("電話：").strip()
            email = input("Email：").strip()
            address = input("地址：").strip()
            birthday = input("生日（YYYY-MM-DD）：").strip()
            
            print("分類選項：朋友、家人、同事、其他")
            category = input("分類：").strip() or "其他"
            
            contacts[name] = {
                "電話": phone,
                "email": email,
                "地址": address,
                "生日": birthday,
                "分類": category
            }
            
            print(f"✅ 成功新增聯絡人：{name}")
        
        elif choice == "3":
            # 搜尋聯絡人
            if not contacts:
                print("\n❌ 通訊錄是空的！")
                continue
            
            keyword = input("\n🔍 請輸入搜尋關鍵字（姓名/電話/分類）：").strip().lower()
            found = []
            
            for name, info in contacts.items():
                if (keyword in name.lower() or 
                    keyword in info["電話"] or 
                    keyword in info["分類"].lower()):
                    found.append((name, info))
            
            if found:
                print(f"\n🔍 找到 {len(found)} 個相關結果：")
                for name, info in found:
                    print(f"\n👤 {name}")
                    print(f"📞 {info['電話']} | 📧 {info['email']}")
                    print(f"🏠 {info['地址']} | 🎂 {info['生日']}")
                    print(f"🏷️  分類：{info['分類']}")
            else:
                print("❌ 沒有找到相關聯絡人")
        
        elif choice == "4":
            # 修改聯絡人
            if not contacts:
                print("\n❌ 通訊錄是空的！")
                continue
            
            name = input("\n📝 請輸入要修改的聯絡人姓名：").strip()
            if name not in contacts:
                print("❌ 找不到此聯絡人！")
                continue
            
            print(f"\n目前 {name} 的資料：")
            info = contacts[name]
            print(f"1. 電話：{info['電話']}")
            print(f"2. Email：{info['email']}")
            print(f"3. 地址：{info['地址']}")
            print(f"4. 生日：{info['生日']}")
            print(f"5. 分類：{info['分類']}")
            
            field_choice = input("請選擇要修改的欄位 (1-5)：")
            fields = ["電話", "email", "地址", "生日", "分類"]
            
            if field_choice.isdigit() and 1 <= int(field_choice) <= 5:
                field_name = fields[int(field_choice) - 1]
                new_value = input(f"請輸入新的{field_name}：").strip()
                if new_value:
                    contacts[name][field_name] = new_value
                    print(f"✅ 已更新 {name} 的{field_name}")
                else:
                    print("❌ 輸入不能為空！")
            else:
                print("❌ 無效的選擇！")
        
        elif choice == "5":
            # 刪除聯絡人
            if not contacts:
                print("\n❌ 通訊錄是空的！")
                continue
            
            name = input("\n❌ 請輸入要刪除的聯絡人姓名：").strip()
            if name in contacts:
                confirm = input(f"確定要刪除 {name} 嗎？(y/N): ").lower()
                if confirm == 'y':
                    del contacts[name]
                    print(f"✅ 已刪除聯絡人：{name}")
                else:
                    print("❌ 取消刪除")
            else:
                print("❌ 找不到此聯絡人！")
        
        elif choice == "6":
            # 統計資料
            if not contacts:
                print("\n❌ 通訊錄是空的！")
                continue
            
            print(f"\n📊 通訊錄統計")
            print("="*30)
            print(f"總聯絡人數：{len(contacts)}")
            
            # 按分類統計
            categories = {}
            for info in contacts.values():
                category = info["分類"]
                categories[category] = categories.get(category, 0) + 1
            
            print("\n分類統計：")
            for category, count in categories.items():
                print(f"  {category}：{count} 人")
            
            # 生日月份統計
            birth_months = {}
            for name, info in contacts.items():
                try:
                    month = info["生日"].split("-")[1]
                    birth_months[month] = birth_months.get(month, 0) + 1
                except:
                    pass  # 忽略格式錯誤的生日
            
            if birth_months:
                print("\n生日月份分佈：")
                for month, count in sorted(birth_months.items()):
                    print(f"  {month}月：{count} 人")
        
        elif choice == "7":
            print("\n👋 感謝使用通訊錄管理系統，再見！")
            break
        
        else:
            print("❌ 無效的選擇，請輸入1-7！")

if __name__ == "__main__":
    main()
```

## 11. 常見錯誤與解決

### 錯誤1：鍵不存在
```python
# 錯誤
data = {"name": "小明"}
# print(data["age"])  # KeyError

# 正確：使用get()或先檢查
age = data.get("age", "未知")
# 或
if "age" in data:
    print(data["age"])
```

### 錯誤2：鍵的資料型別
```python
# 錯誤：使用可變物件作為鍵
# data = {[1, 2]: "value"}  # TypeError

# 正確：使用不可變物件
data = {(1, 2): "value"}  # 元組可以作為鍵
data = {"1,2": "value"}   # 字串可以作為鍵
```

## 12. 今日總結

今天你學會了：
- ✅ 字典的概念和重要性
- ✅ 建立、存取、修改字典
- ✅ 字典的常用方法
- ✅ 巢狀字典的操作
- ✅ 遍歷字典的不同方法
- ✅ 製作完整的通訊錄程式

## 13. 明日預告

明天我們將學習：
- 元組（Tuple）的概念
- 不可變序列的特性
- 元組的應用場景
- 製作座標系統程式

## 14. 作業練習

1. 建立一個學生成績字典，包含多個學生的多科成績
2. 實作一個簡單的商品庫存管理系統
3. 建立一個單字翻譯字典程式
4. 嘗試使用字典來統計文字中每個單字的出現次數

記住：**字典是處理對應關係資料的最佳選擇，掌握字典操作能大大提升程式的效率和可讀性！**