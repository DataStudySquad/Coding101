"""
Day 17: 統計分析工具
實作重點：內建函數的使用 - len(), max(), min(), sum(), map(), filter(), sorted() 等
"""

import math
import random
from collections import Counter

class StatisticalAnalyzer:
    """統計分析工具類別 - 展示內建函數的強大應用"""
    
    def __init__(self, data=None):
        """初始化分析器"""
        self.original_data = data if data else []
        self.numeric_data = []
        self.prepare_data()
    
    def prepare_data(self):
        """準備數值資料 - 使用 filter() 過濾有效數據"""
        if not self.original_data:
            self.numeric_data = []
            return
        
        # 使用 filter 和 lambda 過濾數值資料
        def is_numeric(value):
            try:
                float(value)
                return True
            except (ValueError, TypeError):
                return False
        
        # 過濾出數值資料並轉換為 float
        valid_data = filter(is_numeric, self.original_data)
        self.numeric_data = list(map(float, valid_data))
    
    def add_data(self, *values):
        """添加資料 - 使用 *args"""
        self.original_data.extend(values)
        self.prepare_data()
    
    def basic_stats(self):
        """基本統計 - 展示基本內建函數的使用"""
        if not self.numeric_data:
            return None
        
        data = self.numeric_data
        n = len(data)  # len() 函數
        
        return {
            "資料數量": n,
            "總和": sum(data),           # sum() 函數
            "平均值": sum(data) / n,
            "最大值": max(data),         # max() 函數
            "最小值": min(data),         # min() 函數
            "範圍": max(data) - min(data),
            "中位數": self.calculate_median(),
            "眾數": self.calculate_mode()
        }
    
    def calculate_median(self):
        """計算中位數 - 使用 sorted() 函數"""
        if not self.numeric_data:
            return None
        
        sorted_data = sorted(self.numeric_data)  # sorted() 函數
        n = len(sorted_data)
        
        if n % 2 == 0:
            # 偶數個數據：中間兩數的平均
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            # 奇數個數據：中間的數
            return sorted_data[n//2]
    
    def calculate_mode(self):
        """計算眾數 - 使用 Counter 和 max()"""
        if not self.numeric_data:
            return None
        
        # 使用 Counter 計算頻率
        counter = Counter(self.numeric_data)
        
        if not counter:
            return None
        
        # 找出最高頻率
        max_count = max(counter.values())  # max() 應用於字典的值
        
        # 找出所有具有最高頻率的值
        modes = [value for value, count in counter.items() if count == max_count]
        
        return modes[0] if len(modes) == 1 else modes
    
    def quartiles_analysis(self):
        """四分位數分析 - 進階排序應用"""
        if len(self.numeric_data) < 4:
            return None
        
        sorted_data = sorted(self.numeric_data)
        n = len(sorted_data)
        
        def get_percentile(data, p):
            """計算百分位數"""
            index = p * (len(data) - 1)
            if index.is_integer():
                return data[int(index)]
            else:
                lower_idx = int(index)
                upper_idx = lower_idx + 1
                weight = index - lower_idx
                return data[lower_idx] * (1 - weight) + data[upper_idx] * weight
        
        return {
            "Q1": get_percentile(sorted_data, 0.25),
            "Q2": self.calculate_median(),
            "Q3": get_percentile(sorted_data, 0.75)
        }
    
    def detect_outliers_iqr(self):
        """使用 IQR 方法檢測異常值 - filter() 的應用"""
        quartiles = self.quartiles_analysis()
        if not quartiles:
            return []
        
        q1, q3 = quartiles["Q1"], quartiles["Q3"]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        # 使用 filter() 找出異常值
        outliers = list(filter(
            lambda x: x < lower_bound or x > upper_bound, 
            self.numeric_data
        ))
        
        return sorted(outliers)  # sorted() 排序異常值
    
    def data_distribution(self, bins=10):
        """資料分佈分析 - 綜合應用多個內建函數"""
        if not self.numeric_data:
            return {}
        
        min_val, max_val = min(self.numeric_data), max(self.numeric_data)
        
        if min_val == max_val:
            return {f"{min_val}": len(self.numeric_data)}
        
        bin_width = (max_val - min_val) / bins
        bins_dict = {}
        
        for i in range(bins):
            lower = min_val + i * bin_width
            upper = min_val + (i + 1) * bin_width
            
            # 使用 filter() 計算每個區間的數據量
            if i == bins - 1:  # 最後一個區間包含上界
                count = len(list(filter(lambda x: lower <= x <= upper, self.numeric_data)))
            else:
                count = len(list(filter(lambda x: lower <= x < upper, self.numeric_data)))
            
            bins_dict[f"{lower:.2f}-{upper:.2f}"] = count
        
        return bins_dict
    
    def descriptive_statistics(self):
        """描述性統計 - 變異性指標"""
        if len(self.numeric_data) < 2:
            return None
        
        mean = sum(self.numeric_data) / len(self.numeric_data)
        
        # 計算變異數 - 使用 map() 和 sum()
        squared_diffs = map(lambda x: (x - mean) ** 2, self.numeric_data)
        variance = sum(squared_diffs) / (len(self.numeric_data) - 1)
        
        std_dev = math.sqrt(variance)
        
        return {
            "變異數": variance,
            "標準差": std_dev,
            "變異係數": (std_dev / mean * 100) if mean != 0 else 0
        }
    
    def percentile_analysis(self, percentiles=None):
        """百分位數分析"""
        if not percentiles:
            percentiles = [10, 25, 50, 75, 90, 95, 99]
        
        if not self.numeric_data:
            return {}
        
        sorted_data = sorted(self.numeric_data)
        n = len(sorted_data)
        
        result = {}
        for p in percentiles:
            # 計算百分位數的位置
            pos = (p / 100) * (n - 1)
            
            if pos.is_integer():
                result[f"P{p}"] = sorted_data[int(pos)]
            else:
                # 線性插值
                lower_idx = int(pos)
                upper_idx = min(lower_idx + 1, n - 1)
                weight = pos - lower_idx
                
                if upper_idx < n:
                    result[f"P{p}"] = (
                        sorted_data[lower_idx] * (1 - weight) + 
                        sorted_data[upper_idx] * weight
                    )
                else:
                    result[f"P{p}"] = sorted_data[lower_idx]
        
        return result
    
    def correlation_analysis(self, other_data):
        """相關性分析 - 兩組資料的關係"""
        if not self.numeric_data or not other_data:
            return None
        
        # 確保兩組資料長度相同
        min_length = min(len(self.numeric_data), len(other_data))
        data1 = self.numeric_data[:min_length]
        data2 = other_data[:min_length]
        
        if len(data1) < 2:
            return None
        
        # 計算平均值
        mean1 = sum(data1) / len(data1)
        mean2 = sum(data2) / len(data2)
        
        # 使用 zip() 和 map() 計算相關係數
        numerator = sum(map(lambda pair: (pair[0] - mean1) * (pair[1] - mean2), 
                           zip(data1, data2)))
        
        sum_sq1 = sum(map(lambda x: (x - mean1) ** 2, data1))
        sum_sq2 = sum(map(lambda x: (x - mean2) ** 2, data2))
        
        denominator = math.sqrt(sum_sq1 * sum_sq2)
        
        if denominator == 0:
            return 0
        
        correlation = numerator / denominator
        return round(correlation, 4)
    
    def data_quality_report(self):
        """資料品質報告"""
        total_count = len(self.original_data)
        valid_count = len(self.numeric_data)
        invalid_count = total_count - valid_count
        
        # 找出無效資料
        invalid_data = []
        for item in self.original_data:
            try:
                float(item)
            except (ValueError, TypeError):
                invalid_data.append(item)
        
        return {
            "總資料量": total_count,
            "有效資料": valid_count,
            "無效資料": invalid_count,
            "完整度": round((valid_count / total_count * 100), 2) if total_count > 0 else 0,
            "無效項目": invalid_data[:10]  # 只顯示前10個無效項目
        }
    
    def generate_text_chart(self, chart_type="histogram", width=40):
        """生成文字圖表"""
        if not self.numeric_data:
            return "無資料可顯示"
        
        if chart_type == "histogram":
            return self.create_histogram(width)
        elif chart_type == "boxplot":
            return self.create_boxplot(width)
        else:
            return "不支援的圖表類型"
    
    def create_histogram(self, width=40):
        """創建文字直方圖"""
        distribution = self.data_distribution(bins=10)
        
        if not distribution:
            return "無資料分佈"
        
        # 找出最大頻率來調整縮放比例
        max_count = max(distribution.values())
        
        chart = "\n📊 資料分佈直方圖\n"
        chart += "=" * (width + 20) + "\n"
        
        for range_str, count in distribution.items():
            # 計算長條長度
            if max_count > 0:
                bar_length = int((count / max_count) * width)
            else:
                bar_length = 0
            
            bar = "█" * bar_length
            chart += f"{range_str:>15} │{bar:<{width}} {count:>4}\n"
        
        chart += "=" * (width + 20) + "\n"
        return chart
    
    def create_boxplot(self, width=40):
        """創建文字箱型圖"""
        if len(self.numeric_data) < 4:
            return "資料不足，無法繪製箱型圖"
        
        quartiles = self.quartiles_analysis()
        if not quartiles:
            return "無法計算四分位數"
        
        min_val = min(self.numeric_data)
        max_val = max(self.numeric_data)
        q1, q2, q3 = quartiles["Q1"], quartiles["Q2"], quartiles["Q3"]
        
        # 計算各位置在圖上的相對位置
        data_range = max_val - min_val
        if data_range == 0:
            return "資料無變異，無法繪製箱型圖"
        
        def get_position(value):
            return int(((value - min_val) / data_range) * width)
        
        min_pos = 0
        q1_pos = get_position(q1)
        q2_pos = get_position(q2)
        q3_pos = get_position(q3)
        max_pos = width
        
        chart = "\n📦 箱型圖\n"
        chart += "=" * (width + 10) + "\n"
        
        # 創建箱型圖線條
        line = [" "] * (width + 1)
        
        # 最小值標記
        line[min_pos] = "├"
        
        # Q1到Q3的箱子
        for i in range(q1_pos, q3_pos + 1):
            if i == q1_pos:
                line[i] = "┌" if i != q2_pos else "┬"
            elif i == q3_pos:
                line[i] = "┐" if i != q2_pos else "┬"
            elif i == q2_pos:
                line[i] = "┼"
            else:
                line[i] = "─"
        
        # 鬚狀線
        for i in range(min_pos + 1, q1_pos):
            line[i] = "─"
        for i in range(q3_pos + 1, max_pos):
            line[i] = "─"
        
        # 最大值標記
        line[max_pos] = "┤"
        
        chart += "".join(line) + "\n"
        
        # 添加數值標籤
        chart += f"Min: {min_val:.2f}  Q1: {q1:.2f}  Q2: {q2:.2f}  Q3: {q3:.2f}  Max: {max_val:.2f}\n"
        chart += "=" * (width + 10) + "\n"
        
        return chart
    
    def comprehensive_report(self):
        """綜合統計報告"""
        if not self.numeric_data:
            return "❌ 無有效資料進行分析"
        
        report = "\n" + "=" * 80 + "\n"
        report += "📊 綜合統計分析報告\n"
        report += "=" * 80 + "\n"
        
        # 1. 資料品質
        quality = self.data_quality_report()
        report += f"\n📋 資料品質摘要:\n"
        report += f"{'總資料量':>12}: {quality['總資料量']:>8}\n"
        report += f"{'有效資料':>12}: {quality['有效資料']:>8}\n"
        report += f"{'資料完整度':>12}: {quality['完整度']:>7}%\n"
        
        if quality['無效項目']:
            report += f"{'無效項目':>12}: {str(quality['無效項目'][:5])}\n"
        
        # 2. 基本統計
        basic = self.basic_stats()
        report += f"\n📈 基本統計:\n"
        for key, value in basic.items():
            if isinstance(value, (int, float)):
                if isinstance(value, float):
                    report += f"{key:>12}: {value:>12.3f}\n"
                else:
                    report += f"{key:>12}: {value:>12}\n"
            else:
                report += f"{key:>12}: {str(value):>12}\n"
        
        # 3. 變異性指標
        desc_stats = self.descriptive_statistics()
        if desc_stats:
            report += f"\n📊 變異性指標:\n"
            for key, value in desc_stats.items():
                if "係數" in key:
                    report += f"{key:>12}: {value:>11.2f}%\n"
                else:
                    report += f"{key:>12}: {value:>12.3f}\n"
        
        # 4. 四分位數
        quartiles = self.quartiles_analysis()
        if quartiles:
            report += f"\n📐 四分位數:\n"
            for q, value in quartiles.items():
                report += f"{q:>12}: {value:>12.3f}\n"
        
        # 5. 百分位數
        percentiles = self.percentile_analysis([5, 10, 25, 50, 75, 90, 95])
        if percentiles:
            report += f"\n📊 百分位數:\n"
            for p, value in percentiles.items():
                report += f"{p:>12}: {value:>12.3f}\n"
        
        # 6. 異常值檢測
        outliers = self.detect_outliers_iqr()
        if outliers:
            report += f"\n⚠️  異常值 ({len(outliers)} 個):\n"
            # 只顯示前10個異常值
            display_outliers = outliers[:10]
            for i, outlier in enumerate(display_outliers, 1):
                report += f"{'Outlier ' + str(i):>12}: {outlier:>12.3f}\n"
            if len(outliers) > 10:
                report += f"{'...等':>12}: {len(outliers) - 10:>8} 個\n"
        else:
            report += f"\n✅ 無檢測到異常值\n"
        
        # 7. 資料分佈
        report += self.create_histogram(width=50)
        
        # 8. 箱型圖
        if len(self.numeric_data) >= 4:
            report += self.create_boxplot(width=50)
        
        report += "\n" + "=" * 80 + "\n"
        
        return report

# 示範內建函數的具體應用
def builtin_functions_demo():
    """示範內建函數在統計分析中的應用"""
    print("🧮 Python內建函數在統計分析中的應用")
    print("=" * 60)
    
    # 示範資料
    sales_data = [120, 135, 98, 156, 142, 189, 176, 203, 167, 145, 198, 134, 178, 165, 187]
    temperatures = [25.2, 26.8, 24.5, 27.3, 23.9, 28.1, 26.4, 25.7, 29.2, 24.8, 27.6, 25.1, 28.5]
    
    print(f"銷售資料: {sales_data}")
    print(f"溫度資料: {temperatures}")
    
    # 1. 基本統計函數示範
    print(f"\n📊 基本統計函數示範:")
    print(f"len() - 資料筆數: {len(sales_data)}")
    print(f"sum() - 總銷售額: {sum(sales_data)}")
    print(f"max() - 最高銷售: {max(sales_data)}")
    print(f"min() - 最低銷售: {min(sales_data)}")
    print(f"平均銷售額: {sum(sales_data) / len(sales_data):.2f}")
    
    # 2. sorted() 函數示範
    print(f"\n📈 sorted() 函數應用:")
    sorted_sales = sorted(sales_data)
    print(f"銷售額排序: {sorted_sales}")
    
    # 計算中位數
    n = len(sorted_sales)
    median = sorted_sales[n//2] if n % 2 == 1 else (sorted_sales[n//2-1] + sorted_sales[n//2]) / 2
    print(f"中位數: {median}")
    
    # 3. map() 函數示範
    print(f"\n🔄 map() 函數應用:")
    
    # 溫度單位轉換
    fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, temperatures))
    print("攝氏轉華氏溫度:")
    for c, f in zip(temperatures[:5], fahrenheit_temps[:5]):  # 只顯示前5個
        print(f"  {c}°C = {f:.1f}°F")
    
    # 銷售額分級
    sales_grades = list(map(lambda x: 'A' if x >= 180 else 'B' if x >= 150 else 'C' if x >= 120 else 'D', sales_data))
    print(f"\n銷售等級: {sales_grades}")
    
    # 4. filter() 函數示範
    print(f"\n🔍 filter() 函數應用:")
    
    # 篩選高銷售額
    high_sales = list(filter(lambda x: x >= 160, sales_data))
    print(f"高銷售額 (>=160): {high_sales}")
    print(f"高銷售筆數: {len(high_sales)}")
    
    # 篩選高溫天氣
    hot_days = list(filter(lambda temp: temp >= 27, temperatures))
    print(f"高溫天氣 (>=27°C): {hot_days}")
    
    # 5. any() 和 all() 函數示範
    print(f"\n✅ any() 和 all() 函數應用:")
    print(f"有銷售額超過200: {any(x > 200 for x in sales_data)}")
    print(f"所有銷售額都超過90: {all(x > 90 for x in sales_data)}")
    print(f"有溫度低於24度: {any(temp < 24 for temp in temperatures)}")
    print(f"所有溫度都在20-30度間: {all(20 <= temp <= 30 for temp in temperatures)}")
    
    # 6. enumerate() 函數示範
    print(f"\n📋 enumerate() 函數應用:")
    print("前5天的銷售記錄:")
    for day, sales in enumerate(sales_data[:5], 1):
        print(f"  第{day:2d}天: {sales:3d}")
    
    # 7. zip() 函數示範
    print(f"\n🔗 zip() 函數應用:")
    print("銷售額與對應等級:")
    for sales, grade in list(zip(sales_data, sales_grades))[:5]:
        print(f"  銷售額 {sales:3d} → 等級 {grade}")
    
    # 8. reversed() 函數示範
    print(f"\n🔄 reversed() 函數應用:")
    recent_sales = list(reversed(sales_data[-5:]))  # 最近5天的銷售，倒序顯示
    print(f"最近5天銷售(由近到遠): {recent_sales}")
    
    # 9. 組合使用示範
    print(f"\n🎯 綜合應用 - 找出銷售額前3名的天數:")
    
    # 使用 enumerate 添加天數，sorted 排序，切片取前3
    sales_with_day = list(enumerate(sales_data, 1))  # (天數, 銷售額)
    top_3_days = sorted(sales_with_day, key=lambda x: x[1], reverse=True)[:3]
    
    for rank, (day, sales) in enumerate(top_3_days, 1):
        print(f"  第{rank}名: 第{day:2d}天，銷售額 {sales}")

def interactive_statistical_tool():
    """互動式統計分析工具"""
    print("📊 歡迎使用統計分析工具！")
    print("這個工具展示了Python內建函數的強大威力")
    
    analyzer = StatisticalAnalyzer()
    
    while True:
        print("\n" + "=" * 60)
        print("🛠️  功能選單:")
        print("1. 📝 輸入資料")
        print("2. 📊 基本統計分析")
        print("3. 📈 進階統計分析") 
        print("4. 📋 完整分析報告")
        print("5. 📊 視覺化圖表")
        print("6. 🔍 異常值檢測")
        print("7. 📊 百分位數分析")
        print("8. 🧪 載入示範資料")
        print("9. 🧮 內建函數示範")
        print("10. 🧹 清除資料")
        print("0. 🚪 退出程式")
        print("=" * 60)
        
        try:
            choice = input("請選擇功能 (0-10): ").strip()
            
            if choice == "0":
                print("\n👋 感謝使用統計分析工具！")
                print("🎓 希望您已經掌握了內建函數的使用技巧！")
                break
            elif choice == "1":
                input_data_interface(analyzer)
            elif choice == "2":
                basic_analysis_interface(analyzer)
            elif choice == "3":
                advanced_analysis_interface(analyzer)
            elif choice == "4":
                print(analyzer.comprehensive_report())
            elif choice == "5":
                visualization_interface(analyzer)
            elif choice == "6":
                outlier_detection_interface(analyzer)
            elif choice == "7":
                percentile_interface(analyzer)
            elif choice == "8":
                load_demo_data_interface(analyzer)
            elif choice == "9":
                builtin_functions_demo()
            elif choice == "10":
                analyzer.original_data = []
                analyzer.numeric_data = []
                print("✅ 資料已清除")
            else:
                print("❌ 無效選擇，請重新輸入")
        
        except KeyboardInterrupt:
            print("\n\n程式被中斷，感謝使用！")
            break
        
        if choice != "0":
            input("\n按 Enter 繼續...")

def input_data_interface(analyzer):
    """資料輸入介面"""
    print("\n📝 資料輸入")
    print("-" * 30)
    
    print("輸入選項:")
    print("1. 逐一輸入數字")
    print("2. 批量輸入（空格分隔）")
    print("3. 從清單輸入")
    
    method = input("選擇輸入方法 (1-3): ").strip()
    
    if method == "1":
        print("\n逐一輸入數字（輸入 'done' 結束）:")
        count = 0
        while True:
            try:
                data = input(f"數字 #{count + 1}: ").strip()
                if data.lower() == 'done':
                    break
                
                number = float(data)
                analyzer.add_data(number)
                count += 1
                print(f"✅ 已添加: {number}")
                
            except ValueError:
                print("❌ 請輸入有效數字")
        
        print(f"📊 總共輸入了 {count} 個數據")
    
    elif method == "2":
        data_str = input("\n請輸入數字（用空格分隔）: ").strip()
        try:
            numbers = list(map(float, data_str.split()))
            analyzer.add_data(*numbers)
            print(f"✅ 已添加 {len(numbers)} 個數據: {numbers}")
        except ValueError:
            print("❌ 輸入格式錯誤，請確保都是數字")
    
    elif method == "3":
        print("\n請輸入Python清單格式，例如: [1, 2, 3, 4.5, 6]")
        try:
            list_str = input("清單: ").strip()
            # 安全評估輸入
            if list_str.startswith('[') and list_str.endswith(']'):
                numbers = eval(list_str)  # 注意：實際應用中應該避免使用eval
                if isinstance(numbers, list):
                    analyzer.add_data(*numbers)
                    print(f"✅ 已添加 {len(numbers)} 個數據")
                else:
                    print("❌ 請輸入清單格式")
            else:
                print("❌ 請輸入有效的清單格式")
        except:
            print("❌ 輸入格式錯誤")

def basic_analysis_interface(analyzer):
    """基本分析介面"""
    if not analyzer.numeric_data:
        print("❌ 沒有有效資料進行分析")
        return
    
    print("\n📊 基本統計分析")
    print("-" * 40)
    
    basic_stats = analyzer.basic_stats()
    for key, value in basic_stats.items():
        if isinstance(value, float):
            print(f"{key:>10}: {value:>12.3f}")
        elif isinstance(value, list):
            print(f"{key:>10}: {value}")
        else:
            print(f"{key:>10}: {value:>12}")
    
    # 顯示排序後的資料
    sorted_data = sorted(analyzer.numeric_data)
    print(f"\n排序結果: {sorted_data}")

def advanced_analysis_interface(analyzer):
    """進階分析介面"""
    if not analyzer.numeric_data:
        print("❌ 沒有有效資料進行分析")
        return
    
    print("\n📈 進階統計分析")
    print("-" * 40)
    
    # 變異性指標
    desc_stats = analyzer.descriptive_statistics()
    if desc_stats:
        print("變異性指標:")
        for key, value in desc_stats.items():
            if "係數" in key:
                print(f"  {key}: {value:.2f}%")
            else:
                print(f"  {key}: {value:.4f}")
    
    # 四分位數
    quartiles = analyzer.quartiles_analysis()
    if quartiles:
        print(f"\n四分位數:")
        for q, value in quartiles.items():
            print(f"  {q}: {value:.3f}")
        
        # 四分位距
        iqr = quartiles["Q3"] - quartiles["Q1"]
        print(f"  IQR: {iqr:.3f}")

def visualization_interface(analyzer):
    """視覺化介面"""
    if not analyzer.numeric_data:
        print("❌ 沒有有效資料進行視覺化")
        return
    
    print("\n📊 資料視覺化")
    print("-" * 30)
    
    print("選擇圖表類型:")
    print("1. 直方圖")
    print("2. 箱型圖")
    print("3. 兩者都顯示")
    
    choice = input("請選擇 (1-3): ").strip()
    
    if choice == "1":
        print(analyzer.create_histogram(width=50))
    elif choice == "2":
        print(analyzer.create_boxplot(width=50))
    elif choice == "3":
        print(analyzer.create_histogram(width=50))
        print(analyzer.create_boxplot(width=50))
    else:
        print("❌ 無效選擇")

def outlier_detection_interface(analyzer):
    """異常值檢測介面"""
    if not analyzer.numeric_data:
        print("❌ 沒有有效資料進行異常值檢測")
        return
    
    print("\n🔍 異常值檢測")
    print("-" * 30)
    
    outliers = analyzer.detect_outliers_iqr()
    
    if outliers:
        print(f"發現 {len(outliers)} 個異常值:")
        for i, outlier in enumerate(outliers, 1):
            print(f"  {i:2d}. {outlier:.3f}")
        
        print(f"\n異常值統計:")
        print(f"  異常值比例: {len(outliers) / len(analyzer.numeric_data) * 100:.2f}%")
        print(f"  異常值範圍: {min(outliers):.3f} ~ {max(outliers):.3f}")
        
    else:
        print("✅ 未檢測到異常值")
        print("資料分佈相對正常")

def percentile_interface(analyzer):
    """百分位數分析介面"""
    if not analyzer.numeric_data:
        print("❌ 沒有有效資料進行百分位數分析")
        return
    
    print("\n📊 百分位數分析")
    print("-" * 30)
    
    # 預設百分位數
    percentiles = analyzer.percentile_analysis()
    
    print("標準百分位數:")
    for p, value in percentiles.items():
        print(f"  {p}: {value:.3f}")
    
    # 自訂百分位數
    custom_input = input("\n輸入自訂百分位數（空格分隔，如: 5 25 75 95）: ").strip()
    
    if custom_input:
        try:
            custom_percentiles = list(map(int, custom_input.split()))
            custom_results = analyzer.percentile_analysis(custom_percentiles)
            
            print(f"\n自訂百分位數:")
            for p, value in custom_results.items():
                print(f"  {p}: {value:.3f}")
                
        except ValueError:
            print("❌ 輸入格式錯誤")

def load_demo_data_interface(analyzer):
    """載入示範資料介面"""
    demo_datasets = {
        "1": {
            "name": "學生成績",
            "data": [85, 92, 78, 88, 95, 67, 82, 90, 76, 84, 89, 93, 71, 87, 94, 83, 96, 74, 91, 86],
            "description": "20名學生的考試成績"
        },
        "2": {
            "name": "月度銷售額",
            "data": [120, 135, 98, 156, 142, 189, 176, 203, 167, 145, 198, 134, 178, 165, 187],
            "description": "15個月的銷售數據（千元）"
        },
        "3": {
            "name": "每日溫度",
            "data": [25.2, 26.8, 24.5, 27.3, 23.9, 28.1, 26.4, 25.7, 29.2, 24.8, 27.6, 25.1, 28.5, 26.9, 24.3],
            "description": "15天的氣溫記錄（攝氏度）"
        },
        "4": {
            "name": "股票價格",
            "data": [1250, 1180, 1320, 1290, 1156, 1380, 1420, 1350, 1275, 1195, 1445, 1398, 1267, 1389, 1456],
            "description": "15個交易日的收盤價"
        },
        "5": {
            "name": "混合資料（含異常值）",
            "data": [10, 12, 11, 13, 9, 14, 10, 12, 11, 50, 13, 9, 15, 11, 10, 200, 12, 13],
            "description": "含有異常值的測試資料"
        }
    }
    
    print("\n🧪 選擇示範資料集:")
    print("-" * 35)
    
    for key, dataset in demo_datasets.items():
        print(f"{key}. {dataset['name']:12} - {dataset['description']}")
    
    choice = input("\n請選擇資料集 (1-5): ").strip()
    
    if choice in demo_datasets:
        selected = demo_datasets[choice]
        analyzer.original_data = selected["data"].copy()
        analyzer.prepare_data()
        
        print(f"✅ 已載入「{selected['name']}」資料集")
        print(f"📊 資料內容: {selected['data']}")
        print(f"📈 有效資料量: {len(analyzer.numeric_data)}")
        
        # 顯示基本統計
        basic = analyzer.basic_stats()
        if basic:
            print(f"📋 快速統計: 平均值 {basic['平均值']:.2f}, 最大值 {basic['最大值']}, 最小值 {basic['最小值']}")
    else:
        print("❌ 無效選擇")

if __name__ == "__main__":
    interactive_statistical_tool()