# 互動式對話程式
print("=== 歡迎使用個人助理 ===")
print("我想更認識你！")

# 收集使用者資料
name = input("請告訴我你的姓名：")
age = int(input("你幾歲了？"))
hobby = input("你的興趣是什麼？")
city = input("你住在哪個城市？")

# 計算一些有趣的資料
birth_year = 2024 - age
next_age = age + 1

# 友善的回應
print(f"\n很高興認識你，{name}！")
print(f"原來你是{birth_year}年出生的")
print(f"明年你就{next_age}歲了")
print(f"住在{city}很不錯呢！")
print(f"我也喜歡{hobby}，我們真有緣")

print("\n感謝你跟我分享這些資訊！")