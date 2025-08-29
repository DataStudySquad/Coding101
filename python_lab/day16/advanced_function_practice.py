"""
Day 16: 函數進階概念練習
練習預設參數、變數作用域、*args、**kwargs
"""

# =============== 全域變數示範 ===============
APP_VERSION = "1.0.0"
DEBUG_MODE = True
DEFAULT_LANGUAGE = "中文"

# =============== 預設參數練習 ===============

def greet_user(name, greeting="你好", punctuation="！"):
    """
    打招呼函數 - 預設參數練習
    """
    return f"{greeting}，{name}{punctuation}"

def calculate_discount(price, discount_rate=0.1, tax_rate=0.05):
    """
    計算折扣後價格 - 多個預設參數
    """
    discounted_price = price * (1 - discount_rate)
    final_price = discounted_price * (1 + tax_rate)
    return round(final_price, 2)

def create_user_profile(username, email, age=18, country="台灣", interests=None):
    """
    創建使用者檔案 - 避免可變預設參數的陷阱
    """
    if interests is None:
        interests = ["閱讀"]  # 每次都創建新的清單
    
    profile = {
        "username": username,
        "email": email,
        "age": age,
        "country": country,
        "interests": interests
    }
    return profile

# =============== 變數作用域練習 ===============

counter = 0  # 全域變數

def increment_counter():
    """修改全域變數 - 使用 global 關鍵字"""
    global counter
    counter += 1
    return counter

def create_counter():
    """區域變數示範"""
    local_counter = 0
    
    def inner_increment():
        nonlocal local_counter  # 修改外層函數的區域變數
        local_counter += 1
        return local_counter
    
    return inner_increment

def scope_demo():
    """作用域示範函數"""
    local_var = "我是區域變數"
    print(f"函數內部 - 全域變數 APP_VERSION: {APP_VERSION}")
    print(f"函數內部 - 區域變數 local_var: {local_var}")
    
    # 可以使用全域變數
    if DEBUG_MODE:
        print("除錯模式已開啟")

# =============== *args 練習 ===============

def sum_all(*numbers):
    """
    計算任意數量數字的總和
    *args 基本用法
    """
    print(f"接收到的參數: {numbers}")
    return sum(numbers)

def find_max(*values):
    """
    找出最大值 - *args 進階用法
    """
    if not values:
        return None
    return max(values)

def create_shopping_list(store_name, *items):
    """
    創建購物清單 - 結合固定參數和 *args
    """
    print(f"\n📝 {store_name} 購物清單:")
    for i, item in enumerate(items, 1):
        print(f"   {i}. {item}")
    return list(items)

def log_message(level, *messages):
    """
    記錄多條訊息 - 實用的 *args 範例
    """
    timestamp = "2024-01-15 10:30:00"  # 簡化時間戳
    combined_message = " ".join(str(msg) for msg in messages)
    print(f"[{timestamp}] {level}: {combined_message}")

# =============== **kwargs 練習 ===============

def create_database_connection(**config):
    """
    創建資料庫連接 - **kwargs 基本用法
    """
    print("資料庫連接設定:")
    for key, value in config.items():
        print(f"   {key}: {value}")
    
    # 設定預設值
    host = config.get('host', 'localhost')
    port = config.get('port', 5432)
    
    return f"連接到 {host}:{port}"

def send_notification(recipient, message, **options):
    """
    發送通知 - 結合固定參數和 **kwargs
    """
    print(f"發送通知給: {recipient}")
    print(f"訊息內容: {message}")
    
    # 處理選項
    priority = options.get('priority', 'normal')
    email = options.get('email', False)
    sms = options.get('sms', False)
    
    print(f"優先度: {priority}")
    if email:
        print("✅ 透過電子郵件發送")
    if sms:
        print("✅ 透過簡訊發送")

def build_query(table, **conditions):
    """
    建立查詢語句 - **kwargs 實用範例
    """
    base_query = f"SELECT * FROM {table}"
    
    if conditions:
        where_clauses = []
        for field, value in conditions.items():
            where_clauses.append(f"{field} = '{value}'")
        
        base_query += " WHERE " + " AND ".join(where_clauses)
    
    return base_query

# =============== 混合參數練習 ===============

def advanced_calculator(operation, *numbers, precision=2, show_steps=False, **options):
    """
    進階計算器 - 展示所有參數類型的組合使用
    """
    if show_steps:
        print(f"🔢 執行 {operation} 運算")
        print(f"數字: {numbers}")
        print(f"精度: {precision}")
        print(f"選項: {options}")
    
    result = None
    
    if operation == "add":
        result = sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "average":
        result = sum(numbers) / len(numbers) if numbers else 0
    
    if result is not None:
        return round(result, precision)
    else:
        return "不支援的運算"

def format_report(title, *data_points, format_type="table", show_header=True, **styling):
    """
    格式化報告 - 複雜參數組合範例
    """
    print(f"\n📊 {title}")
    
    if format_type == "table":
        if show_header:
            print("=" * 40)
        
        for i, point in enumerate(data_points, 1):
            print(f"{i:2d}. {point}")
        
        if show_header:
            print("=" * 40)
    
    # 處理樣式選項
    if styling.get('color'):
        print(f"🎨 顏色: {styling['color']}")
    if styling.get('bold'):
        print("**粗體顯示**")

# =============== Lambda 函數練習 ===============

def lambda_examples():
    """Lambda 函數範例"""
    print("\n🔧 Lambda 函數示範:")
    
    # 基本 lambda
    square = lambda x: x ** 2
    print(f"5的平方: {square(5)}")
    
    # 多參數 lambda
    add = lambda x, y: x + y
    print(f"3 + 7 = {add(3, 7)}")
    
    # 條件 lambda
    is_adult = lambda age: "成年" if age >= 18 else "未成年"
    print(f"20歲: {is_adult(20)}")
    print(f"16歲: {is_adult(16)}")
    
    # 與內建函數結合
    numbers = [1, 2, 3, 4, 5]
    
    squares = list(map(lambda x: x**2, numbers))
    print(f"平方: {squares}")
    
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"偶數: {evens}")
    
    # 排序應用
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    sorted_students = sorted(students, key=lambda student: student[1])
    print(f"按成績排序: {sorted_students}")

# =============== 實際應用範例 ===============

def create_web_server(host="localhost", port=8000, **settings):
    """
    模擬網路伺服器設定 - 實際應用範例
    """
    print(f"🌐 啟動網路伺服器")
    print(f"   地址: {host}:{port}")
    
    # 處理各種設定
    debug = settings.get('debug', False)
    max_connections = settings.get('max_connections', 100)
    timeout = settings.get('timeout', 30)
    
    print(f"   除錯模式: {'開啟' if debug else '關閉'}")
    print(f"   最大連接數: {max_connections}")
    print(f"   逾時時間: {timeout}秒")

def data_processor(*datasets, operation="merge", **options):
    """
    數據處理器 - 展示複雜參數處理
    """
    print(f"📊 處理 {len(datasets)} 個資料集")
    print(f"操作類型: {operation}")
    
    if operation == "merge":
        merged = []
        for dataset in datasets:
            merged.extend(dataset)
        
        if options.get('remove_duplicates', False):
            merged = list(set(merged))
        
        if options.get('sort', False):
            merged.sort()
        
        return merged
    
    return []

# =============== 測試與示範函數 ===============

def test_default_parameters():
    """測試預設參數"""
    print("\n🧪 測試預設參數:")
    
    # 基本使用
    print(greet_user("小明"))
    print(greet_user("小美", "早安"))
    print(greet_user("老師", "午安", "。"))
    
    # 計算折扣
    print(f"原價1000，預設折扣: {calculate_discount(1000)}")
    print(f"原價1000，20%折扣: {calculate_discount(1000, 0.2)}")
    
    # 使用者檔案
    profile1 = create_user_profile("user1", "user1@email.com")
    profile2 = create_user_profile("user2", "user2@email.com", interests=["音樂", "電影"])
    print(f"檔案1: {profile1}")
    print(f"檔案2: {profile2}")

def test_variable_scope():
    """測試變數作用域"""
    print("\n🏠 測試變數作用域:")
    
    print(f"初始 counter: {counter}")
    
    # 修改全域變數
    new_value = increment_counter()
    print(f"遞增後 counter: {new_value}")
    
    # 區域計數器
    local_counter = create_counter()
    print(f"區域計數器1: {local_counter()}")
    print(f"區域計數器2: {local_counter()}")
    
    # 作用域示範
    scope_demo()

def test_args():
    """測試 *args"""
    print("\n🎯 測試 *args:")
    
    # 數字總和
    print(f"總和 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
    print(f"總和 10,20: {sum_all(10, 20)}")
    
    # 最大值
    print(f"最大值 5,2,8,1: {find_max(5, 2, 8, 1)}")
    
    # 購物清單
    create_shopping_list("全聯", "蘋果", "香蕉", "牛奶", "麵包")
    
    # 記錄訊息
    log_message("INFO", "系統", "啟動", "成功")
    log_message("ERROR", "連接失敗")

def test_kwargs():
    """測試 **kwargs"""
    print("\n⚙️ 測試 **kwargs:")
    
    # 資料庫連接
    connection = create_database_connection(
        host="localhost",
        port=5432,
        database="myapp",
        username="admin"
    )
    print(f"連接結果: {connection}")
    
    # 發送通知
    send_notification(
        "user@example.com",
        "系統維護通知",
        priority="high",
        email=True,
        sms=True
    )
    
    # 建立查詢
    query1 = build_query("users")
    query2 = build_query("products", category="electronics", price=1000)
    print(f"查詢1: {query1}")
    print(f"查詢2: {query2}")

def test_mixed_parameters():
    """測試混合參數"""
    print("\n🔄 測試混合參數:")
    
    # 進階計算器
    result1 = advanced_calculator("add", 1, 2, 3, 4, 5)
    print(f"加法結果: {result1}")
    
    result2 = advanced_calculator("multiply", 2, 3, 4, precision=3, show_steps=True)
    print(f"乘法結果: {result2}")
    
    # 格式化報告
    format_report(
        "月度銷售報告",
        "產品A: 100件",
        "產品B: 85件", 
        "產品C: 120件",
        format_type="table",
        show_header=True,
        color="藍色",
        bold=True
    )

def test_practical_examples():
    """測試實際應用範例"""
    print("\n💼 測試實際應用:")
    
    # 網路伺服器
    create_web_server(
        port=3000,
        debug=True,
        max_connections=200,
        timeout=60
    )
    
    # 數據處理
    data1 = [1, 2, 3, 4]
    data2 = [3, 4, 5, 6]
    data3 = [5, 6, 7, 8]
    
    merged_data = data_processor(
        data1, data2, data3,
        operation="merge",
        remove_duplicates=True,
        sort=True
    )
    print(f"合併後數據: {merged_data}")

def main():
    """主程式 - 展示所有函數進階概念"""
    print("🎉 歡迎來到函數進階概念練習！")
    print("這個程式展示了 Day 16 的所有重要概念")
    
    while True:
        print("\n" + "=" * 50)
        print("請選擇要測試的概念：")
        print("1. 📝 預設參數")
        print("2. 🏠 變數作用域")
        print("3. 🎯 *args 可變位置參數")
        print("4. ⚙️ **kwargs 可變關鍵字參數")
        print("5. 🔄 混合參數使用")
        print("6. 🔧 Lambda 函數")
        print("7. 💼 實際應用範例")
        print("8. 🧪 執行所有測試")
        print("0. 🚪 退出")
        print("=" * 50)
        
        choice = input("請選擇 (0-8): ").strip()
        
        if choice == "0":
            print("感謝使用函數進階概念練習！")
            break
        elif choice == "1":
            test_default_parameters()
        elif choice == "2":
            test_variable_scope()
        elif choice == "3":
            test_args()
        elif choice == "4":
            test_kwargs()
        elif choice == "5":
            test_mixed_parameters()
        elif choice == "6":
            lambda_examples()
        elif choice == "7":
            test_practical_examples()
        elif choice == "8":
            print("🧪 執行所有測試...")
            test_default_parameters()
            test_variable_scope()
            test_args()
            test_kwargs()
            test_mixed_parameters()
            lambda_examples()
            test_practical_examples()
            print("✅ 所有測試完成！")
        else:
            print("❌ 無效選擇！")
        
        if choice != "0":
            input("\n按 Enter 繼續...")

if __name__ == "__main__":
    main()