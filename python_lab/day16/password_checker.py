"""
Day 16: 密碼強度檢查器
實作重點：預設參數、區域變數與全域變數、*args和**kwargs
"""

import string
import random
import re
import os
import json
from datetime import datetime

# 全域設定變數
MIN_LENGTH = 8
RECOMMENDED_LENGTH = 12
SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;':\".,<>?/~`"
COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "qwerty",
    "letmein", "welcome", "monkey", "dragon", "master"
]

# 密碼歷史記錄檔案
HISTORY_FILE = "password_history.json"

def load_password_history():
    """載入密碼檢查歷史"""
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"載入歷史記錄失敗：{e}")
    return []

def save_password_history(history):
    """儲存密碼檢查歷史"""
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"儲存歷史記錄失敗：{e}")

def check_password_length(password, min_length=MIN_LENGTH, recommended_length=RECOMMENDED_LENGTH):
    """
    檢查密碼長度
    使用預設參數示範
    """
    length = len(password)
    
    if length >= recommended_length:
        return True, f"✅ 長度優秀 ({length} 個字符，超過建議長度)"
    elif length >= min_length:
        return True, f"✅ 長度足夠 ({length} 個字符)"
    else:
        return False, f"❌ 長度不足 ({length} 個字符，至少需要 {min_length} 個)"

def check_character_types(password, *required_types):
    """
    檢查密碼字符類型
    使用 *args 示範
    
    參數:
        password: 要檢查的密碼
        *required_types: 要求的字符類型 ('upper', 'lower', 'digit', 'special')
    """
    results = {}
    
    # 預設檢查所有類型
    if not required_types:
        required_types = ('upper', 'lower', 'digit', 'special')
    
    for char_type in required_types:
        if char_type == 'upper':
            count = len(re.findall(r'[A-Z]', password))
            results['upper'] = (count > 0, f"大寫字母: {count} 個")
        elif char_type == 'lower':
            count = len(re.findall(r'[a-z]', password))
            results['lower'] = (count > 0, f"小寫字母: {count} 個")
        elif char_type == 'digit':
            count = len(re.findall(r'\d', password))
            results['digit'] = (count > 0, f"數字: {count} 個")
        elif char_type == 'special':
            count = len([c for c in password if c in SPECIAL_CHARS])
            results['special'] = (count > 0, f"特殊字符: {count} 個")
    
    return results

def analyze_password_patterns(password, **options):
    """
    分析密碼模式
    使用 **kwargs 示範
    
    可選參數:
        check_common: 檢查常見密碼
        check_keyboard: 檢查鍵盤模式
        check_repetition: 檢查重複字符
        check_sequence: 檢查連續字符
    """
    # 預設選項
    default_options = {
        'check_common': True,
        'check_keyboard': True,
        'check_repetition': True,
        'check_sequence': True
    }
    
    # 合併使用者選項
    default_options.update(options)
    
    issues = []
    
    if default_options['check_common']:
        # 檢查常見密碼
        for common in COMMON_PASSWORDS:
            if common.lower() in password.lower():
                issues.append(f"包含常見密碼模式: {common}")
    
    if default_options['check_keyboard']:
        # 檢查鍵盤模式
        keyboard_patterns = ['qwerty', 'asdf', '1234', 'abcd']
        for pattern in keyboard_patterns:
            if pattern in password.lower():
                issues.append(f"包含鍵盤模式: {pattern}")
    
    if default_options['check_repetition']:
        # 檢查重複字符
        if re.search(r'(.)\1{2,}', password):
            issues.append("包含重複字符 (如: aaa, 111)")
    
    if default_options['check_sequence']:
        # 檢查連續字符
        sequences = ['abcdefg', '1234567', '7654321']
        for seq in sequences:
            if any(seq[i:i+3] in password.lower() for i in range(len(seq)-2)):
                issues.append("包含連續字符序列")
                break
    
    return issues

def calculate_entropy(password):
    """計算密碼熵值"""
    char_space = 0
    
    if re.search(r'[a-z]', password):
        char_space += 26
    if re.search(r'[A-Z]', password):
        char_space += 26
    if re.search(r'\d', password):
        char_space += 10
    if re.search(r'[' + re.escape(SPECIAL_CHARS) + ']', password):
        char_space += len(SPECIAL_CHARS)
    
    if char_space == 0:
        return 0
    
    import math
    entropy = len(password) * math.log2(char_space)
    return entropy

def get_password_strength_score(password, custom_weights=None):
    """
    計算密碼強度分數
    使用預設參數和區域變數示範
    """
    # 預設權重
    default_weights = {
        'length': 0.25,
        'character_diversity': 0.25,
        'entropy': 0.2,
        'pattern_safety': 0.2,
        'uniqueness': 0.1
    }
    
    # 如果有自訂權重，使用自訂權重
    weights = custom_weights if custom_weights else default_weights
    
    # 區域變數計算各項分數
    length_score = min(100, (len(password) / RECOMMENDED_LENGTH) * 100)
    
    # 字符多樣性分數
    char_types = check_character_types(password)
    diversity_score = (sum(1 for passed, _ in char_types.values() if passed) / 4) * 100
    
    # 熵值分數
    entropy = calculate_entropy(password)
    entropy_score = min(100, (entropy / 50) * 100)  # 50 bits 為參考值
    
    # 模式安全性分數
    issues = analyze_password_patterns(password)
    pattern_score = max(0, 100 - len(issues) * 20)
    
    # 唯一性分數（簡化版）
    uniqueness_score = 100 if len(set(password)) / len(password) > 0.7 else 60
    
    # 加權總分
    total_score = (
        length_score * weights['length'] +
        diversity_score * weights['character_diversity'] +
        entropy_score * weights['entropy'] +
        pattern_score * weights['pattern_safety'] +
        uniqueness_score * weights['uniqueness']
    )
    
    return min(100, max(0, total_score))

def generate_password_suggestions(*requirements, **options):
    """
    生成密碼建議
    結合 *args 和 **kwargs 的使用
    
    *requirements: 可以傳入多個要求 ('strong', 'memorable', 'complex')
    **options: 選項如 length, include_numbers 等
    """
    # 預設選項
    default_options = {
        'length': RECOMMENDED_LENGTH,
        'include_numbers': True,
        'include_uppercase': True,
        'include_lowercase': True,
        'include_special': True,
        'count': 3
    }
    
    # 更新選項
    default_options.update(options)
    
    suggestions = []
    
    for requirement in requirements:
        if requirement == 'strong':
            # 產生高強度密碼
            suggestions.append(generate_strong_password(**default_options))
        elif requirement == 'memorable':
            # 產生容易記憶的密碼
            suggestions.append(generate_memorable_password(**default_options))
        elif requirement == 'complex':
            # 產生複雜密碼
            suggestions.append(generate_complex_password(**default_options))
    
    # 如果沒有指定要求，產生預設密碼
    if not requirements:
        for _ in range(default_options['count']):
            suggestions.append(generate_strong_password(**default_options))
    
    return suggestions

def generate_strong_password(length=RECOMMENDED_LENGTH, **options):
    """生成高強度密碼"""
    chars = ""
    required_chars = []
    
    if options.get('include_lowercase', True):
        chars += string.ascii_lowercase
        required_chars.append(random.choice(string.ascii_lowercase))
    
    if options.get('include_uppercase', True):
        chars += string.ascii_uppercase
        required_chars.append(random.choice(string.ascii_uppercase))
    
    if options.get('include_numbers', True):
        chars += string.digits
        required_chars.append(random.choice(string.digits))
    
    if options.get('include_special', True):
        chars += SPECIAL_CHARS
        required_chars.append(random.choice(SPECIAL_CHARS))
    
    # 生成剩餘字符
    remaining_length = length - len(required_chars)
    random_chars = [random.choice(chars) for _ in range(remaining_length)]
    
    # 組合並打亂
    password_chars = required_chars + random_chars
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def generate_memorable_password(length=RECOMMENDED_LENGTH, **options):
    """生成易記憶密碼（使用單詞組合）"""
    # 簡單的單詞列表
    words = [
        'Apple', 'Brave', 'Cloud', 'Dance', 'Eagle',
        'Forest', 'Grace', 'Happy', 'Island', 'Joy',
        'Knight', 'Light', 'Magic', 'Noble', 'Ocean'
    ]
    
    # 選擇單詞
    selected_words = random.sample(words, 2)
    base_password = ''.join(selected_words)
    
    # 添加數字
    if options.get('include_numbers', True):
        base_password += str(random.randint(10, 99))
    
    # 添加特殊字符
    if options.get('include_special', True):
        base_password += random.choice('!@#$%')
    
    # 調整長度
    while len(base_password) < length:
        base_password += random.choice(string.digits)
    
    return base_password[:length]

def generate_complex_password(length=RECOMMENDED_LENGTH, **options):
    """生成複雜密碼（最大化熵值）"""
    # 使用所有可能的字符
    all_chars = (string.ascii_letters + string.digits + SPECIAL_CHARS)
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def create_detailed_report(password):
    """
    創建詳細的密碼分析報告
    示範函數內的區域變數使用
    """
    # 區域變數 - 報告數據
    report_data = {
        'timestamp': datetime.now().isoformat(),
        'password_length': len(password),
        'analysis_results': {}
    }
    
    print(f"\n🔍 詳細密碼分析報告")
    print("=" * 60)
    print(f"📅 分析時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📏 密碼長度: {len(password)} 個字符")
    
    # 基本檢查
    length_ok, length_msg = check_password_length(password)
    print(f"\n📏 長度檢查:")
    print(f"   {length_msg}")
    report_data['analysis_results']['length'] = {'passed': length_ok, 'message': length_msg}
    
    # 字符類型檢查
    char_results = check_character_types(password)
    print(f"\n🔤 字符類型檢查:")
    for char_type, (passed, message) in char_results.items():
        status = "✅" if passed else "❌"
        print(f"   {status} {message}")
        report_data['analysis_results'][char_type] = {'passed': passed, 'message': message}
    
    # 模式分析
    issues = analyze_password_patterns(password)
    print(f"\n🔍 安全模式分析:")
    if issues:
        for issue in issues:
            print(f"   ⚠️ {issue}")
        report_data['analysis_results']['patterns'] = {'issues': issues}
    else:
        print("   ✅ 未發現安全問題")
        report_data['analysis_results']['patterns'] = {'issues': []}
    
    # 強度分數
    score = get_password_strength_score(password)
    strength_level = get_strength_description(score)
    print(f"\n📊 強度評分:")
    print(f"   分數: {score:.1f}/100")
    print(f"   等級: {strength_level}")
    report_data['analysis_results']['score'] = score
    report_data['analysis_results']['strength'] = strength_level
    
    # 熵值計算
    entropy = calculate_entropy(password)
    print(f"\n🎲 熵值分析:")
    print(f"   熵值: {entropy:.2f} bits")
    print(f"   理論破解時間: {estimate_crack_time(entropy)}")
    report_data['analysis_results']['entropy'] = entropy
    
    return report_data

def get_strength_description(score):
    """根據分數返回強度描述"""
    if score >= 90:
        return "🔒 非常強 - 極難破解"
    elif score >= 75:
        return "🔐 強 - 很難破解"
    elif score >= 60:
        return "🔓 中等 - 一般安全"
    elif score >= 40:
        return "⚠️ 弱 - 容易破解"
    else:
        return "❌ 非常弱 - 極易破解"

def estimate_crack_time(entropy):
    """估算破解時間"""
    if entropy < 30:
        return "幾秒到幾分鐘"
    elif entropy < 50:
        return "幾小時到幾天"
    elif entropy < 70:
        return "幾年到幾十年"
    else:
        return "數百年以上"

def interactive_password_checker():
    """互動式密碼檢查器主程式"""
    print("🔐 歡迎使用進階密碼強度檢查器！")
    print("這個工具展示了函數進階概念的應用")
    
    # 載入歷史記錄
    history = load_password_history()
    
    while True:
        print("\n" + "=" * 60)
        print("🛠️  請選擇功能：")
        print("1. 🔍 基本密碼檢查")
        print("2. 📊 詳細密碼分析")
        print("3. 🎲 生成密碼建議")
        print("4. ⚙️ 自訂檢查參數")
        print("5. 📈 批次密碼分析")
        print("6. 📜 檢查歷史記錄")
        print("7. 🧪 函數概念示範")
        print("0. 🚪 退出程式")
        print("=" * 60)
        
        choice = input("請選擇 (0-7): ").strip()
        
        if choice == "1":
            basic_password_check()
        elif choice == "2":
            detailed_password_analysis()
        elif choice == "3":
            password_generation_menu()
        elif choice == "4":
            custom_parameter_check()
        elif choice == "5":
            batch_password_analysis()
        elif choice == "6":
            show_history(history)
        elif choice == "7":
            function_concept_demo()
        elif choice == "0":
            save_password_history(history)
            print("\n👋 感謝使用密碼檢查器！")
            print("🔐 記住：好密碼是數位安全的基礎！")
            break
        else:
            print("❌ 無效選擇！")

def basic_password_check():
    """基本密碼檢查"""
    print("\n🔍 基本密碼檢查")
    print("-" * 30)
    
    password = input("請輸入密碼: ")
    if not password:
        print("❌ 密碼不能為空！")
        return
    
    # 基本檢查
    length_ok, length_msg = check_password_length(password)
    char_results = check_character_types(password)
    score = get_password_strength_score(password)
    
    print(f"\n📋 檢查結果:")
    print(f"   {length_msg}")
    
    for char_type, (passed, message) in char_results.items():
        status = "✅" if passed else "❌"
        print(f"   {status} {message}")
    
    print(f"\n📊 總體評分: {score:.1f}/100 - {get_strength_description(score)}")

def detailed_password_analysis():
    """詳細密碼分析"""
    print("\n📊 詳細密碼分析")
    print("-" * 30)
    
    password = input("請輸入密碼: ")
    if not password:
        print("❌ 密碼不能為空！")
        return
    
    # 創建詳細報告
    report = create_detailed_report(password)
    
    # 儲存到歷史記錄
    history = load_password_history()
    history.append({
        'timestamp': report['timestamp'],
        'score': report['analysis_results']['score'],
        'length': report['password_length']
    })
    
    # 只保留最近50筆記錄
    if len(history) > 50:
        history = history[-50:]
    
    save_password_history(history)

def password_generation_menu():
    """密碼生成選單"""
    print("\n🎲 密碼生成器")
    print("-" * 25)
    
    print("請選擇生成類型：")
    print("1. 高強度密碼")
    print("2. 易記憶密碼")
    print("3. 複雜密碼")
    print("4. 自訂要求")
    
    choice = input("請選擇 (1-4): ").strip()
    
    if choice == "1":
        passwords = generate_password_suggestions("strong")
    elif choice == "2":
        passwords = generate_password_suggestions("memorable")
    elif choice == "3":
        passwords = generate_password_suggestions("complex")
    elif choice == "4":
        passwords = custom_password_generation()
    else:
        print("❌ 無效選擇！")
        return
    
    if passwords:
        print(f"\n🎯 為您生成的密碼建議:")
        for i, pwd in enumerate(passwords, 1):
            score = get_password_strength_score(pwd)
            print(f"{i}. {pwd} (強度: {score:.1f}/100)")

def custom_password_generation():
    """自訂密碼生成"""
    print("\n⚙️ 自訂密碼生成")
    
    try:
        length = int(input("密碼長度 (8-32): ") or "12")
        if not 8 <= length <= 32:
            print("長度設定為預設值 12")
            length = 12
        
        count = int(input("生成數量 (1-10): ") or "3")
        if not 1 <= count <= 10:
            count = 3
        
        # 字符類型選擇
        print("\n字符類型選擇:")
        include_upper = input("包含大寫字母？(Y/n): ").strip().lower() != 'n'
        include_lower = input("包含小寫字母？(Y/n): ").strip().lower() != 'n'
        include_numbers = input("包含數字？(Y/n): ").strip().lower() != 'n'
        include_special = input("包含特殊字符？(Y/n): ").strip().lower() != 'n'
        
        passwords = []
        for _ in range(count):
            pwd = generate_strong_password(
                length=length,
                include_uppercase=include_upper,
                include_lowercase=include_lower,
                include_numbers=include_numbers,
                include_special=include_special
            )
            passwords.append(pwd)
        
        return passwords
        
    except ValueError:
        print("❌ 請輸入有效數字！")
        return []

def custom_parameter_check():
    """自訂參數檢查"""
    print("\n⚙️ 自訂檢查參數")
    print("-" * 25)
    
    password = input("請輸入密碼: ")
    if not password:
        print("❌ 密碼不能為空！")
        return
    
    # 自訂最小長度
    try:
        min_len = int(input(f"自訂最小長度 (預設 {MIN_LENGTH}): ") or MIN_LENGTH)
        rec_len = int(input(f"自訂建議長度 (預設 {RECOMMENDED_LENGTH}): ") or RECOMMENDED_LENGTH)
    except ValueError:
        print("使用預設長度設定")
        min_len, rec_len = MIN_LENGTH, RECOMMENDED_LENGTH
    
    # 自訂字符類型檢查
    print("\n選擇要檢查的字符類型:")
    check_types = []
    if input("檢查大寫字母？(Y/n): ").strip().lower() != 'n':
        check_types.append('upper')
    if input("檢查小寫字母？(Y/n): ").strip().lower() != 'n':
        check_types.append('lower')
    if input("檢查數字？(Y/n): ").strip().lower() != 'n':
        check_types.append('digit')
    if input("檢查特殊字符？(Y/n): ").strip().lower() != 'n':
        check_types.append('special')
    
    # 執行自訂檢查
    print(f"\n📋 自訂檢查結果:")
    
    # 長度檢查
    length_ok, length_msg = check_password_length(password, min_len, rec_len)
    print(f"   {length_msg}")
    
    # 字符類型檢查
    if check_types:
        char_results = check_character_types(password, *check_types)
        for char_type, (passed, message) in char_results.items():
            status = "✅" if passed else "❌"
            print(f"   {status} {message}")

def batch_password_analysis():
    """批次密碼分析"""
    print("\n📈 批次密碼分析")
    print("-" * 25)
    
    passwords = []
    print("請輸入要分析的密碼（每行一個），輸入 'done' 結束：")
    
    while True:
        pwd = input(f"密碼 #{len(passwords) + 1}: ").strip()
        if pwd.lower() == 'done':
            break
        if pwd:
            passwords.append(pwd)
    
    if not passwords:
        print("❌ 沒有輸入任何密碼！")
        return
    
    print(f"\n📊 分析 {len(passwords)} 個密碼的結果:")
    print("=" * 60)
    
    total_score = 0
    for i, pwd in enumerate(passwords, 1):
        score = get_password_strength_score(pwd)
        total_score += score
        strength = get_strength_description(score)
        print(f"{i:2d}. {'*' * len(pwd)} ({len(pwd)} 字符) - {score:.1f}/100 - {strength}")
    
    avg_score = total_score / len(passwords)
    print(f"\n📈 統計摘要:")
    print(f"   平均分數: {avg_score:.1f}/100")
    print(f"   總密碼數: {len(passwords)}")
    print(f"   安全密碼數: {sum(1 for pwd in passwords if get_password_strength_score(pwd) >= 70)}")

def show_history(history):
    """顯示檢查歷史"""
    print("\n📜 密碼檢查歷史")
    print("-" * 30)
    
    if not history:
        print("沒有歷史記錄")
        return
    
    print(f"最近 {len(history)} 次檢查:")
    for i, record in enumerate(reversed(history[-10:]), 1):  # 顯示最近10筆
        timestamp = record['timestamp'][:19].replace('T', ' ')
        print(f"{i:2d}. {timestamp} - 長度:{record['length']} - 分數:{record['score']:.1f}")

def function_concept_demo():
    """函數概念示範"""
    print("\n🧪 函數進階概念示範")
    print("-" * 35)
    
    print("這個示範展示了今天學習的函數概念：")
    
    # 1. 預設參數示範
    print("\n1. 📝 預設參數示範:")
    demo_password = "TestPass123!"
    print(f"   檢查密碼: {demo_password}")
    
    # 使用預設參數
    result1 = check_password_length(demo_password)
    print(f"   使用預設參數: {result1[1]}")
    
    # 使用自訂參數
    result2 = check_password_length(demo_password, min_length=15)
    print(f"   自訂最小長度15: {result2[1]}")
    
    # 2. *args 示範
    print("\n2. 🎯 *args 示範:")
    print("   只檢查大寫和數字:")
    results = check_character_types(demo_password, 'upper', 'digit')
    for char_type, (passed, msg) in results.items():
        print(f"     {msg}: {'✅' if passed else '❌'}")
    
    # 3. **kwargs 示範
    print("\n3. ⚙️ **kwargs 示範:")
    print("   自訂模式檢查選項:")
    issues = analyze_password_patterns(
        demo_password,
        check_common=True,
        check_keyboard=False,
        check_repetition=True
    )
    if issues:
        for issue in issues:
            print(f"     ⚠️ {issue}")
    else:
        print("     ✅ 沒有發現問題")
    
    # 4. 區域變數與全域變數示範
    print("\n4. 🏠 變數作用域示範:")
    print(f"   全域 MIN_LENGTH: {MIN_LENGTH}")
    print(f"   全域 RECOMMENDED_LENGTH: {RECOMMENDED_LENGTH}")
    
    def demo_scope():
        local_var = "我是區域變數"
        global RECOMMENDED_LENGTH
        print(f"   函數內可以使用全域變數: {RECOMMENDED_LENGTH}")
        print(f"   區域變數: {local_var}")
        return local_var
    
    local_result = demo_scope()
    print(f"   函數回傳的區域變數: {local_result}")
    # print(f"   直接使用區域變數會出錯: {local_var}")  # 這行會出錯

if __name__ == "__main__":
    interactive_password_checker()