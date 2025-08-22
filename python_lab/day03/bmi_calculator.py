print("=== BMI計算器 ===")
name = input("姓名：")
weight = float(input("體重(公斤)："))
height = float(input("身高(公分)："))

height_m = height / 100  # 轉換為公尺
bmi = weight / (height_m ** 2)

print(f"\n{name}的BMI計算結果：")
print(f"身高：{height}公分")
print(f"體重：{weight}公斤")
print(f"BMI：{bmi:.2f}")  # 保留兩位小數