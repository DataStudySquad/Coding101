# 變數型態示例

# 字串變數
name = "小明"
hobby = "閱讀"
message = "Hello World"

# 數字變數
age = 25
score = 95
height = 170.5
weight = 65.2

# 布林變數
is_student = True
is_married = False

# 印出變數和其型態
print("=== 變數內容 ===")
print("姓名：", name, "型態：", type(name))
print("年齡：", age, "型態：", type(age))
print("身高：", height, "型態：", type(height))
print("學生？", is_student, "型態：", type(is_student))

# 變數賦值示例
print("\n=== 變數賦值 ===")
x = 10
print("x =", x)
x = 20  # 改變變數值
print("x =", x)

# 多重賦值
a, b, c = 1, 2, 3
print("a =", a, "b =", b, "c =", c)