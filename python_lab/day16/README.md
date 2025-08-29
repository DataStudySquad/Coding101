# Day 16：函數進階

## 今日學習目標
- 掌握預設參數的使用方法
- 理解區域變數與全域變數的區別
- 學會使用*args和**kwargs
- 實作密碼強度檢查器程式
- 理解變數作用域的重要概念

## 1. 預設參數（Default Parameters）

### 1.1 什麼是預設參數？
預設參數就像是**餐廳的套餐選項**：
- 如果你不特別要求，餐廳會給你標準配置
- 如果你有特別需求，可以客製化更改
- 這樣既方便又有彈性

### 1.2 基本語法
```python
def function_name(parameter1, parameter2=default_value):
    # 函數內容
    pass
```

### 1.3 預設參數範例
```python
def greet_person(name, greeting="你好"):
    """打招呼函數，可以自訂問候語"""
    print(f"{greeting}，{name}！")

# 使用預設問候語
greet_person("小明")  # 輸出：你好，小明！

# 自訂問候語
greet_person("小美", "早安")  # 輸出：早安，小美！
greet_person("老師", greeting="午安")  # 輸出：午安，老師！
```

### 1.4 實用的預設參數範例
```python
def calculate_power(base, exponent=2):
    """計算次方，預設為平方"""
    return base ** exponent

# 計算平方（使用預設值）
print(calculate_power(5))      # 25 (5的平方)

# 計算立方
print(calculate_power(5, 3))   # 125 (5的立方)

def format_name(first_name, last_name, middle_initial=""):
    """格式化姓名，中間名是可選的"""
    if middle_initial:
        return f"{first_name} {middle_initial}. {last_name}"
    else:
        return f"{first_name} {last_name}"

# 沒有中間名
print(format_name("John", "Smith"))         # John Smith

# 有中間名
print(format_name("John", "Smith", "M"))    # John M. Smith

def send_email(to, subject, body, priority="normal"):
    """發送電子郵件，預設為普通優先度"""
    print(f"發送郵件到：{to}")
    print(f"主題：{subject}")
    print(f"內容：{body}")
    print(f"優先度：{priority}")

# 使用預設優先度
send_email("user@example.com", "會議通知", "明天開會")

# 設定高優先度
send_email("boss@company.com", "緊急！", "系統故障", "high")
```

### 1.5 預設參數的陷阱
```python
# ❌ 危險：使用可變物件作為預設值
def add_item_bad(item, target_list=[]):
    """錯誤示範：預設參數是可變物件"""
    target_list.append(item)
    return target_list

# 這會產生意外的結果
list1 = add_item_bad("蘋果")
print(list1)  # ['蘋果']

list2 = add_item_bad("香蕉")
print(list2)  # ['蘋果', '香蕉'] ← 意外！包含了之前的項目

# ✅ 正確：使用None作為預設值
def add_item_good(item, target_list=None):
    """正確示範：安全的預設參數"""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

# 正常結果
list1 = add_item_good("蘋果")
print(list1)  # ['蘋果']

list2 = add_item_good("香蕉")
print(list2)  # ['香蕉'] ← 正確！
```

## 2. 區域變數與全域變數（Local vs Global Variables）

### 2.1 變數作用域概念
想像變數作用域就像是**房間的概念**：
- **全域變數**：客廳的東西，整個房子都能看到和使用
- **區域變數**：個人房間的東西，只有在那個房間才能使用
- 如果房間裡沒有某樣東西，會去客廳找

### 2.2 基本範例
```python
# 全域變數（在函數外定義）
global_message = "我是全域變數"
counter = 0

def show_variables():
    """示範變數作用域"""
    # 區域變數（在函數內定義）
    local_message = "我是區域變數"
    
    # 可以使用全域變數
    print(global_message)
    
    # 可以使用區域變數
    print(local_message)

show_variables()
print(global_message)  # 可以使用
# print(local_message)  # ❌ 錯誤！區域變數在函數外無法使用
```

### 2.3 同名變數的處理
```python
name = "全域的小明"  # 全域變數

def test_scope():
    name = "區域的小美"  # 區域變數（會覆蓋全域變數）
    print(f"函數內的name：{name}")

def test_global():
    # 使用全域變數
    print(f"函數內使用全域name：{name}")

test_scope()   # 輸出：函數內的name：區域的小美
test_global()  # 輸出：函數內使用全域name：全域的小明
print(f"全域name：{name}")  # 輸出：全域name：全域的小明
```

### 2.4 修改全域變數
```python
counter = 0  # 全域變數

def increment_wrong():
    """❌ 錯誤的方式：嘗試修改全域變數"""
    # counter = counter + 1  # 這會出錯！
    pass

def increment_correct():
    """✅ 正確的方式：使用global關鍵字"""
    global counter
    counter = counter + 1

def increment_better():
    """✅ 更好的方式：回傳新值"""
    return counter + 1

print(f"初始counter：{counter}")  # 0

increment_correct()
print(f"使用global後：{counter}")  # 1

# 更好的做法是避免直接修改全域變數
new_counter = increment_better()
print(f"回傳新值：{new_counter}")  # 2（但counter還是1）
```

### 2.5 實際應用範例
```python
# 設定檔案（全域變數）
APP_NAME = "我的應用程式"
VERSION = "1.0.0"
DEBUG_MODE = True

def get_app_info():
    """獲取應用程式資訊"""
    return f"{APP_NAME} v{VERSION}"

def log_message(message):
    """記錄訊息"""
    if DEBUG_MODE:
        print(f"[DEBUG] {message}")

def calculate_tax(income):
    """計算稅額"""
    # 區域變數
    tax_rate = 0.2
    tax_bracket = 50000
    
    if income <= tax_bracket:
        tax = income * 0.05
    else:
        tax = tax_bracket * 0.05 + (income - tax_bracket) * tax_rate
    
    log_message(f"收入：{income}，稅額：{tax}")
    return tax

# 使用函數
print(get_app_info())
my_tax = calculate_tax(60000)
print(f"我的稅額：{my_tax}")
```

## 3. 可變參數（*args 和 **kwargs）

### 3.1 *args：可變位置參數
```python
def add_numbers(*args):
    """加總任意數量的數字"""
    print(f"接收到的參數：{args}")  # args是一個元組
    total = sum(args)
    return total

# 可以傳入任意數量的參數
print(add_numbers(1, 2, 3))           # 6
print(add_numbers(1, 2, 3, 4, 5))     # 15
print(add_numbers(10, 20))            # 30

def create_message(prefix, *messages):
    """創建訊息，第一個參數是前綴，後面可以有任意數量的訊息"""
    result = prefix + ": "
    for msg in messages:
        result += str(msg) + " "
    return result.strip()

print(create_message("錯誤", "檔案不存在", "請檢查路徑"))
print(create_message("成功", "資料已儲存"))
```

### 3.2 **kwargs：可變關鍵字參數
```python
def create_profile(**kwargs):
    """創建個人檔案"""
    print(f"接收到的關鍵字參數：{kwargs}")  # kwargs是一個字典
    
    profile = "個人檔案：\n"
    for key, value in kwargs.items():
        profile += f"  {key}: {value}\n"
    
    return profile

# 可以傳入任意關鍵字參數
profile = create_profile(
    name="張小明",
    age=25,
    city="台北",
    job="工程師"
)
print(profile)

def configure_app(app_name, version, **settings):
    """配置應用程式"""
    print(f"應用程式：{app_name} v{version}")
    print("設定：")
    for setting, value in settings.items():
        print(f"  {setting} = {value}")

configure_app(
    "MyApp", 
    "2.0",
    debug=True,
    database_url="localhost:5432",
    max_connections=100,
    timeout=30
)
```

### 3.3 混合使用所有參數類型
```python
def advanced_function(required_param, default_param="預設值", *args, **kwargs):
    """示範所有參數類型的使用"""
    print(f"必需參數：{required_param}")
    print(f"預設參數：{default_param}")
    print(f"位置參數：{args}")
    print(f"關鍵字參數：{kwargs}")

# 測試各種組合
advanced_function("必需的")

advanced_function("必需的", "自訂預設")

advanced_function("必需的", "自訂預設", "額外1", "額外2")

advanced_function(
    "必需的", 
    "自訂預設", 
    "額外1", "額外2",
    option1="值1",
    option2="值2"
)
```

## 4. Lambda 函數（匿名函數）

### 4.1 Lambda 基礎
```python
# 一般函數
def square(x):
    return x ** 2

# Lambda 函數（等效）
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25

# 多參數 lambda
add = lambda x, y: x + y
print(add(3, 5))  # 8

# 條件判斷 lambda
is_even = lambda x: x % 2 == 0
print(is_even(4))  # True
print(is_even(5))  # False
```

### 4.2 Lambda 的實際應用
```python
# 與內建函數一起使用
numbers = [1, 2, 3, 4, 5]

# 使用 map
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# 使用 filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# 使用 sorted
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(sorted_by_grade)  # [('Charlie', 78), ('Alice', 85), ('Bob', 90)]
```

## 5. 實作項目：密碼強度檢查器

### 5.1 功能需求
1. 檢查密碼長度
2. 檢查是否包含大小寫字母
3. 檢查是否包含數字
4. 檢查是否包含特殊字符
5. 計算密碼強度分數
6. 提供改善建議
7. 生成安全密碼建議

### 5.2 完整實作
```python
import string
import random
import re

# 全域設定
MIN_LENGTH = 8
RECOMMENDED_LENGTH = 12
SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;':\".,<>?"

def check_password_length(password, min_length=MIN_LENGTH):
    """檢查密碼長度"""
    length = len(password)
    if length >= min_length:
        return True, f"✅ 長度足夠 ({length} 個字符)"
    else:
        return False, f"❌ 長度不足 ({length} 個字符，至少需要 {min_length} 個)"

def check_uppercase(password):
    """檢查是否包含大寫字母"""
    if re.search(r'[A-Z]', password):
        count = len(re.findall(r'[A-Z]', password))
        return True, f"✅ 包含大寫字母 ({count} 個)"
    else:
        return False, "❌ 缺少大寫字母"

def check_lowercase(password):
    """檢查是否包含小寫字母"""
    if re.search(r'[a-z]', password):
        count = len(re.findall(r'[a-z]', password))
        return True, f"✅ 包含小寫字母 ({count} 個)"
    else:
        return False, "❌ 缺少小寫字母"

def check_digits(password):
    """檢查是否包含數字"""
    if re.search(r'\d', password):
        count = len(re.findall(r'\d', password))
        return True, f"✅ 包含數字 ({count} 個)"
    else:
        return False, "❌ 缺少數字"

def check_special_chars(password, special_chars=SPECIAL_CHARS):
    """檢查是否包含特殊字符"""
    special_found = [char for char in password if char in special_chars]
    if special_found:
        return True, f"✅ 包含特殊字符 ({len(special_found)} 個): {''.join(set(special_found))}"
    else:
        return False, f"❌ 缺少特殊字符（建議使用：{special_chars[:10]}...）"

def check_common_patterns(password):
    """檢查常見的不安全模式"""
    issues = []
    
    # 檢查連續字符
    if re.search(r'(.)\1{2,}', password):
        issues.append("包含連續相同字符")
    
    # 檢查鍵盤順序
    keyboard_patterns = ['qwerty', '123456', 'abcdef', 'password']
    for pattern in keyboard_patterns:
        if pattern.lower() in password.lower():
            issues.append(f"包含常見模式：{pattern}")
    
    # 檢查日期模式
    if re.search(r'\d{4}', password):  # 可能是年份
        issues.append("可能包含年份")
    
    if issues:
        return False, "⚠️ 發現不安全模式：" + ", ".join(issues)
    else:
        return True, "✅ 沒有發現常見不安全模式"

def calculate_password_score(password):
    """計算密碼強度分數 (0-100)"""
    score = 0
    
    # 長度分數 (最多40分)
    length = len(password)
    if length >= 12:
        score += 40
    elif length >= 8:
        score += 25
    elif length >= 6:
        score += 10
    
    # 字符多樣性分數 (每種類型15分)
    if re.search(r'[A-Z]', password):
        score += 15
    if re.search(r'[a-z]', password):
        score += 15
    if re.search(r'\d', password):
        score += 15
    if re.search(r'[' + re.escape(SPECIAL_CHARS) + ']', password):
        score += 15
    
    # 複雜性獎勵
    char_types = sum([
        bool(re.search(r'[A-Z]', password)),
        bool(re.search(r'[a-z]', password)),
        bool(re.search(r'\d', password)),
        bool(re.search(r'[' + re.escape(SPECIAL_CHARS) + ']', password))
    ])
    
    if char_types >= 3:
        score += 10
    
    # 長度獎勵
    if length >= 16:
        score += 10
    
    # 扣分項目
    if re.search(r'(.)\1{2,}', password):  # 連續字符
        score -= 10
    
    return min(100, max(0, score))

def get_strength_level(score):
    """根據分數獲取強度等級"""
    if score >= 90:
        return "非常強", "🔒"
    elif score >= 70:
        return "強", "🔐"
    elif score >= 50:
        return "中等", "🔓"
    elif score >= 30:
        return "弱", "⚠️"
    else:
        return "非常弱", "❌"

def generate_improvement_suggestions(password):
    """生成密碼改善建議"""
    suggestions = []
    
    # 檢查各項要求
    length_ok, _ = check_password_length(password)
    if not length_ok:
        suggestions.append(f"增加密碼長度至少 {MIN_LENGTH} 個字符")
    
    upper_ok, _ = check_uppercase(password)
    if not upper_ok:
        suggestions.append("添加大寫字母 (A-Z)")
    
    lower_ok, _ = check_lowercase(password)
    if not lower_ok:
        suggestions.append("添加小寫字母 (a-z)")
    
    digit_ok, _ = check_digits(password)
    if not digit_ok:
        suggestions.append("添加數字 (0-9)")
    
    special_ok, _ = check_special_chars(password)
    if not special_ok:
        suggestions.append("添加特殊字符 (!@#$%^&*等)")
    
    # 額外建議
    if len(password) < RECOMMENDED_LENGTH:
        suggestions.append(f"建議密碼長度至少 {RECOMMENDED_LENGTH} 個字符")
    
    pattern_ok, _ = check_common_patterns(password)
    if not pattern_ok:
        suggestions.append("避免使用常見模式和個人資訊")
    
    return suggestions

def generate_secure_password(length=RECOMMENDED_LENGTH, 
                           include_uppercase=True,
                           include_lowercase=True, 
                           include_digits=True,
                           include_special=True):
    """生成安全密碼"""
    chars = ""
    
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += SPECIAL_CHARS
    
    if not chars:
        return "錯誤：至少要選擇一種字符類型"
    
    # 確保每種類型都至少有一個
    password = []
    
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice(SPECIAL_CHARS))
    
    # 填充剩餘長度
    for _ in range(length - len(password)):
        password.append(random.choice(chars))
    
    # 打亂順序
    random.shuffle(password)
    
    return ''.join(password)

def analyze_password(password):
    """完整分析密碼"""
    print(f"\n🔍 分析密碼：{'*' * len(password)} ({len(password)} 個字符)")
    print("=" * 50)
    
    # 各項檢查
    checks = [
        check_password_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_digits(password),
        check_special_chars(password),
        check_common_patterns(password)
    ]
    
    print("📋 檢查結果：")
    for passed, message in checks:
        print(f"   {message}")
    
    # 計算分數
    score = calculate_password_score(password)
    strength, emoji = get_strength_level(score)
    
    print(f"\n📊 密碼強度：{score}/100 分 - {strength} {emoji}")
    
    # 改善建議
    suggestions = generate_improvement_suggestions(password)
    if suggestions:
        print("\n💡 改善建議：")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"   {i}. {suggestion}")
    else:
        print("\n🎉 恭喜！您的密碼已經很安全了！")
    
    return score

def password_strength_checker():
    """密碼強度檢查器主程式"""
    print("🔐 歡迎使用密碼強度檢查器！")
    print("這個工具可以幫助您評估和改善密碼安全性")
    
    while True:
        print("\n" + "=" * 60)
        print("請選擇功能：")
        print("1. 🔍 檢查密碼強度")
        print("2. 🎲 生成安全密碼")
        print("3. 📚 密碼安全知識")
        print("4. 🧪 密碼安全測試")
        print("0. 🚪 退出程式")
        print("=" * 60)
        
        choice = input("請選擇 (0-4): ").strip()
        
        if choice == "1":
            check_password_interface()
        elif choice == "2":
            generate_password_interface()
        elif choice == "3":
            show_security_tips()
        elif choice == "4":
            password_security_test()
        elif choice == "0":
            print("\n👋 感謝使用密碼強度檢查器！")
            print("🔐 記住：好的密碼是網路安全的第一道防線！")
            break
        else:
            print("❌ 無效選擇！")

def check_password_interface():
    """檢查密碼介面"""
    while True:
        print("\n🔍 密碼強度檢查")
        print("-" * 30)
        
        password = input("請輸入要檢查的密碼（或輸入 'back' 返回）: ")
        
        if password.lower() == 'back':
            break
        
        if not password.strip():
            print("❌ 密碼不能為空！")
            continue
        
        analyze_password(password)
        
        again = input("\n是否要檢查其他密碼？(y/N): ").strip().lower()
        if again != 'y':
            break

def generate_password_interface():
    """生成密碼介面"""
    print("\n🎲 生成安全密碼")
    print("-" * 25)
    
    try:
        # 獲取參數
        length = int(input(f"密碼長度 (預設 {RECOMMENDED_LENGTH}): ") or RECOMMENDED_LENGTH)
        if length < 4:
            print("密碼長度至少要4個字符，設定為4")
            length = 4
        
        print("\n字符類型選擇 (直接按 Enter 表示是):")
        include_upper = input("包含大寫字母？(Y/n): ").strip().lower() != 'n'
        include_lower = input("包含小寫字母？(Y/n): ").strip().lower() != 'n'
        include_digits = input("包含數字？(Y/n): ").strip().lower() != 'n'
        include_special = input("包含特殊字符？(Y/n): ").strip().lower() != 'n'
        
        # 生成多個密碼選項
        print(f"\n🎯 為您生成 {length} 個字符的安全密碼：")
        print("-" * 40)
        
        for i in range(3):
            password = generate_secure_password(
                length, include_upper, include_lower, 
                include_digits, include_special
            )
            score = calculate_password_score(password)
            strength, emoji = get_strength_level(score)
            print(f"{i+1}. {password} (強度: {score}/100 {emoji})")
        
        # 讓使用者選擇分析其中一個
        choice = input("\n要詳細分析哪個密碼？(1-3，或按 Enter 跳過): ").strip()
        if choice in ['1', '2', '3']:
            password = generate_secure_password(
                length, include_upper, include_lower, 
                include_digits, include_special
            )
            analyze_password(password)
            
    except ValueError:
        print("❌ 請輸入有效的數字！")

def show_security_tips():
    """顯示密碼安全知識"""
    print("\n📚 密碼安全知識")
    print("=" * 40)
    
    tips = [
        "🔐 使用至少 12 個字符的密碼",
        "🔤 混合使用大小寫字母、數字和特殊字符",
        "🚫 避免使用個人資訊（生日、姓名、電話等）",
        "🎲 每個帳戶使用不同的密碼",
        "🔄 定期更換重要帳戶的密碼",
        "💾 使用密碼管理器儲存密碼",
        "🔐 啟用雙因素驗證 (2FA)",
        "⚠️ 不要在公共場所輸入密碼",
        "📱 注意網路釣魚攻擊",
        "🔒 使用 HTTPS 網站進行敏感操作"
    ]
    
    for tip in tips:
        print(f"   {tip}")
    
    print("\n💡 記住：密碼是您數位身份的第一道防線！")

def password_security_test():
    """密碼安全測試"""
    print("\n🧪 密碼安全知識小測驗")
    print("-" * 35)
    
    questions = [
        {
            "question": "理想的密碼長度至少應該是幾個字符？",
            "options": ["A) 6個", "B) 8個", "C) 12個", "D) 16個"],
            "answer": "C",
            "explanation": "建議至少12個字符，更長更安全"
        },
        {
            "question": "以下哪種密碼最安全？",
            "options": ["A) password123", "B) Password123", "C) P@ssw0rd123", "D) MyD0g&Cat#2023"],
            "answer": "D",
            "explanation": "長度足夠，包含多種字符類型，避免常見詞彙"
        },
        {
            "question": "應該多久更換一次重要密碼？",
            "options": ["A) 每個月", "B) 每3-6個月", "C) 每年", "D) 從不更換"],
            "answer": "B",
            "explanation": "定期更換可以降低被破解的風險"
        }
    ]
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n問題 {i}: {q['question']}")
        for option in q['options']:
            print(f"   {option}")
        
        answer = input("請選擇 (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("✅ 正確！")
            score += 1
        else:
            print(f"❌ 錯誤！正確答案是 {q['answer']}")
        
        print(f"💡 解釋：{q['explanation']}")
    
    print(f"\n📊 測驗結果：{score}/{len(questions)} 分")
    
    if score == len(questions):
        print("🏆 優秀！您對密碼安全很了解！")
    elif score >= len(questions) * 0.7:
        print("👍 不錯！繼續保持安全意識！")
    else:
        print("📖 建議多學習密碼安全知識！")

if __name__ == "__main__":
    password_strength_checker()
```

## 6. 程式設計最佳實踐進階

### 6.1 函數設計原則
```python
# ✅ 好的函數設計
def calculate_total_price(base_price, tax_rate=0.05, discount=0):
    """
    計算總價格
    
    參數:
        base_price (float): 基本價格
        tax_rate (float): 稅率，預設 5%
        discount (float): 折扣金額，預設 0
    
    回傳:
        float: 總價格
    """
    if base_price < 0:
        raise ValueError("基本價格不能為負數")
    
    discounted_price = base_price - discount
    tax_amount = discounted_price * tax_rate
    total = discounted_price + tax_amount
    
    return round(total, 2)

# ❌ 不好的函數設計
def calc(p, t=0.05, d=0):  # 名稱不清楚
    return p - d + (p - d) * t  # 沒有錯誤處理，邏輯不清楚
```

### 6.2 錯誤處理
```python
def safe_divide(a, b, default=None):
    """安全的除法運算"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        if default is not None:
            return default
        else:
            print("錯誤：不能除以零")
            return None
    except TypeError:
        print("錯誤：參數必須是數字")
        return None

# 使用範例
print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # 錯誤訊息，回傳None
print(safe_divide(10, 0, 0))   # 0 (使用預設值)
```

## 7. 今日總結

今天你學會了：
- ✅ 預設參數讓函數更靈活好用
- ✅ 區域變數和全域變數的區別和使用
- ✅ *args和**kwargs處理可變參數
- ✅ Lambda函數的基本使用
- ✅ 實作完整的密碼強度檢查器

**關鍵概念回顧：**
- 預設參數提供便利性和彈性
- 變數作用域影響變數的可見性和生命週期
- 可變參數讓函數能處理不確定數量的輸入
- Lambda適合簡短的匿名函數

**明天預告：**
我們將學習Python的內建函數，包括len()、max()、min()、sum()等，並實作統計分析工具！

記住：**掌握進階函數概念，讓你的程式更加靈活和強大！**