# Day 18：模組與套件

## 今日學習目標
- 理解模組和套件的概念與重要性
- 學會使用import語句導入模組
- 掌握Python標準函式庫的使用
- 學會創建自己的模組
- 實作隨機密碼產生器程式

## 1. 什麼是模組和套件？

### 1.1 生活中的類比
想像模組就像是**工具箱中的專用工具**：
- **螺絲起子組**：專門處理各種螺絲（如math模組專門處理數學運算）
- **測量工具組**：專門用於測量（如datetime模組專門處理時間）
- **電工工具組**：專門處理電路（如random模組專門產生隨機數）

或者想像模組像是**圖書館的不同樓層**：
- **1樓：文學類書籍**（string模組 - 字串處理）
- **2樓：科學類書籍**（math模組 - 數學運算）  
- **3樓：歷史類書籍**（datetime模組 - 時間處理）
- **4樓：藝術類書籍**（random模組 - 隨機功能）

### 1.2 模組的優勢
```python
# ❌ 沒有模組：所有功能都要自己寫
def calculate_sin(x):
    # 需要自己實作複雜的數學公式
    pass

def get_current_time():
    # 需要自己處理複雜的時間邏輯
    pass

def generate_random():
    # 需要自己實作隨機數演算法
    pass

# ✅ 使用模組：直接使用現成功能
import math
import datetime
import random

result = math.sin(1.0)           # 簡潔可靠
current_time = datetime.datetime.now()  # 功能完整
random_number = random.randint(1, 10)   # 效能優化
```

## 2. 導入模組的方法

### 2.1 基本導入（import）
```python
# 完整導入模組
import math
import datetime
import random

# 使用模組功能
print(f"圓周率: {math.pi}")
print(f"平方根: {math.sqrt(16)}")
print(f"現在時間: {datetime.datetime.now()}")
print(f"隨機數: {random.randint(1, 100)}")
```

### 2.2 從模組導入特定功能（from import）
```python
# 只導入需要的功能
from math import pi, sqrt, sin, cos
from datetime import datetime, date
from random import randint, choice

# 直接使用功能，不需要模組前綴
print(f"π = {pi}")
print(f"√16 = {sqrt(16)}")
print(f"現在時間: {datetime.now()}")
print(f"隨機數: {randint(1, 100)}")
```

### 2.3 使用別名（as）
```python
# 為模組設定別名
import datetime as dt
import random as rnd
import math as m

# 使用別名
current_time = dt.datetime.now()
random_num = rnd.randint(1, 10)
pi_value = m.pi

# 為函數設定別名
from random import randint as random_int
from datetime import datetime as now

number = random_int(1, 100)
current = now()
```

### 2.4 導入所有功能（*）
```python
# ⚠️ 不建議使用，可能造成名稱衝突
from math import *

# 可以直接使用所有數學函數
print(sin(pi/2))  # 1.0
print(sqrt(16))   # 4.0

# ❌ 問題：可能覆蓋內建函數
from math import *
print(pow(2, 3))  # 使用的是math.pow還是內建pow？
```

## 3. 常用標準函式庫

### 3.1 math - 數學運算模組
```python
import math

print("🧮 math 模組示範:")
print("-" * 30)

# 常數
print(f"圓周率 π: {math.pi}")
print(f"自然對數底數 e: {math.e}")

# 基本數學函數
print(f"平方根 √16: {math.sqrt(16)}")
print(f"次方 2³: {math.pow(2, 3)}")
print(f"絕對值 |-5|: {math.fabs(-5)}")

# 三角函數
print(f"sin(π/2): {math.sin(math.pi/2)}")
print(f"cos(0): {math.cos(0)}")

# 對數函數
print(f"自然對數 ln(e): {math.log(math.e)}")
print(f"常用對數 log₁₀(100): {math.log10(100)}")

# 取整函數
print(f"向上取整 ceil(4.2): {math.ceil(4.2)}")
print(f"向下取整 floor(4.8): {math.floor(4.8)}")

# 實際應用：計算兩點間距離
def calculate_distance(x1, y1, x2, y2):
    """計算二維平面上兩點間的距離"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

dist = calculate_distance(0, 0, 3, 4)
print(f"兩點距離: {dist}")  # 5.0
```

### 3.2 random - 隨機數模組
```python
import random

print("\n🎲 random 模組示範:")
print("-" * 30)

# 基本隨機數
print(f"0-1間隨機浮點數: {random.random()}")
print(f"1-10間隨機整數: {random.randint(1, 10)}")
print(f"0-9間隨機整數: {random.randrange(10)}")

# 隨機選擇
fruits = ["蘋果", "香蕉", "橘子", "葡萄", "草莓"]
print(f"隨機水果: {random.choice(fruits)}")

# 隨機抽樣（不重複）
sample = random.sample(fruits, 3)
print(f"隨機選3個水果: {sample}")

# 打亂清單
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"打亂後的數字: {numbers}")

# 隨機浮點數範圍
print(f"1.5-9.5間隨機數: {random.uniform(1.5, 9.5):.2f}")

# 實際應用：擲骰子遊戲
def roll_dice(num_dice=2):
    """擲骰子"""
    return [random.randint(1, 6) for _ in range(num_dice)]

dice_result = roll_dice()
print(f"擲骰子結果: {dice_result}, 總和: {sum(dice_result)}")
```

### 3.3 datetime - 日期時間模組
```python
import datetime

print("\n📅 datetime 模組示範:")
print("-" * 30)

# 當前時間
now = datetime.datetime.now()
today = datetime.date.today()
print(f"現在日期時間: {now}")
print(f"今天日期: {today}")

# 格式化時間
formatted_time = now.strftime("%Y年%m月%d日 %H:%M:%S")
print(f"格式化時間: {formatted_time}")

# 建立特定時間
birthday = datetime.date(1990, 5, 15)
meeting_time = datetime.datetime(2024, 1, 15, 14, 30, 0)
print(f"生日: {birthday}")
print(f"會議時間: {meeting_time}")

# 時間計算
age_days = today - birthday
print(f"年齡天數: {age_days.days} 天")

# 時間增減
tomorrow = today + datetime.timedelta(days=1)
next_week = today + datetime.timedelta(weeks=1)
print(f"明天: {tomorrow}")
print(f"下週同一天: {next_week}")

# 實際應用：計算年齡
def calculate_age(birth_date):
    """計算年齡"""
    today = datetime.date.today()
    age = today.year - birth_date.year
    
    # 檢查是否還沒過生日
    if today.month < birth_date.month or \
       (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    
    return age

age = calculate_age(birthday)
print(f"年齡: {age} 歲")
```

### 3.4 os - 作業系統介面模組
```python
import os

print("\n💻 os 模組示範:")
print("-" * 30)

# 當前工作目錄
current_dir = os.getcwd()
print(f"當前目錄: {current_dir}")

# 環境變數
username = os.getenv("USERNAME") or os.getenv("USER")
print(f"使用者名稱: {username}")

# 路徑操作
file_path = os.path.join("data", "files", "document.txt")
print(f"組合路徑: {file_path}")

# 檢查檔案/目錄是否存在
print(f"當前目錄存在: {os.path.exists(current_dir)}")

# 列出目錄內容（安全版本）
try:
    files = os.listdir(".")
    print(f"當前目錄檔案數量: {len(files)}")
except PermissionError:
    print("無權限列出目錄內容")
```

### 3.5 string - 字串處理模組
```python
import string

print("\n📝 string 模組示範:")
print("-" * 30)

# 預定義的字元常數
print(f"小寫字母: {string.ascii_lowercase}")
print(f"大寫字母: {string.ascii_uppercase}")
print(f"所有字母: {string.ascii_letters}")
print(f"數字: {string.digits}")
print(f"標點符號: {string.punctuation}")

# 實際應用：產生隨機密碼字元集
def get_password_characters(include_symbols=True):
    """取得密碼字元集"""
    chars = string.ascii_letters + string.digits
    if include_symbols:
        chars += string.punctuation
    return chars

chars = get_password_characters()
print(f"密碼字元集長度: {len(chars)}")
```

## 4. 創建自己的模組

### 4.1 創建簡單模組（utils.py）
```python
# utils.py - 實用工具模組
"""
實用工具模組
提供常用的輔助函數
"""

def format_currency(amount):
    """格式化貨幣顯示"""
    return f"NT$ {amount:,.2f}"

def calculate_bmi(weight, height):
    """計算BMI值"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def is_valid_email(email):
    """簡單的電子郵件驗證"""
    return "@" in email and "." in email.split("@")[1]

def celsius_to_fahrenheit(celsius):
    """攝氏轉華氏"""
    return celsius * 9/5 + 32

# 模組變數
VERSION = "1.0.0"
AUTHOR = "Python學習者"

# 如果直接執行這個檔案時的測試程式碼
if __name__ == "__main__":
    print(f"utils 模組 v{VERSION} by {AUTHOR}")
    print(f"測試BMI計算: {calculate_bmi(70, 1.75)}")
    print(f"測試貨幣格式: {format_currency(12345.67)}")
    print(f"測試溫度轉換: {celsius_to_fahrenheit(25)}°F")
```

### 4.2 使用自定義模組
```python
# main.py - 使用自定義模組
import utils

print("使用自定義模組:")
print(f"模組版本: {utils.VERSION}")
print(f"BMI計算: {utils.calculate_bmi(65, 1.68)}")
print(f"溫度轉換: 30°C = {utils.celsius_to_fahrenheit(30)}°F")
print(f"貨幣格式: {utils.format_currency(25000)}")
print(f"郵箱驗證: {utils.is_valid_email('user@example.com')}")

# 或者使用 from import
from utils import calculate_bmi, format_currency

bmi = calculate_bmi(70, 1.75)
price = format_currency(15000)
print(f"簡化使用: BMI={bmi}, 價格={price}")
```

## 5. 實作項目：隨機密碼產生器

### 5.1 功能需求
1. 產生指定長度的隨機密碼
2. 可選擇字元類型（大小寫、數字、符號）
3. 避免相似字元（如0和O、1和l）
4. 密碼強度評估
5. 批量產生多個密碼
6. 記錄和匯出密碼

### 5.2 完整實作
```python
# password_generator.py
"""
隨機密碼產生器
使用多個標準模組實作完整的密碼管理工具
"""

import random
import string
import datetime
import os
import json
import math

class PasswordGenerator:
    """隨機密碼產生器類別"""
    
    def __init__(self):
        """初始化產生器"""
        # 字元集定義
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase  
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;':\".,<>?/~`"
        
        # 容易混淆的字元
        self.confusing_chars = "0O1lI"
        
        # 產生歷史
        self.generation_history = []
        
        # 設定檔案
        self.config_file = "password_config.json"
        self.history_file = "password_history.json"
        
        # 載入配置
        self.load_config()
        self.load_history()
    
    def load_config(self):
        """載入配置"""
        default_config = {
            "default_length": 12,
            "include_lowercase": True,
            "include_uppercase": True,
            "include_digits": True,
            "include_symbols": True,
            "avoid_confusing": True
        }
        
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            else:
                self.config = default_config
                self.save_config()
        except Exception:
            self.config = default_config
    
    def save_config(self):
        """儲存配置"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"儲存配置失敗: {e}")
    
    def load_history(self):
        """載入歷史記錄"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.generation_history = json.load(f)
        except Exception:
            self.generation_history = []
    
    def save_history(self):
        """儲存歷史記錄"""
        try:
            # 只保留最近100筆記錄
            if len(self.generation_history) > 100:
                self.generation_history = self.generation_history[-100:]
            
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.generation_history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"儲存歷史失敗: {e}")
    
    def get_character_set(self, include_lowercase=None, include_uppercase=None, 
                         include_digits=None, include_symbols=None, 
                         avoid_confusing=None):
        """取得字元集"""
        # 使用參數或預設配置
        inc_lower = include_lowercase if include_lowercase is not None else self.config["include_lowercase"]
        inc_upper = include_uppercase if include_uppercase is not None else self.config["include_uppercase"]
        inc_digits = include_digits if include_digits is not None else self.config["include_digits"]
        inc_symbols = include_symbols if include_symbols is not None else self.config["include_symbols"]
        avoid_conf = avoid_confusing if avoid_confusing is not None else self.config["avoid_confusing"]
        
        chars = ""
        required_chars = []
        
        if inc_lower:
            chars += self.lowercase
            required_chars.append(random.choice(self.lowercase))
        
        if inc_upper:
            chars += self.uppercase
            required_chars.append(random.choice(self.uppercase))
        
        if inc_digits:
            chars += self.digits
            required_chars.append(random.choice(self.digits))
        
        if inc_symbols:
            chars += self.symbols
            required_chars.append(random.choice(self.symbols))
        
        # 移除容易混淆的字元
        if avoid_conf:
            for char in self.confusing_chars:
                chars = chars.replace(char, "")
        
        return chars, required_chars
    
    def generate_password(self, length=None, **kwargs):
        """產生單個密碼"""
        length = length or self.config["default_length"]
        
        if length < 4:
            raise ValueError("密碼長度至少需要4個字元")
        
        chars, required_chars = self.get_character_set(**kwargs)
        
        if not chars:
            raise ValueError("至少需要選擇一種字元類型")
        
        # 確保包含各種類型的字元
        password_chars = required_chars.copy()
        
        # 填充剩餘長度
        remaining_length = length - len(required_chars)
        for _ in range(remaining_length):
            password_chars.append(random.choice(chars))
        
        # 打亂順序
        random.shuffle(password_chars)
        
        password = ''.join(password_chars)
        
        # 記錄到歷史
        history_record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "length": length,
            "strength_score": self.calculate_strength(password),
            "character_types": len(required_chars)
        }
        self.generation_history.append(history_record)
        
        return password
    
    def generate_multiple_passwords(self, count, length=None, **kwargs):
        """產生多個密碼"""
        passwords = []
        for _ in range(count):
            password = self.generate_password(length, **kwargs)
            strength = self.calculate_strength(password)
            passwords.append({
                "password": password,
                "strength": strength,
                "length": len(password)
            })
        
        return passwords
    
    def calculate_strength(self, password):
        """計算密碼強度（0-100分）"""
        score = 0
        
        # 長度分數（最多30分）
        if len(password) >= 12:
            score += 30
        elif len(password) >= 8:
            score += 20
        elif len(password) >= 6:
            score += 10
        
        # 字元類型多樣性（每種10分，最多40分）
        if any(c.islower() for c in password):
            score += 10
        if any(c.isupper() for c in password):
            score += 10
        if any(c.isdigit() for c in password):
            score += 10
        if any(c in self.symbols for c in password):
            score += 10
        
        # 複雜性獎勵（最多30分）
        unique_chars = len(set(password))
        complexity_ratio = unique_chars / len(password)
        score += int(complexity_ratio * 30)
        
        return min(100, score)
    
    def get_strength_description(self, score):
        """取得強度描述"""
        if score >= 80:
            return "非常強", "🔒"
        elif score >= 60:
            return "強", "🔐"
        elif score >= 40:
            return "中等", "🔓"
        elif score >= 20:
            return "弱", "⚠️"
        else:
            return "非常弱", "❌"
    
    def analyze_password(self, password):
        """分析密碼"""
        analysis = {
            "length": len(password),
            "has_lowercase": any(c.islower() for c in password),
            "has_uppercase": any(c.isupper() for c in password),
            "has_digits": any(c.isdigit() for c in password),
            "has_symbols": any(c in self.symbols for c in password),
            "unique_characters": len(set(password)),
            "strength_score": self.calculate_strength(password)
        }
        
        strength_desc, emoji = self.get_strength_description(analysis["strength_score"])
        analysis["strength_level"] = strength_desc
        analysis["emoji"] = emoji
        
        return analysis
    
    def estimate_crack_time(self, password):
        """估算破解時間"""
        # 計算字元空間
        char_space = 0
        if any(c.islower() for c in password):
            char_space += 26
        if any(c.isupper() for c in password):
            char_space += 26
        if any(c.isdigit() for c in password):
            char_space += 10
        if any(c in self.symbols for c in password):
            char_space += len(self.symbols)
        
        if char_space == 0:
            return "無法計算"
        
        # 計算可能組合數
        combinations = char_space ** len(password)
        
        # 假設每秒可嘗試10億次（現代GPU的大致速度）
        attempts_per_second = 1_000_000_000
        
        # 平均需要嘗試一半的組合
        avg_time_seconds = combinations / (2 * attempts_per_second)
        
        # 轉換為人類可讀的時間
        if avg_time_seconds < 1:
            return "不到1秒"
        elif avg_time_seconds < 60:
            return f"{avg_time_seconds:.1f}秒"
        elif avg_time_seconds < 3600:
            return f"{avg_time_seconds/60:.1f}分鐘"
        elif avg_time_seconds < 86400:
            return f"{avg_time_seconds/3600:.1f}小時"
        elif avg_time_seconds < 31536000:
            return f"{avg_time_seconds/86400:.1f}天"
        else:
            years = avg_time_seconds / 31536000
            if years > 1000000:
                return "超過百萬年"
            else:
                return f"{years:.1f}年"
    
    def export_passwords(self, passwords, filename=None):
        """匯出密碼到檔案"""
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"passwords_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("密碼列表\n")
                f.write("=" * 50 + "\n")
                f.write(f"產生時間: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"密碼數量: {len(passwords)}\n\n")
                
                for i, pwd_info in enumerate(passwords, 1):
                    password = pwd_info["password"]
                    strength = pwd_info["strength"]
                    strength_desc, emoji = self.get_strength_description(strength)
                    
                    f.write(f"{i:2d}. {password} (強度: {strength}/100 {emoji})\n")
                
                f.write("\n" + "=" * 50 + "\n")
                f.write("注意：請妥善保管此檔案並定期刪除\n")
            
            return filename
        except Exception as e:
            print(f"匯出失敗: {e}")
            return None
    
    def get_statistics(self):
        """取得使用統計"""
        if not self.generation_history:
            return None
        
        total_generated = len(self.generation_history)
        avg_length = sum(record["length"] for record in self.generation_history) / total_generated
        avg_strength = sum(record["strength_score"] for record in self.generation_history) / total_generated
        
        # 最近7天的產生數量
        recent_week = datetime.datetime.now() - datetime.timedelta(days=7)
        recent_count = sum(1 for record in self.generation_history 
                          if datetime.datetime.fromisoformat(record["timestamp"]) > recent_week)
        
        return {
            "total_generated": total_generated,
            "average_length": round(avg_length, 1),
            "average_strength": round(avg_strength, 1),
            "recent_week_count": recent_count
        }

def interactive_password_generator():
    """互動式密碼產生器"""
    generator = PasswordGenerator()
    
    print("🔐 歡迎使用隨機密碼產生器！")
    print("這個工具展示了Python模組的強大功能")
    
    while True:
        print("\n" + "=" * 60)
        print("🛠️  功能選單:")
        print("1. 🎲 產生單個密碼")
        print("2. 📝 產生多個密碼")
        print("3. 🔍 分析密碼強度")
        print("4. ⚙️ 自訂設定")
        print("5. 📊 使用統計")
        print("6. 📄 匯出密碼")
        print("7. 🧪 密碼安全測試")
        print("8. 📚 模組使用示範")
        print("0. 🚪 退出程式")
        print("=" * 60)
        
        try:
            choice = input("請選擇功能 (0-8): ").strip()
            
            if choice == "0":
                generator.save_history()
                generator.save_config()
                print("\n👋 感謝使用密碼產生器！")
                print("🔐 記住：好密碼是網路安全的基礎！")
                break
            elif choice == "1":
                generate_single_password(generator)
            elif choice == "2":
                generate_multiple_passwords_interface(generator)
            elif choice == "3":
                analyze_password_interface(generator)
            elif choice == "4":
                settings_interface(generator)
            elif choice == "5":
                show_statistics(generator)
            elif choice == "6":
                export_passwords_interface(generator)
            elif choice == "7":
                security_test_interface(generator)
            elif choice == "8":
                module_demonstration()
            else:
                print("❌ 無效選擇，請重新輸入")
                
        except KeyboardInterrupt:
            print("\n\n程式被中斷，正在儲存資料...")
            generator.save_history()
            generator.save_config()
            break
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")
        
        if choice != "0":
            input("\n按 Enter 繼續...")

def generate_single_password(generator):
    """產生單個密碼介面"""
    print("\n🎲 產生單個密碼")
    print("-" * 30)
    
    try:
        # 獲取自訂參數
        length_input = input(f"密碼長度 (預設 {generator.config['default_length']}): ").strip()
        length = int(length_input) if length_input else generator.config['default_length']
        
        if length < 4:
            print("❌ 密碼長度至少需要4個字元")
            return
        
        # 字元類型選擇
        print("\n字元類型選擇 (直接按 Enter 使用預設設定):")
        inc_lower = input("包含小寫字母？(Y/n): ").strip().lower() != 'n'
        inc_upper = input("包含大寫字母？(Y/n): ").strip().lower() != 'n'
        inc_digits = input("包含數字？(Y/n): ").strip().lower() != 'n'
        inc_symbols = input("包含特殊字符？(Y/n): ").strip().lower() != 'n'
        avoid_confusing = input("避免混淆字元？(Y/n): ").strip().lower() != 'n'
        
        # 產生密碼
        password = generator.generate_password(
            length=length,
            include_lowercase=inc_lower,
            include_uppercase=inc_upper,
            include_digits=inc_digits,
            include_symbols=inc_symbols,
            avoid_confusing=avoid_confusing
        )
        
        # 分析密碼
        analysis = generator.analyze_password(password)
        crack_time = generator.estimate_crack_time(password)
        
        # 顯示結果
        print(f"\n🎯 產生的密碼:")
        print(f"密碼: {password}")
        print(f"長度: {analysis['length']} 字元")
        print(f"強度: {analysis['strength_score']}/100 - {analysis['strength_level']} {analysis['emoji']}")
        print(f"估算破解時間: {crack_time}")
        
        print(f"\n📋 字元分析:")
        print(f"  小寫字母: {'✅' if analysis['has_lowercase'] else '❌'}")
        print(f"  大寫字母: {'✅' if analysis['has_uppercase'] else '❌'}")
        print(f"  數字: {'✅' if analysis['has_digits'] else '❌'}")
        print(f"  特殊字符: {'✅' if analysis['has_symbols'] else '❌'}")
        print(f"  唯一字元數: {analysis['unique_characters']}")
        
    except ValueError as e:
        print(f"❌ 輸入錯誤: {e}")
    except Exception as e:
        print(f"❌ 產生失敗: {e}")

def generate_multiple_passwords_interface(generator):
    """產生多個密碼介面"""
    print("\n📝 產生多個密碼")
    print("-" * 30)
    
    try:
        count = int(input("要產生幾個密碼 (1-50): ") or "5")
        if not 1 <= count <= 50:
            print("❌ 密碼數量必須在1-50之間")
            return
        
        length = int(input(f"密碼長度 (預設 {generator.config['default_length']}): ") or generator.config['default_length'])
        
        print(f"\n正在產生 {count} 個長度為 {length} 的密碼...")
        passwords = generator.generate_multiple_passwords(count, length)
        
        print(f"\n📋 產生結果:")
        print("-" * 60)
        for i, pwd_info in enumerate(passwords, 1):
            password = pwd_info["password"]
            strength = pwd_info["strength"]
            strength_desc, emoji = generator.get_strength_description(strength)
            
            print(f"{i:2d}. {password} (強度: {strength:2d}/100 {emoji})")
        
        # 統計
        avg_strength = sum(p["strength"] for p in passwords) / len(passwords)
        print(f"\n📊 統計資訊:")
        print(f"平均強度: {avg_strength:.1f}/100")
        print(f"最高強度: {max(p['strength'] for p in passwords)}/100")
        print(f"最低強度: {min(p['strength'] for p in passwords)}/100")
        
        # 詢問是否匯出
        export_choice = input("\n是否匯出到檔案？(y/N): ").strip().lower()
        if export_choice == 'y':
            filename = generator.export_passwords(passwords)
            if filename:
                print(f"✅ 已匯出到: {filename}")
                
    except ValueError:
        print("❌ 請輸入有效的數字")
    except Exception as e:
        print(f"❌ 產生失敗: {e}")

def analyze_password_interface(generator):
    """密碼分析介面"""
    print("\n🔍 分析密碼強度")
    print("-" * 30)
    
    password = input("請輸入要分析的密碼: ").strip()
    if not password:
        print("❌ 密碼不能為空")
        return
    
    analysis = generator.analyze_password(password)
    crack_time = generator.estimate_crack_time(password)
    
    print(f"\n📊 密碼分析結果:")
    print("=" * 40)
    print(f"密碼: {'*' * len(password)} ({len(password)} 字元)")
    print(f"強度評分: {analysis['strength_score']}/100")
    print(f"強度等級: {analysis['strength_level']} {analysis['emoji']}")
    print(f"估算破解時間: {crack_time}")
    
    print(f"\n📋 詳細分析:")
    print(f"  包含小寫字母: {'✅' if analysis['has_lowercase'] else '❌'}")
    print(f"  包含大寫字母: {'✅' if analysis['has_uppercase'] else '❌'}")
    print(f"  包含數字: {'✅' if analysis['has_digits'] else '❌'}")
    print(f"  包含特殊字符: {'✅' if analysis['has_symbols'] else '❌'}")
    print(f"  唯一字元數: {analysis['unique_characters']}")
    print(f"  字元多樣性: {analysis['unique_characters'] / analysis['length'] * 100:.1f}%")
    
    # 改善建議
    suggestions = []
    if analysis['length'] < 12:
        suggestions.append("建議密碼長度至少12個字元")
    if not analysis['has_lowercase']:
        suggestions.append("添加小寫字母")
    if not analysis['has_uppercase']:
        suggestions.append("添加大寫字母")
    if not analysis['has_digits']:
        suggestions.append("添加數字")
    if not analysis['has_symbols']:
        suggestions.append("添加特殊字符")
    
    if suggestions:
        print(f"\n💡 改善建議:")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"  {i}. {suggestion}")
    else:
        print(f"\n🎉 恭喜！這是一個強度很好的密碼！")

def settings_interface(generator):
    """設定介面"""
    print("\n⚙️ 產生器設定")
    print("-" * 30)
    
    current_config = generator.config
    
    print("目前設定:")
    print(f"  預設長度: {current_config['default_length']}")
    print(f"  包含小寫字母: {'是' if current_config['include_lowercase'] else '否'}")
    print(f"  包含大寫字母: {'是' if current_config['include_uppercase'] else '否'}")
    print(f"  包含數字: {'是' if current_config['include_digits'] else '否'}")
    print(f"  包含特殊字符: {'是' if current_config['include_symbols'] else '否'}")
    print(f"  避免混淆字元: {'是' if current_config['avoid_confusing'] else '否'}")
    
    modify = input("\n是否要修改設定？(y/N): ").strip().lower()
    if modify != 'y':
        return
    
    try:
        # 修改設定
        new_length = input(f"新的預設長度 (目前: {current_config['default_length']}): ").strip()
        if new_length:
            generator.config['default_length'] = max(4, int(new_length))
        
        print("\n字元類型設定 (y/n):")
        
        lower_input = input(f"包含小寫字母 (目前: {'是' if current_config['include_lowercase'] else '否'}): ").strip().lower()
        if lower_input in ['y', 'n']:
            generator.config['include_lowercase'] = lower_input == 'y'
        
        upper_input = input(f"包含大寫字母 (目前: {'是' if current_config['include_uppercase'] else '否'}): ").strip().lower()
        if upper_input in ['y', 'n']:
            generator.config['include_uppercase'] = upper_input == 'y'
        
        digits_input = input(f"包含數字 (目前: {'是' if current_config['include_digits'] else '否'}): ").strip().lower()
        if digits_input in ['y', 'n']:
            generator.config['include_digits'] = digits_input == 'y'
        
        symbols_input = input(f"包含特殊字符 (目前: {'是' if current_config['include_symbols'] else '否'}): ").strip().lower()
        if symbols_input in ['y', 'n']:
            generator.config['include_symbols'] = symbols_input == 'y'
        
        confusing_input = input(f"避免混淆字元 (目前: {'是' if current_config['avoid_confusing'] else '否'}): ").strip().lower()
        if confusing_input in ['y', 'n']:
            generator.config['avoid_confusing'] = confusing_input == 'y'
        
        generator.save_config()
        print("✅ 設定已儲存")
        
    except ValueError:
        print("❌ 輸入格式錯誤")

def show_statistics(generator):
    """顯示使用統計"""
    print("\n📊 使用統計")
    print("-" * 30)
    
    stats = generator.get_statistics()
    if not stats:
        print("暫無使用記錄")
        return
    
    print(f"總共產生密碼: {stats['total_generated']} 個")
    print(f"平均密碼長度: {stats['average_length']} 字元")
    print(f"平均密碼強度: {stats['average_strength']}/100")
    print(f"最近7天產生: {stats['recent_week_count']} 個")
    
    # 顯示最近幾次產生記錄
    recent_records = generator.generation_history[-5:]
    if recent_records:
        print(f"\n📋 最近5次產生記錄:")
        for record in reversed(recent_records):
            timestamp = datetime.datetime.fromisoformat(record["timestamp"])
            time_str = timestamp.strftime("%m-%d %H:%M")
            print(f"  {time_str} | 長度:{record['length']:2d} | 強度:{record['strength_score']:2d}/100")

def export_passwords_interface(generator):
    """匯出密碼介面"""
    print("\n📄 匯出密碼")
    print("-" * 30)
    
    try:
        count = int(input("要產生並匯出幾個密碼 (1-100): ") or "10")
        if not 1 <= count <= 100:
            print("❌ 密碼數量必須在1-100之間")
            return
        
        length = int(input(f"密碼長度 (預設 {generator.config['default_length']}): ") or generator.config['default_length'])
        
        print(f"\n正在產生 {count} 個密碼...")
        passwords = generator.generate_multiple_passwords(count, length)
        
        filename = input("檔案名稱 (留空自動產生): ").strip()
        if not filename:
            filename = None
        
        exported_file = generator.export_passwords(passwords, filename)
        
        if exported_file:
            print(f"✅ 成功匯出 {count} 個密碼到: {exported_file}")
            
            # 顯示統計
            avg_strength = sum(p["strength"] for p in passwords) / len(passwords)
            print(f"📊 匯出統計: 平均強度 {avg_strength:.1f}/100")
        
    except ValueError:
        print("❌ 請輸入有效的數字")
    except Exception as e:
        print(f"❌ 匯出失敗: {e}")

def security_test_interface(generator):
    """安全測試介面"""
    print("\n🧪 密碼安全測試")
    print("-" * 30)
    
    # 測試不同長度和設定的密碼
    test_configs = [
        {"length": 8, "name": "短密碼(8字元)"},
        {"length": 12, "name": "中等密碼(12字元)"},
        {"length": 16, "name": "長密碼(16字元)"},
        {"length": 20, "name": "超長密碼(20字元)"}
    ]
    
    print("🔒 測試不同長度密碼的安全性:")
    print("-" * 50)
    
    for config in test_configs:
        password = generator.generate_password(length=config["length"])
        analysis = generator.analyze_password(password)
        crack_time = generator.estimate_crack_time(password)
        
        print(f"{config['name']:15} | 強度: {analysis['strength_score']:2d}/100 | 破解時間: {crack_time}")
    
    # 測試不同字元類型組合
    print(f"\n🔧 測試不同字元類型組合:")
    print("-" * 50)
    
    type_tests = [
        {"name": "僅小寫字母", "kwargs": {"include_lowercase": True, "include_uppercase": False, "include_digits": False, "include_symbols": False}},
        {"name": "大小寫字母", "kwargs": {"include_lowercase": True, "include_uppercase": True, "include_digits": False, "include_symbols": False}},
        {"name": "字母+數字", "kwargs": {"include_lowercase": True, "include_uppercase": True, "include_digits": True, "include_symbols": False}},
        {"name": "完整字元集", "kwargs": {"include_lowercase": True, "include_uppercase": True, "include_digits": True, "include_symbols": True}}
    ]
    
    for test in type_tests:
        password = generator.generate_password(length=12, **test["kwargs"])
        analysis = generator.analyze_password(password)
        crack_time = generator.estimate_crack_time(password)
        
        print(f"{test['name']:15} | 強度: {analysis['strength_score']:2d}/100 | 破解時間: {crack_time}")

def module_demonstration():
    """模組使用示範"""
    print("\n📚 Python模組使用示範")
    print("-" * 40)
    
    print("🔧 本程式使用的Python標準模組:")
    
    # random 模組示範
    print(f"\n🎲 random 模組:")
    print(f"  random.randint(1, 10): {random.randint(1, 10)}")
    print(f"  random.choice(['A','B','C']): {random.choice(['A','B','C'])}")
    print(f"  random.random(): {random.random():.3f}")
    
    # string 模組示範
    print(f"\n📝 string 模組:")
    print(f"  string.ascii_letters: {string.ascii_letters}")
    print(f"  string.digits: {string.digits}")
    print(f"  string.punctuation[:10]: {string.punctuation[:10]}...")
    
    # datetime 模組示範
    print(f"\n📅 datetime 模組:")
    now = datetime.datetime.now()
    print(f"  datetime.datetime.now(): {now}")
    print(f"  格式化時間: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # os 模組示範
    print(f"\n💻 os 模組:")
    print(f"  os.getcwd(): {os.getcwd()}")
    print(f"  os.path.exists('.'): {os.path.exists('.')}")
    
    # json 模組示範
    print(f"\n📋 json 模組:")
    sample_data = {"name": "測試", "value": 123, "active": True}
    json_str = json.dumps(sample_data, ensure_ascii=False)
    print(f"  JSON序列化: {json_str}")
    
    # math 模組示範
    print(f"\n🧮 math 模組:")
    print(f"  math.pi: {math.pi:.6f}")
    print(f"  math.sqrt(16): {math.sqrt(16)}")
    print(f"  math.log2(8): {math.log2(8)}")

if __name__ == "__main__":
    interactive_password_generator()
```

## 6. 今日總結

今天你學會了：
- ✅ 模組和套件的概念與重要性
- ✅ 使用import語句導入模組的各種方法
- ✅ Python標準函式庫的常用模組
- ✅ 創建自己的模組
- ✅ 實作完整的隨機密碼產生器

**關鍵概念回顧：**
- 模組讓程式更有組織性和可重用性
- Python標準函式庫提供豐富的功能
- import有多種形式，選擇適合的方式
- 自定義模組讓代碼更模組化

**明天預告：**
我們將學習檔案處理，了解如何讀寫檔案，並實作日記程式！

記住：**善用模組是Python程式設計的精髓，站在巨人的肩膀上編程！**