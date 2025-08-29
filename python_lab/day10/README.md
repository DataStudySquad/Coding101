# Day 10：清單（List）

## 今日學習目標
- 理解清單的概念和重要性
- 掌握清單的建立、修改、存取方法
- 學會清單的常用方法
- 實作待辦事項清單程式

## 1. 什麼是清單？

### 生活中的清單概念
想像一下這些日常場景：
- **購物清單**：牛奶、麵包、蘋果、雞蛋
- **學生名單**：小明、小美、小華、小強
- **課程清單**：數學、英文、歷史、化學

### 程式中的清單
清單就像是一個**可以放很多東西的收納盒**：
- 可以放不同的物品（資料）
- 物品有順序（索引）
- 可以隨時增加或移除物品
- 可以知道盒子裡有什麼、有幾個

```python
# 程式中的清單
shopping_list = ["牛奶", "麵包", "蘋果", "雞蛋"]
student_names = ["小明", "小美", "小華", "小強"]
scores = [85, 92, 78, 96, 88]
```

## 2. 建立清單

### 方法1：直接建立
```python
# 空清單
empty_list = []

# 有內容的清單
fruits = ["蘋果", "香蕉", "橘子"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["小明", 25, True, 3.14]  # 可以混合不同資料型態
```

### 方法2：使用list()函數
```python
# 將字串轉成清單
letters = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']

# 將range轉成清單
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
```

### 方法3：重複建立
```python
# 建立重複元素的清單
zeros = [0] * 5  # [0, 0, 0, 0, 0]
greetings = ["Hello"] * 3  # ["Hello", "Hello", "Hello"]
```

## 3. 存取清單元素

### 索引的概念
清單中的每個位置都有一個**門牌號碼**（索引）：

```python
fruits = ["蘋果", "香蕉", "橘子", "芒果"]
#         [0]    [1]    [2]    [3]    # 正向索引
#        [-4]   [-3]   [-2]   [-1]    # 反向索引
```

### 正向索引（從0開始）
```python
fruits = ["蘋果", "香蕉", "橘子", "芒果"]

print(fruits[0])    # 蘋果（第一個）
print(fruits[1])    # 香蕉（第二個）
print(fruits[3])    # 芒果（第四個）
```

### 反向索引（從-1開始）
```python
fruits = ["蘋果", "香蕉", "橘子", "芒果"]

print(fruits[-1])   # 芒果（最後一個）
print(fruits[-2])   # 橘子（倒數第二個）
print(fruits[-4])   # 蘋果（倒數第四個）
```

### 索引錯誤
```python
fruits = ["蘋果", "香蕉", "橘子"]

# print(fruits[5])  # IndexError！清單只有3個元素（索引0-2）
```

## 4. 修改清單元素

### 直接修改
```python
fruits = ["蘋果", "香蕉", "橘子"]
print("修改前：", fruits)

fruits[1] = "草莓"  # 將第二個元素改成草莓
print("修改後：", fruits)  # ['蘋果', '草莓', '橘子']
```

### 修改多個元素
```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30]  # 將索引1-2的元素替換
print(numbers)  # [1, 20, 30, 4, 5]
```

## 5. 清單的常用方法

### 5.1 新增元素

#### append()：在末尾新增一個元素
```python
fruits = ["蘋果", "香蕉"]
fruits.append("橘子")
print(fruits)  # ['蘋果', '香蕉', '橘子']
```

#### insert()：在指定位置插入元素
```python
fruits = ["蘋果", "香蕉", "橘子"]
fruits.insert(1, "草莓")  # 在索引1的位置插入草莓
print(fruits)  # ['蘋果', '草莓', '香蕉', '橘子']
```

#### extend()：合併兩個清單
```python
fruits = ["蘋果", "香蕉"]
more_fruits = ["橘子", "芒果"]
fruits.extend(more_fruits)
print(fruits)  # ['蘋果', '香蕉', '橘子', '芒果']
```

### 5.2 移除元素

#### remove()：移除指定值的第一個元素
```python
fruits = ["蘋果", "香蕉", "橘子", "香蕉"]
fruits.remove("香蕉")  # 只移除第一個香蕉
print(fruits)  # ['蘋果', '橘子', '香蕉']
```

#### pop()：移除並返回指定位置的元素
```python
fruits = ["蘋果", "香蕉", "橘子"]
last_fruit = fruits.pop()    # 移除最後一個
print(last_fruit)  # 橘子
print(fruits)      # ['蘋果', '香蕉']

first_fruit = fruits.pop(0)  # 移除第一個
print(first_fruit) # 蘋果
print(fruits)      # ['香蕉']
```

#### clear()：清空整個清單
```python
fruits = ["蘋果", "香蕉", "橘子"]
fruits.clear()
print(fruits)  # []
```

### 5.3 查詢方法

#### index()：找出元素的位置
```python
fruits = ["蘋果", "香蕉", "橘子"]
position = fruits.index("香蕉")
print(position)  # 1
```

#### count()：計算元素出現次數
```python
numbers = [1, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(count)  # 3
```

#### in 關鍵字：檢查元素是否存在
```python
fruits = ["蘋果", "香蕉", "橘子"]
print("香蕉" in fruits)     # True
print("草莓" in fruits)     # False
print("草莓" not in fruits) # True
```

### 5.4 排序方法

#### sort()：永久排序（修改原清單）
```python
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# 反向排序
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]
```

#### sorted()：暫時排序（不修改原清單）
```python
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print("原清單：", numbers)        # [3, 1, 4, 1, 5, 9, 2]
print("排序後：", sorted_numbers) # [1, 1, 2, 3, 4, 5, 9]
```

#### reverse()：反轉清單
```python
fruits = ["蘋果", "香蕉", "橘子"]
fruits.reverse()
print(fruits)  # ['橘子', '香蕉', '蘋果']
```

## 6. 清單的實用操作

### 清單長度
```python
fruits = ["蘋果", "香蕉", "橘子"]
print(len(fruits))  # 3
```

### 清單運算
```python
# 合併清單
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# 重複清單
repeated = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]
```

### 最大值、最小值、總和
```python
numbers = [10, 5, 8, 3, 12]
print(max(numbers))  # 12
print(min(numbers))  # 3
print(sum(numbers))  # 38
```

## 7. 遍歷清單

### 方法1：直接遍歷元素
```python
fruits = ["蘋果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"我喜歡{fruit}")
```

### 方法2：使用索引
```python
fruits = ["蘋果", "香蕉", "橘子"]
for i in range(len(fruits)):
    print(f"第{i+1}個水果是：{fruits[i]}")
```

### 方法3：同時取得索引和值
```python
fruits = ["蘋果", "香蕉", "橘子"]
for index, fruit in enumerate(fruits):
    print(f"索引{index}：{fruit}")
```

## 8. 實作範例：成績管理

```python
# 建立學生成績清單
student_scores = []

# 輸入成績
print("請輸入學生成績（輸入-1結束）：")
while True:
    score = float(input("成績："))
    if score == -1:
        break
    if 0 <= score <= 100:
        student_scores.append(score)
    else:
        print("成績必須在0-100之間！")

# 統計分析
if student_scores:
    print(f"\n📊 成績統計")
    print(f"學生人數：{len(student_scores)}")
    print(f"最高分：{max(student_scores)}")
    print(f"最低分：{min(student_scores)}")
    print(f"平均分：{sum(student_scores)/len(student_scores):.2f}")
    
    # 排序顯示
    sorted_scores = sorted(student_scores, reverse=True)
    print(f"成績排名：{sorted_scores}")
    
    # 等第統計
    excellent = [s for s in student_scores if s >= 90]
    good = [s for s in student_scores if 80 <= s < 90]
    pass_scores = [s for s in student_scores if 60 <= s < 80]
    fail = [s for s in student_scores if s < 60]
    
    print(f"優秀（90+）：{len(excellent)}人")
    print(f"良好（80-89）：{len(good)}人")
    print(f"及格（60-79）：{len(pass_scores)}人")
    print(f"不及格（<60）：{len(fail)}人")
```

## 9. 實作項目：待辦事項清單

讓我們建立一個完整的待辦事項管理程式：

```python
def display_menu():
    print("\n📝 待辦事項管理程式")
    print("1. 📋 查看所有待辦事項")
    print("2. ➕ 新增待辦事項")
    print("3. ✅ 標記為已完成")
    print("4. ❌ 刪除待辦事項")
    print("5. 📊 顯示統計資料")
    print("6. 🚪 離開程式")

def main():
    todo_list = []
    completed_list = []
    
    while True:
        display_menu()
        choice = input("\n請選擇功能 (1-6): ")
        
        if choice == "1":
            # 查看待辦事項
            print("\n📋 目前的待辦事項：")
            if todo_list:
                for i, item in enumerate(todo_list, 1):
                    print(f"{i}. {item}")
            else:
                print("目前沒有待辦事項！")
            
            if completed_list:
                print("\n✅ 已完成的事項：")
                for i, item in enumerate(completed_list, 1):
                    print(f"{i}. {item}")
        
        elif choice == "2":
            # 新增待辦事項
            new_item = input("\n請輸入新的待辦事項：").strip()
            if new_item:
                todo_list.append(new_item)
                print(f"✅ 已新增：{new_item}")
            else:
                print("❌ 事項不能為空！")
        
        elif choice == "3":
            # 標記為已完成
            if not todo_list:
                print("❌ 沒有待辦事項可以完成！")
                continue
            
            print("\n📋 選擇要完成的事項：")
            for i, item in enumerate(todo_list, 1):
                print(f"{i}. {item}")
            
            try:
                index = int(input("請輸入編號：")) - 1
                if 0 <= index < len(todo_list):
                    completed_item = todo_list.pop(index)
                    completed_list.append(completed_item)
                    print(f"🎉 已完成：{completed_item}")
                else:
                    print("❌ 編號無效！")
            except ValueError:
                print("❌ 請輸入有效的數字！")
        
        elif choice == "4":
            # 刪除待辦事項
            if not todo_list:
                print("❌ 沒有待辦事項可以刪除！")
                continue
            
            print("\n🗑️ 選擇要刪除的事項：")
            for i, item in enumerate(todo_list, 1):
                print(f"{i}. {item}")
            
            try:
                index = int(input("請輸入編號：")) - 1
                if 0 <= index < len(todo_list):
                    deleted_item = todo_list.pop(index)
                    print(f"🗑️ 已刪除：{deleted_item}")
                else:
                    print("❌ 編號無效！")
            except ValueError:
                print("❌ 請輸入有效的數字！")
        
        elif choice == "5":
            # 顯示統計
            total_todo = len(todo_list)
            total_completed = len(completed_list)
            total_items = total_todo + total_completed
            
            print(f"\n📊 統計資料")
            print(f"待辦事項：{total_todo} 項")
            print(f"已完成事項：{total_completed} 項")
            print(f"總事項數：{total_items} 項")
            
            if total_items > 0:
                completion_rate = (total_completed / total_items) * 100
                print(f"完成率：{completion_rate:.1f}%")
        
        elif choice == "6":
            print("👋 感謝使用待辦事項管理程式，再見！")
            break
        
        else:
            print("❌ 無效的選擇，請輸入1-6！")

if __name__ == "__main__":
    main()
```

## 10. 常見錯誤與解決

### 錯誤1：索引超出範圍
```python
# 錯誤
my_list = [1, 2, 3]
# print(my_list[3])  # IndexError

# 正確：先檢查長度
if len(my_list) > 3:
    print(my_list[3])
else:
    print("索引超出範圍")
```

### 錯誤2：在迴圈中修改清單
```python
# 錯誤：可能跳過某些元素
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # 危險！

# 正確：使用副本或反向迴圈
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # 使用副本
    if num % 2 == 0:
        numbers.remove(num)
```

## 11. 今日總結

今天你學會了：
- ✅ 清單的概念和重要性
- ✅ 建立、存取、修改清單
- ✅ 清單的常用方法（增刪改查）
- ✅ 清單的排序和反轉
- ✅ 遍歷清單的不同方法
- ✅ 製作完整的待辦事項程式

## 12. 明日預告

明天我們將學習：
- 清單的進階操作（切片）
- 清單推導式（List Comprehension）
- 多維清單的概念
- 製作成績統計分析程式

## 13. 作業練習

1. 建立一個班級學生名單管理程式
2. 實作一個簡單的購物清單程式
3. 嘗試用清單記錄你一週的學習進度

記住：**清單是程式設計中最重要的資料結構之一，熟練掌握清單操作是寫好程式的基礎！**