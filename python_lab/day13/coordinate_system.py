# 座標系統程式 - Day 13主要項目
# 完整的2D座標系統管理程式

import math
import json
import os
from datetime import datetime

class CoordinateSystem:
    def __init__(self):
        self.points = []  # 儲存點的清單：[(name, (x, y)), ...]
        self.shapes = []  # 儲存圖形的清單：[(name, point_names, shape_type), ...]
        self.data_file = "coordinates.json"
        self.load_data()
    
    def save_data(self):
        """儲存座標資料"""
        try:
            data = {
                "points": self.points,
                "shapes": self.shapes,
                "saved_at": datetime.now().isoformat()
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ 儲存失敗：{e}")
    
    def load_data(self):
        """載入座標資料"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.points = [tuple(point) if isinstance(point, list) and len(point) == 2 
                                 else (point[0], tuple(point[1])) 
                                 for point in data.get("points", [])]
                    self.shapes = data.get("shapes", [])
        except Exception as e:
            print(f"⚠️ 載入失敗：{e}")
            self.load_default_points()
    
    def load_default_points(self):
        """載入預設座標點"""
        self.points = [
            ("原點", (0, 0)),
            ("A", (3, 4)),
            ("B", (-2, 1)),
            ("C", (5, -3)),
            ("D", (-1, -2))
        ]
    
    def display_header(self):
        """顯示程式標題"""
        print("\n" + "="*60)
        print("📊              2D座標系統管理程式              📊")
        print("="*60)
        print(f"📅 當前時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"📍 座標點數量：{len(self.points)}")
        print(f"📐 圖形數量：{len(self.shapes)}")
    
    def display_menu(self):
        """顯示主選單"""
        print("\n" + "─"*40)
        print("🏠 主選單")
        print("─"*40)
        print("1. 📍 查看所有座標點")
        print("2. ➕ 新增座標點")
        print("3. 📝 修改座標點")
        print("4. ❌ 刪除座標點")
        print("5. 📏 計算距離")
        print("6. 🎯 計算中點")
        print("7. 📐 幾何分析")
        print("8. 🗺️  繪製座標圖")
        print("9. 💾 匯出資料")
        print("0. 🚪 離開系統")
        print("─"*40)
    
    def validate_coordinates(self, x, y):
        """驗證座標有效性"""
        try:
            x = float(x)
            y = float(y)
            return True, (x, y)
        except ValueError:
            return False, None
    
    def find_point(self, name):
        """尋找指定名稱的點"""
        for point in self.points:
            if point[0] == name:
                return point
        return None
    
    def get_quadrant(self, x, y):
        """判斷點所在象限"""
        if x > 0 and y > 0:
            return "第一象限"
        elif x < 0 and y > 0:
            return "第二象限"
        elif x < 0 and y < 0:
            return "第三象限"
        elif x > 0 and y < 0:
            return "第四象限"
        elif x == 0 and y == 0:
            return "原點"
        elif x == 0:
            return "Y軸上"
        else:
            return "X軸上"
    
    def calculate_distance(self, point1, point2):
        """計算兩點間距離"""
        x1, y1 = point1[1]
        x2, y2 = point2[1]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def view_all_points(self):
        """查看所有座標點"""
        if not self.points:
            print("\n❌ 目前沒有任何座標點！")
            return
        
        print(f"\n📍 所有座標點 - 共{len(self.points)}個")
        print("="*60)
        print(f"{'名稱':<10} {'座標':<15} {'象限':<10} {'距離原點':<10}")
        print("-" * 60)
        
        # 按距離原點排序
        origin = (0, 0)
        points_with_distance = []
        for name, (x, y) in self.points:
            distance = math.sqrt(x ** 2 + y ** 2)
            quadrant = self.get_quadrant(x, y)
            points_with_distance.append((name, (x, y), quadrant, distance))
        
        points_with_distance.sort(key=lambda x: x[3])  # 按距離排序
        
        for name, (x, y), quadrant, distance in points_with_distance:
            print(f"{name:<10} ({x:>5.1f}, {y:>5.1f})   {quadrant:<10} {distance:<10.2f}")
        
        # 統計各象限點數
        quadrant_count = {}
        for _, _, quadrant, _ in points_with_distance:
            quadrant_count[quadrant] = quadrant_count.get(quadrant, 0) + 1
        
        print(f"\n📊 象限分佈：")
        for quadrant, count in quadrant_count.items():
            print(f"  {quadrant}：{count}個點")
    
    def add_point(self):
        """新增座標點"""
        print("\n➕ 新增座標點")
        print("─"*20)
        
        # 輸入點名稱
        while True:
            name = input("📝 點的名稱：").strip()
            if not name:
                print("❌ 名稱不能為空！")
                continue
            
            if self.find_point(name):
                print("❌ 該名稱已存在！")
                continue
            
            break
        
        # 輸入座標
        while True:
            try:
                x_input = input("📍 X座標：").strip()
                y_input = input("📍 Y座標：").strip()
                
                if not x_input or not y_input:
                    print("❌ 座標不能為空！")
                    continue
                
                valid, coords = self.validate_coordinates(x_input, y_input)
                if not valid:
                    print("❌ 請輸入有效的數字！")
                    continue
                
                x, y = coords
                break
                
            except KeyboardInterrupt:
                print("\n❌ 取消新增")
                return
        
        # 新增點
        new_point = (name, (x, y))
        self.points.append(new_point)
        self.save_data()
        
        quadrant = self.get_quadrant(x, y)
        distance_origin = math.sqrt(x ** 2 + y ** 2)
        
        print(f"\n✅ 成功新增座標點：{name}")
        print(f"📍 座標：({x}, {y})")
        print(f"📊 象限：{quadrant}")
        print(f"📏 距離原點：{distance_origin:.2f}")
    
    def modify_point(self):
        """修改座標點"""
        if not self.points:
            print("\n❌ 目前沒有任何座標點！")
            return
        
        print("\n📝 修改座標點")
        print("現有座標點：", [point[0] for point in self.points])
        
        name = input("請輸入要修改的點名稱：").strip()
        point = self.find_point(name)
        
        if not point:
            print("❌ 找不到該座標點！")
            return
        
        current_x, current_y = point[1]
        print(f"目前座標：({current_x}, {current_y})")
        
        print("\n請選擇修改方式：")
        print("1. 修改名稱")
        print("2. 修改座標")
        print("3. 修改名稱和座標")
        
        choice = input("請選擇 (1-3): ").strip()
        
        if choice == "1":
            new_name = input("請輸入新名稱：").strip()
            if not new_name:
                print("❌ 名稱不能為空！")
                return
            
            if self.find_point(new_name) and new_name != name:
                print("❌ 該名稱已存在！")
                return
            
            # 更新點名稱
            for i, (old_name, coords) in enumerate(self.points):
                if old_name == name:
                    self.points[i] = (new_name, coords)
                    break
            
            print(f"✅ 已將 {name} 重命名為 {new_name}")
        
        elif choice == "2":
            try:
                x_input = input("請輸入新的X座標：").strip()
                y_input = input("請輸入新的Y座標：").strip()
                
                valid, new_coords = self.validate_coordinates(x_input, y_input)
                if not valid:
                    print("❌ 請輸入有效的數字！")
                    return
                
                # 更新座標
                for i, (point_name, old_coords) in enumerate(self.points):
                    if point_name == name:
                        self.points[i] = (point_name, new_coords)
                        break
                
                print(f"✅ 已將 {name} 的座標更新為 {new_coords}")
                
            except ValueError:
                print("❌ 請輸入有效的數字！")
                return
        
        elif choice == "3":
            new_name = input("請輸入新名稱：").strip()
            if not new_name:
                print("❌ 名稱不能為空！")
                return
            
            if self.find_point(new_name) and new_name != name:
                print("❌ 該名稱已存在！")
                return
            
            try:
                x_input = input("請輸入新的X座標：").strip()
                y_input = input("請輸入新的Y座標：").strip()
                
                valid, new_coords = self.validate_coordinates(x_input, y_input)
                if not valid:
                    print("❌ 請輸入有效的數字！")
                    return
                
                # 更新名稱和座標
                for i, (old_name, old_coords) in enumerate(self.points):
                    if old_name == name:
                        self.points[i] = (new_name, new_coords)
                        break
                
                print(f"✅ 已將 {name}{point[1]} 更新為 {new_name}{new_coords}")
                
            except ValueError:
                print("❌ 請輸入有效的數字！")
                return
        
        else:
            print("❌ 無效的選擇！")
            return
        
        self.save_data()
    
    def delete_point(self):
        """刪除座標點"""
        if not self.points:
            print("\n❌ 目前沒有任何座標點！")
            return
        
        print("\n❌ 刪除座標點")
        print("現有座標點：", [point[0] for point in self.points])
        
        name = input("請輸入要刪除的點名稱：").strip()
        point = self.find_point(name)
        
        if not point:
            print("❌ 找不到該座標點！")
            return
        
        print(f"即將刪除：{name}{point[1]}")
        confirm = input("確定要刪除嗎？(y/N): ").lower().strip()
        
        if confirm == 'y':
            self.points = [p for p in self.points if p[0] != name]
            self.save_data()
            print(f"✅ 已刪除座標點：{name}")
        else:
            print("❌ 取消刪除")
    
    def calculate_distances(self):
        """計算距離"""
        if len(self.points) < 2:
            print("\n❌ 至少需要兩個座標點！")
            return
        
        print("\n📏 距離計算")
        print("─"*20)
        print("選擇計算方式：")
        print("1. 計算兩點間距離")
        print("2. 計算某點到所有點的距離")
        print("3. 顯示所有點對的距離矩陣")
        
        choice = input("請選擇 (1-3): ").strip()
        
        if choice == "1":
            print("現有座標點：", [point[0] for point in self.points])
            name1 = input("第一個點的名稱：").strip()
            name2 = input("第二個點的名稱：").strip()
            
            point1 = self.find_point(name1)
            point2 = self.find_point(name2)
            
            if not point1 or not point2:
                print("❌ 找不到指定的點！")
                return
            
            distance = self.calculate_distance(point1, point2)
            print(f"\n📏 {name1} 到 {name2} 的距離：{distance:.4f}")
            
            # 額外資訊
            x1, y1 = point1[1]
            x2, y2 = point2[1]
            dx = x2 - x1
            dy = y2 - y1
            print(f"📊 水平距離：{abs(dx):.4f}")
            print(f"📊 垂直距離：{abs(dy):.4f}")
            
            if dx != 0:
                slope = dy / dx
                print(f"📊 直線斜率：{slope:.4f}")
            else:
                print("📊 直線斜率：無限大（垂直線）")
        
        elif choice == "2":
            print("現有座標點：", [point[0] for point in self.points])
            name = input("請選擇中心點：").strip()
            
            center_point = self.find_point(name)
            if not center_point:
                print("❌ 找不到該座標點！")
                return
            
            print(f"\n📏 從 {name} 到各點的距離：")
            print("-" * 40)
            
            distances = []
            for point in self.points:
                if point[0] != name:
                    distance = self.calculate_distance(center_point, point)
                    distances.append((point[0], distance))
            
            # 按距離排序
            distances.sort(key=lambda x: x[1])
            
            for target_name, distance in distances:
                print(f"  {name} → {target_name}: {distance:.4f}")
            
            if distances:
                closest = distances[0]
                farthest = distances[-1]
                print(f"\n🎯 最近的點：{closest[0]} (距離: {closest[1]:.4f})")
                print(f"🎯 最遠的點：{farthest[0]} (距離: {farthest[1]:.4f})")
        
        elif choice == "3":
            print(f"\n📏 距離矩陣：")
            print("─" * 60)
            
            # 建立表頭
            names = [point[0] for point in self.points]
            print(f"{'':>10}", end="")
            for name in names:
                print(f"{name:>10}", end="")
            print()
            
            # 輸出距離矩陣
            for i, point1 in enumerate(self.points):
                print(f"{names[i]:>10}", end="")
                for j, point2 in enumerate(self.points):
                    if i == j:
                        print(f"{'0.0000':>10}", end="")
                    else:
                        distance = self.calculate_distance(point1, point2)
                        print(f"{distance:>10.4f}", end="")
                print()
        
        else:
            print("❌ 無效的選擇！")
    
    def calculate_midpoint(self):
        """計算中點"""
        if len(self.points) < 2:
            print("\n❌ 至少需要兩個座標點！")
            return
        
        print("\n🎯 計算中點")
        print("現有座標點：", [point[0] for point in self.points])
        
        name1 = input("第一個點的名稱：").strip()
        name2 = input("第二個點的名稱：").strip()
        
        point1 = self.find_point(name1)
        point2 = self.find_point(name2)
        
        if not point1 or not point2:
            print("❌ 找不到指定的點！")
            return
        
        x1, y1 = point1[1]
        x2, y2 = point2[1]
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        print(f"\n🎯 {name1} 和 {name2} 的中點：({mid_x:.4f}, {mid_y:.4f})")
        
        # 詢問是否要新增中點
        add_midpoint = input("\n是否要將中點加入座標系統？(y/N): ").lower().strip()
        if add_midpoint == 'y':
            midpoint_name = input("請為中點命名：").strip()
            if midpoint_name and not self.find_point(midpoint_name):
                self.points.append((midpoint_name, (mid_x, mid_y)))
                self.save_data()
                print(f"✅ 已新增中點：{midpoint_name}")
            else:
                print("❌ 名稱無效或已存在！")
    
    def geometric_analysis(self):
        """幾何分析"""
        if len(self.points) < 3:
            print("\n❌ 至少需要三個座標點進行幾何分析！")
            return
        
        print("\n📐 幾何分析")
        print("─"*20)
        print("選擇分析類型：")
        print("1. 三角形分析")
        print("2. 四邊形分析") 
        print("3. 多邊形周長")
        print("4. 重心計算")
        
        choice = input("請選擇 (1-4): ").strip()
        
        if choice == "1":
            self.analyze_triangle()
        elif choice == "2":
            self.analyze_quadrilateral()
        elif choice == "3":
            self.calculate_polygon_perimeter()
        elif choice == "4":
            self.calculate_centroid()
        else:
            print("❌ 無效的選擇！")
    
    def analyze_triangle(self):
        """分析三角形"""
        print("\n📐 三角形分析")
        print("現有座標點：", [point[0] for point in self.points])
        
        names = []
        for i in range(3):
            name = input(f"第{i+1}個頂點名稱：").strip()
            point = self.find_point(name)
            if not point:
                print("❌ 找不到該座標點！")
                return
            names.append(name)
        
        points = [self.find_point(name) for name in names]
        coords = [point[1] for point in points]
        
        # 計算三邊長
        side_a = self.calculate_distance(points[1], points[2])  # BC
        side_b = self.calculate_distance(points[0], points[2])  # AC  
        side_c = self.calculate_distance(points[0], points[1])  # AB
        
        print(f"\n📐 三角形分析（{'-'.join(names)}）：")
        print(f"頂點座標：")
        for name, (x, y) in zip(names, coords):
            print(f"  {name}: ({x:.2f}, {y:.2f})")
        
        print(f"\n邊長：")
        print(f"  {names[1]}{names[2]}: {side_a:.4f}")
        print(f"  {names[0]}{names[2]}: {side_b:.4f}")
        print(f"  {names[0]}{names[1]}: {side_c:.4f}")
        
        # 計算周長和面積
        perimeter = side_a + side_b + side_c
        print(f"\n周長：{perimeter:.4f}")
        
        # 面積計算（海倫公式）
        s = perimeter / 2
        discriminant = s * (s - side_a) * (s - side_b) * (s - side_c)
        
        if discriminant >= 0:
            area = math.sqrt(discriminant)
            print(f"面積：{area:.4f}")
        else:
            print("面積：無法計算（三點共線或數據有誤）")
            return
        
        # 判斷三角形類型
        sides = sorted([side_a, side_b, side_c])
        tolerance = 1e-10
        
        if abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < tolerance:
            triangle_type = "直角三角形"
        elif abs(sides[0] - sides[1]) < tolerance and abs(sides[1] - sides[2]) < tolerance:
            triangle_type = "正三角形"
        elif (abs(sides[0] - sides[1]) < tolerance or 
              abs(sides[1] - sides[2]) < tolerance or 
              abs(sides[0] - sides[2]) < tolerance):
            triangle_type = "等腰三角形"
        else:
            triangle_type = "一般三角形"
        
        print(f"類型：{triangle_type}")
        
        # 計算重心
        centroid_x = sum(x for x, y in coords) / 3
        centroid_y = sum(y for x, y in coords) / 3
        print(f"重心：({centroid_x:.4f}, {centroid_y:.4f})")
    
    def analyze_quadrilateral(self):
        """分析四邊形"""
        if len(self.points) < 4:
            print("\n❌ 至少需要四個座標點！")
            return
        
        print("\n⬜ 四邊形分析")
        print("現有座標點：", [point[0] for point in self.points])
        
        names = []
        for i in range(4):
            name = input(f"第{i+1}個頂點名稱：").strip()
            point = self.find_point(name)
            if not point:
                print("❌ 找不到該座標點！")
                return
            names.append(name)
        
        points = [self.find_point(name) for name in names]
        coords = [point[1] for point in points]
        
        print(f"\n⬜ 四邊形分析（{'-'.join(names)}）：")
        print(f"頂點座標：")
        for name, (x, y) in zip(names, coords):
            print(f"  {name}: ({x:.2f}, {y:.2f})")
        
        # 計算四邊長
        sides = []
        side_names = []
        for i in range(4):
            next_i = (i + 1) % 4
            side_length = self.calculate_distance(points[i], points[next_i])
            sides.append(side_length)
            side_names.append(f"{names[i]}{names[next_i]}")
        
        print(f"\n邊長：")
        for side_name, length in zip(side_names, sides):
            print(f"  {side_name}: {length:.4f}")
        
        # 對角線
        diagonal1 = self.calculate_distance(points[0], points[2])
        diagonal2 = self.calculate_distance(points[1], points[3])
        
        print(f"\n對角線：")
        print(f"  {names[0]}{names[2]}: {diagonal1:.4f}")
        print(f"  {names[1]}{names[3]}: {diagonal2:.4f}")
        
        # 周長
        perimeter = sum(sides)
        print(f"\n周長：{perimeter:.4f}")
        
        # 判斷四邊形類型
        tolerance = 1e-10
        if (abs(sides[0] - sides[2]) < tolerance and 
            abs(sides[1] - sides[3]) < tolerance and
            abs(diagonal1 - diagonal2) < tolerance):
            quad_type = "正方形"
        elif (abs(sides[0] - sides[2]) < tolerance and 
              abs(sides[1] - sides[3]) < tolerance):
            quad_type = "長方形"
        elif (abs(sides[0] - sides[1]) < tolerance and
              abs(sides[1] - sides[2]) < tolerance and
              abs(sides[2] - sides[3]) < tolerance):
            quad_type = "菱形"
        else:
            quad_type = "一般四邊形"
        
        print(f"類型：{quad_type}")
    
    def calculate_polygon_perimeter(self):
        """計算多邊形周長"""
        print("\n📏 多邊形周長計算")
        print("現有座標點：", [point[0] for point in self.points])
        
        vertex_names = input("請輸入頂點名稱（用空格分隔）：").strip().split()
        
        if len(vertex_names) < 3:
            print("❌ 至少需要三個頂點！")
            return
        
        vertices = []
        for name in vertex_names:
            point = self.find_point(name)
            if not point:
                print(f"❌ 找不到座標點：{name}")
                return
            vertices.append(point)
        
        total_perimeter = 0
        print(f"\n📏 多邊形周長計算：")
        
        for i in range(len(vertices)):
            next_i = (i + 1) % len(vertices)
            side_length = self.calculate_distance(vertices[i], vertices[next_i])
            total_perimeter += side_length
            print(f"  {vertex_names[i]} → {vertex_names[next_i]}: {side_length:.4f}")
        
        print(f"\n總周長：{total_perimeter:.4f}")
    
    def calculate_centroid(self):
        """計算重心"""
        print("\n🎯 重心計算")
        print("現有座標點：", [point[0] for point in self.points])
        
        vertex_names = input("請輸入頂點名稱（用空格分隔）：").strip().split()
        
        if len(vertex_names) < 2:
            print("❌ 至少需要兩個頂點！")
            return
        
        vertices = []
        for name in vertex_names:
            point = self.find_point(name)
            if not point:
                print(f"❌ 找不到座標點：{name}")
                return
            vertices.append(point)
        
        # 計算重心
        sum_x = sum(point[1][0] for point in vertices)
        sum_y = sum(point[1][1] for point in vertices)
        n = len(vertices)
        
        centroid_x = sum_x / n
        centroid_y = sum_y / n
        
        print(f"\n🎯 重心座標：({centroid_x:.4f}, {centroid_y:.4f})")
        
        # 詢問是否要新增重心點
        add_centroid = input("\n是否要將重心加入座標系統？(y/N): ").lower().strip()
        if add_centroid == 'y':
            centroid_name = input("請為重心命名：").strip()
            if centroid_name and not self.find_point(centroid_name):
                self.points.append((centroid_name, (centroid_x, centroid_y)))
                self.save_data()
                print(f"✅ 已新增重心：{centroid_name}")
            else:
                print("❌ 名稱無效或已存在！")
    
    def draw_coordinate_plot(self):
        """繪製座標圖"""
        if not self.points:
            print("\n❌ 沒有座標點可以繪製！")
            return
        
        print("\n🗺️ 座標圖")
        print("="*60)
        
        # 找出座標範圍
        x_coords = [point[1][0] for point in self.points]
        y_coords = [point[1][1] for point in self.points]
        
        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)
        
        # 擴展顯示範圍
        range_x = max_x - min_x if max_x != min_x else 2
        range_y = max_y - min_y if max_y != min_y else 2
        
        margin = 0.1
        plot_min_x = min_x - range_x * margin
        plot_max_x = max_x + range_x * margin
        plot_min_y = min_y - range_y * margin
        plot_max_y = max_y + range_y * margin
        
        print(f"座標範圍：X[{plot_min_x:.2f}, {plot_max_x:.2f}], Y[{plot_min_y:.2f}, {plot_max_y:.2f}]")
        
        # ASCII座標圖設定
        width, height = 50, 25
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # 繪製座標軸
        # 找到原點在網格中的位置
        origin_x = int((0 - plot_min_x) / (plot_max_x - plot_min_x) * (width - 1))
        origin_y = int((plot_max_y - 0) / (plot_max_y - plot_min_y) * (height - 1))
        
        # 如果原點在可視範圍內，繪製座標軸
        if 0 <= origin_x < width:
            for i in range(height):
                grid[i][origin_x] = '|'
        
        if 0 <= origin_y < height:
            for i in range(width):
                grid[origin_y][i] = '-'
        
        # 標記原點
        if 0 <= origin_x < width and 0 <= origin_y < height:
            grid[origin_y][origin_x] = '+'
        
        # 標記座標點
        for name, (x, y) in self.points:
            grid_x = int((x - plot_min_x) / (plot_max_x - plot_min_x) * (width - 1))
            grid_y = int((plot_max_y - y) / (plot_max_y - plot_min_y) * (height - 1))
            
            if 0 <= grid_x < width and 0 <= grid_y < height:
                grid[grid_y][grid_x] = name[0].upper()
        
        # 輸出網格
        print("\n座標圖：")
        print("+" + "-" * width + "+")
        for row in grid:
            print("|" + ''.join(row) + "|")
        print("+" + "-" * width + "+")
        
        # 圖例
        print(f"\n📝 圖例：")
        for name, (x, y) in self.points:
            symbol = name[0].upper()
            print(f"  {symbol} = {name}({x:.2f}, {y:.2f})")
        
        print(f"  | = Y軸, - = X軸, + = 原點")
    
    def export_data(self):
        """匯出資料"""
        if not self.points:
            print("\n❌ 沒有資料可以匯出！")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        txt_filename = f"coordinates_export_{timestamp}.txt"
        
        try:
            with open(txt_filename, 'w', encoding='utf-8') as f:
                f.write("📊 座標系統資料匯出\n")
                f.write("="*50 + "\n")
                f.write(f"匯出時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"座標點數量：{len(self.points)}\n\n")
                
                f.write("📍 座標點清單：\n")
                f.write("-" * 30 + "\n")
                for name, (x, y) in self.points:
                    quadrant = self.get_quadrant(x, y)
                    distance_origin = math.sqrt(x ** 2 + y ** 2)
                    f.write(f"名稱：{name}\n")
                    f.write(f"座標：({x:.4f}, {y:.4f})\n")
                    f.write(f"象限：{quadrant}\n")
                    f.write(f"距離原點：{distance_origin:.4f}\n")
                    f.write("\n")
                
                # 距離矩陣
                if len(self.points) > 1:
                    f.write("📏 距離矩陣：\n")
                    f.write("-" * 30 + "\n")
                    
                    names = [point[0] for point in self.points]
                    
                    # 表頭
                    f.write(f"{'':>10}")
                    for name in names:
                        f.write(f"{name:>10}")
                    f.write("\n")
                    
                    # 距離資料
                    for i, point1 in enumerate(self.points):
                        f.write(f"{names[i]:>10}")
                        for j, point2 in enumerate(self.points):
                            if i == j:
                                f.write(f"{'0.0000':>10}")
                            else:
                                distance = self.calculate_distance(point1, point2)
                                f.write(f"{distance:>10.4f}")
                        f.write("\n")
            
            print(f"✅ 資料已匯出至：{txt_filename}")
            
        except Exception as e:
            print(f"❌ 匯出失敗：{e}")
    
    def run(self):
        """執行主程式"""
        self.display_header()
        print("🎉 歡迎使用2D座標系統管理程式！")
        
        while True:
            self.display_menu()
            choice = input("\n請選擇功能 (0-9): ").strip()
            
            try:
                if choice == "1":
                    self.view_all_points()
                elif choice == "2":
                    self.add_point()
                elif choice == "3":
                    self.modify_point()
                elif choice == "4":
                    self.delete_point()
                elif choice == "5":
                    self.calculate_distances()
                elif choice == "6":
                    self.calculate_midpoint()
                elif choice == "7":
                    self.geometric_analysis()
                elif choice == "8":
                    self.draw_coordinate_plot()
                elif choice == "9":
                    self.export_data()
                elif choice == "0":
                    self.save_data()
                    print("\n👋 感謝使用座標系統程式！")
                    print("💾 資料已自動儲存")
                    break
                else:
                    print("❌ 無效選擇，請輸入0-9！")
                
                input("\n按Enter鍵繼續...")
                
            except KeyboardInterrupt:
                print("\n\n⚠️ 操作被中斷")
                continue
            except Exception as e:
                print(f"\n❌ 發生錯誤：{e}")
                continue

# 執行程式
if __name__ == "__main__":
    system = CoordinateSystem()
    try:
        system.run()
    except KeyboardInterrupt:
        print("\n\n👋 程式被中斷，資料已儲存！")
        system.save_data()