"""
Day 19: 數位日記程式
實作重點：檔案處理 - 讀寫檔案、檔案模式、路徑處理、編碼處理
"""

import datetime
import os
import json
import glob
import shutil

class DigitalDiary:
    """數位日記程式 - 展示完整的檔案處理應用"""
    
    def __init__(self, diary_dir="diary_entries"):
        """
        初始化數位日記程式
        
        參數:
            diary_dir (str): 日記儲存目錄
        """
        self.diary_dir = diary_dir
        self.config_file = "diary_config.json"
        self.stats_file = "diary_stats.json"
        
        # 確保目錄存在
        self.ensure_directory_exists()
        
        # 載入配置和統計
        self.config = self.load_config()
        self.stats = self.load_statistics()
        
        print(f"📁 日記目錄：{os.path.abspath(self.diary_dir)}")
    
    def ensure_directory_exists(self):
        """確保日記目錄存在 - 展示目錄操作"""
        try:
            # 使用 os.makedirs 創建目錄，exist_ok=True 避免已存在時出錯
            os.makedirs(self.diary_dir, exist_ok=True)
            print(f"✅ 日記目錄已準備就緒")
        except PermissionError:
            print(f"❌ 沒有權限創建目錄：{self.diary_dir}")
            raise
        except Exception as e:
            print(f"❌ 創建目錄失敗：{e}")
            raise
    
    def load_config(self):
        """載入配置檔案 - 展示JSON檔案讀取"""
        default_config = {
            "author": "日記作者",
            "date_format": "%Y-%m-%d",
            "time_format": "%H:%M:%S",
            "encoding": "utf-8",
            "auto_backup": True,
            "default_mood": "普通"
        }
        
        config_path = os.path.join(self.diary_dir, self.config_file)
        
        try:
            # 檢查檔案是否存在
            if os.path.exists(config_path):
                print("📖 載入現有配置檔案...")
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                
                # 合併預設配置（處理新增的配置項目）
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                
                return config
            else:
                print("📝 建立預設配置檔案...")
                self.save_config(default_config)
                return default_config
                
        except json.JSONDecodeError as e:
            print(f"⚠️ 配置檔案格式錯誤：{e}")
            print("使用預設配置...")
            return default_config
        except Exception as e:
            print(f"⚠️ 載入配置失敗：{e}")
            return default_config
    
    def save_config(self, config=None):
        """儲存配置檔案 - 展示JSON檔案寫入"""
        if config is None:
            config = self.config
        
        config_path = os.path.join(self.diary_dir, self.config_file)
        
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                # ensure_ascii=False 確保中文正確顯示，indent=2 讓格式更易讀
                json.dump(config, f, ensure_ascii=False, indent=2)
            print(f"✅ 配置已儲存到 {config_path}")
        except Exception as e:
            print(f"❌ 儲存配置失敗：{e}")
    
    def load_statistics(self):
        """載入統計資料 - 展示檔案存在性檢查"""
        default_stats = {
            "total_entries": 0,
            "first_entry_date": None,
            "last_entry_date": None,
            "total_words": 0,
            "mood_counts": {},
            "writing_days": []
        }
        
        stats_path = os.path.join(self.diary_dir, self.stats_file)
        
        try:
            if os.path.exists(stats_path):
                with open(stats_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return default_stats
        except Exception as e:
            print(f"⚠️ 載入統計失敗：{e}")
            return default_stats
    
    def save_statistics(self):
        """儲存統計資料"""
        stats_path = os.path.join(self.diary_dir, self.stats_file)
        
        try:
            with open(stats_path, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ 儲存統計失敗：{e}")
    
    def get_diary_filename(self, date):
        """
        取得日記檔案名稱 - 展示路徑組合
        
        參數:
            date: datetime.date 物件
        
        回傳:
            str: 完整的檔案路徑
        """
        # 使用日期生成檔案名稱
        filename = f"diary_{date.strftime('%Y_%m_%d')}.txt"
        
        # 使用 os.path.join 組合路徑，確保跨平台相容性
        return os.path.join(self.diary_dir, filename)
    
    def write_diary_entry(self, content, date=None, mood=None):
        """
        寫入日記條目 - 展示檔案寫入和追加
        
        參數:
            content (str): 日記內容
            date (datetime.date): 日記日期，預設今天
            mood (str): 心情，預設使用設定中的預設心情
        """
        if date is None:
            date = datetime.date.today()
        
        if mood is None:
            mood = self.config["default_mood"]
        
        filename = self.get_diary_filename(date)
        
        try:
            # 檢查檔案是否已存在
            file_exists = os.path.exists(filename)
            
            # 如果檔案已存在，使用追加模式；否則使用寫入模式
            mode = 'a' if file_exists else 'w'
            
            with open(filename, mode, encoding=self.config["encoding"]) as f:
                current_time = datetime.datetime.now()
                
                # 如果是新檔案，寫入檔頭
                if not file_exists:
                    f.write(f"📅 日記 - {date.strftime(self.config['date_format'])}\n")
                    f.write(f"✍️  作者：{self.config['author']}\n")
                    f.write("=" * 60 + "\n\n")
                
                # 寫入日記條目
                f.write(f"⏰ 時間：{current_time.strftime(self.config['time_format'])}\n")
                f.write(f"😊 心情：{mood}\n")
                f.write("─" * 40 + "\n")
                f.write(content)
                f.write("\n\n" + "─" * 40 + "\n\n")
            
            # 更新統計
            self.update_statistics(date, content, mood)
            
            print(f"✅ 日記已儲存到：{filename}")
            return True
            
        except UnicodeEncodeError as e:
            print(f"❌ 編碼錯誤：{e}")
            return False
        except PermissionError:
            print(f"❌ 沒有權限寫入檔案：{filename}")
            return False
        except Exception as e:
            print(f"❌ 寫入日記失敗：{e}")
            return False
    
    def read_diary_entry(self, date):
        """
        讀取日記條目 - 展示檔案讀取
        
        參數:
            date (datetime.date): 要讀取的日期
        
        回傳:
            str: 日記內容，如果不存在則返回None
        """
        filename = self.get_diary_filename(date)
        
        try:
            # 檢查檔案是否存在
            if not os.path.exists(filename):
                print(f"📝 {date.strftime(self.config['date_format'])} 沒有日記條目")
                return None
            
            # 讀取整個檔案
            with open(filename, 'r', encoding=self.config["encoding"]) as f:
                content = f.read()
                return content
                
        except UnicodeDecodeError as e:
            print(f"❌ 檔案編碼錯誤：{e}")
            # 嘗試其他編碼
            return self.read_with_fallback_encoding(filename)
        except PermissionError:
            print(f"❌ 沒有權限讀取檔案：{filename}")
            return None
        except Exception as e:
            print(f"❌ 讀取日記失敗：{e}")
            return None
    
    def read_with_fallback_encoding(self, filename):
        """使用備用編碼讀取檔案"""
        fallback_encodings = ['utf-8', 'utf-8-sig', 'big5', 'gbk', 'cp1252']
        
        for encoding in fallback_encodings:
            try:
                with open(filename, 'r', encoding=encoding) as f:
                    content = f.read()
                    print(f"✅ 使用 {encoding} 編碼成功讀取")
                    return content
            except UnicodeDecodeError:
                continue
        
        print("❌ 嘗試所有編碼都失敗")
        return None
    
    def list_all_entries(self):
        """
        列出所有日記條目 - 展示目錄遍歷和glob模式匹配
        
        回傳:
            list: 日記條目資訊列表
        """
        try:
            # 使用glob模式匹配找出所有日記檔案
            pattern = os.path.join(self.diary_dir, "diary_*.txt")
            diary_files = glob.glob(pattern)
            
            if not diary_files:
                return []
            
            entries = []
            
            for file_path in diary_files:
                try:
                    # 從檔案名稱解析日期
                    filename = os.path.basename(file_path)
                    date_part = filename.replace('diary_', '').replace('.txt', '')
                    date = datetime.datetime.strptime(date_part, '%Y_%m_%d').date()
                    
                    # 取得檔案資訊
                    stat_info = os.stat(file_path)
                    file_size = stat_info.st_size
                    modified_time = datetime.datetime.fromtimestamp(stat_info.st_mtime)
                    
                    entries.append({
                        'date': date,
                        'filename': file_path,
                        'size': file_size,
                        'modified': modified_time
                    })
                    
                except ValueError:
                    # 忽略檔名格式不正確的檔案
                    continue
                except OSError:
                    # 忽略無法存取的檔案
                    continue
            
            # 按日期排序（最新的在前）
            entries.sort(key=lambda x: x['date'], reverse=True)
            return entries
            
        except Exception as e:
            print(f"❌ 列出日記條目失敗：{e}")
            return []
    
    def search_entries(self, keyword, case_sensitive=False):
        """
        搜尋日記條目 - 展示檔案內容搜尋
        
        參數:
            keyword (str): 搜尋關鍵字
            case_sensitive (bool): 是否區分大小寫
        
        回傳:
            list: 搜尋結果列表
        """
        try:
            results = []
            all_entries = self.list_all_entries()
            
            for entry in all_entries:
                try:
                    with open(entry['filename'], 'r', encoding=self.config["encoding"]) as f:
                        content = f.read()
                        
                        # 根據設定決定是否區分大小寫
                        search_content = content if case_sensitive else content.lower()
                        search_keyword = keyword if case_sensitive else keyword.lower()
                        
                        if search_keyword in search_content:
                            # 找出包含關鍵字的行
                            lines = content.split('\n')
                            matching_lines = []
                            
                            for line_num, line in enumerate(lines, 1):
                                check_line = line if case_sensitive else line.lower()
                                if search_keyword in check_line:
                                    matching_lines.append({
                                        'line_number': line_num,
                                        'content': line.strip()
                                    })
                            
                            results.append({
                                'date': entry['date'],
                                'filename': entry['filename'],
                                'matches': matching_lines
                            })
                            
                except Exception:
                    # 忽略無法讀取的檔案
                    continue
            
            return results
            
        except Exception as e:
            print(f"❌ 搜尋失敗：{e}")
            return []
    
    def delete_entry(self, date, create_backup=True):
        """
        刪除日記條目 - 展示檔案刪除和備份
        
        參數:
            date (datetime.date): 要刪除的日期
            create_backup (bool): 是否建立備份
        """
        filename = self.get_diary_filename(date)
        
        try:
            if not os.path.exists(filename):
                print(f"📝 {date.strftime(self.config['date_format'])} 沒有日記可刪除")
                return False
            
            # 如果啟用備份功能
            if create_backup and self.config.get("auto_backup", True):
                backup_filename = f"{filename}.backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                shutil.copy2(filename, backup_filename)
                print(f"💾 已建立備份：{backup_filename}")
            
            # 刪除檔案
            os.remove(filename)
            print(f"🗑️ 已刪除 {date.strftime(self.config['date_format'])} 的日記")
            
            return True
            
        except PermissionError:
            print(f"❌ 沒有權限刪除檔案：{filename}")
            return False
        except Exception as e:
            print(f"❌ 刪除失敗：{e}")
            return False
    
    def update_statistics(self, date, content, mood):
        """更新統計資料"""
        try:
            # 更新基本統計
            self.stats["total_entries"] += 1
            
            # 更新日期統計
            date_str = date.strftime(self.config["date_format"])
            if not self.stats["first_entry_date"]:
                self.stats["first_entry_date"] = date_str
            self.stats["last_entry_date"] = date_str
            
            # 更新字數統計
            word_count = len(content.split())
            self.stats["total_words"] += word_count
            
            # 更新心情統計
            if mood not in self.stats["mood_counts"]:
                self.stats["mood_counts"][mood] = 0
            self.stats["mood_counts"][mood] += 1
            
            # 更新寫作日期
            if date_str not in self.stats["writing_days"]:
                self.stats["writing_days"].append(date_str)
            
            # 儲存統計
            self.save_statistics()
            
        except Exception as e:
            print(f"⚠️ 更新統計失敗：{e}")
    
    def export_diary(self, format='txt', start_date=None, end_date=None):
        """
        匯出日記 - 展示不同格式的檔案輸出
        
        參數:
            format (str): 匯出格式 ('txt', 'html', 'json', 'markdown')
            start_date (datetime.date): 開始日期
            end_date (datetime.date): 結束日期
        """
        try:
            all_entries = self.list_all_entries()
            
            if not all_entries:
                print("📝 沒有日記可匯出")
                return None
            
            # 過濾日期範圍
            if start_date or end_date:
                filtered_entries = []
                for entry in all_entries:
                    if start_date and entry['date'] < start_date:
                        continue
                    if end_date and entry['date'] > end_date:
                        continue
                    filtered_entries.append(entry)
                all_entries = filtered_entries
            
            if not all_entries:
                print("📝 指定日期範圍內沒有日記")
                return None
            
            # 生成匯出檔名
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            export_filename = f"diary_export_{timestamp}.{format}"
            export_path = os.path.join(self.diary_dir, export_filename)
            
            # 根據格式執行匯出
            if format == 'txt':
                success = self._export_txt(all_entries, export_path)
            elif format == 'html':
                success = self._export_html(all_entries, export_path)
            elif format == 'json':
                success = self._export_json(all_entries, export_path)
            elif format == 'markdown':
                success = self._export_markdown(all_entries, export_path)
            else:
                print(f"❌ 不支援的格式：{format}")
                return None
            
            if success:
                print(f"✅ 日記已匯出：{export_path}")
                return export_path
            else:
                return None
                
        except Exception as e:
            print(f"❌ 匯出失敗：{e}")
            return None
    
    def _export_txt(self, entries, filename):
        """匯出為純文字檔"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # 寫入標題
                f.write(f"📚 {self.config['author']} 的日記集\n")
                f.write(f"📅 匯出時間：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"📊 共 {len(entries)} 篇日記\n")
                f.write("=" * 80 + "\n\n")
                
                # 按時間順序寫入日記
                for entry in reversed(entries):
                    try:
                        with open(entry['filename'], 'r', encoding=self.config["encoding"]) as diary_file:
                            content = diary_file.read()
                            f.write(content)
                            f.write("\n" + "=" * 80 + "\n\n")
                    except Exception:
                        f.write(f"❌ 無法讀取 {entry['date']} 的日記\n\n")
            
            return True
        except Exception as e:
            print(f"❌ 匯出TXT失敗：{e}")
            return False
    
    def _export_html(self, entries, filename):
        """匯出為HTML檔案"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # 寫入HTML標頭
                f.write("""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的日記</title>
    <style>
        body {
            font-family: 'Microsoft JhengHei', Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
            background-color: #f9f9f9;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .diary-entry {
            background: white;
            margin-bottom: 30px;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .date {
            color: #2c3e50;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .content {
            white-space: pre-wrap;
            color: #34495e;
        }
        .stats {
            background: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
            text-align: center;
            color: #7f8c8d;
        }
    </style>
</head>
<body>""")
                
                # 寫入標題
                f.write(f"""
    <div class="header">
        <h1>📚 {self.config['author']} 的日記</h1>
        <div class="stats">
            📅 匯出時間：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | 
            📊 共 {len(entries)} 篇日記
        </div>
    </div>
""")
                
                # 寫入日記內容
                for entry in reversed(entries):
                    try:
                        with open(entry['filename'], 'r', encoding=self.config["encoding"]) as diary_file:
                            content = diary_file.read()
                            # HTML轉義
                            content = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                            
                            date_str = entry['date'].strftime('%Y年%m月%d日')
                            f.write(f"""
    <div class="diary-entry">
        <div class="date">{date_str}</div>
        <div class="content">{content}</div>
    </div>
""")
                    except Exception:
                        date_str = entry['date'].strftime('%Y年%m月%d日')
                        f.write(f"""
    <div class="diary-entry">
        <div class="date">{date_str}</div>
        <div class="content">❌ 無法讀取此日記</div>
    </div>
""")
                
                # 結束HTML
                f.write("</body></html>")
            
            return True
        except Exception as e:
            print(f"❌ 匯出HTML失敗：{e}")
            return False
    
    def _export_json(self, entries, filename):
        """匯出為JSON格式"""
        try:
            export_data = {
                "author": self.config['author'],
                "export_time": datetime.datetime.now().isoformat(),
                "total_entries": len(entries),
                "statistics": self.stats,
                "entries": []
            }
            
            for entry in entries:
                try:
                    with open(entry['filename'], 'r', encoding=self.config["encoding"]) as diary_file:
                        content = diary_file.read()
                        
                        entry_data = {
                            "date": entry['date'].isoformat(),
                            "content": content,
                            "file_size": entry['size'],
                            "modified_time": entry['modified'].isoformat()
                        }
                        export_data["entries"].append(entry_data)
                except Exception:
                    # 記錄無法讀取的條目
                    entry_data = {
                        "date": entry['date'].isoformat(),
                        "content": "無法讀取",
                        "file_size": entry['size'],
                        "modified_time": entry['modified'].isoformat(),
                        "error": True
                    }
                    export_data["entries"].append(entry_data)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"❌ 匯出JSON失敗：{e}")
            return False
    
    def _export_markdown(self, entries, filename):
        """匯出為Markdown格式"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # Markdown 標題
                f.write(f"# 📚 {self.config['author']} 的日記\n\n")
                f.write(f"**匯出時間：** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
                f.write(f"**日記數量：** {len(entries)} 篇\n\n")
                f.write("---\n\n")
                
                # 寫入日記內容
                for entry in reversed(entries):
                    try:
                        with open(entry['filename'], 'r', encoding=self.config["encoding"]) as diary_file:
                            content = diary_file.read()
                            
                            date_str = entry['date'].strftime('%Y年%m月%d日')
                            f.write(f"## 📅 {date_str}\n\n")
                            f.write("```\n")
                            f.write(content)
                            f.write("\n```\n\n")
                            f.write("---\n\n")
                    except Exception:
                        date_str = entry['date'].strftime('%Y年%m月%d日')
                        f.write(f"## 📅 {date_str}\n\n")
                        f.write("❌ 無法讀取此日記\n\n")
                        f.write("---\n\n")
            
            return True
        except Exception as e:
            print(f"❌ 匯出Markdown失敗：{e}")
            return False
    
    def get_statistics(self):
        """取得統計資訊"""
        stats = self.stats.copy()
        
        # 計算額外統計
        if stats["total_entries"] > 0:
            stats["average_words"] = stats["total_words"] / stats["total_entries"]
        else:
            stats["average_words"] = 0
        
        # 計算寫作頻率（最近30天）
        try:
            recent_days = 0
            today = datetime.date.today()
            
            for date_str in stats["writing_days"]:
                try:
                    date = datetime.datetime.strptime(date_str, self.config["date_format"]).date()
                    if (today - date).days <= 30:
                        recent_days += 1
                except ValueError:
                    continue
            
            stats["recent_30_days"] = recent_days
        except Exception:
            stats["recent_30_days"] = 0
        
        return stats
    
    def cleanup_backups(self, days_old=7):
        """清理舊的備份檔案"""
        try:
            pattern = os.path.join(self.diary_dir, "*.backup_*")
            backup_files = glob.glob(pattern)
            
            cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days_old)
            deleted_count = 0
            
            for backup_file in backup_files:
                try:
                    # 取得檔案修改時間
                    file_time = datetime.datetime.fromtimestamp(os.path.getmtime(backup_file))
                    
                    if file_time < cutoff_date:
                        os.remove(backup_file)
                        deleted_count += 1
                        print(f"🗑️ 已刪除舊備份：{os.path.basename(backup_file)}")
                
                except Exception:
                    continue
            
            if deleted_count == 0:
                print(f"✅ 沒有超過 {days_old} 天的備份檔案")
            else:
                print(f"🧹 已清理 {deleted_count} 個舊備份檔案")
        
        except Exception as e:
            print(f"❌ 清理備份失敗：{e}")

# 使用者介面函數
def get_date_input(prompt, allow_empty=True):
    """取得日期輸入"""
    while True:
        date_str = input(prompt).strip()
        
        if not date_str and allow_empty:
            return datetime.date.today()
        
        if not date_str and not allow_empty:
            print("❌ 請輸入日期")
            continue
        
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("❌ 日期格式錯誤，請使用 YYYY-MM-DD 格式")

def write_diary_interface(diary):
    """寫日記介面"""
    print("\n✍️ 寫日記")
    print("─" * 30)
    
    # 取得日期
    date = get_date_input("日期 (YYYY-MM-DD，按Enter使用今天): ")
    
    # 選擇心情
    moods = ["😊開心", "😐普通", "😢難過", "😠生氣", "🤩興奮", "😰焦慮", "😌平靜"]
    print("\n心情選擇:")
    for i, mood in enumerate(moods, 1):
        print(f"  {i}. {mood}")
    
    mood_choice = input("選擇心情 (1-7，按Enter使用預設): ").strip()
    
    if mood_choice.isdigit() and 1 <= int(mood_choice) <= len(moods):
        mood = moods[int(mood_choice) - 1][2:]  # 移除emoji
    else:
        mood = diary.config["default_mood"]
    
    # 輸入內容
    print("\n📝 請輸入日記內容 (按 Ctrl+C 結束輸入):")
    print("─" * 40)
    
    content_lines = []
    try:
        while True:
            try:
                line = input()
                content_lines.append(line)
            except EOFError:
                break
    except KeyboardInterrupt:
        if content_lines:
            print(f"\n📝 已輸入 {len(content_lines)} 行")
        else:
            print("\n❌ 沒有輸入內容")
            return
    
    if not content_lines:
        print("❌ 沒有輸入內容")
        return
    
    content = "\n".join(content_lines)
    
    # 儲存日記
    success = diary.write_diary_entry(content, date, mood)
    
    if success:
        word_count = len(content.split())
        print(f"\n✅ 日記儲存成功！")
        print(f"📊 統計：{word_count} 個字詞，心情：{mood}")

def read_diary_interface(diary):
    """讀日記介面"""
    print("\n📖 讀日記")
    print("─" * 20)
    
    date = get_date_input("請輸入日期 (YYYY-MM-DD，按Enter使用今天): ")
    
    content = diary.read_diary_entry(date)
    
    if content:
        print(f"\n📖 {date.strftime('%Y年%m月%d日')} 的日記:")
        print("=" * 60)
        print(content)
    else:
        print(f"📝 {date.strftime('%Y年%m月%d日')} 沒有日記")

def list_entries_interface(diary):
    """列出日記介面"""
    print("\n📋 所有日記")
    print("─" * 20)
    
    entries = diary.list_all_entries()
    
    if not entries:
        print("📝 還沒有任何日記")
        return
    
    print(f"📚 共找到 {len(entries)} 篇日記:\n")
    
    # 顯示日記列表
    print(f"{'編號':<4} {'日期':<12} {'大小':<8} {'修改時間'}")
    print("─" * 40)
    
    for i, entry in enumerate(entries, 1):
        date_str = entry['date'].strftime('%Y-%m-%d')
        size_str = f"{entry['size']}B"
        modified_str = entry['modified'].strftime('%m/%d %H:%M')
        
        print(f"{i:<4} {date_str:<12} {size_str:<8} {modified_str}")
    
    # 選擇讀取
    choice = input(f"\n輸入編號讀取日記 (1-{len(entries)})，按Enter返回: ").strip()
    
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(entries):
            selected_entry = entries[index]
            content = diary.read_diary_entry(selected_entry['date'])
            if content:
                print(f"\n📖 {selected_entry['date'].strftime('%Y年%m月%d日')} 的日記:")
                print("=" * 60)
                print(content)

def search_interface(diary):
    """搜尋介面"""
    print("\n🔍 搜尋日記")
    print("─" * 20)
    
    keyword = input("請輸入搜尋關鍵字: ").strip()
    
    if not keyword:
        print("❌ 請輸入關鍵字")
        return
    
    case_sensitive = input("區分大小寫？(y/N): ").strip().lower() == 'y'
    
    print(f"\n🔍 搜尋 '{keyword}'...")
    results = diary.search_entries(keyword, case_sensitive)
    
    if not results:
        print(f"📝 沒有找到包含 '{keyword}' 的日記")
        return
    
    print(f"\n📊 找到 {len(results)} 篇相關日記:\n")
    
    for i, result in enumerate(results, 1):
        date_str = result['date'].strftime('%Y-%m-%d')
        match_count = len(result['matches'])
        
        print(f"{i}. 📅 {date_str} - 找到 {match_count} 處匹配")
        
        # 顯示前3個匹配
        for j, match in enumerate(result['matches'][:3]):
            line_content = match['content']
            if len(line_content) > 50:
                line_content = line_content[:50] + "..."
            print(f"   第{match['line_number']}行: {line_content}")
        
        if match_count > 3:
            print(f"   ... 還有 {match_count - 3} 處匹配")
        print()

def statistics_interface(diary):
    """統計介面"""
    print("\n📊 日記統計")
    print("─" * 20)
    
    stats = diary.get_statistics()
    
    if stats["total_entries"] == 0:
        print("📝 還沒有日記，開始寫第一篇吧！")
        return
    
    print("📈 寫作統計:")
    print(f"  📝 總日記數: {stats['total_entries']} 篇")
    print(f"  📅 寫作時間: {stats['first_entry_date']} ~ {stats['last_entry_date']}")
    print(f"  ✏️  總字數: {stats['total_words']:,} 字")
    print(f"  📊 平均字數: {stats['average_words']:.1f} 字/篇")
    print(f"  🗓️  最近30天: {stats['recent_30_days']} 天有寫日記")
    
    # 心情統計
    if stats["mood_counts"]:
        print(f"\n😊 心情分佈:")
        sorted_moods = sorted(stats["mood_counts"].items(), key=lambda x: x[1], reverse=True)
        
        for mood, count in sorted_moods:
            percentage = (count / stats["total_entries"]) * 100
            bar_length = int(percentage / 5)  # 每5%一個方塊
            bar = "█" * bar_length
            
            print(f"  {mood:6}: {count:2d}次 ({percentage:4.1f}%) {bar}")

def export_interface(diary):
    """匯出介面"""
    print("\n📦 匯出日記")
    print("─" * 20)
    
    # 選擇格式
    formats = [
        ("txt", "純文字檔 (.txt)"),
        ("html", "網頁檔案 (.html)"),
        ("json", "JSON格式 (.json)"),
        ("markdown", "Markdown (.md)")
    ]
    
    print("選擇匯出格式:")
    for i, (fmt, desc) in enumerate(formats, 1):
        print(f"  {i}. {desc}")
    
    format_choice = input(f"請選擇 (1-{len(formats)}): ").strip()
    
    if not format_choice.isdigit() or not 1 <= int(format_choice) <= len(formats):
        print("❌ 無效選擇")
        return
    
    selected_format = formats[int(format_choice) - 1][0]
    
    # 選擇日期範圍
    range_choice = input("\n是否指定日期範圍？(y/N): ").strip().lower() == 'y'
    
    start_date = None
    end_date = None
    
    if range_choice:
        try:
            start_date = get_date_input("開始日期 (YYYY-MM-DD): ", allow_empty=False)
            end_date = get_date_input("結束日期 (YYYY-MM-DD): ", allow_empty=False)
            
            if start_date > end_date:
                print("❌ 開始日期不能晚於結束日期")
                return
            
        except KeyboardInterrupt:
            print("\n❌ 取消匯出")
            return
    
    # 執行匯出
    print(f"\n📦 正在匯出為 {selected_format.upper()} 格式...")
    
    export_path = diary.export_diary(selected_format, start_date, end_date)
    
    if export_path:
        file_size = os.path.getsize(export_path)
        print(f"✅ 匯出完成！")
        print(f"📁 檔案: {export_path}")
        print(f"📊 大小: {file_size:,} bytes")

def settings_interface(diary):
    """設定介面"""
    print("\n⚙️ 設定")
    print("─" * 15)
    
    config = diary.config
    
    print("目前設定:")
    settings = [
        ("作者", "author"),
        ("預設心情", "default_mood"),
        ("自動備份", "auto_backup")
    ]
    
    for i, (name, key) in enumerate(settings, 1):
        value = config[key]
        if isinstance(value, bool):
            value = "開啟" if value else "關閉"
        print(f"  {i}. {name}: {value}")
    
    print(f"  4. 清理備份檔案")
    
    choice = input(f"\n選擇要修改的項目 (1-4)，按Enter返回: ").strip()
    
    if choice == "1":
        new_author = input(f"新的作者名稱 (目前: {config['author']}): ").strip()
        if new_author:
            config['author'] = new_author
            diary.save_config()
            print("✅ 作者名稱已更新")
    
    elif choice == "2":
        moods = ["開心", "普通", "難過", "生氣", "興奮", "焦慮", "平靜"]
        print("心情選項:")
        for i, mood in enumerate(moods, 1):
            print(f"  {i}. {mood}")
        
        mood_choice = input("選擇預設心情 (1-7): ").strip()
        if mood_choice.isdigit() and 1 <= int(mood_choice) <= len(moods):
            config['default_mood'] = moods[int(mood_choice) - 1]
            diary.save_config()
            print("✅ 預設心情已更新")
    
    elif choice == "3":
        backup_choice = input("啟用自動備份？(y/N): ").strip().lower() == 'y'
        config['auto_backup'] = backup_choice
        diary.save_config()
        status = "啟用" if backup_choice else "停用"
        print(f"✅ 自動備份已{status}")
    
    elif choice == "4":
        days = input("刪除多少天前的備份檔案？(預設7天): ").strip()
        try:
            days = int(days) if days else 7
            diary.cleanup_backups(days)
        except ValueError:
            print("❌ 請輸入有效數字")

def main():
    """主程式"""
    print("📖 歡迎使用數位日記程式！")
    print("這是一個展示檔案處理功能的完整應用程式")
    
    try:
        # 建立日記物件
        diary = DigitalDiary()
        
        while True:
            print("\n" + "=" * 60)
            print("📚 數位日記 v1.0")
            print("=" * 60)
            print("1. ✍️  寫日記")
            print("2. 📖 讀日記")  
            print("3. 📋 列出所有日記")
            print("4. 🔍 搜尋日記")
            print("5. 📊 日記統計")
            print("6. 📦 匯出日記")
            print("7. ⚙️  設定")
            print("0. 🚪 退出")
            print("─" * 60)
            
            try:
                choice = input("請選擇功能 (0-7): ").strip()
                
                if choice == "0":
                    print("\n👋 感謝使用數位日記程式！")
                    print("📝 記錄生活，記錄成長～")
                    break
                elif choice == "1":
                    write_diary_interface(diary)
                elif choice == "2":
                    read_diary_interface(diary)
                elif choice == "3":
                    list_entries_interface(diary)
                elif choice == "4":
                    search_interface(diary)
                elif choice == "5":
                    statistics_interface(diary)
                elif choice == "6":
                    export_interface(diary)
                elif choice == "7":
                    settings_interface(diary)
                else:
                    print("❌ 無效選擇，請重新輸入")
            
            except KeyboardInterrupt:
                print("\n\n⚠️ 程式被中斷")
                break
            except Exception as e:
                print(f"\n❌ 發生錯誤：{e}")
                print("程式將繼續運行...")
            
            if choice != "0":
                input("\n按 Enter 繼續...")
    
    except Exception as e:
        print(f"❌ 程式初始化失敗：{e}")
        print("請檢查檔案權限和磁碟空間")

if __name__ == "__main__":
    main()