"""
Day 18: 隨機密碼產生器
實作重點：模組與套件的使用 - import, random, string, datetime, os, json 等
"""

import random
import string
import datetime
import os
import json
import math

class PasswordGenerator:
    """隨機密碼產生器 - 展示多個標準模組的整合使用"""
    
    def __init__(self):
        """初始化產生器"""
        # 使用 string 模組定義字元集
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase  
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;':\".,<>?/~`"
        
        # 容易混淆的字元 (避免 0O1lI 等)
        self.confusing_chars = "0O1lI"
        
        # 使用 os 模組處理檔案路徑
        self.config_file = "password_config.json"
        self.history_file = "password_history.json"
        
        # 初始化配置和歷史
        self.config = {}
        self.generation_history = []
        
        self.load_config()
        self.load_history()
    
    def load_config(self):
        """載入配置 - 展示 json 和 os 模組的使用"""
        default_config = {
            "default_length": 12,
            "include_lowercase": True,
            "include_uppercase": True,
            "include_digits": True,
            "include_symbols": True,
            "avoid_confusing": True
        }
        
        try:
            # 使用 os.path.exists() 檢查檔案是否存在
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    # 使用 json.load() 讀取配置
                    self.config = json.load(f)
                print(f"✅ 已載入配置檔案: {self.config_file}")
            else:
                self.config = default_config
                self.save_config()
                print("📝 建立預設配置檔案")
        except Exception as e:
            print(f"⚠️ 配置載入失敗，使用預設設定: {e}")
            self.config = default_config
    
    def save_config(self):
        """儲存配置 - 展示 json 模組的使用"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                # 使用 json.dump() 儲存配置，ensure_ascii=False 支援中文
                json.dump(self.config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ 儲存配置失敗: {e}")
    
    def load_history(self):
        """載入歷史記錄"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.generation_history = json.load(f)
                print(f"📚 載入了 {len(self.generation_history)} 筆歷史記錄")
        except Exception as e:
            print(f"⚠️ 歷史記錄載入失敗: {e}")
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
            print(f"❌ 儲存歷史失敗: {e}")
    
    def get_character_set(self, **options):
        """
        取得字元集 - 展示 string 模組的應用
        使用 **kwargs 接受選項參數
        """
        # 使用配置或參數中的設定
        inc_lower = options.get("include_lowercase", self.config["include_lowercase"])
        inc_upper = options.get("include_uppercase", self.config["include_uppercase"])
        inc_digits = options.get("include_digits", self.config["include_digits"])
        inc_symbols = options.get("include_symbols", self.config["include_symbols"])
        avoid_conf = options.get("avoid_confusing", self.config["avoid_confusing"])
        
        chars = ""
        required_chars = []
        
        # 組建字元集
        if inc_lower:
            chars += self.lowercase
            # 使用 random.choice() 確保包含各種類型字元
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
    
    def generate_password(self, length=None, **options):
        """
        產生單個密碼 - 展示 random 模組的核心功能
        """
        length = length or self.config["default_length"]
        
        if length < 4:
            raise ValueError("密碼長度至少需要4個字元")
        
        chars, required_chars = self.get_character_set(**options)
        
        if not chars:
            raise ValueError("至少需要選擇一種字元類型")
        
        # 確保包含各種類型的字元
        password_chars = required_chars.copy()
        
        # 使用 random.choice() 填充剩餘長度
        remaining_length = length - len(required_chars)
        for _ in range(remaining_length):
            password_chars.append(random.choice(chars))
        
        # 使用 random.shuffle() 打亂順序
        random.shuffle(password_chars)
        
        password = ''.join(password_chars)
        
        # 記錄到歷史 - 使用 datetime 模組
        self.add_to_history(password, length)
        
        return password
    
    def add_to_history(self, password, length):
        """添加到歷史記錄 - 展示 datetime 模組的使用"""
        # 使用 datetime.datetime.now() 取得當前時間
        current_time = datetime.datetime.now()
        
        history_record = {
            # 使用 isoformat() 將時間轉為標準格式
            "timestamp": current_time.isoformat(),
            # 格式化時間為人類可讀格式
            "formatted_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            "length": length,
            "strength_score": self.calculate_strength(password),
            "character_types": self.count_character_types(password)
        }
        
        self.generation_history.append(history_record)
    
    def count_character_types(self, password):
        """計算密碼包含的字元類型數量"""
        types = 0
        if any(c.islower() for c in password):
            types += 1
        if any(c.isupper() for c in password):
            types += 1
        if any(c.isdigit() for c in password):
            types += 1
        if any(c in self.symbols for c in password):
            types += 1
        return types
    
    def generate_multiple_passwords(self, count, length=None, **options):
        """產生多個密碼"""
        passwords = []
        for i in range(count):
            try:
                password = self.generate_password(length, **options)
                strength = self.calculate_strength(password)
                passwords.append({
                    "index": i + 1,
                    "password": password,
                    "strength": strength,
                    "length": len(password)
                })
            except Exception as e:
                print(f"❌ 產生第 {i+1} 個密碼失敗: {e}")
        
        return passwords
    
    def calculate_strength(self, password):
        """
        計算密碼強度 - 使用 math 模組進行數學計算
        回傳 0-100 的分數
        """
        score = 0
        length = len(password)
        
        # 長度分數（最多40分）
        if length >= 16:
            score += 40
        elif length >= 12:
            score += 30
        elif length >= 8:
            score += 20
        else:
            score += 10
        
        # 字元類型多樣性（每種類型15分，最多60分）
        if any(c.islower() for c in password):
            score += 15
        if any(c.isupper() for c in password):
            score += 15
        if any(c.isdigit() for c in password):
            score += 15
        if any(c in self.symbols for c in password):
            score += 15
        
        # 字元唯一性獎勵
        unique_chars = len(set(password))
        uniqueness_ratio = unique_chars / length
        score += int(uniqueness_ratio * 20)
        
        # 使用 min() 確保不超過100分
        return min(100, max(0, score))
    
    def get_strength_description(self, score):
        """根據分數取得強度描述"""
        if score >= 90:
            return "非常強", "🔒"
        elif score >= 75:
            return "強", "🔐"
        elif score >= 60:
            return "中等", "🔓"
        elif score >= 40:
            return "弱", "⚠️"
        else:
            return "非常弱", "❌"
    
    def estimate_crack_time(self, password):
        """
        估算密碼破解時間 - 展示 math 模組的應用
        """
        # 計算字元空間大小
        char_space = 0
        if any(c.islower() for c in password):
            char_space += 26  # 小寫字母
        if any(c.isupper() for c in password):
            char_space += 26  # 大寫字母
        if any(c.isdigit() for c in password):
            char_space += 10  # 數字
        if any(c in self.symbols for c in password):
            char_space += len(self.symbols)  # 特殊字符
        
        if char_space == 0:
            return "無法計算"
        
        # 使用 math.pow() 計算總組合數
        total_combinations = math.pow(char_space, len(password))
        
        # 假設每秒可嘗試 1 億次（保守估計）
        attempts_per_second = 100_000_000
        
        # 平均需要嘗試一半的組合
        avg_time_seconds = total_combinations / (2 * attempts_per_second)
        
        # 轉換為可讀的時間格式
        return self.format_time_duration(avg_time_seconds)
    
    def format_time_duration(self, seconds):
        """格式化時間長度為人類可讀格式"""
        if seconds < 1:
            return "不到1秒"
        elif seconds < 60:
            return f"{seconds:.1f}秒"
        elif seconds < 3600:
            return f"{seconds/60:.1f}分鐘"
        elif seconds < 86400:
            return f"{seconds/3600:.1f}小時"
        elif seconds < 31536000:  # 一年
            return f"{seconds/86400:.1f}天"
        elif seconds < 31536000000:  # 1000年
            years = seconds / 31536000
            return f"{years:.0f}年"
        else:
            return "超過1000年"
    
    def analyze_password(self, password):
        """
        完整分析密碼 - 整合多個模組的功能
        """
        analysis = {
            "length": len(password),
            "has_lowercase": any(c.islower() for c in password),
            "has_uppercase": any(c.isupper() for c in password),
            "has_digits": any(c.isdigit() for c in password),
            "has_symbols": any(c in self.symbols for c in password),
            "unique_characters": len(set(password)),
            "character_types": self.count_character_types(password),
            "strength_score": self.calculate_strength(password),
            "crack_time": self.estimate_crack_time(password)
        }
        
        strength_desc, emoji = self.get_strength_description(analysis["strength_score"])
        analysis["strength_level"] = strength_desc
        analysis["emoji"] = emoji
        
        return analysis
    
    def export_passwords(self, passwords, filename=None):
        """
        匯出密碼到檔案 - 展示檔案操作和 datetime 格式化
        """
        if not filename:
            # 使用 datetime 生成時間戳檔名
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"passwords_{timestamp}.txt"
        
        try:
            # 使用 os.path.abspath() 取得絕對路徑
            full_path = os.path.abspath(filename)
            
            with open(filename, 'w', encoding='utf-8') as f:
                # 寫入檔案標頭
                f.write("🔐 密碼列表\n")
                f.write("=" * 60 + "\n")
                
                # 使用 datetime 格式化當前時間
                current_time = datetime.datetime.now()
                f.write(f"產生時間: {current_time.strftime('%Y年%m月%d日 %H:%M:%S')}\n")
                f.write(f"密碼數量: {len(passwords)}\n")
                f.write(f"檔案路徑: {full_path}\n\n")
                
                # 寫入密碼列表
                for pwd_info in passwords:
                    password = pwd_info["password"]
                    strength = pwd_info["strength"]
                    strength_desc, emoji = self.get_strength_description(strength)
                    
                    f.write(f"{pwd_info['index']:2d}. {password:20} ")
                    f.write(f"(長度: {len(password):2d}, 強度: {strength:2d}/100 {emoji})\n")
                
                # 寫入檔案尾部
                f.write("\n" + "=" * 60 + "\n")
                f.write("⚠️  安全提醒:\n")
                f.write("• 請妥善保管此檔案\n")
                f.write("• 使用後請刪除此檔案\n")
                f.write("• 不要透過不安全的管道傳送密碼\n")
                f.write("• 建議為每個帳戶使用不同的密碼\n")
            
            return full_path
            
        except Exception as e:
            print(f"❌ 匯出失敗: {e}")
            return None
    
    def get_usage_statistics(self):
        """
        取得使用統計 - 展示 datetime 模組的時間計算
        """
        if not self.generation_history:
            return None
        
        total_count = len(self.generation_history)
        
        # 計算平均值
        avg_length = sum(record["length"] for record in self.generation_history) / total_count
        avg_strength = sum(record["strength_score"] for record in self.generation_history) / total_count
        
        # 計算最近7天的使用量 - 使用 datetime 進行時間計算
        current_time = datetime.datetime.now()
        week_ago = current_time - datetime.timedelta(days=7)
        
        recent_count = 0
        for record in self.generation_history:
            try:
                # 使用 datetime.fromisoformat() 解析時間字串
                record_time = datetime.datetime.fromisoformat(record["timestamp"])
                if record_time > week_ago:
                    recent_count += 1
            except (ValueError, KeyError):
                continue
        
        # 找出最常用的長度
        length_counts = {}
        for record in self.generation_history:
            length = record["length"]
            length_counts[length] = length_counts.get(length, 0) + 1
        
        most_common_length = max(length_counts.items(), key=lambda x: x[1]) if length_counts else (0, 0)
        
        return {
            "total_generated": total_count,
            "average_length": round(avg_length, 1),
            "average_strength": round(avg_strength, 1),
            "recent_week_count": recent_count,
            "most_common_length": most_common_length[0],
            "most_common_count": most_common_length[1]
        }
    
    def cleanup_old_files(self, days_old=30):
        """
        清理舊檔案 - 展示 os 和 datetime 模組的結合使用
        """
        try:
            current_dir = os.getcwd()
            cutoff_time = datetime.datetime.now() - datetime.timedelta(days=days_old)
            
            deleted_count = 0
            for filename in os.listdir(current_dir):
                if filename.startswith("passwords_") and filename.endswith(".txt"):
                    file_path = os.path.join(current_dir, filename)
                    
                    # 取得檔案修改時間
                    file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    
                    if file_time < cutoff_time:
                        try:
                            os.remove(file_path)
                            deleted_count += 1
                            print(f"🗑️ 已刪除舊檔案: {filename}")
                        except Exception as e:
                            print(f"❌ 刪除檔案失敗 {filename}: {e}")
            
            if deleted_count == 0:
                print(f"✅ 沒有超過 {days_old} 天的檔案需要清理")
            else:
                print(f"🧹 總共清理了 {deleted_count} 個檔案")
                
        except Exception as e:
            print(f"❌ 清理操作失敗: {e}")

# 示範各個模組的具體應用
def demonstrate_modules():
    """示範各個標準模組的使用"""
    print("📚 Python 標準模組使用示範")
    print("=" * 50)
    
    # 1. random 模組示範
    print("\n🎲 random 模組應用:")
    print("-" * 30)
    
    # 基本隨機功能
    print(f"random.randint(1, 10): {random.randint(1, 10)}")
    print(f"random.random(): {random.random():.3f}")
    print(f"random.uniform(1.0, 10.0): {random.uniform(1.0, 10.0):.3f}")
    
    # 隨機選擇
    choices = ["優", "良", "可", "需加強"]
    print(f"random.choice(評級): {random.choice(choices)}")
    
    # 隨機抽樣
    numbers = list(range(1, 21))
    sample = random.sample(numbers, 5)
    print(f"random.sample(1-20, 5): {sample}")
    
    # 隨機打亂
    deck = ["♠A", "♠K", "♠Q", "♠J"]
    random.shuffle(deck)
    print(f"random.shuffle(撲克牌): {deck}")
    
    # 2. string 模組示範
    print("\n📝 string 模組應用:")
    print("-" * 30)
    
    print(f"ascii_lowercase: {string.ascii_lowercase}")
    print(f"ascii_uppercase: {string.ascii_uppercase}")
    print(f"digits: {string.digits}")
    print(f"punctuation: {string.punctuation[:20]}...")
    
    # 組合使用
    all_chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(all_chars, k=8))
    print(f"隨機字串 (8字元): {random_string}")
    
    # 3. datetime 模組示範
    print("\n📅 datetime 模組應用:")
    print("-" * 30)
    
    # 當前時間
    now = datetime.datetime.now()
    today = datetime.date.today()
    
    print(f"datetime.now(): {now}")
    print(f"date.today(): {today}")
    
    # 時間格式化
    formatted = now.strftime("%Y年%m月%d日 %A %H:%M:%S")
    print(f"格式化時間: {formatted}")
    
    # 時間計算
    tomorrow = today + datetime.timedelta(days=1)
    next_week = today + datetime.timedelta(weeks=1)
    print(f"明天: {tomorrow}")
    print(f"下週: {next_week}")
    
    # 時間解析
    time_str = "2024-12-25"
    christmas = datetime.datetime.strptime(time_str, "%Y-%m-%d")
    days_to_christmas = (christmas.date() - today).days
    print(f"距離聖誕節: {days_to_christmas} 天")
    
    # 4. os 模組示範
    print("\n💻 os 模組應用:")
    print("-" * 30)
    
    # 目錄操作
    current_dir = os.getcwd()
    print(f"os.getcwd(): {current_dir}")
    
    # 路徑操作
    example_path = os.path.join("data", "files", "example.txt")
    print(f"os.path.join(): {example_path}")
    
    # 檢查檔案/目錄
    print(f"os.path.exists('.'): {os.path.exists('.')}")
    print(f"os.path.isdir('.'): {os.path.isdir('.')}")
    
    # 環境變數
    user = os.getenv("USERNAME") or os.getenv("USER") or "unknown"
    print(f"使用者名稱: {user}")
    
    # 5. json 模組示範
    print("\n📋 json 模組應用:")
    print("-" * 30)
    
    # 資料序列化
    data = {
        "name": "Python學習者",
        "level": "初學者",
        "progress": 75.5,
        "completed": True,
        "skills": ["變數", "函數", "迴圈", "模組"],
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # 轉為 JSON 字串
    json_string = json.dumps(data, ensure_ascii=False, indent=2)
    print(f"JSON序列化:")
    print(json_string[:100] + "...")
    
    # 從 JSON 字串解析
    parsed_data = json.loads(json_string)
    print(f"解析後的姓名: {parsed_data['name']}")
    
    # 6. math 模組示範
    print("\n🧮 math 模組應用:")
    print("-" * 30)
    
    import math
    
    # 數學常數
    print(f"math.pi: {math.pi:.6f}")
    print(f"math.e: {math.e:.6f}")
    
    # 數學函數
    print(f"math.sqrt(16): {math.sqrt(16)}")
    print(f"math.pow(2, 8): {math.pow(2, 8)}")
    print(f"math.log2(256): {math.log2(256)}")
    
    # 三角函數
    print(f"math.sin(π/2): {math.sin(math.pi/2):.3f}")
    print(f"math.cos(0): {math.cos(0)}")
    
    # 取整函數
    print(f"math.ceil(4.2): {math.ceil(4.2)}")
    print(f"math.floor(4.8): {math.floor(4.8)}")

def interactive_password_tool():
    """互動式密碼工具主程式"""
    print("🔐 歡迎使用隨機密碼產生器！")
    print("這個工具展示了Python標準模組的強大功能")
    print("使用的模組：random, string, datetime, os, json, math")
    
    generator = PasswordGenerator()
    
    while True:
        print("\n" + "=" * 60)
        print("🛠️  功能選單:")
        print("1. 🎲 產生單個密碼")
        print("2. 📝 產生多個密碼")
        print("3. 🔍 分析密碼強度")
        print("4. ⚙️ 修改設定")
        print("5. 📊 使用統計")
        print("6. 📄 匯出密碼到檔案")
        print("7. 🧹 清理舊檔案")
        print("8. 📚 模組使用示範")
        print("9. 🎯 快速產生常用密碼")
        print("0. 🚪 退出程式")
        print("=" * 60)
        
        try:
            choice = input("請選擇功能 (0-9): ").strip()
            
            if choice == "0":
                # 儲存資料並退出
                generator.save_history()
                generator.save_config()
                print("\n👋 感謝使用隨機密碼產生器！")
                print("🔐 記住：好密碼是網路安全的第一道防線！")
                break
            elif choice == "1":
                generate_single_password_interface(generator)
            elif choice == "2":
                generate_multiple_passwords_interface(generator)
            elif choice == "3":
                analyze_password_interface(generator)
            elif choice == "4":
                settings_interface(generator)
            elif choice == "5":
                show_statistics_interface(generator)
            elif choice == "6":
                export_passwords_interface(generator)
            elif choice == "7":
                cleanup_interface(generator)
            elif choice == "8":
                demonstrate_modules()
            elif choice == "9":
                quick_generate_interface(generator)
            else:
                print("❌ 無效選擇，請重新輸入")
                
        except KeyboardInterrupt:
            print("\n\n⚠️ 程式被中斷，正在儲存資料...")
            generator.save_history()
            generator.save_config()
            print("✅ 資料已儲存，程式退出")
            break
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")
            print("程式將繼續運行...")
        
        if choice != "0":
            input("\n按 Enter 繼續...")

def generate_single_password_interface(generator):
    """產生單個密碼的互動介面"""
    print("\n🎲 產生單個密碼")
    print("-" * 30)
    
    try:
        # 獲取密碼長度
        length_input = input(f"密碼長度 (預設 {generator.config['default_length']}): ").strip()
        length = int(length_input) if length_input else generator.config['default_length']
        
        if length < 4 or length > 100:
            print("❌ 密碼長度必須在 4-100 之間")
            return
        
        # 字元類型選擇
        print("\n字元類型設定 (直接按 Enter 使用預設):")
        
        options = {}
        
        lower_input = input("包含小寫字母？(Y/n): ").strip().lower()
        if lower_input in ['y', 'n', '']:
            options['include_lowercase'] = lower_input != 'n'
        
        upper_input = input("包含大寫字母？(Y/n): ").strip().lower()
        if upper_input in ['y', 'n', '']:
            options['include_uppercase'] = upper_input != 'n'
        
        digits_input = input("包含數字？(Y/n): ").strip().lower()
        if digits_input in ['y', 'n', '']:
            options['include_digits'] = digits_input != 'n'
        
        symbols_input = input("包含特殊字符？(Y/n): ").strip().lower()
        if symbols_input in ['y', 'n', '']:
            options['include_symbols'] = symbols_input != 'n'
        
        confusing_input = input("避免混淆字元 (0O1lI)？(Y/n): ").strip().lower()
        if confusing_input in ['y', 'n', '']:
            options['avoid_confusing'] = confusing_input != 'n'
        
        # 產生密碼
        password = generator.generate_password(length, **options)
        
        # 分析密碼
        analysis = generator.analyze_password(password)
        
        # 顯示結果
        print(f"\n🎯 產生的密碼:")
        print("=" * 50)
        print(f"密碼: {password}")
        print(f"長度: {analysis['length']} 字元")
        print(f"強度: {analysis['strength_score']}/100 - {analysis['strength_level']} {analysis['emoji']}")
        print(f"破解時間估算: {analysis['crack_time']}")
        
        print(f"\n📋 字元分析:")
        print(f"  小寫字母: {'✅' if analysis['has_lowercase'] else '❌'}")
        print(f"  大寫字母: {'✅' if analysis['has_uppercase'] else '❌'}")
        print(f"  數字: {'✅' if analysis['has_digits'] else '❌'}")
        print(f"  特殊字符: {'✅' if analysis['has_symbols'] else '❌'}")
        print(f"  字元類型數: {analysis['character_types']}")
        print(f"  唯一字元數: {analysis['unique_characters']}")
        
        # 提供改善建議
        suggestions = []
        if analysis['length'] < 12:
            suggestions.append("建議密碼長度至少 12 字元")
        if analysis['character_types'] < 3:
            suggestions.append("建議使用至少 3 種不同類型的字元")
        if analysis['strength_score'] < 70:
            suggestions.append("建議增加密碼複雜度")
        
        if suggestions:
            print(f"\n💡 改善建議:")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"  {i}. {suggestion}")
        
    except ValueError:
        print("❌ 請輸入有效的數字")
    except Exception as e:
        print(f"❌ 產生密碼失敗: {e}")

def generate_multiple_passwords_interface(generator):
    """產生多個密碼的介面"""
    print("\n📝 產生多個密碼")
    print("-" * 30)
    
    try:
        count = int(input("要產生幾個密碼 (1-20): ") or "5")
        if not 1 <= count <= 20:
            print("❌ 密碼數量必須在 1-20 之間")
            return
        
        length = int(input(f"密碼長度 (預設 {generator.config['default_length']}): ") or generator.config['default_length'])
        
        print(f"\n⏳ 正在產生 {count} 個長度為 {length} 的密碼...")
        
        passwords = generator.generate_multiple_passwords(count, length)
        
        if not passwords:
            print("❌ 沒有成功產生任何密碼")
            return
        
        # 顯示結果
        print(f"\n📋 產生結果:")
        print("-" * 70)
        print(f"{'序號':<4} {'密碼':<25} {'長度':<4} {'強度':<6} {'等級'}")
        print("-" * 70)
        
        for pwd_info in passwords:
            password = pwd_info["password"]
            strength = pwd_info["strength"]
            strength_desc, emoji = generator.get_strength_description(strength)
            
            print(f"{pwd_info['index']:<4} {password:<25} {len(password):<4} {strength:<3}/100 {strength_desc}")
        
        # 顯示統計
        strengths = [p["strength"] for p in passwords]
        print(f"\n📊 統計資訊:")
        print(f"密碼數量: {len(passwords)}")
        print(f"平均強度: {sum(strengths) / len(strengths):.1f}/100")
        print(f"最高強度: {max(strengths)}/100")
        print(f"最低強度: {min(strengths)}/100")
        
        # 強度分佈
        strength_levels = {}
        for pwd_info in passwords:
            level = generator.get_strength_description(pwd_info["strength"])[0]
            strength_levels[level] = strength_levels.get(level, 0) + 1
        
        print(f"\n📈 強度分佈:")
        for level, count in strength_levels.items():
            print(f"  {level}: {count} 個")
        
        # 詢問是否匯出
        export_choice = input("\n是否匯出到檔案？(y/N): ").strip().lower()
        if export_choice == 'y':
            filename = generator.export_passwords(passwords)
            if filename:
                print(f"✅ 已匯出到: {filename}")
        
    except ValueError:
        print("❌ 請輸入有效的數字")
    except Exception as e:
        print(f"❌ 產生密碼失敗: {e}")

def analyze_password_interface(generator):
    """密碼分析介面"""
    print("\n🔍 分析密碼強度")
    print("-" * 30)
    
    password = input("請輸入要分析的密碼: ").strip()
    if not password:
        print("❌ 密碼不能為空")
        return
    
    analysis = generator.analyze_password(password)
    
    print(f"\n📊 密碼分析報告")
    print("=" * 50)
    print(f"密碼長度: {analysis['length']} 字元")
    print(f"強度評分: {analysis['strength_score']}/100")
    print(f"強度等級: {analysis['strength_level']} {analysis['emoji']}")
    print(f"破解時間: {analysis['crack_time']}")
    
    print(f"\n📋 字元組成分析:")
    char_types = []
    if analysis['has_lowercase']:
        char_types.append("小寫字母")
    if analysis['has_uppercase']:
        char_types.append("大寫字母")
    if analysis['has_digits']:
        char_types.append("數字")
    if analysis['has_symbols']:
        char_types.append("特殊字符")
    
    print(f"  包含字元類型: {', '.join(char_types)} ({len(char_types)}/4 種)")
    print(f"  唯一字元數: {analysis['unique_characters']}")
    print(f"  字元重複度: {(1 - analysis['unique_characters'] / analysis['length']) * 100:.1f}%")
    
    # 安全評估
    print(f"\n🛡️ 安全評估:")
    
    security_tips = []
    if analysis['length'] < 8:
        security_tips.append("❌ 密碼太短，容易被暴力破解")
    elif analysis['length'] < 12:
        security_tips.append("⚠️ 密碼長度一般，建議增加到12字元以上")
    else:
        security_tips.append("✅ 密碼長度符合安全要求")
    
    if analysis['character_types'] < 2:
        security_tips.append("❌ 字元類型太少，安全性不足")
    elif analysis['character_types'] < 3:
        security_tips.append("⚠️ 建議增加更多字元類型")
    else:
        security_tips.append("✅ 字元類型多樣，安全性較好")
    
    if analysis['unique_characters'] / analysis['length'] < 0.5:
        security_tips.append("⚠️ 字元重複較多，可能影響安全性")
    else:
        security_tips.append("✅ 字元多樣性良好")
    
    for tip in security_tips:
        print(f"  {tip}")

def settings_interface(generator):
    """設定介面"""
    print("\n⚙️ 產生器設定")
    print("-" * 30)
    
    config = generator.config
    
    print("目前設定:")
    print(f"  預設密碼長度: {config['default_length']}")
    print(f"  包含小寫字母: {'是' if config['include_lowercase'] else '否'}")
    print(f"  包含大寫字母: {'是' if config['include_uppercase'] else '否'}")
    print(f"  包含數字: {'是' if config['include_digits'] else '否'}")
    print(f"  包含特殊字符: {'是' if config['include_symbols'] else '否'}")
    print(f"  避免混淆字元: {'是' if config['avoid_confusing'] else '否'}")
    
    modify = input("\n是否要修改設定？(y/N): ").strip().lower()
    if modify != 'y':
        return
    
    try:
        print("\n請輸入新的設定值 (直接按 Enter 保持不變):")
        
        # 修改預設長度
        length_input = input(f"預設密碼長度 (目前: {config['default_length']}): ").strip()
        if length_input:
            new_length = int(length_input)
            if 4 <= new_length <= 100:
                generator.config['default_length'] = new_length
            else:
                print("⚠️ 長度必須在 4-100 之間，保持原設定")
        
        # 修改字元類型設定
        settings_map = [
            ('include_lowercase', '包含小寫字母'),
            ('include_uppercase', '包含大寫字母'),
            ('include_digits', '包含數字'),
            ('include_symbols', '包含特殊字符'),
            ('avoid_confusing', '避免混淆字元')
        ]
        
        for key, description in settings_map:
            current_value = '是' if config[key] else '否'
            user_input = input(f"{description} (目前: {current_value}, y/n): ").strip().lower()
            if user_input in ['y', 'n']:
                generator.config[key] = (user_input == 'y')
        
        # 儲存設定
        generator.save_config()
        print("✅ 設定已儲存")
        
        # 驗證設定
        char_types = sum([
            generator.config['include_lowercase'],
            generator.config['include_uppercase'],
            generator.config['include_digits'],
            generator.config['include_symbols']
        ])
        
        if char_types == 0:
            print("⚠️ 警告：沒有選擇任何字元類型！")
            print("   將自動啟用小寫字母")
            generator.config['include_lowercase'] = True
            generator.save_config()
        
    except ValueError:
        print("❌ 輸入格式錯誤")
    except Exception as e:
        print(f"❌ 設定失敗: {e}")

def show_statistics_interface(generator):
    """顯示使用統計介面"""
    print("\n📊 使用統計")
    print("-" * 30)
    
    stats = generator.get_usage_statistics()
    if not stats:
        print("📝 暫無使用記錄")
        print("   開始產生密碼後就會有統計資訊了！")
        return
    
    print("📈 總體統計:")
    print(f"  總共產生密碼: {stats['total_generated']} 個")
    print(f"  平均密碼長度: {stats['average_length']} 字元")
    print(f"  平均密碼強度: {stats['average_strength']}/100")
    print(f"  最近7天產生: {stats['recent_week_count']} 個")
    print(f"  最常用長度: {stats['most_common_length']} 字元 (使用 {stats['most_common_count']} 次)")
    
    # 顯示最近的產生記錄
    recent_records = generator.generation_history[-10:]  # 最近10筆
    if recent_records:
        print(f"\n📋 最近 {len(recent_records)} 次產生記錄:")
        print("-" * 60)
        print(f"{'時間':<20} {'長度':<6} {'強度':<8} {'字元類型'}")
        print("-" * 60)
        
        for record in reversed(recent_records):
            try:
                # 格式化時間顯示
                time_str = record.get('formatted_time', record['timestamp'][:19])
                if 'T' in time_str:
                    time_str = time_str.replace('T', ' ')
                
                print(f"{time_str:<20} {record['length']:<6} {record['strength_score']:<3}/100 {record.get('character_types', '?')}")
            except (KeyError, ValueError):
                continue
    
    # 使用活躍度分析
    if stats['total_generated'] > 0:
        print(f"\n📊 使用分析:")
        activity_level = "高" if stats['recent_week_count'] > 10 else "中" if stats['recent_week_count'] > 3 else "低"
        print(f"  近期活躍度: {activity_level}")
        
        if stats['average_strength'] >= 80:
            print(f"  安全意識: 優秀 (平均強度 {stats['average_strength']:.1f})")
        elif stats['average_strength'] >= 60:
            print(f"  安全意識: 良好 (平均強度 {stats['average_strength']:.1f})")
        else:
            print(f"  安全意識: 需要改善 (平均強度 {stats['average_strength']:.1f})")

def export_passwords_interface(generator):
    """匯出密碼介面"""
    print("\n📄 匯出密碼到檔案")
    print("-" * 30)
    
    try:
        count = int(input("要產生並匯出幾個密碼 (1-50): ") or "10")
        if not 1 <= count <= 50:
            print("❌ 密碼數量必須在 1-50 之間")
            return
        
        length = int(input(f"密碼長度 (預設 {generator.config['default_length']}): ") or generator.config['default_length'])
        
        print(f"\n⏳ 正在產生 {count} 個密碼...")
        passwords = generator.generate_multiple_passwords(count, length)
        
        if not passwords:
            print("❌ 沒有成功產生任何密碼")
            return
        
        # 獲取檔案名稱
        filename = input("檔案名稱 (留空自動產生): ").strip()
        if not filename:
            filename = None
        
        # 匯出密碼
        exported_file = generator.export_passwords(passwords, filename)
        
        if exported_file:
            print(f"✅ 成功匯出 {len(passwords)} 個密碼")
            print(f"📁 檔案位置: {exported_file}")
            
            # 顯示統計
            avg_strength = sum(p["strength"] for p in passwords) / len(passwords)
            high_strength_count = sum(1 for p in passwords if p["strength"] >= 75)
            
            print(f"\n📊 匯出統計:")
            print(f"  平均強度: {avg_strength:.1f}/100")
            print(f"  高強度密碼: {high_strength_count}/{len(passwords)} 個")
            
            print(f"\n⚠️  安全提醒:")
            print(f"  • 請妥善保管匯出的檔案")
            print(f"  • 使用後建議刪除檔案")
            print(f"  • 不要透過不安全管道分享密碼")
        
    except ValueError:
        print("❌ 請輸入有效的數字")
    except Exception as e:
        print(f"❌ 匯出失敗: {e}")

def cleanup_interface(generator):
    """清理舊檔案介面"""
    print("\n🧹 清理舊檔案")
    print("-" * 30)
    
    try:
        # 顯示當前目錄中的密碼檔案
        current_dir = os.getcwd()
        password_files = []
        
        for filename in os.listdir(current_dir):
            if filename.startswith("passwords_") and filename.endswith(".txt"):
                file_path = os.path.join(current_dir, filename)
                file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                file_size = os.path.getsize(file_path)
                password_files.append((filename, file_time, file_size))
        
        if not password_files:
            print("📁 目前沒有發現密碼檔案")
            return
        
        print(f"📋 發現 {len(password_files)} 個密碼檔案:")
        print("-" * 60)
        print(f"{'檔案名稱':<25} {'建立時間':<20} {'大小':<10}")
        print("-" * 60)
        
        for filename, file_time, file_size in password_files:
            time_str = file_time.strftime("%Y-%m-%d %H:%M")
            size_str = f"{file_size} bytes"
            print(f"{filename:<25} {time_str:<20} {size_str:<10}")
        
        # 詢問清理選項
        print(f"\n清理選項:")
        print(f"1. 清理超過7天的檔案")
        print(f"2. 清理超過30天的檔案")
        print(f"3. 清理所有檔案")
        print(f"4. 取消")
        
        choice = input("請選擇 (1-4): ").strip()
        
        if choice == "1":
            generator.cleanup_old_files(days_old=7)
        elif choice == "2":
            generator.cleanup_old_files(days_old=30)
        elif choice == "3":
            confirm = input("確定要刪除所有密碼檔案嗎？(y/N): ").strip().lower()
            if confirm == 'y':
                deleted_count = 0
                for filename, _, _ in password_files:
                    try:
                        os.remove(filename)
                        deleted_count += 1
                        print(f"🗑️ 已刪除: {filename}")
                    except Exception as e:
                        print(f"❌ 刪除失敗 {filename}: {e}")
                
                print(f"✅ 總共刪除了 {deleted_count} 個檔案")
            else:
                print("❌ 取消刪除操作")
        elif choice == "4":
            print("❌ 取消清理操作")
        else:
            print("❌ 無效選擇")
    
    except Exception as e:
        print(f"❌ 清理操作失敗: {e}")

def quick_generate_interface(generator):
    """快速產生常用密碼介面"""
    print("\n🎯 快速產生常用密碼")
    print("-" * 30)
    
    presets = [
        {
            "name": "網站註冊密碼",
            "description": "12字元，包含大小寫字母、數字和符號",
            "options": {"length": 12, "include_symbols": True}
        },
        {
            "name": "WiFi密碼",
            "description": "16字元，高強度，易於輸入",
            "options": {"length": 16, "include_symbols": False, "avoid_confusing": True}
        },
        {
            "name": "銀行密碼",
            "description": "8字元，僅數字和字母",
            "options": {"length": 8, "include_symbols": False}
        },
        {
            "name": "超高強度密碼",
            "description": "20字元，包含所有字元類型",
            "options": {"length": 20, "include_symbols": True}
        },
        {
            "name": "簡單密碼",
            "description": "8字元，僅字母和數字",
            "options": {"length": 8, "include_symbols": False}
        }
    ]
    
    print("預設密碼類型:")
    for i, preset in enumerate(presets, 1):
        print(f"{i}. {preset['name']} - {preset['description']}")
    
    try:
        choice = int(input(f"\n請選擇類型 (1-{len(presets)}): "))
        if not 1 <= choice <= len(presets):
            print("❌ 無效選擇")
            return
        
        selected_preset = presets[choice - 1]
        count = int(input("產生數量 (1-10): ") or "3")
        if not 1 <= count <= 10:
            print("❌ 數量必須在 1-10 之間")
            return
        
        print(f"\n⏳ 正在產生 {count} 個「{selected_preset['name']}」...")
        
        passwords = []
        for i in range(count):
            try:
                password = generator.generate_password(**selected_preset['options'])
                analysis = generator.analyze_password(password)
                passwords.append({
                    "index": i + 1,
                    "password": password,
                    "strength": analysis['strength_score'],
                    "length": len(password)
                })
            except Exception as e:
                print(f"❌ 產生第 {i+1} 個密碼失敗: {e}")
        
        if passwords:
            print(f"\n🎯 「{selected_preset['name']}」產生結果:")
            print("-" * 50)
            
            for pwd_info in passwords:
                password = pwd_info["password"]
                strength = pwd_info["strength"]
                strength_desc, emoji = generator.get_strength_description(strength)
                
                print(f"{pwd_info['index']}. {password} ({strength}/100 {emoji})")
            
            # 統計
            avg_strength = sum(p["strength"] for p in passwords) / len(passwords)
            print(f"\n📊 平均強度: {avg_strength:.1f}/100")
        
    except ValueError:
        print("❌ 請輸入有效的數字")
    except Exception as e:
        print(f"❌ 產生失敗: {e}")

if __name__ == "__main__":
    # 設定隨機數種子以保證每次運行有不同結果
    random.seed()
    
    # 啟動互動式密碼工具
    interactive_password_tool()