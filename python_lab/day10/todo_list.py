# 待辦事項清單管理程式 - Day 10主要項目
# 完整的待辦事項管理系統

import datetime
import json
import os

class TodoManager:
    def __init__(self):
        self.todo_list = []
        self.completed_list = []
        self.data_file = "todo_data.json"
        self.load_data()
    
    def save_data(self):
        """儲存資料到檔案"""
        try:
            data = {
                "todo_list": self.todo_list,
                "completed_list": self.completed_list
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ 儲存資料失敗：{e}")
    
    def load_data(self):
        """從檔案載入資料"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.todo_list = data.get("todo_list", [])
                    self.completed_list = data.get("completed_list", [])
        except Exception as e:
            print(f"⚠️ 載入資料失敗：{e}")
            self.todo_list = []
            self.completed_list = []
    
    def display_header(self):
        """顯示程式標題"""
        print("\n" + "="*50)
        print("📝         待辦事項管理程式         📝")
        print("="*50)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"📅 當前時間：{current_time}")
    
    def display_menu(self):
        """顯示主選單"""
        print("\n" + "─"*30)
        print("🏠 主選單")
        print("─"*30)
        print("1. 📋 查看所有事項")
        print("2. ➕ 新增待辦事項")
        print("3. ✅ 標記為已完成")
        print("4. ❌ 刪除事項")
        print("5. 📝 編輯事項")
        print("6. 📊 顯示統計")
        print("7. 🔍 搜尋事項")
        print("8. 🧹 清理已完成事項")
        print("9. 💾 匯出資料")
        print("0. 🚪 離開程式")
        print("─"*30)
    
    def view_all_items(self):
        """查看所有事項"""
        print("\n📋 所有事項一覽")
        print("="*40)
        
        if self.todo_list:
            print("\n🔲 待辦事項：")
            for i, item in enumerate(self.todo_list, 1):
                print(f"  {i:2d}. ⏰ {item}")
        else:
            print("\n🎉 太棒了！目前沒有待辦事項！")
        
        if self.completed_list:
            print(f"\n✅ 已完成事項（共{len(self.completed_list)}項）：")
            for i, item in enumerate(self.completed_list, 1):
                print(f"  {i:2d}. 🎯 {item}")
        
        if not self.todo_list and not self.completed_list:
            print("\n📝 還沒有任何事項，來新增第一個吧！")
    
    def add_item(self):
        """新增待辦事項"""
        print("\n➕ 新增待辦事項")
        print("─"*20)
        
        new_item = input("📝 請輸入新的待辦事項：").strip()
        
        if not new_item:
            print("❌ 事項內容不能為空！")
            return
        
        if new_item in self.todo_list:
            print("⚠️ 這個事項已經存在於待辦清單中！")
            return
        
        # 詢問優先級
        print("\n設定優先級：")
        print("1. 🔴 高優先級")
        print("2. 🟡 中優先級")  
        print("3. 🔵 低優先級")
        
        while True:
            priority = input("選擇優先級 (1-3)，或直接按Enter使用預設: ").strip()
            if priority == "1":
                new_item = "🔴 " + new_item
                break
            elif priority == "2":
                new_item = "🟡 " + new_item
                break
            elif priority == "3":
                new_item = "🔵 " + new_item
                break
            elif priority == "":
                break
            else:
                print("請輸入1-3或直接按Enter")
        
        self.todo_list.append(new_item)
        self.save_data()
        print(f"✅ 成功新增：{new_item}")
    
    def complete_item(self):
        """標記事項為已完成"""
        if not self.todo_list:
            print("\n❌ 沒有待辦事項可以完成！")
            return
        
        print("\n✅ 選擇要完成的事項：")
        print("─"*30)
        for i, item in enumerate(self.todo_list, 1):
            print(f"{i:2d}. {item}")
        
        try:
            choice = input("\n請輸入事項編號（或按Enter取消）：").strip()
            if not choice:
                print("已取消操作")
                return
            
            index = int(choice) - 1
            if 0 <= index < len(self.todo_list):
                completed_item = self.todo_list.pop(index)
                
                # 移除優先級標記並添加完成時間
                clean_item = completed_item.replace("🔴 ", "").replace("🟡 ", "").replace("🔵 ", "")
                timestamp = datetime.datetime.now().strftime("%m-%d %H:%M")
                completed_item_with_time = f"{clean_item} (完成於{timestamp})"
                
                self.completed_list.append(completed_item_with_time)
                self.save_data()
                print(f"🎉 恭喜完成：{clean_item}")
            else:
                print("❌ 編號無效！")
        except ValueError:
            print("❌ 請輸入有效的數字！")
    
    def delete_item(self):
        """刪除事項"""
        print("\n❌ 刪除事項")
        print("選擇要刪除的類型：")
        print("1. 🔲 待辦事項")
        print("2. ✅ 已完成事項")
        
        choice = input("請選擇 (1-2): ").strip()
        
        if choice == "1":
            if not self.todo_list:
                print("❌ 沒有待辦事項可以刪除！")
                return
            
            print("\n選擇要刪除的待辦事項：")
            for i, item in enumerate(self.todo_list, 1):
                print(f"{i:2d}. {item}")
            
            try:
                index = int(input("\n請輸入編號：")) - 1
                if 0 <= index < len(self.todo_list):
                    deleted_item = self.todo_list.pop(index)
                    self.save_data()
                    print(f"🗑️ 已刪除：{deleted_item}")
                else:
                    print("❌ 編號無效！")
            except ValueError:
                print("❌ 請輸入有效的數字！")
        
        elif choice == "2":
            if not self.completed_list:
                print("❌ 沒有已完成事項可以刪除！")
                return
            
            print("\n選擇要刪除的已完成事項：")
            for i, item in enumerate(self.completed_list, 1):
                print(f"{i:2d}. {item}")
            
            try:
                index = int(input("\n請輸入編號：")) - 1
                if 0 <= index < len(self.completed_list):
                    deleted_item = self.completed_list.pop(index)
                    self.save_data()
                    print(f"🗑️ 已刪除：{deleted_item}")
                else:
                    print("❌ 編號無效！")
            except ValueError:
                print("❌ 請輸入有效的數字！")
        else:
            print("❌ 無效選擇！")
    
    def edit_item(self):
        """編輯待辦事項"""
        if not self.todo_list:
            print("\n❌ 沒有待辦事項可以編輯！")
            return
        
        print("\n📝 選擇要編輯的事項：")
        for i, item in enumerate(self.todo_list, 1):
            print(f"{i:2d}. {item}")
        
        try:
            index = int(input("\n請輸入編號：")) - 1
            if 0 <= index < len(self.todo_list):
                old_item = self.todo_list[index]
                print(f"\n原內容：{old_item}")
                
                new_content = input("請輸入新內容：").strip()
                if new_content:
                    self.todo_list[index] = new_content
                    self.save_data()
                    print(f"✅ 已更新：{new_content}")
                else:
                    print("❌ 新內容不能為空！")
            else:
                print("❌ 編號無效！")
        except ValueError:
            print("❌ 請輸入有效的數字！")
    
    def show_statistics(self):
        """顯示統計資料"""
        total_todo = len(self.todo_list)
        total_completed = len(self.completed_list)
        total_items = total_todo + total_completed
        
        print("\n📊 統計資料")
        print("="*30)
        print(f"📋 待辦事項：{total_todo:3d} 項")
        print(f"✅ 已完成：  {total_completed:3d} 項")
        print(f"📑 總計：    {total_items:3d} 項")
        print("─"*30)
        
        if total_items > 0:
            completion_rate = (total_completed / total_items) * 100
            print(f"🎯 完成率：  {completion_rate:5.1f}%")
            
            # 進度條
            bar_length = 20
            filled_length = int(bar_length * completion_rate / 100)
            bar = "█" * filled_length + "░" * (bar_length - filled_length)
            print(f"📈 進度條：  [{bar}]")
        
        # 優先級統計
        if self.todo_list:
            high_priority = sum(1 for item in self.todo_list if "🔴" in item)
            medium_priority = sum(1 for item in self.todo_list if "🟡" in item)
            low_priority = sum(1 for item in self.todo_list if "🔵" in item)
            no_priority = total_todo - high_priority - medium_priority - low_priority
            
            print("\n🎯 優先級分佈：")
            print(f"🔴 高優先級：{high_priority:2d} 項")
            print(f"🟡 中優先級：{medium_priority:2d} 項")
            print(f"🔵 低優先級：{low_priority:2d} 項")
            print(f"⚪ 無設定：  {no_priority:2d} 項")
    
    def search_items(self):
        """搜尋事項"""
        if not self.todo_list and not self.completed_list:
            print("\n❌ 沒有任何事項可以搜尋！")
            return
        
        keyword = input("\n🔍 請輸入搜尋關鍵字：").strip().lower()
        if not keyword:
            print("❌ 搜尋關鍵字不能為空！")
            return
        
        print(f"\n🔍 搜尋結果「{keyword}」：")
        print("="*40)
        
        found_todo = []
        found_completed = []
        
        # 搜尋待辦事項
        for i, item in enumerate(self.todo_list):
            if keyword in item.lower():
                found_todo.append((i+1, item))
        
        # 搜尋已完成事項
        for i, item in enumerate(self.completed_list):
            if keyword in item.lower():
                found_completed.append((i+1, item))
        
        if found_todo:
            print("\n🔲 待辦事項中找到：")
            for num, item in found_todo:
                print(f"  {num:2d}. {item}")
        
        if found_completed:
            print("\n✅ 已完成事項中找到：")
            for num, item in found_completed:
                print(f"  {num:2d}. {item}")
        
        if not found_todo and not found_completed:
            print(f"❌ 沒有找到包含「{keyword}」的事項")
        else:
            total_found = len(found_todo) + len(found_completed)
            print(f"\n📊 共找到 {total_found} 個相關事項")
    
    def clean_completed(self):
        """清理已完成事項"""
        if not self.completed_list:
            print("\n❌ 沒有已完成的事項需要清理！")
            return
        
        print(f"\n🧹 目前有 {len(self.completed_list)} 項已完成事項")
        confirm = input("確定要清除所有已完成事項嗎？(y/N): ").lower().strip()
        
        if confirm == 'y':
            count = len(self.completed_list)
            self.completed_list.clear()
            self.save_data()
            print(f"✅ 已清除 {count} 項已完成事項")
        else:
            print("❌ 已取消清理操作")
    
    def export_data(self):
        """匯出資料"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"todo_export_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("📝 待辦事項匯出報告\n")
                f.write("="*40 + "\n")
                f.write(f"匯出時間：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("🔲 待辦事項：\n")
                if self.todo_list:
                    for i, item in enumerate(self.todo_list, 1):
                        f.write(f"  {i:2d}. {item}\n")
                else:
                    f.write("  (無)\n")
                
                f.write(f"\n✅ 已完成事項：\n")
                if self.completed_list:
                    for i, item in enumerate(self.completed_list, 1):
                        f.write(f"  {i:2d}. {item}\n")
                else:
                    f.write("  (無)\n")
                
                f.write(f"\n📊 統計：\n")
                f.write(f"  待辦事項：{len(self.todo_list)} 項\n")
                f.write(f"  已完成事項：{len(self.completed_list)} 項\n")
                f.write(f"  總計：{len(self.todo_list) + len(self.completed_list)} 項\n")
                
                if len(self.todo_list) + len(self.completed_list) > 0:
                    completion_rate = len(self.completed_list) / (len(self.todo_list) + len(self.completed_list)) * 100
                    f.write(f"  完成率：{completion_rate:.1f}%\n")
            
            print(f"✅ 資料已匯出到：{filename}")
        except Exception as e:
            print(f"❌ 匯出失敗：{e}")
    
    def run(self):
        """執行主程式"""
        self.display_header()
        print("🎉 歡迎使用待辦事項管理程式！")
        
        while True:
            self.display_menu()
            choice = input("\n請選擇功能 (0-9): ").strip()
            
            if choice == "1":
                self.view_all_items()
            elif choice == "2":
                self.add_item()
            elif choice == "3":
                self.complete_item()
            elif choice == "4":
                self.delete_item()
            elif choice == "5":
                self.edit_item()
            elif choice == "6":
                self.show_statistics()
            elif choice == "7":
                self.search_items()
            elif choice == "8":
                self.clean_completed()
            elif choice == "9":
                self.export_data()
            elif choice == "0":
                self.save_data()
                print("\n👋 感謝使用待辦事項管理程式！")
                print("📄 資料已自動儲存")
                break
            else:
                print("❌ 無效的選擇，請輸入0-9之間的數字！")
            
            input("\n按Enter鍵繼續...")

# 執行程式
if __name__ == "__main__":
    todo_manager = TodoManager()
    try:
        todo_manager.run()
    except KeyboardInterrupt:
        print("\n\n👋 程式被中斷，資料已儲存！")
        todo_manager.save_data()