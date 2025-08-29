# 通訊錄管理程式 - Day 12主要項目
# 完整的聯絡人管理系統

import json
import os
from datetime import datetime, date
import re

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.data_file = "contacts.json"
        self.categories = ["朋友", "家人", "同事", "同學", "其他"]
        self.load_data()
    
    def save_data(self):
        """儲存聯絡人資料"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.contacts, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ 儲存失敗：{e}")
    
    def load_data(self):
        """載入聯絡人資料"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.contacts = json.load(f)
        except Exception as e:
            print(f"⚠️ 載入失敗：{e}")
            self.load_sample_data()
    
    def load_sample_data(self):
        """載入示例資料"""
        self.contacts = {
            "小明": {
                "電話": "0912-345-678",
                "email": "xiaoming@example.com",
                "地址": "台北市信義區忠孝東路123號",
                "生日": "1990-05-15",
                "分類": "朋友",
                "公司": "ABC科技",
                "備註": "大學同學，現在在科技業工作"
            },
            "小美": {
                "電話": "0987-654-321",
                "email": "xiaomei@example.com", 
                "地址": "台中市西區美村路456號",
                "生日": "1992-08-20",
                "分類": "同事",
                "公司": "XYZ設計",
                "備註": "設計部門同事"
            },
            "媽媽": {
                "電話": "0920-111-222",
                "email": "mom@family.com",
                "地址": "高雄市左營區中華路789號",
                "生日": "1965-12-03",
                "分類": "家人",
                "公司": "",
                "備註": "最愛的媽媽"
            }
        }
    
    def display_header(self):
        """顯示程式標題"""
        print("\n" + "="*60)
        print("📞              通訊錄管理系統              📞")
        print("="*60)
        print(f"📅 當前時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"👥 聯絡人數量：{len(self.contacts)}")
        
        if self.contacts:
            categories_count = {}
            for contact in self.contacts.values():
                cat = contact.get("分類", "其他")
                categories_count[cat] = categories_count.get(cat, 0) + 1
            
            print("📊 分類統計：", end="")
            for cat, count in categories_count.items():
                print(f" {cat}({count})", end="")
            print()
    
    def display_menu(self):
        """顯示主選單"""
        print("\n" + "─"*40)
        print("🏠 主選單")
        print("─"*40)
        print("1. 📋 查看所有聯絡人")
        print("2. ➕ 新增聯絡人")
        print("3. 🔍 搜尋聯絡人")
        print("4. 📝 修改聯絡人")
        print("5. ❌ 刪除聯絡人")
        print("6. 📊 統計分析")
        print("7. 🎂 生日提醒")
        print("8. 📤 匯出資料")
        print("9. 📥 匯入資料")
        print("0. 🚪 離開系統")
        print("─"*40)
    
    def validate_phone(self, phone):
        """驗證電話號碼格式"""
        pattern = r'^09\d{2}-\d{3}-\d{3}$'
        return re.match(pattern, phone) is not None
    
    def validate_email(self, email):
        """驗證email格式"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_birthday(self, birthday):
        """驗證生日格式"""
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    def view_all_contacts(self):
        """查看所有聯絡人"""
        if not self.contacts:
            print("\n❌ 通訊錄是空的！")
            return
        
        print(f"\n📋 通訊錄 - 共{len(self.contacts)}位聯絡人")
        print("="*80)
        
        # 按分類排序
        sorted_contacts = sorted(self.contacts.items(), 
                               key=lambda x: (x[1].get("分類", "其他"), x[0]))
        
        current_category = ""
        for name, info in sorted_contacts:
            category = info.get("分類", "其他")
            
            if category != current_category:
                if current_category:
                    print()  # 分類間空行
                print(f"\n【{category}】")
                print("-" * 40)
                current_category = category
            
            print(f"👤 {name}")
            print(f"   📞 {info.get('電話', '未提供')}")
            print(f"   📧 {info.get('email', '未提供')}")
            print(f"   🏠 {info.get('地址', '未提供')}")
            print(f"   🎂 {info.get('生日', '未提供')}")
            
            if info.get('公司'):
                print(f"   🏢 {info['公司']}")
            
            if info.get('備註'):
                print(f"   📝 {info['備註']}")
            print()
    
    def add_contact(self):
        """新增聯絡人"""
        print("\n➕ 新增聯絡人")
        print("─"*30)
        
        # 姓名（必填）
        while True:
            name = input("👤 姓名：").strip()
            if not name:
                print("❌ 姓名不能為空！")
                continue
            if name in self.contacts:
                print("❌ 此聯絡人已存在！")
                continue
            break
        
        # 電話（必填，有格式驗證）
        while True:
            phone = input("📞 電話（格式：09XX-XXX-XXX）：").strip()
            if not phone:
                print("❌ 電話不能為空！")
                continue
            if not self.validate_phone(phone):
                print("❌ 電話格式錯誤！請使用：09XX-XXX-XXX")
                continue
            break
        
        # Email（選填，有格式驗證）
        while True:
            email = input("📧 Email（選填）：").strip()
            if not email:
                break
            if self.validate_email(email):
                break
            print("❌ Email格式錯誤！")
        
        # 地址（選填）
        address = input("🏠 地址（選填）：").strip()
        
        # 生日（選填，有格式驗證）
        birthday = ""
        while True:
            birthday_input = input("🎂 生日（格式：YYYY-MM-DD，選填）：").strip()
            if not birthday_input:
                break
            if self.validate_birthday(birthday_input):
                birthday = birthday_input
                break
            print("❌ 生日格式錯誤！請使用：YYYY-MM-DD")
        
        # 分類
        print(f"\n📂 分類選項：")
        for i, cat in enumerate(self.categories, 1):
            print(f"{i}. {cat}")
        
        while True:
            cat_choice = input("請選擇分類（1-5）：").strip()
            if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(self.categories):
                category = self.categories[int(cat_choice) - 1]
                break
            print("❌ 請選擇有效的分類編號！")
        
        # 公司（選填）
        company = input("🏢 公司（選填）：").strip()
        
        # 備註（選填）
        note = input("📝 備註（選填）：").strip()
        
        # 建立聯絡人資料
        contact_info = {
            "電話": phone,
            "email": email,
            "地址": address,
            "生日": birthday,
            "分類": category,
            "公司": company,
            "備註": note
        }
        
        self.contacts[name] = contact_info
        self.save_data()
        
        print(f"\n✅ 成功新增聯絡人：{name}")
        self.display_contact_info(name, contact_info)
    
    def display_contact_info(self, name, info):
        """顯示聯絡人詳細資訊"""
        print(f"\n👤 {name} 的詳細資料")
        print("─" * 30)
        print(f"📞 電話：{info.get('電話', '未提供')}")
        print(f"📧 Email：{info.get('email', '未提供')}")
        print(f"🏠 地址：{info.get('地址', '未提供')}")
        print(f"🎂 生日：{info.get('生日', '未提供')}")
        print(f"📂 分類：{info.get('分類', '未提供')}")
        print(f"🏢 公司：{info.get('公司', '未提供')}")
        print(f"📝 備註：{info.get('備註', '未提供')}")
    
    def search_contacts(self):
        """搜尋聯絡人"""
        if not self.contacts:
            print("\n❌ 通訊錄是空的！")
            return
        
        print("\n🔍 搜尋聯絡人")
        print("─"*20)
        print("搜尋選項：")
        print("1. 按姓名搜尋")
        print("2. 按電話搜尋")
        print("3. 按分類搜尋")
        print("4. 按公司搜尋")
        print("5. 綜合搜尋")
        
        choice = input("請選擇搜尋方式 (1-5): ").strip()
        
        results = []
        
        if choice == "1":
            keyword = input("請輸入姓名關鍵字：").strip().lower()
            results = [(name, info) for name, info in self.contacts.items() 
                      if keyword in name.lower()]
        
        elif choice == "2":
            keyword = input("請輸入電話號碼：").strip()
            results = [(name, info) for name, info in self.contacts.items() 
                      if keyword in info.get("電話", "")]
        
        elif choice == "3":
            print("分類選項：", ", ".join(self.categories))
            category = input("請輸入分類：").strip()
            results = [(name, info) for name, info in self.contacts.items() 
                      if info.get("分類", "") == category]
        
        elif choice == "4":
            keyword = input("請輸入公司名稱：").strip().lower()
            results = [(name, info) for name, info in self.contacts.items() 
                      if keyword in info.get("公司", "").lower()]
        
        elif choice == "5":
            keyword = input("請輸入關鍵字（姓名/電話/分類/公司/備註）：").strip().lower()
            results = []
            for name, info in self.contacts.items():
                search_text = f"{name} {info.get('電話', '')} {info.get('分類', '')} {info.get('公司', '')} {info.get('備註', '')}"
                if keyword in search_text.lower():
                    results.append((name, info))
        
        else:
            print("❌ 無效的選擇！")
            return
        
        # 顯示搜尋結果
        if results:
            print(f"\n🔍 找到 {len(results)} 個結果：")
            print("="*50)
            for name, info in results:
                print(f"\n👤 {name} ({info.get('分類', '未分類')})")
                print(f"📞 {info.get('電話', '未提供')}")
                print(f"📧 {info.get('email', '未提供')}")
                if info.get('公司'):
                    print(f"🏢 {info['公司']}")
                if info.get('備註'):
                    print(f"📝 {info['備註']}")
        else:
            print("❌ 沒有找到相關聯絡人")
    
    def modify_contact(self):
        """修改聯絡人"""
        if not self.contacts:
            print("\n❌ 通訊錄是空的！")
            return
        
        print("\n📝 修改聯絡人")
        name = input("請輸入要修改的聯絡人姓名：").strip()
        
        if name not in self.contacts:
            print("❌ 找不到此聯絡人！")
            return
        
        info = self.contacts[name]
        print(f"\n目前 {name} 的資料：")
        self.display_contact_info(name, info)
        
        print(f"\n請選擇要修改的欄位：")
        fields = [
            ("電話", "phone"), ("Email", "email"), ("地址", "address"),
            ("生日", "birthday"), ("分類", "category"), ("公司", "company"), ("備註", "note")
        ]
        
        for i, (field_name, _) in enumerate(fields, 1):
            print(f"{i}. {field_name}")
        print("8. 修改姓名")
        
        choice = input("請選擇 (1-8): ").strip()
        
        if not choice.isdigit() or not (1 <= int(choice) <= 8):
            print("❌ 無效的選擇！")
            return
        
        choice = int(choice)
        
        if choice == 8:
            # 修改姓名
            new_name = input("請輸入新姓名：").strip()
            if not new_name:
                print("❌ 姓名不能為空！")
                return
            if new_name in self.contacts and new_name != name:
                print("❌ 新姓名已存在！")
                return
            
            self.contacts[new_name] = self.contacts.pop(name)
            print(f"✅ 已將 {name} 改名為 {new_name}")
        
        else:
            field_name, field_key = fields[choice - 1]
            current_value = info.get(field_key if field_key != "phone" else "電話", "")
            
            print(f"目前{field_name}：{current_value}")
            
            if field_key == "phone":
                while True:
                    new_value = input(f"請輸入新的{field_name}（格式：09XX-XXX-XXX）：").strip()
                    if not new_value:
                        print("❌ 電話不能為空！")
                        continue
                    if self.validate_phone(new_value):
                        info["電話"] = new_value
                        break
                    print("❌ 電話格式錯誤！")
            
            elif field_key == "email":
                while True:
                    new_value = input(f"請輸入新的{field_name}：").strip()
                    if not new_value or self.validate_email(new_value):
                        info["email"] = new_value
                        break
                    print("❌ Email格式錯誤！")
            
            elif field_key == "birthday":
                while True:
                    new_value = input(f"請輸入新的{field_name}（YYYY-MM-DD）：").strip()
                    if not new_value or self.validate_birthday(new_value):
                        info["生日"] = new_value
                        break
                    print("❌ 生日格式錯誤！")
            
            elif field_key == "category":
                print("分類選項：")
                for i, cat in enumerate(self.categories, 1):
                    print(f"{i}. {cat}")
                
                while True:
                    cat_choice = input("請選擇分類（1-5）：").strip()
                    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(self.categories):
                        info["分類"] = self.categories[int(cat_choice) - 1]
                        break
                    print("❌ 請選擇有效的分類編號！")
            
            else:
                # 地址、公司、備註
                new_value = input(f"請輸入新的{field_name}：").strip()
                key_map = {"address": "地址", "company": "公司", "note": "備註"}
                info[key_map[field_key]] = new_value
            
            print(f"✅ 已更新 {name} 的{field_name}")
        
        self.save_data()
    
    def delete_contact(self):
        """刪除聯絡人"""
        if not self.contacts:
            print("\n❌ 通訊錄是空的！")
            return
        
        print("\n❌ 刪除聯絡人")
        name = input("請輸入要刪除的聯絡人姓名：").strip()
        
        if name not in self.contacts:
            print("❌ 找不到此聯絡人！")
            return
        
        # 顯示即將刪除的聯絡人資訊
        print(f"\n即將刪除以下聯絡人：")
        self.display_contact_info(name, self.contacts[name])
        
        confirm = input(f"\n確定要刪除 {name} 嗎？(y/N): ").lower().strip()
        if confirm == 'y':
            del self.contacts[name]
            self.save_data()
            print(f"✅ 已刪除聯絡人：{name}")
        else:
            print("❌ 取消刪除")
    
    def show_statistics(self):
        """顯示統計分析"""
        if not self.contacts:
            print("\n❌ 通訊錄是空的！")
            return
        
        print("\n📊 通訊錄統計分析")
        print("="*40)
        
        # 基本統計
        total_contacts = len(self.contacts)
        print(f"📈 總聯絡人數：{total_contacts}")
        
        # 分類統計
        category_stats = {}
        email_count = 0
        birthday_count = 0
        company_count = 0
        note_count = 0
        
        for name, info in self.contacts.items():
            # 分類統計
            category = info.get("分類", "其他")
            category_stats[category] = category_stats.get(category, 0) + 1
            
            # 完整度統計
            if info.get("email"):
                email_count += 1
            if info.get("生日"):
                birthday_count += 1
            if info.get("公司"):
                company_count += 1
            if info.get("備註"):
                note_count += 1
        
        print(f"\n📂 分類統計：")
        for category in self.categories:
            count = category_stats.get(category, 0)
            percentage = (count / total_contacts) * 100 if total_contacts > 0 else 0
            print(f"  {category}：{count} 人 ({percentage:.1f}%)")
        
        # 資料完整度
        print(f"\n📋 資料完整度：")
        print(f"  有Email：{email_count} 人 ({email_count/total_contacts*100:.1f}%)")
        print(f"  有生日：{birthday_count} 人 ({birthday_count/total_contacts*100:.1f}%)")
        print(f"  有公司：{company_count} 人 ({company_count/total_contacts*100:.1f}%)")
        print(f"  有備註：{note_count} 人 ({note_count/total_contacts*100:.1f}%)")
        
        # 生日月份統計
        if birthday_count > 0:
            month_stats = {}
            for name, info in self.contacts.items():
                birthday = info.get("生日")
                if birthday:
                    try:
                        month = datetime.strptime(birthday, '%Y-%m-%d').month
                        month_stats[month] = month_stats.get(month, 0) + 1
                    except ValueError:
                        pass
            
            if month_stats:
                print(f"\n🎂 生日月份分佈：")
                month_names = ["", "1月", "2月", "3月", "4月", "5月", "6月",
                             "7月", "8月", "9月", "10月", "11月", "12月"]
                for month in sorted(month_stats.keys()):
                    count = month_stats[month]
                    print(f"  {month_names[month]}：{count} 人")
    
    def birthday_reminder(self):
        """生日提醒"""
        if not self.contacts:
            print("\n❌ 通訊錄是空的！")
            return
        
        today = date.today()
        print(f"\n🎂 生日提醒 - 今天是 {today}")
        print("="*40)
        
        # 今日生日
        today_birthdays = []
        # 本週生日
        week_birthdays = []
        # 本月生日
        month_birthdays = []
        
        for name, info in self.contacts.items():
            birthday = info.get("生日")
            if not birthday:
                continue
            
            try:
                birth_date = datetime.strptime(birthday, '%Y-%m-%d').date()
                # 計算今年的生日
                this_year_birthday = birth_date.replace(year=today.year)
                
                # 如果今年生日已過，考慮明年的
                if this_year_birthday < today:
                    this_year_birthday = birth_date.replace(year=today.year + 1)
                
                days_until = (this_year_birthday - today).days
                age = today.year - birth_date.year
                
                if days_until == 0:
                    today_birthdays.append((name, age, birth_date))
                elif days_until <= 7:
                    week_birthdays.append((name, age, birth_date, days_until))
                elif this_year_birthday.month == today.month:
                    month_birthdays.append((name, age, birth_date, days_until))
                    
            except ValueError:
                pass
        
        # 顯示提醒
        if today_birthdays:
            print("🎉 今日生日：")
            for name, age, birth_date in today_birthdays:
                print(f"  🎂 {name} - {age}歲生日快樂！")
        
        if week_birthdays:
            print(f"\n📅 本週生日（未來7天）：")
            week_birthdays.sort(key=lambda x: x[3])  # 按天數排序
            for name, age, birth_date, days in week_birthdays:
                print(f"  📅 {name} - {days}天後 ({birth_date.strftime('%m-%d')})，將滿{age}歲")
        
        if month_birthdays:
            print(f"\n📆 本月其他生日：")
            month_birthdays.sort(key=lambda x: x[3])  # 按天數排序
            for name, age, birth_date, days in month_birthdays:
                print(f"  📆 {name} - {days}天後 ({birth_date.strftime('%m-%d')})，將滿{age}歲")
        
        if not (today_birthdays or week_birthdays or month_birthdays):
            print("📅 近期沒有生日提醒")
    
    def export_data(self):
        """匯出資料"""
        if not self.contacts:
            print("\n❌ 通訊錄是空的！")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 匯出為文字檔
        txt_filename = f"contacts_export_{timestamp}.txt"
        try:
            with open(txt_filename, 'w', encoding='utf-8') as f:
                f.write("📞 通訊錄匯出資料\n")
                f.write("="*50 + "\n")
                f.write(f"匯出時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"總聯絡人數：{len(self.contacts)}\n\n")
                
                # 按分類分組
                categories = {}
                for name, info in self.contacts.items():
                    cat = info.get("分類", "其他")
                    if cat not in categories:
                        categories[cat] = []
                    categories[cat].append((name, info))
                
                for category, contacts_in_cat in categories.items():
                    f.write(f"【{category}】\n")
                    f.write("-" * 30 + "\n")
                    
                    for name, info in contacts_in_cat:
                        f.write(f"姓名：{name}\n")
                        f.write(f"電話：{info.get('電話', '未提供')}\n")
                        f.write(f"Email：{info.get('email', '未提供')}\n")
                        f.write(f"地址：{info.get('地址', '未提供')}\n")
                        f.write(f"生日：{info.get('生日', '未提供')}\n")
                        if info.get('公司'):
                            f.write(f"公司：{info['公司']}\n")
                        if info.get('備註'):
                            f.write(f"備註：{info['備註']}\n")
                        f.write("\n")
                    f.write("\n")
            
            print(f"✅ 資料已匯出至：{txt_filename}")
            
        except Exception as e:
            print(f"❌ 匯出失敗：{e}")
    
    def import_data(self):
        """匯入資料"""
        filename = input("\n📥 請輸入要匯入的JSON檔案名稱：").strip()
        
        if not os.path.exists(filename):
            print("❌ 檔案不存在！")
            return
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                import_data = json.load(f)
            
            if not isinstance(import_data, dict):
                print("❌ 檔案格式錯誤！")
                return
            
            # 顯示即將匯入的資料
            print(f"📋 即將匯入 {len(import_data)} 筆聯絡人資料")
            
            existing_count = 0
            for name in import_data.keys():
                if name in self.contacts:
                    existing_count += 1
            
            if existing_count > 0:
                print(f"⚠️ 其中 {existing_count} 筆資料已存在，將被覆蓋")
            
            confirm = input("確定要匯入嗎？(y/N): ").lower().strip()
            if confirm != 'y':
                print("❌ 取消匯入")
                return
            
            # 執行匯入
            imported_count = 0
            for name, info in import_data.items():
                self.contacts[name] = info
                imported_count += 1
            
            self.save_data()
            print(f"✅ 成功匯入 {imported_count} 筆聯絡人資料")
            
        except Exception as e:
            print(f"❌ 匯入失敗：{e}")
    
    def run(self):
        """執行主程式"""
        self.display_header()
        print("🎉 歡迎使用通訊錄管理系統！")
        
        while True:
            self.display_menu()
            choice = input("\n請選擇功能 (0-9): ").strip()
            
            if choice == "1":
                self.view_all_contacts()
            elif choice == "2":
                self.add_contact()
            elif choice == "3":
                self.search_contacts()
            elif choice == "4":
                self.modify_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                self.show_statistics()
            elif choice == "7":
                self.birthday_reminder()
            elif choice == "8":
                self.export_data()
            elif choice == "9":
                self.import_data()
            elif choice == "0":
                self.save_data()
                print("\n👋 感謝使用通訊錄管理系統！")
                print("💾 資料已自動儲存")
                break
            else:
                print("❌ 無效選擇，請輸入0-9！")
            
            input("\n按Enter鍵繼續...")

# 執行程式
if __name__ == "__main__":
    contact_book = ContactBook()
    try:
        contact_book.run()
    except KeyboardInterrupt:
        print("\n\n👋 程式被中斷，資料已儲存！")
        contact_book.save_data()