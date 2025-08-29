"""
Day 15: 溫度轉換器
實作重點：函數的定義、呼叫、參數傳遞和回傳值
"""

import os
import sys

# 基本溫度轉換函數
def celsius_to_fahrenheit(celsius):
    """
    攝氏轉華氏
    公式：F = C × 9/5 + 32
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    華氏轉攝氏  
    公式：C = (F - 32) × 5/9
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    """
    攝氏轉克氏
    公式：K = C + 273.15
    """
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    """
    克氏轉攝氏
    公式：C = K - 273.15
    """
    celsius = kelvin - 273.15
    return celsius

# 輔助函數
def validate_temperature(temp, scale):
    """
    驗證溫度是否在合理範圍內
    
    參數:
        temp (float): 溫度值
        scale (str): 溫度單位 ('C', 'F', 'K')
    
    回傳:
        bool: 溫度是否有效
    """
    if scale.upper() == 'C':
        # 攝氏：絕對零度 -273.15°C 到合理上限 10000°C
        return -273.15 <= temp <= 10000
    elif scale.upper() == 'F':
        # 華氏：絕對零度 -459.67°F 到合理上限
        return -459.67 <= temp <= 18000
    elif scale.upper() == 'K':
        # 克氏：絕對零度 0K 到合理上限
        return 0 <= temp <= 10273.15
    return False

def format_temperature(temp, scale):
    """
    格式化溫度顯示
    
    參數:
        temp (float): 溫度值
        scale (str): 溫度單位
    
    回傳:
        str: 格式化的溫度字串
    """
    scale_symbols = {'C': '°C', 'F': '°F', 'K': 'K'}
    symbol = scale_symbols.get(scale.upper(), '°')
    return f"{temp:.2f}{symbol}"

def display_conversion_result(original_temp, original_scale, converted_temp, converted_scale):
    """
    顯示轉換結果
    
    參數:
        original_temp (float): 原始溫度
        original_scale (str): 原始單位
        converted_temp (float): 轉換後溫度
        converted_scale (str): 轉換後單位
    """
    original_formatted = format_temperature(original_temp, original_scale)
    converted_formatted = format_temperature(converted_temp, converted_scale)
    print(f"\n🌡️  轉換結果：{original_formatted} = {converted_formatted}")
    
    # 顯示轉換說明
    conversion_type = f"{original_scale.upper()}→{converted_scale.upper()}"
    explanations = {
        "C→F": "攝氏轉華氏：將攝氏溫度乘以9/5再加32",
        "F→C": "華氏轉攝氏：將華氏溫度減32後乘以5/9", 
        "C→K": "攝氏轉克氏：將攝氏溫度加273.15",
        "K→C": "克氏轉攝氏：將克氏溫度減273.15"
    }
    explanation = explanations.get(conversion_type, "")
    if explanation:
        print(f"💡 {explanation}")

# 輸入處理函數
def get_temperature_input():
    """
    獲取溫度輸入
    
    回傳:
        float: 有效的溫度值
    """
    while True:
        try:
            temp_str = input("\n請輸入溫度數值: ").strip()
            temp = float(temp_str)
            return temp
        except ValueError:
            print("❌ 請輸入有效的數字！")
        except KeyboardInterrupt:
            print("\n程式已中斷")
            sys.exit()

def get_scale_input(prompt):
    """
    獲取溫度單位輸入
    
    參數:
        prompt (str): 提示訊息
    
    回傳:
        str: 有效的溫度單位
    """
    while True:
        try:
            scale = input(prompt).strip().upper()
            if scale in ['C', 'F', 'K']:
                return scale
            print("❌ 請輸入 C（攝氏）、F（華氏）或 K（克氏）！")
        except KeyboardInterrupt:
            print("\n程式已中斷")
            sys.exit()

# 選單和顯示函數
def clear_screen():
    """清空螢幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """顯示程式標題"""
    print("\n" + "="*55)
    print("🌡️            溫度轉換器 v1.0            🌡️")
    print("="*55)
    print("✨ 支援攝氏、華氏、克氏之間的相互轉換")

def display_menu():
    """顯示主選單"""
    print("\n" + "-"*40)
    print("📋 請選擇轉換類型：")
    print("-"*40)
    print("1. 🌡️  攝氏 → 華氏 (C → F)")
    print("2. 🌡️  華氏 → 攝氏 (F → C)")
    print("3. 🌡️  攝氏 → 克氏 (C → K)")
    print("4. 🌡️  克氏 → 攝氏 (K → C)")
    print("5. 🔄 自訂轉換")
    print("6. 📊 溫度對照表")
    print("7. 🧮 批次轉換")
    print("8. 📖 使用說明")
    print("0. 🚪 離開程式")
    print("-"*40)

def show_temperature_reference():
    """顯示溫度對照表"""
    print("\n🌡️ 常見溫度對照表")
    print("="*65)
    
    # 常見溫度點
    reference_points = [
        ("絕對零度", -273.15, "極低溫的物理極限"),
        ("液氮沸點", -196, "液態氮氣的沸點"),
        ("乾冰昇華點", -78.5, "乾冰直接變成氣體的溫度"),
        ("水結冰點", 0, "水變成冰的溫度"),
        ("室溫", 25, "舒適的室內溫度"),
        ("人體體溫", 37, "正常人體溫度"),
        ("水沸點", 100, "水變成水蒸氣的溫度"),
        ("烤箱溫度", 200, "烘焙常用溫度"),
        ("鐵熔點", 1538, "鐵開始熔化的溫度"),
        ("太陽表面", 5500, "太陽表面的溫度")
    ]
    
    print(f"{'項目':<12} {'攝氏(°C)':<10} {'華氏(°F)':<10} {'克氏(K)':<10} {'說明'}")
    print("-"*65)
    
    for name, temp_c, description in reference_points:
        temp_f = celsius_to_fahrenheit(temp_c)
        temp_k = celsius_to_kelvin(temp_c)
        print(f"{name:<12} {temp_c:<10.1f} {temp_f:<10.1f} {temp_k:<10.1f} {description}")

def show_instructions():
    """顯示使用說明"""
    print("\n📖 溫度轉換器使用說明")
    print("="*50)
    print("""
🌡️ 支援的溫度單位：
   • C: 攝氏度 (Celsius)
   • F: 華氏度 (Fahrenheit)  
   • K: 克氏度 (Kelvin)

🔄 轉換公式：
   • 攝氏 → 華氏: F = C × 9/5 + 32
   • 華氏 → 攝氏: C = (F - 32) × 5/9
   • 攝氏 → 克氏: K = C + 273.15
   • 克氏 → 攝氏: C = K - 273.15

⚠️ 溫度範圍限制：
   • 攝氏: -273.15°C ~ 10000°C
   • 華氏: -459.67°F ~ 18000°F
   • 克氏: 0K ~ 10273.15K

💡 使用技巧：
   • 支援小數點輸入
   • 可使用負數
   • 按 Ctrl+C 隨時退出
    """)

# 核心轉換功能
def convert_temperature(temp, from_scale, to_scale):
    """
    通用溫度轉換函數
    
    參數:
        temp (float): 原始溫度
        from_scale (str): 來源溫度單位
        to_scale (str): 目標溫度單位
    
    回傳:
        float: 轉換後的溫度，若轉換失敗則回傳None
    """
    # 先轉換為攝氏度作為中間值
    if from_scale == 'C':
        celsius = temp
    elif from_scale == 'F':
        celsius = fahrenheit_to_celsius(temp)
    elif from_scale == 'K':
        celsius = kelvin_to_celsius(temp)
    else:
        return None
    
    # 從攝氏度轉換為目標單位
    if to_scale == 'C':
        return celsius
    elif to_scale == 'F':
        return celsius_to_fahrenheit(celsius)
    elif to_scale == 'K':
        return celsius_to_kelvin(celsius)
    else:
        return None

def custom_conversion():
    """自訂轉換功能"""
    print("\n🔄 自訂溫度轉換")
    print("="*30)
    
    # 獲取原始溫度和單位
    temp = get_temperature_input()
    from_scale = get_scale_input("請輸入原始溫度單位 (C/F/K): ")
    
    # 驗證溫度
    if not validate_temperature(temp, from_scale):
        print(f"❌ 溫度 {temp}°{from_scale} 超出合理範圍！")
        return
    
    # 獲取目標單位
    to_scale = get_scale_input("請輸入目標溫度單位 (C/F/K): ")
    
    if from_scale == to_scale:
        print("⚠️  相同的溫度單位不需要轉換！")
        return
    
    # 執行轉換
    converted_temp = convert_temperature(temp, from_scale, to_scale)
    if converted_temp is not None:
        display_conversion_result(temp, from_scale, converted_temp, to_scale)
    else:
        print("❌ 轉換失敗！")

def batch_conversion():
    """批次轉換功能"""
    print("\n🧮 批次溫度轉換")
    print("="*30)
    
    # 獲取轉換設定
    from_scale = get_scale_input("請輸入原始溫度單位 (C/F/K): ")
    to_scale = get_scale_input("請輸入目標溫度單位 (C/F/K): ")
    
    if from_scale == to_scale:
        print("⚠️  相同的溫度單位不需要轉換！")
        return
    
    print(f"\n將進行 {from_scale} → {to_scale} 批次轉換")
    print("輸入溫度值（每行一個），輸入 'done' 結束：")
    
    temperatures = []
    while True:
        try:
            temp_input = input(f"溫度 #{len(temperatures) + 1}: ").strip()
            if temp_input.lower() == 'done':
                break
            
            temp = float(temp_input)
            if validate_temperature(temp, from_scale):
                temperatures.append(temp)
                print(f"✅ 已添加: {format_temperature(temp, from_scale)}")
            else:
                print(f"❌ 溫度 {temp}°{from_scale} 超出合理範圍，跳過")
                
        except ValueError:
            print("❌ 請輸入有效的數字！")
        except KeyboardInterrupt:
            print("\n批次轉換已中斷")
            return
    
    if not temperatures:
        print("沒有有效的溫度值！")
        return
    
    # 執行批次轉換
    print(f"\n📊 批次轉換結果 ({from_scale} → {to_scale})：")
    print("="*50)
    
    for i, temp in enumerate(temperatures, 1):
        converted = convert_temperature(temp, from_scale, to_scale)
        original_formatted = format_temperature(temp, from_scale)
        converted_formatted = format_temperature(converted, to_scale)
        print(f"{i:2d}. {original_formatted} = {converted_formatted}")

# 單一轉換處理函數
def handle_single_conversion(from_scale, to_scale, conversion_name):
    """
    處理單一類型的溫度轉換
    
    參數:
        from_scale (str): 來源溫度單位
        to_scale (str): 目標溫度單位
        conversion_name (str): 轉換名稱（用於顯示）
    """
    print(f"\n🌡️ {conversion_name}")
    print("="*25)
    
    temp = get_temperature_input()
    
    if not validate_temperature(temp, from_scale):
        print(f"❌ {from_scale}溫度超出合理範圍！")
        return
    
    converted_temp = convert_temperature(temp, from_scale, to_scale)
    if converted_temp is not None:
        display_conversion_result(temp, from_scale, converted_temp, to_scale)
        
        # 顯示生活化的溫度比較
        show_temperature_context(converted_temp, to_scale)

def show_temperature_context(temp, scale):
    """
    顯示溫度的生活化背景說明
    
    參數:
        temp (float): 溫度值
        scale (str): 溫度單位
    """
    # 統一轉換為攝氏度進行比較
    if scale == 'C':
        celsius = temp
    elif scale == 'F':
        celsius = fahrenheit_to_celsius(temp)
    elif scale == 'K':
        celsius = kelvin_to_celsius(temp)
    else:
        return
    
    print("\n💡 溫度背景說明：")
    
    if celsius < -200:
        print("   這是極低溫，接近絕對零度，在自然界中很少見")
    elif celsius < 0:
        print("   這是冰點以下的溫度，水會結冰")
    elif celsius < 10:
        print("   這是寒冷的溫度，需要穿厚外套")
    elif celsius < 20:
        print("   這是涼爽的溫度，適合戶外活動")
    elif celsius < 30:
        print("   這是舒適的溫度，很適合日常生活")
    elif celsius < 40:
        print("   這是炎熱的溫度，需要注意防曬和補水")
    elif celsius < 100:
        print("   這是非常高的溫度，人體無法承受")
    elif celsius == 100:
        print("   這是水的沸點，水會變成水蒸氣")
    else:
        print("   這是極高溫，可能會造成燙傷或其他危險")

# 主程式
def main():
    """溫度轉換器主程式"""
    try:
        # 顯示歡迎畫面
        clear_screen()
        display_header()
        print("🎉 歡迎使用溫度轉換器！")
        print("💡 提示：隨時按 Ctrl+C 可以退出程式")
        
        while True:
            display_menu()
            
            try:
                choice = input("\n請選擇功能 (0-8): ").strip()
            except KeyboardInterrupt:
                print("\n\n👋 感謝使用溫度轉換器！")
                break
            
            if choice == "1":
                handle_single_conversion('C', 'F', "攝氏轉華氏")
                
            elif choice == "2":
                handle_single_conversion('F', 'C', "華氏轉攝氏")
                
            elif choice == "3":
                handle_single_conversion('C', 'K', "攝氏轉克氏")
                
            elif choice == "4":
                handle_single_conversion('K', 'C', "克氏轉攝氏")
                
            elif choice == "5":
                custom_conversion()
                
            elif choice == "6":
                show_temperature_reference()
                
            elif choice == "7":
                batch_conversion()
                
            elif choice == "8":
                show_instructions()
                
            elif choice == "0":
                print("\n👋 感謝使用溫度轉換器！")
                print("🌟 希望這個小工具對你有幫助～")
                break
                
            else:
                print("❌ 無效選擇！請輸入 0-8 之間的數字。")
            
            # 暫停讓使用者查看結果
            if choice != "0":
                try:
                    input("\n按 Enter 鍵繼續...")
                except KeyboardInterrupt:
                    print("\n\n👋 感謝使用溫度轉換器！")
                    break
                    
    except Exception as e:
        print(f"\n❌ 程式發生錯誤：{e}")
        print("請重新啟動程式")

# 程式入口點
if __name__ == "__main__":
    main()