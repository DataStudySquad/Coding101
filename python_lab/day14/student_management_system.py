# 學生管理系統 - Day 14主要項目
# 整合第二週所有學習內容的綜合實作項目

import json
import os
from datetime import datetime
import statistics
import math

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.classes = {}
        self.subjects = ["國文", "英文", "數學", "自然", "社會"]
        self.data_file = "student_data.json"
        self.load_data()
    
    def save_data(self):
        """儲存資料到檔案"""
        try:
            data = {
                "students": self.students,
                "classes": self.classes,
                "subjects": self.subjects,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ 儲存失敗：{e}")
    
    def load_data(self):
        """從檔案載入資料"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.students = data.get("students", [])
                    self.classes = data.get("classes", {})
                    self.subjects = data.get("subjects", self.subjects)
                    print(f"✅ 成功載入 {len(self.students)} 位學生的資料")
            else:
                self.initialize_sample_data()
        except Exception as e:
            print(f"⚠️ 載入失敗：{e}")
            self.initialize_sample_data()
    
    def initialize_sample_data(self):
        """初始化範例資料"""
        print("🔧 初始化範例資料...")
        
        # 範例學生資料
        sample_students = [
            {
                "student_id": "S001",
                "name": "張小明",
                "age": 16,
                "gender": "男",
                "class": "一年一班",
                "contact": {
                    "phone": "0912-345-678",
                    "email": "xiaoming@school.edu",
                    "address": "台北市信義區忠孝東路123號"
                },
                "grades": {
                    "國文": [85, 88, 92, 87, 90],
                    "英文": [78, 82, 85, 80, 84],
                    "數學": [92, 88, 95, 89, 93],
                    "自然": [79, 83, 87, 85, 88],
                    "社會": [91, 89, 93, 87, 92]
                },
                "activities": ["籃球社", "學生會"],
                "join_date": "2024-09-01"
            },
            {
                "student_id": "S002", 
                "name": "李小美",
                "age": 16,
                "gender": "女",
                "class": "一年一班",
                "contact": {
                    "phone": "0987-654-321",
                    "email": "xiaomei@school.edu",
                    "address": "台北市大安區敦化南路456號"
                },
                "grades": {
                    "國文": [92, 88, 91, 94, 89],
                    "英文": [85, 89, 87, 91, 88],
                    "數學": [78, 82, 80, 85, 83],
                    "自然": [88, 91, 85, 89, 87],
                    "社會": [94, 90, 92, 88, 91]
                },
                "activities": ["合唱團", "志工社"],
                "join_date": "2024-09-01"
            },
            {
                "student_id": "S003",
                "name": "王小華",
                "age": 17,
                "gender": "男", 
                "class": "一年二班",
                "contact": {
                    "phone": "0923-456-789",
                    "email": "xiaohua@school.edu",
                    "address": "台北市中山區中山北路789號"
                },
                "grades": {
                    "國文": [79, 83, 86, 82, 85],
                    "英文": [85, 88, 82, 87, 84],
                    "數學": [88, 85, 91, 86, 89],
                    "自然": [92, 89, 94, 90, 93],
                    "社會": [81, 84, 87, 85, 88]
                },
                "activities": ["資訊社", "辯論社"],
                "join_date": "2024-09-01"
            },
            {
                "student_id": "S004",
                "name": "陳小雅",
                "age": 16,
                "gender": "女",
                "class": "一年二班",
                "contact": {
                    "phone": "0934-567-890",
                    "email": "xiaoya@school.edu", 
                    "address": "台北市松山區松山路321號"
                },
                "grades": {
                    "國文": [88, 92, 87, 90, 89],
                    "英文": [91, 88, 93, 89, 92],
                    "數學": [85, 89, 82, 88, 86],
                    "自然": [87, 84, 89, 85, 88],
                    "社會": [93, 90, 94, 91, 92]
                },
                "activities": ["美術社"],
                "join_date": "2024-09-01"
            },
            {
                "student_id": "S005",
                "name": "林小強",
                "age": 17,
                "gender": "男",
                "class": "二年一班",
                "contact": {
                    "phone": "0945-678-901",
                    "email": "xiaoqiang@school.edu",
                    "address": "台北市內湖區內湖路654號"
                },
                "grades": {
                    "國文": [86, 89, 84, 87, 88],
                    "英文": [88, 85, 91, 87, 89],
                    "數學": [94, 91, 96, 92, 95],
                    "自然": [89, 92, 88, 91, 90],
                    "社會": [85, 88, 86, 89, 87]
                },
                "activities": ["足球社", "攝影社"],
                "join_date": "2023-09-01"
            }
        ]
        
        self.students = sample_students
        
        # 範例班級資料
        self.classes = {
            "一年一班": {
                "class_id": "C001",
                "teacher": "王老師",
                "room": "A101",
                "student_count": 2,
                "subjects": self.subjects
            },
            "一年二班": {
                "class_id": "C002",
                "teacher": "李老師",
                "room": "A102",
                "student_count": 2,
                "subjects": self.subjects
            },
            "二年一班": {
                "class_id": "C003",
                "teacher": "張老師",
                "room": "B201",
                "student_count": 1,
                "subjects": self.subjects
            }
        }
        
        self.save_data()
        print("✅ 範例資料初始化完成")
    
    def display_header(self):
        """顯示系統標題"""
        print("\n" + "="*70)
        print("🎓              學生管理系統 v2.0              🎓")
        print("="*70)
        print(f"📅 當前時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"👥 學生總數：{len(self.students)}")
        print(f"🏫 班級數量：{len(self.classes)}")
        
        if self.students:
            # 快速統計
            total_grades = []
            for student in self.students:
                for subject_grades in student['grades'].values():
                    total_grades.extend(subject_grades)
            
            if total_grades:
                avg_grade = sum(total_grades) / len(total_grades)
                print(f"📊 整體平均：{avg_grade:.1f}分")
    
    def display_main_menu(self):
        """顯示主選單"""
        print("\n" + "─"*50)
        print("🏠 主選單")
        print("─"*50)
        print("1. 👤 學生資料管理")
        print("2. 📊 成績管理")
        print("3. 🏫 班級管理")
        print("4. 📈 資料分析")
        print("5. 🔍 搜尋與篩選")
        print("6. 📋 報表與統計")
        print("7. 💾 資料管理")
        print("8. ⚙️  系統設定")
        print("0. 🚪 離開系統")
        print("─"*50)
    
    # ===== 學生資料管理 =====
    def student_management_menu(self):
        """學生資料管理選單"""
        while True:
            print("\n" + "─"*40)
            print("👤 學生資料管理")
            print("─"*40)
            print("1. 📋 查看所有學生")
            print("2. ➕ 新增學生")
            print("3. 📝 修改學生資料")
            print("4. ❌ 刪除學生")
            print("5. 👁️  學生詳細資料")
            print("6. 📊 學生排名")
            print("0. 🔙 回到主選單")
            
            choice = input("\n請選擇功能: ").strip()
            
            if choice == "1":
                self.view_all_students()
            elif choice == "2":
                self.add_student()
            elif choice == "3":
                self.modify_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.view_student_details()
            elif choice == "6":
                self.student_ranking()
            elif choice == "0":
                break
            else:
                print("❌ 無效選擇！")
            
            if choice != "0":
                input("\n按Enter繼續...")
    
    def view_all_students(self):
        """查看所有學生"""
        if not self.students:
            print("\n❌ 目前沒有學生資料！")
            return
        
        # 排序選項
        print("📊 排序方式：")
        print("1. 按學號")
        print("2. 按姓名")
        print("3. 按班級")
        print("4. 按平均成績")
        
        sort_choice = input("請選擇排序方式 (1-4, 預設按學號): ").strip()
        
        # 排序學生清單
        if sort_choice == "2":
            sorted_students = sorted(self.students, key=lambda x: x["name"])
        elif sort_choice == "3":
            sorted_students = sorted(self.students, key=lambda x: x["class"])
        elif sort_choice == "4":
            sorted_students = sorted(self.students, 
                                  key=lambda x: self.calculate_student_average(x), 
                                  reverse=True)
        else:
            sorted_students = sorted(self.students, key=lambda x: x["student_id"])
        
        print(f"\n👥 學生清單（共{len(sorted_students)}人）")
        print("="*90)
        print(f"{'學號':<8} {'姓名':<10} {'年齡':<4} {'性別':<4} {'班級':<12} {'平均成績':<8} {'社團':<15}")
        print("-" * 90)
        
        for student in sorted_students:
            avg_grade = self.calculate_student_average(student)
            activities = ", ".join(student.get("activities", []))
            if len(activities) > 12:
                activities = activities[:12] + "..."
            
            print(f"{student['student_id']:<8} {student['name']:<10} "
                  f"{student['age']:<4} {student['gender']:<4} "
                  f"{student['class']:<12} {avg_grade:<8.1f} {activities:<15}")
    
    def calculate_student_average(self, student):
        """計算學生平均成績"""
        all_grades = []
        for subject_grades in student.get('grades', {}).values():
            if subject_grades:
                all_grades.extend(subject_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def add_student(self):
        """新增學生"""
        print("\n➕ 新增學生")
        print("─"*20)
        
        # 生成學號
        existing_ids = [s['student_id'] for s in self.students]
        next_num = 1
        while f"S{next_num:03d}" in existing_ids:
            next_num += 1
        student_id = f"S{next_num:03d}"
        
        print(f"🆔 學號：{student_id}")
        
        # 輸入基本資料
        name = input("👤 姓名：").strip()
        if not name:
            print("❌ 姓名不能為空！")
            return
        
        # 檢查重複姓名
        if any(s['name'] == name for s in self.students):
            confirm = input(f"⚠️ 已有同名學生，確定要新增嗎？(y/N): ")
            if confirm.lower() != 'y':
                print("❌ 取消新增")
                return
        
        try:
            age = int(input("🎂 年齡："))
            if not 10 <= age <= 25:
                print("❌ 年齡必須在10-25之間！")
                return
        except ValueError:
            print("❌ 請輸入有效年齡！")
            return
        
        gender = input("⚥ 性別（男/女）：").strip()
        if gender not in ["男", "女"]:
            print("❌ 性別必須是'男'或'女'！")
            return
        
        # 選擇班級
        print("\n🏫 可選班級：")
        for i, class_name in enumerate(self.classes.keys(), 1):
            print(f"  {i}. {class_name}")
        print(f"  {len(self.classes)+1}. 新建班級")
        
        try:
            class_choice = int(input("請選擇班級: "))
            class_names = list(self.classes.keys())
            
            if 1 <= class_choice <= len(class_names):
                class_name = class_names[class_choice - 1]
            elif class_choice == len(class_names) + 1:
                class_name = self.create_new_class()
                if not class_name:
                    print("❌ 取消新增學生")
                    return
            else:
                print("❌ 無效選擇！")
                return
        except ValueError:
            print("❌ 請輸入有效數字！")
            return
        
        # 聯絡資訊
        print("\n📞 聯絡資訊（可選填）：")
        phone = input("電話：").strip()
        email = input("Email：").strip()
        address = input("地址：").strip()
        
        # 社團活動
        print("\n🎭 社團活動（用逗號分隔，可選填）：")
        activities_input = input("社團：").strip()
        activities = [activity.strip() for activity in activities_input.split(",") if activity.strip()]
        
        # 建立學生資料
        new_student = {
            "student_id": student_id,
            "name": name,
            "age": age,
            "gender": gender,
            "class": class_name,
            "contact": {
                "phone": phone,
                "email": email,
                "address": address
            },
            "grades": {subject: [] for subject in self.subjects},
            "activities": activities,
            "join_date": datetime.now().strftime("%Y-%m-%d")
        }
        
        self.students.append(new_student)
        
        # 更新班級人數
        self.update_class_student_count(class_name)
        
        self.save_data()
        print(f"✅ 成功新增學生：{name}（學號：{student_id}）")
        
        # 詢問是否立即新增成績
        add_grades = input("\n是否立即新增成績？(y/N): ")
        if add_grades.lower() == 'y':
            self.add_student_grades(student_id)
    
    def create_new_class(self):
        """建立新班級"""
        print("\n🏫 建立新班級")
        print("─"*15)
        
        class_name = input("班級名稱：").strip()
        if not class_name:
            print("❌ 班級名稱不能為空！")
            return None
        
        if class_name in self.classes:
            print("❌ 班級名稱已存在！")
            return None
        
        teacher = input("導師姓名：").strip() or "未設定"
        room = input("教室：").strip() or "未設定"
        
        # 生成班級ID
        class_ids = [info.get('class_id', '') for info in self.classes.values()]
        next_num = 1
        while f"C{next_num:03d}" in class_ids:
            next_num += 1
        class_id = f"C{next_num:03d}"
        
        self.classes[class_name] = {
            "class_id": class_id,
            "teacher": teacher,
            "room": room,
            "student_count": 0,
            "subjects": self.subjects.copy()
        }
        
        print(f"✅ 成功建立班級：{class_name}")
        return class_name
    
    def update_class_student_count(self, class_name):
        """更新班級學生人數"""
        if class_name in self.classes:
            count = len([s for s in self.students if s["class"] == class_name])
            self.classes[class_name]["student_count"] = count
    
    def view_student_details(self):
        """查看學生詳細資料"""
        if not self.students:
            print("\n❌ 目前沒有學生資料！")
            return
        
        # 顯示學生清單供選擇
        print("\n👥 學生清單：")
        for i, student in enumerate(self.students, 1):
            print(f"{i:2d}. {student['student_id']} - {student['name']} ({student['class']})")
        
        try:
            choice = int(input("\n請選擇學生編號: "))
            if 1 <= choice <= len(self.students):
                student = self.students[choice - 1]
                self.display_student_detail(student)
            else:
                print("❌ 無效選擇！")
        except ValueError:
            print("❌ 請輸入有效數字！")
    
    def display_student_detail(self, student):
        """顯示單一學生詳細資料"""
        print(f"\n👤 {student['name']} 的詳細資料")
        print("="*50)
        
        # 基本資料
        print(f"🆔 學號：{student['student_id']}")
        print(f"👤 姓名：{student['name']}")
        print(f"🎂 年齡：{student['age']}歲")
        print(f"⚥ 性別：{student['gender']}")
        print(f"🏫 班級：{student['class']}")
        print(f"📅 入學日期：{student.get('join_date', '未記錄')}")
        
        # 聯絡資訊
        contact = student.get('contact', {})
        print(f"\n📞 聯絡資訊：")
        print(f"  電話：{contact.get('phone', '未提供')}")
        print(f"  Email：{contact.get('email', '未提供')}")
        print(f"  地址：{contact.get('address', '未提供')}")
        
        # 社團活動
        activities = student.get('activities', [])
        print(f"\n🎭 社團活動：")
        if activities:
            for activity in activities:
                print(f"  • {activity}")
        else:
            print("  未參加任何社團")
        
        # 成績資料
        grades = student.get('grades', {})
        print(f"\n📊 成績資料：")
        if any(grades.values()):
            total_score = 0
            total_count = 0
            
            for subject in self.subjects:
                subject_grades = grades.get(subject, [])
                if subject_grades:
                    avg = sum(subject_grades) / len(subject_grades)
                    print(f"  {subject}：{subject_grades} (平均：{avg:.1f})")
                    total_score += avg
                    total_count += 1
                else:
                    print(f"  {subject}：無成績記錄")
            
            if total_count > 0:
                overall_avg = total_score / total_count
                print(f"\n  📈 總平均：{overall_avg:.1f}分")
        else:
            print("  尚無成績記錄")
    
    # ===== 成績管理 =====
    def grade_management_menu(self):
        """成績管理選單"""
        while True:
            print("\n" + "─"*40)
            print("📊 成績管理")
            print("─"*40)
            print("1. ➕ 新增成績")
            print("2. 📋 查看成績")
            print("3. 📝 修改成績")
            print("4. ❌ 刪除成績")
            print("5. 📈 成績統計")
            print("6. 🏆 成績排名")
            print("0. 🔙 回到主選單")
            
            choice = input("\n請選擇功能: ").strip()
            
            if choice == "1":
                self.add_grades_menu()
            elif choice == "2":
                self.view_grades()
            elif choice == "3":
                self.modify_grades()
            elif choice == "4":
                self.delete_grades()
            elif choice == "5":
                self.grade_statistics()
            elif choice == "6":
                self.grade_ranking()
            elif choice == "0":
                break
            else:
                print("❌ 無效選擇！")
            
            if choice != "0":
                input("\n按Enter繼續...")
    
    def add_grades_menu(self):
        """新增成績選單"""
        if not self.students:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n➕ 新增成績")
        print("─"*15)
        print("1. 為單一學生新增成績")
        print("2. 為整個班級新增成績")
        print("3. 批量匯入成績")
        
        choice = input("\n請選擇方式 (1-3): ").strip()
        
        if choice == "1":
            self.add_single_student_grade()
        elif choice == "2":
            self.add_class_grades()
        elif choice == "3":
            self.batch_import_grades()
        else:
            print("❌ 無效選擇！")
    
    def add_single_student_grade(self):
        """為單一學生新增成績"""
        # 選擇學生
        print("\n👥 學生清單：")
        for i, student in enumerate(self.students, 1):
            avg = self.calculate_student_average(student)
            print(f"{i:2d}. {student['student_id']} - {student['name']} (平均:{avg:.1f})")
        
        try:
            choice = int(input("\n請選擇學生: "))
            if 1 <= choice <= len(self.students):
                student = self.students[choice - 1]
                self.add_student_grades(student['student_id'])
            else:
                print("❌ 無效選擇！")
        except ValueError:
            print("❌ 請輸入有效數字！")
    
    def add_student_grades(self, student_id):
        """新增特定學生的成績"""
        student = self.find_student_by_id(student_id)
        if not student:
            print("❌ 找不到該學生！")
            return
        
        print(f"\n📊 為 {student['name']} 新增成績")
        print("─"*30)
        
        # 選擇科目
        print("📚 可選科目：")
        for i, subject in enumerate(self.subjects, 1):
            current_grades = student['grades'].get(subject, [])
            avg = sum(current_grades) / len(current_grades) if current_grades else 0
            print(f"{i}. {subject} (目前平均: {avg:.1f})")
        
        try:
            subject_choice = int(input("請選擇科目: "))
            if 1 <= subject_choice <= len(self.subjects):
                subject = self.subjects[subject_choice - 1]
            else:
                print("❌ 無效選擇！")
                return
        except ValueError:
            print("❌ 請輸入有效數字！")
            return
        
        # 輸入成績
        try:
            score = float(input(f"請輸入{subject}成績 (0-100): "))
            if 0 <= score <= 100:
                student['grades'][subject].append(score)
                self.save_data()
                print(f"✅ 成功新增 {student['name']} 的{subject}成績：{score}分")
            else:
                print("❌ 成績必須在0-100之間！")
        except ValueError:
            print("❌ 請輸入有效成績！")
    
    def find_student_by_id(self, student_id):
        """根據學號查找學生"""
        for student in self.students:
            if student['student_id'] == student_id:
                return student
        return None
    
    # ===== 資料分析 =====
    def data_analysis_menu(self):
        """資料分析選單"""
        while True:
            print("\n" + "─"*40)
            print("📈 資料分析")
            print("─"*40)
            print("1. 📊 整體統計")
            print("2. 🏫 班級分析")
            print("3. 📚 科目分析") 
            print("4. 👥 性別分析")
            print("5. 🎭 社團分析")
            print("6. 📈 成績趨勢")
            print("0. 🔙 回到主選單")
            
            choice = input("\n請選擇功能: ").strip()
            
            if choice == "1":
                self.overall_statistics()
            elif choice == "2":
                self.class_analysis()
            elif choice == "3":
                self.subject_analysis()
            elif choice == "4":
                self.gender_analysis()
            elif choice == "5":
                self.activity_analysis()
            elif choice == "6":
                self.grade_trend_analysis()
            elif choice == "0":
                break
            else:
                print("❌ 無效選擇！")
            
            if choice != "0":
                input("\n按Enter繼續...")
    
    def overall_statistics(self):
        """整體統計"""
        if not self.students:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n📊 整體統計分析")
        print("="*50)
        
        # 基本統計
        total_students = len(self.students)
        total_classes = len(self.classes)
        
        print(f"👥 學生總數：{total_students}")
        print(f"🏫 班級總數：{total_classes}")
        print(f"📚 科目總數：{len(self.subjects)}")
        
        # 年齡統計
        ages = [student['age'] for student in self.students]
        print(f"\n🎂 年齡統計：")
        print(f"  平均年齡：{sum(ages) / len(ages):.1f}歲")
        print(f"  最大年齡：{max(ages)}歲")
        print(f"  最小年齡：{min(ages)}歲")
        
        # 性別統計
        gender_count = {}
        for student in self.students:
            gender = student['gender']
            gender_count[gender] = gender_count.get(gender, 0) + 1
        
        print(f"\n⚥ 性別分布：")
        for gender, count in gender_count.items():
            percentage = (count / total_students) * 100
            print(f"  {gender}：{count}人 ({percentage:.1f}%)")
        
        # 成績統計
        all_grades = []
        grade_counts = {}
        
        for student in self.students:
            for subject_grades in student['grades'].values():
                all_grades.extend(subject_grades)
                for grade in subject_grades:
                    grade_counts[self.get_grade_level(grade)] = grade_counts.get(self.get_grade_level(grade), 0) + 1
        
        if all_grades:
            print(f"\n📈 成績統計：")
            print(f"  總成績筆數：{len(all_grades)}")
            print(f"  平均成績：{sum(all_grades) / len(all_grades):.1f}")
            print(f"  最高成績：{max(all_grades):.1f}")
            print(f"  最低成績：{min(all_grades):.1f}")
            print(f"  標準差：{statistics.stdev(all_grades):.1f}")
            
            print(f"\n🏆 等第分布：")
            total_grade_records = sum(grade_counts.values())
            for level in ["優秀", "良好", "普通", "待加強"]:
                count = grade_counts.get(level, 0)
                if total_grade_records > 0:
                    percentage = (count / total_grade_records) * 100
                    print(f"  {level}：{count}筆 ({percentage:.1f}%)")
        
        # 社團參與統計
        all_activities = []
        for student in self.students:
            all_activities.extend(student.get('activities', []))
        
        if all_activities:
            activity_count = {}
            for activity in all_activities:
                activity_count[activity] = activity_count.get(activity, 0) + 1
            
            print(f"\n🎭 社團參與統計：")
            print(f"  參與社團總人次：{len(all_activities)}")
            print(f"  平均每人參與：{len(all_activities) / total_students:.1f}個社團")
            
            # 最熱門社團
            popular_activities = sorted(activity_count.items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  熱門社團：")
            for activity, count in popular_activities:
                print(f"    {activity}：{count}人")
    
    def get_grade_level(self, grade):
        """根據分數判斷等第"""
        if grade >= 90:
            return "優秀"
        elif grade >= 80:
            return "良好"
        elif grade >= 60:
            return "普通"
        else:
            return "待加強"
    
    def subject_analysis(self):
        """科目分析"""
        if not self.students:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n📚 科目分析")
        print("="*60)
        
        print(f"{'科目':<8} {'人數':<6} {'平均':<8} {'最高':<8} {'最低':<8} {'標準差':<8}")
        print("-" * 60)
        
        for subject in self.subjects:
            # 收集該科目所有成績
            subject_grades = []
            student_count = 0
            
            for student in self.students:
                grades = student['grades'].get(subject, [])
                if grades:
                    subject_grades.extend(grades)
                    student_count += 1
            
            if subject_grades:
                avg = sum(subject_grades) / len(subject_grades)
                max_grade = max(subject_grades)
                min_grade = min(subject_grades)
                std_dev = statistics.stdev(subject_grades) if len(subject_grades) > 1 else 0
                
                print(f"{subject:<8} {student_count:<6} {avg:<8.1f} {max_grade:<8.1f} {min_grade:<8.1f} {std_dev:<8.1f}")
            else:
                print(f"{subject:<8} {'0':<6} {'N/A':<8} {'N/A':<8} {'N/A':<8} {'N/A':<8}")
        
        # 科目難易度排行
        subject_averages = []
        for subject in self.subjects:
            subject_grades = []
            for student in self.students:
                subject_grades.extend(student['grades'].get(subject, []))
            
            if subject_grades:
                avg = sum(subject_grades) / len(subject_grades)
                subject_averages.append((subject, avg))
        
        if subject_averages:
            subject_averages.sort(key=lambda x: x[1], reverse=True)
            
            print(f"\n📊 科目難易度排行（平均分高到低）：")
            for i, (subject, avg) in enumerate(subject_averages, 1):
                print(f"{i}. {subject}：{avg:.1f}分")
    
    # ===== 搜尋功能 =====
    def search_menu(self):
        """搜尋功能選單"""
        while True:
            print("\n" + "─"*40)
            print("🔍 搜尋與篩選")
            print("─"*40)
            print("1. 🔎 按姓名搜尋")
            print("2. 🆔 按學號搜尋")
            print("3. 🏫 按班級篩選")
            print("4. 📊 按成績範圍篩選")
            print("5. 🎭 按社團篩選")
            print("6. 🔍 綜合搜尋")
            print("0. 🔙 回到主選單")
            
            choice = input("\n請選擇功能: ").strip()
            
            if choice == "1":
                self.search_by_name()
            elif choice == "2":
                self.search_by_id()
            elif choice == "3":
                self.filter_by_class()
            elif choice == "4":
                self.filter_by_grade()
            elif choice == "5":
                self.filter_by_activity()
            elif choice == "6":
                self.comprehensive_search()
            elif choice == "0":
                break
            else:
                print("❌ 無效選擇！")
            
            if choice != "0":
                input("\n按Enter繼續...")
    
    def search_by_name(self):
        """按姓名搜尋"""
        if not self.students:
            print("\n❌ 目前沒有學生資料！")
            return
        
        keyword = input("\n🔎 請輸入姓名關鍵字: ").strip()
        if not keyword:
            print("❌ 關鍵字不能為空！")
            return
        
        # 搜尋匹配的學生
        matches = []
        for student in self.students:
            if keyword.lower() in student['name'].lower():
                matches.append(student)
        
        if matches:
            print(f"\n🔍 找到 {len(matches)} 個符合的結果：")
            print("-" * 50)
            for student in matches:
                avg = self.calculate_student_average(student)
                print(f"👤 {student['name']} ({student['student_id']})")
                print(f"   班級：{student['class']} | 平均成績：{avg:.1f}")
        else:
            print(f"\n❌ 沒有找到包含「{keyword}」的學生")
    
    def filter_by_class(self):
        """按班級篩選"""
        if not self.students:
            print("\n❌ 目前沒有學生資料！")
            return
        
        # 顯示可選班級
        print("\n🏫 可選班級：")
        class_names = list(set(student['class'] for student in self.students))
        for i, class_name in enumerate(sorted(class_names), 1):
            count = len([s for s in self.students if s['class'] == class_name])
            print(f"{i}. {class_name} ({count}人)")
        
        try:
            choice = int(input("請選擇班級: "))
            if 1 <= choice <= len(class_names):
                selected_class = sorted(class_names)[choice - 1]
                
                # 篩選該班級學生
                class_students = [s for s in self.students if s['class'] == selected_class]
                
                print(f"\n🏫 {selected_class} 學生清單：")
                print("-" * 50)
                for student in class_students:
                    avg = self.calculate_student_average(student)
                    activities = ", ".join(student.get('activities', []))
                    print(f"👤 {student['name']} ({student['student_id']})")
                    print(f"   平均成績：{avg:.1f} | 社團：{activities if activities else '無'}")
            else:
                print("❌ 無效選擇！")
        except ValueError:
            print("❌ 請輸入有效數字！")
    
    # ===== 系統功能 =====
    def system_settings_menu(self):
        """系統設定選單"""
        while True:
            print("\n" + "─"*40)
            print("⚙️ 系統設定")
            print("─"*40)
            print("1. 📚 管理科目")
            print("2. 🏫 管理班級")
            print("3. 💾 資料備份")
            print("4. 📥 資料還原")
            print("5. 🗑️ 清除資料")
            print("6. ℹ️ 系統資訊")
            print("0. 🔙 回到主選單")
            
            choice = input("\n請選擇功能: ").strip()
            
            if choice == "1":
                self.manage_subjects()
            elif choice == "2":
                self.manage_classes()
            elif choice == "3":
                self.backup_data()
            elif choice == "4":
                self.restore_data()
            elif choice == "5":
                self.clear_data()
            elif choice == "6":
                self.system_info()
            elif choice == "0":
                break
            else:
                print("❌ 無效選擇！")
            
            if choice != "0":
                input("\n按Enter繼續...")
    
    def backup_data(self):
        """資料備份"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_student_data_{timestamp}.json"
        
        try:
            data = {
                "students": self.students,
                "classes": self.classes,
                "subjects": self.subjects,
                "backup_time": datetime.now().isoformat(),
                "version": "2.0"
            }
            
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"✅ 資料已備份至：{backup_file}")
            print(f"📊 備份內容：{len(self.students)}位學生，{len(self.classes)}個班級")
            
        except Exception as e:
            print(f"❌ 備份失敗：{e}")
    
    def system_info(self):
        """系統資訊"""
        print("\nℹ️ 系統資訊")
        print("="*40)
        print("🎓 學生管理系統 v2.0")
        print("👨‍💻 開發者：Python學習者")
        print(f"📅 版本日期：2024-01-01")
        print(f"🐍 Python版本：{self.get_python_version()}")
        
        # 資料統計
        print(f"\n📊 資料統計：")
        print(f"  學生數量：{len(self.students)}")
        print(f"  班級數量：{len(self.classes)}")
        print(f"  科目數量：{len(self.subjects)}")
        
        # 檔案資訊
        if os.path.exists(self.data_file):
            file_size = os.path.getsize(self.data_file)
            file_modified = datetime.fromtimestamp(os.path.getmtime(self.data_file))
            print(f"  資料檔案大小：{file_size}字節")
            print(f"  最後修改時間：{file_modified.strftime('%Y-%m-%d %H:%M:%S')}")
        
        print(f"\n🚀 功能特色：")
        features = [
            "學生資料管理", "成績管理", "班級管理", "資料分析",
            "搜尋篩選", "統計報表", "資料備份", "批量操作"
        ]
        for i, feature in enumerate(features, 1):
            print(f"  {i}. {feature}")
    
    def get_python_version(self):
        """取得Python版本"""
        import sys
        return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    
    def run(self):
        """執行主程式"""
        try:
            self.display_header()
            print("🎉 歡迎使用學生管理系統 v2.0！")
            
            while True:
                self.display_main_menu()
                choice = input("\n請選擇功能: ").strip()
                
                if choice == "1":
                    self.student_management_menu()
                elif choice == "2":
                    self.grade_management_menu()
                elif choice == "3":
                    self.class_management_menu()
                elif choice == "4":
                    self.data_analysis_menu()
                elif choice == "5":
                    self.search_menu()
                elif choice == "6":
                    self.report_menu()
                elif choice == "7":
                    self.data_management_menu()
                elif choice == "8":
                    self.system_settings_menu()
                elif choice == "0":
                    self.save_data()
                    print("\n👋 感謝使用學生管理系統！")
                    print("💾 資料已自動儲存")
                    print("🎓 祝您學習愉快！")
                    break
                else:
                    print("❌ 無效選擇，請重新輸入！")
                
        except KeyboardInterrupt:
            print("\n\n⚠️ 程式被中斷")
            self.save_data()
            print("💾 資料已儲存，感謝使用！")
        except Exception as e:
            print(f"\n❌ 系統錯誤：{e}")
            self.save_data()
            print("💾 資料已儲存")
    
    # 佔位符方法（為完整性而添加）
    def class_management_menu(self):
        print("🏫 班級管理功能開發中...")
    
    def report_menu(self):
        print("📋 報表功能開發中...")
    
    def data_management_menu(self):
        print("💾 資料管理功能開發中...")

# 程式入口點
if __name__ == "__main__":
    print("🚀 啟動學生管理系統...")
    system = StudentManagementSystem()
    system.run()