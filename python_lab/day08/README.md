# Day 8：迴圈概念（for）

## 今日學習目標
- 理解迴圈的概念和重要性
- 掌握for迴圈的基本語法
- 學會使用range()函數
- 實作九九乘法表和其他實用程式

## 1. 什麼是迴圈？

想像一下你要做這些事情：
- **抄寫課文10遍**
- **檢查班上30個學生的出席**
- **計算1到100的總和**

如果沒有迴圈，你需要寫很多重複的程式碼：
```python
# 沒有迴圈的話...
print("1")
print("2") 
print("3")
print("4")
print("5")
# ... 一直到100，太麻煩了！
```

### 迴圈就像是「重複執行的指令」
就像告訴助手：「把這件事重複做10次」

## 2. for迴圈基本語法

### 基本結構
```python
for 變數名稱 in 序列:
    要重複執行的程式碼
```

### 第一個例子
```python
# 印出1到5
for i in range(1, 6):
    print(i)
```

**解釋：**
- `for`：迴圈關鍵字
- `i`：迴圈變數（習慣用i, j, k等）
- `range(1, 6)`：產生1到5的數字序列
- `print(i)`：重複執行的動作

## 3. range()函數詳解

range()函數就像是**數字產生器**：

### 三種用法

#### 用法一：range(結束值)
```python
# range(5) 產生 0, 1, 2, 3, 4
for i in range(5):
    print(i)
```

#### 用法二：range(開始值, 結束值)
```python
# range(1, 6) 產生 1, 2, 3, 4, 5
for i in range(1, 6):
    print(i)
```

#### 用法三：range(開始值, 結束值, 步進值)
```python
# range(2, 11, 2) 產生 2, 4, 6, 8, 10
for i in range(2, 11, 2):
    print(i)
```

### 重要提醒
- 結束值**不包含**在序列中
- range(1, 6)實際產生1, 2, 3, 4, 5

## 4. 實用範例

### 範例1：問候語
```python
names = ["小明", "小美", "小華"]
for name in names:
    print(f"你好，{name}！")
```

### 範例2：計算總和
```python
total = 0
for i in range(1, 11):
    total += i
print(f"1到10的總和是：{total}")
```

### 範例3：星星圖案
```python
for i in range(1, 6):
    print("★" * i)
```

### 範例4：倒數計時
```python
for i in range(10, 0, -1):
    print(f"倒數：{i}")
print("時間到！")
```

## 5. 巢狀迴圈

迴圈裡面還可以有迴圈，就像**盒子裡還有小盒子**：

```python
# 印出乘法表
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")  # 分隔線
```

## 6. 實作練習：九九乘法表

讓我們用迴圈做出完整的九九乘法表：

```python
print("九九乘法表")
print("=" * 30)

for i in range(1, 10):
    print(f"\n{i}的乘法表：")
    for j in range(1, 10):
        result = i * j
        print(f"{i} x {j} = {result:2d}")
```

## 7. 迴圈的實際應用

### 應用1：成績統計
```python
scores = [85, 92, 78, 96, 88]
total = 0
count = 0

for score in scores:
    total += score
    count += 1

average = total / count
print(f"平均成績：{average:.1f}")
```

### 應用2：尋找最大值
```python
numbers = [45, 23, 89, 12, 67]
max_num = numbers[0]  # 假設第一個是最大的

for num in numbers:
    if num > max_num:
        max_num = num

print(f"最大值是：{max_num}")
```

## 8. 常見錯誤與解決

### 錯誤1：忘記縮排
```python
# 錯誤
for i in range(5):
print(i)  # 沒有縮排

# 正確
for i in range(5):
    print(i)  # 有縮排
```

### 錯誤2：range使用錯誤
```python
# 想要1到5，但寫錯了
for i in range(1, 5):  # 只會有1,2,3,4
    print(i)

# 正確
for i in range(1, 6):  # 才會有1,2,3,4,5
    print(i)
```

## 9. 進階小技巧

### 技巧1：enumerate()函數
當你需要同時知道元素和位置：
```python
fruits = ["蘋果", "香蕉", "橘子"]
for index, fruit in enumerate(fruits):
    print(f"第{index + 1}個水果是：{fruit}")
```

### 技巧2：迴圈變數命名
- 用有意義的名稱：`for student in students`
- 而不是：`for i in students`

## 10. 實作作業

創建 `for_loop_practice.py`：

```python
# 練習1：印出你的名字5次
print("練習1：")
name = input("請輸入你的名字：")
for i in range(5):
    print(f"第{i+1}次：{name}")

# 練習2：計算1到50的總和
print("\n練習2：")
total = 0
for i in range(1, 51):
    total += i
print(f"1到50的總和：{total}")

# 練習3：印出偶數
print("\n練習3：")
print("1到20的偶數：")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# 練習4：簡單的圖案
print("\n練習4：")
for i in range(1, 6):
    print("♥" * i)
```

## 11. 今日總結

今天你學會了：
- ✅ 迴圈的概念和重要性
- ✅ for迴圈的語法結構
- ✅ range()函數的三種用法
- ✅ 巢狀迴圈的概念
- ✅ 實用的迴圈應用

## 12. 明日預告

明天我們將學習：
- while迴圈的概念
- break和continue關鍵字
- 製作猜數字遊戲

## 13. 重要概念回顧

- **迴圈**：重複執行相同程式碼的結構
- **range()**：產生數字序列的函數
- **縮排**：Python用縮排表示程式碼區塊
- **巢狀迴圈**：迴圈裡面包含另一個迴圈

記住：**迴圈是程式設計中處理重複工作的利器，掌握它可以讓你的程式更有效率！**