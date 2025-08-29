"""
Day 18: 模組與套件練習
練習各種import方式和標準模組的使用
"""

# =============== import 語句練習 ===============

# 1. 完整導入模組
import math
import random
import datetime
import string

# 2. 從模組導入特定功能
from os import getcwd, path
from json import dumps, loads

# 3. 使用別名導入
import datetime as dt
import random as rnd

# 4. 導入多個功能
from math import pi, sqrt, sin, cos, pow

print("🐍 Python 模組與套件練習")
print("=" * 50)

# =============== math 模組練習 ===============

def math_module_demo():
    """math 模組示範"""
    print("\n🧮 math 模組練習")
    print("-" * 30)
    
    # 數學常數
    print(f"圓周率 π = {math.pi:.6f}")
    print(f"自然對數底 e = {math.e:.6f}")
    
    # 基本數學運算
    print(f"\n基本運算:")
    print(f"√16 = {math.sqrt(16)}")
    print(f"2^8 = {math.pow(2, 8)}")
    print(f"3! = {math.factorial(3)}")
    print(f"|−5| = {math.fabs(-5)}")
    
    # 三角函數
    print(f"\n三角函數:")
    print(f"sin(π/2) = {math.sin(math.pi/2):.3f}")
    print(f"cos(0) = {math.cos(0)}")
    print(f"tan(π/4) = {math.tan(math.pi/4):.3f}")
    
    # 對數函數
    print(f"\n對數函數:")
    print(f"log₂(8) = {math.log2(8)}")
    print(f"log₁₀(100) = {math.log10(100)}")
    print(f"ln(e) = {math.log(math.e):.3f}")
    
    # 取整函數
    print(f"\n取整函數:")
    print(f"ceil(4.2) = {math.ceil(4.2)}")   # 向上取整
    print(f"floor(4.8) = {math.floor(4.8)}") # 向下取整
    print(f"trunc(4.7) = {math.trunc(4.7)}") # 截斷小數

def math_applications():
    """math 模組實際應用"""
    print("\n📐 math 模組實際應用:")
    
    # 計算兩點間距離
    def distance(x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    
    dist = distance(0, 0, 3, 4)
    print(f"點(0,0)到點(3,4)的距離: {dist}")
    
    # 計算圓的面積和周長
    def circle_info(radius):
        area = math.pi * math.pow(radius, 2)
        circumference = 2 * math.pi * radius
        return area, circumference
    
    area, circumference = circle_info(5)
    print(f"半徑5的圓 - 面積: {area:.2f}, 周長: {circumference:.2f}")
    
    # 角度轉換
    degrees = 45
    radians = math.radians(degrees)
    print(f"{degrees}度 = {radians:.3f}弧度")
    print(f"sin({degrees}°) = {math.sin(radians):.3f}")

# =============== random 模組練習 ===============

def random_module_demo():
    """random 模組示範"""
    print("\n🎲 random 模組練習")
    print("-" * 30)
    
    # 基本隨機數
    print(f"0-1隨機浮點數: {random.random():.3f}")
    print(f"1-10隨機整數: {random.randint(1, 10)}")
    print(f"0-9隨機整數: {random.randrange(10)}")
    print(f"1.0-5.0隨機浮點數: {random.uniform(1.0, 5.0):.2f}")
    
    # 隨機選擇
    colors = ["紅", "綠", "藍", "黃", "紫"]
    print(f"\n隨機選擇:")
    print(f"隨機顏色: {random.choice(colors)}")
    
    # 隨機抽樣
    sample_colors = random.sample(colors, 3)
    print(f"隨機抽3種顏色: {sample_colors}")
    
    # 加權選擇
    fruits = ["蘋果", "香蕉", "橘子"]
    weights = [1, 3, 2]  # 香蕉被選中的機率最高
    weighted_choice = random.choices(fruits, weights=weights, k=5)
    print(f"加權選擇5次: {weighted_choice}")
    
    # 打亂序列
    numbers = [1, 2, 3, 4, 5, 6]
    print(f"原序列: {numbers}")
    random.shuffle(numbers)
    print(f"打亂後: {numbers}")

def random_applications():
    """random 模組實際應用"""
    print("\n🎯 random 模組實際應用:")
    
    # 模擬擲骰子
    def roll_dice(sides=6, count=2):
        return [random.randint(1, sides) for _ in range(count)]
    
    dice_result = roll_dice()
    print(f"擲兩顆骰子: {dice_result}, 總和: {sum(dice_result)}")
    
    # 生成隨機密碼
    def generate_simple_password(length=8):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    
    password = generate_simple_password(10)
    print(f"隨機密碼: {password}")
    
    # 隨機抽獎
    def lottery_draw(participants, winners=3):
        return random.sample(participants, min(winners, len(participants)))
    
    participants = ["小明", "小美", "小華", "小李", "小王", "小張"]
    winners = lottery_draw(participants)
    print(f"抽獎結果: {winners}")
    
    # 隨機決策
    decisions = ["接受", "拒絕", "考慮一下"]
    decision = random.choice(decisions)
    print(f"隨機決策: {decision}")

# =============== datetime 模組練習 ===============

def datetime_module_demo():
    """datetime 模組示範"""
    print("\n📅 datetime 模組練習")
    print("-" * 30)
    
    # 獲取當前時間
    now = datetime.datetime.now()
    today = datetime.date.today()
    current_time = datetime.datetime.now().time()
    
    print(f"現在日期時間: {now}")
    print(f"今天日期: {today}")
    print(f"目前時間: {current_time}")
    
    # 時間格式化
    print(f"\n時間格式化:")
    print(f"標準格式: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"中文格式: {now.strftime('%Y年%m月%d日 %H時%M分')}")
    print(f"12小時制: {now.strftime('%Y-%m-%d %I:%M:%S %p')}")
    print(f"星期幾: {now.strftime('%A')} ({now.strftime('%w')})")
    
    # 創建特定時間
    birthday = datetime.date(1990, 5, 15)
    meeting = datetime.datetime(2024, 1, 15, 14, 30, 0)
    
    print(f"\n特定時間:")
    print(f"生日: {birthday}")
    print(f"會議時間: {meeting}")
    
    # 時間計算
    print(f"\n時間計算:")
    
    # 年齡計算
    age_days = today - birthday
    age_years = age_days.days // 365
    print(f"年齡: {age_years}年 ({age_days.days}天)")
    
    # 未來時間
    tomorrow = today + datetime.timedelta(days=1)
    next_week = today + datetime.timedelta(weeks=1)
    next_month = today + datetime.timedelta(days=30)
    
    print(f"明天: {tomorrow}")
    print(f"下週: {next_week}")
    print(f"下月: {next_month}")

def datetime_applications():
    """datetime 模組實際應用"""
    print("\n🕒 datetime 模組實際應用:")
    
    # 計算工作日
    def is_weekday(date):
        return date.weekday() < 5  # 0-4是週一到週五
    
    today = datetime.date.today()
    print(f"今天是工作日: {is_weekday(today)}")
    
    # 計算年齡
    def calculate_age(birth_date):
        today = datetime.date.today()
        age = today.year - birth_date.year
        if today < birth_date.replace(year=today.year):
            age -= 1
        return age
    
    birth = datetime.date(1995, 3, 15)
    age = calculate_age(birth)
    print(f"1995/3/15出生的人現在{age}歲")
    
    # 倒數計時
    def countdown_to_date(target_date):
        today = datetime.date.today()
        diff = target_date - today
        return diff.days
    
    new_year = datetime.date(2025, 1, 1)
    days_left = countdown_to_date(new_year)
    print(f"距離2025年還有{days_left}天")
    
    # 時間戳轉換
    timestamp = datetime.datetime.now().timestamp()
    from_timestamp = datetime.datetime.fromtimestamp(timestamp)
    print(f"時間戳: {timestamp}")
    print(f"從時間戳轉回: {from_timestamp}")

# =============== string 模組練習 ===============

def string_module_demo():
    """string 模組示範"""
    print("\n📝 string 模組練習")
    print("-" * 30)
    
    # 字符常數
    print(f"小寫字母: {string.ascii_lowercase}")
    print(f"大寫字母: {string.ascii_uppercase}")
    print(f"所有字母: {string.ascii_letters}")
    print(f"數字: {string.digits}")
    print(f"16進制數字: {string.hexdigits}")
    print(f"8進制數字: {string.octdigits}")
    print(f"標點符號: {string.punctuation}")
    print(f"空白字符: '{string.whitespace}'")
    
    # Template 類別
    print(f"\n字串模板:")
    template = string.Template("Hello, $name! You are $age years old.")
    result = template.substitute(name="小明", age=18)
    print(f"模板結果: {result}")
    
    # 安全替換（缺少變數不會出錯）
    safe_result = template.safe_substitute(name="小美")
    print(f"安全替換: {safe_result}")

def string_applications():
    """string 模組實際應用"""
    print("\n🔧 string 模組實際應用:")
    
    # 生成各種字符集
    def get_charset(include_letters=True, include_digits=True, include_symbols=False):
        charset = ""
        if include_letters:
            charset += string.ascii_letters
        if include_digits:
            charset += string.digits
        if include_symbols:
            charset += string.punctuation
        return charset
    
    charset = get_charset()
    print(f"字符集 (字母+數字): {len(charset)} 個字符")
    
    full_charset = get_charset(include_symbols=True)
    print(f"完整字符集: {len(full_charset)} 個字符")
    
    # 檢查字符類型
    def analyze_char(char):
        info = []
        if char in string.ascii_lowercase:
            info.append("小寫字母")
        if char in string.ascii_uppercase:
            info.append("大寫字母")
        if char in string.digits:
            info.append("數字")
        if char in string.punctuation:
            info.append("標點符號")
        return info
    
    test_chars = ['a', 'Z', '5', '!', ' ']
    print(f"\n字符分析:")
    for char in test_chars:
        types = analyze_char(char)
        print(f"'{char}': {types if types else ['其他']}")
    
    # 密碼強度檢查
    def check_password_strength(password):
        score = 0
        feedback = []
        
        if any(c in string.ascii_lowercase for c in password):
            score += 1
            feedback.append("包含小寫字母")
        
        if any(c in string.ascii_uppercase for c in password):
            score += 1
            feedback.append("包含大寫字母")
        
        if any(c in string.digits for c in password):
            score += 1
            feedback.append("包含數字")
        
        if any(c in string.punctuation for c in password):
            score += 1
            feedback.append("包含特殊符號")
        
        strength = ["非常弱", "弱", "中等", "強", "非常強"][score]
        return strength, feedback
    
    test_password = "MyPass123!"
    strength, feedback = check_password_strength(test_password)
    print(f"\n密碼強度檢查:")
    print(f"密碼: {test_password}")
    print(f"強度: {strength}")
    print(f"特點: {', '.join(feedback)}")

# =============== os 模組練習 ===============

def os_module_demo():
    """os 模組示範（安全版本）"""
    print("\n💻 os 模組練習")
    print("-" * 30)
    
    # 目錄操作
    current_dir = getcwd()
    print(f"當前工作目錄: {current_dir}")
    
    # 路徑操作
    example_path = path.join("data", "files", "example.txt")
    print(f"路徑組合: {example_path}")
    
    # 路徑分析
    print(f"\n路徑分析:")
    test_path = "/home/user/documents/file.txt"
    print(f"原路徑: {test_path}")
    print(f"目錄名: {path.dirname(test_path)}")
    print(f"檔案名: {path.basename(test_path)}")
    print(f"檔案名(無擴展): {path.splitext(path.basename(test_path))[0]}")
    print(f"擴展名: {path.splitext(test_path)[1]}")
    
    # 檢查路徑
    print(f"\n路徑檢查:")
    print(f"當前目錄存在: {path.exists('.')}")
    print(f"是目錄: {path.isdir('.')}")
    print(f"是檔案: {path.isfile('README.md')}")
    print(f"絕對路徑: {path.isabs('/home/user')}")

# =============== json 模組練習 ===============

def json_module_demo():
    """json 模組示範"""
    print("\n📋 json 模組練習")
    print("-" * 30)
    
    # Python 物件轉 JSON
    data = {
        "name": "張小明",
        "age": 25,
        "city": "台北",
        "married": False,
        "children": None,
        "hobbies": ["閱讀", "電影", "旅行"],
        "education": {
            "degree": "學士",
            "major": "資訊工程",
            "school": "台北大學"
        }
    }
    
    # 序列化為 JSON 字串
    json_string = dumps(data, ensure_ascii=False, indent=2)
    print(f"JSON 序列化:")
    print(json_string)
    
    # 從 JSON 字串解析
    parsed_data = loads(json_string)
    print(f"\nJSON 解析:")
    print(f"姓名: {parsed_data['name']}")
    print(f"年齡: {parsed_data['age']}")
    print(f"興趣: {', '.join(parsed_data['hobbies'])}")
    print(f"學歷: {parsed_data['education']['school']} {parsed_data['education']['major']}")
    
    # 緊湊格式
    compact_json = dumps(data, ensure_ascii=False, separators=(',', ':'))
    print(f"\n緊湊格式 JSON:")
    print(compact_json[:50] + "...")

# =============== 模組別名練習 ===============

def alias_demo():
    """模組別名示範"""
    print("\n🏷️ 模組別名練習")
    print("-" * 30)
    
    # 使用 datetime 別名
    current = dt.datetime.now()
    print(f"使用 dt 別名: {current}")
    
    # 使用 random 別名
    lucky_number = rnd.randint(1, 100)
    print(f"使用 rnd 別名: 幸運數字 {lucky_number}")
    
    # 使用 from import 的函數
    circle_area = pi * pow(5, 2)
    print(f"使用導入的函數: 圓面積 = π × 5² = {circle_area:.2f}")
    
    # 三角函數
    angle_sin = sin(pi/4)
    angle_cos = cos(pi/4)
    print(f"sin(π/4) = {angle_sin:.3f}")
    print(f"cos(π/4) = {angle_cos:.3f}")

# =============== 綜合練習 ===============

def comprehensive_exercise():
    """綜合練習：隨機事件生成器"""
    print("\n🎪 綜合練習：隨機事件生成器")
    print("-" * 40)
    
    # 使用多個模組創建隨機事件
    events = [
        "參加會議", "寫程式", "看電影", "運動", "閱讀",
        "烹飪", "購物", "學習", "旅行", "睡覺"
    ]
    
    locations = ["家裡", "辦公室", "咖啡廳", "圖書館", "公園", "健身房"]
    
    # 生成隨機事件
    event = random.choice(events)
    location = random.choice(locations)
    
    # 生成隨機時間
    start_hour = random.randint(8, 20)
    start_minute = random.randint(0, 59)
    duration = random.randint(30, 180)  # 30到180分鐘
    
    # 計算結束時間
    start_time = datetime.datetime.now().replace(
        hour=start_hour, 
        minute=start_minute, 
        second=0, 
        microsecond=0
    )
    end_time = start_time + datetime.timedelta(minutes=duration)
    
    # 生成隨機ID
    event_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    # 使用 JSON 格式存儲事件
    event_data = {
        "id": event_id,
        "event": event,
        "location": location,
        "start_time": start_time.strftime("%H:%M"),
        "end_time": end_time.strftime("%H:%M"),
        "duration_minutes": duration,
        "date": start_time.strftime("%Y-%m-%d")
    }
    
    # 輸出事件資訊
    print(f"🎫 隨機事件:")
    print(f"事件ID: {event_data['id']}")
    print(f"活動: {event_data['event']}")
    print(f"地點: {event_data['location']}")
    print(f"時間: {event_data['start_time']} - {event_data['end_time']}")
    print(f"時長: {event_data['duration_minutes']} 分鐘")
    print(f"日期: {event_data['date']}")
    
    # JSON 格式輸出
    json_output = dumps(event_data, ensure_ascii=False, indent=2)
    print(f"\n📋 JSON 格式:")
    print(json_output)
    
    return event_data

def create_simple_module():
    """創建簡單模組示範"""
    print("\n🔨 創建簡單模組")
    print("-" * 30)
    
    # 模擬自定義模組內容
    print("以下是自定義模組可能包含的內容:")
    
    # 工具函數
    def greet(name):
        return f"Hello, {name}!"
    
    def add_numbers(a, b):
        return a + b
    
    def format_currency(amount):
        return f"NT$ {amount:,.2f}"
    
    # 常數
    PI = 3.14159
    AUTHOR = "Python學習者"
    VERSION = "1.0.0"
    
    # 示範使用
    print(f"greet('小明'): {greet('小明')}")
    print(f"add_numbers(5, 3): {add_numbers(5, 3)}")
    print(f"format_currency(12345): {format_currency(12345)}")
    print(f"PI: {PI}")
    print(f"作者: {AUTHOR}")
    print(f"版本: {VERSION}")

def main():
    """主程式"""
    print("歡迎來到Python模組與套件練習！")
    
    while True:
        print("\n" + "=" * 60)
        print("選擇練習項目:")
        print("1. 🧮 math 模組")
        print("2. 🎲 random 模組") 
        print("3. 📅 datetime 模組")
        print("4. 📝 string 模組")
        print("5. 💻 os 模組")
        print("6. 📋 json 模組")
        print("7. 🏷️ 模組別名")
        print("8. 🎪 綜合練習")
        print("9. 🔨 創建模組示範")
        print("10. 🚀 執行所有練習")
        print("0. 🚪 退出")
        print("=" * 60)
        
        choice = input("請選擇 (0-10): ").strip()
        
        if choice == "0":
            print("感謝使用模組練習程式！")
            break
        elif choice == "1":
            math_module_demo()
            math_applications()
        elif choice == "2":
            random_module_demo()
            random_applications()
        elif choice == "3":
            datetime_module_demo()
            datetime_applications()
        elif choice == "4":
            string_module_demo()
            string_applications()
        elif choice == "5":
            os_module_demo()
        elif choice == "6":
            json_module_demo()
        elif choice == "7":
            alias_demo()
        elif choice == "8":
            comprehensive_exercise()
        elif choice == "9":
            create_simple_module()
        elif choice == "10":
            print("🚀 執行所有練習...")
            math_module_demo()
            math_applications()
            random_module_demo()
            random_applications()
            datetime_module_demo()
            datetime_applications()
            string_module_demo()
            string_applications()
            os_module_demo()
            json_module_demo()
            alias_demo()
            comprehensive_exercise()
            create_simple_module()
            print("✅ 所有練習完成！")
        else:
            print("❌ 無效選擇")
        
        if choice != "0":
            input("\n按 Enter 繼續...")

if __name__ == "__main__":
    main()