# Day 19：檔案處理

## 今日學習目標
- 理解檔案輸入輸出的基本概念
- 學會讀取和寫入文字檔案
- 掌握不同的檔案開啟模式
- 了解檔案路徑和編碼問題
- 實作日記程式應用

## 1. 檔案處理概念

### 1.1 生活中的類比
檔案處理就像是**圖書館的借閱系統**：
- **借書**：開啟檔案進行讀取
- **還書時寫心得**：開啟檔案進行寫入
- **續借**：追加內容到現有檔案
- **辦借書證**：創建新檔案
- **歸還並關閉**：關閉檔案釋放資源

或者想像成**日記本的使用**：
- **讀舊日記**：讀取檔案內容
- **寫新日記**：寫入新內容
- **補充日記**：在現有內容後追加
- **換新本子**：創建新檔案

### 1.2 為什麼需要檔案處理？
```python
# ❌ 沒有檔案：資料會消失
user_data = {"name": "小明", "score": 95}
print("程式結束後，資料就消失了...")

# ✅ 使用檔案：資料可以持久保存
with open("user_data.txt", "w", encoding="utf-8") as f:
    f.write("小明的分數是95分")
print("資料已儲存到檔案，下次可以讀取")
```

## 2. 檔案操作基礎

### 2.1 檔案開啟模式
```python
# 基本檔案模式
modes = {
    'r':  '只讀模式（預設）- 檔案必須存在',
    'w':  '寫入模式 - 會覆蓋原檔案或創建新檔案',
    'a':  '追加模式 - 在檔案末尾添加內容',
    'x':  '獨佔創建模式 - 檔案不能已存在',
    'b':  '二進位模式 - 處理圖片、音樂等',
    't':  '文字模式（預設）- 處理文字檔案',
    '+':  '讀寫模式 - 可同時讀寫'
}

# 常用組合
common_modes = {
    'r':   '讀取文字檔案',
    'w':   '寫入文字檔案（覆蓋）',
    'a':   '追加到文字檔案',
    'r+':  '讀寫文字檔案（檔案必須存在）',
    'w+':  '讀寫文字檔案（會覆蓋或創建）',
    'rb':  '讀取二進位檔案',
    'wb':  '寫入二進位檔案'
}
```

### 2.2 基本檔案操作語法
```python
# 基本語法
file = open("檔案名稱", "模式", encoding="編碼")
# 進行檔案操作
file.close()  # 重要：一定要關閉檔案

# 推薦語法（自動關閉檔案）
with open("檔案名稱", "模式", encoding="編碼") as file:
    # 進行檔案操作
    pass
# 檔案會自動關閉
```

## 3. 讀取檔案

### 3.1 讀取整個檔案
```python
# 方法1：讀取所有內容為字串
def read_entire_file(filename):
    """讀取整個檔案內容"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"檔案 {filename} 不存在")
        return None
    except Exception as e:
        print(f"讀取檔案發生錯誤：{e}")
        return None

# 使用範例
content = read_entire_file("example.txt")
if content:
    print("檔案內容：")
    print(content)
```

### 3.2 逐行讀取檔案
```python
# 方法1：readlines() - 讀取所有行到清單
def read_lines_to_list(filename):
    """讀取檔案的所有行到清單"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # 移除每行末尾的換行符號
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"檔案 {filename} 不存在")
        return []

# 方法2：迴圈逐行讀取（適合大檔案）
def read_lines_one_by_one(filename):
    """逐行處理檔案內容"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_number = 1
            for line in file:
                line = line.strip()  # 移除首尾空白和換行符號
                print(f"第{line_number}行：{line}")
                line_number += 1
    except FileNotFoundError:
        print(f"檔案 {filename} 不存在")

# 方法3：readline() - 一次讀一行
def read_line_by_line(filename):
    """使用readline()逐行讀取"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_number = 1
            while True:
                line = file.readline()
                if not line:  # 檔案結束
                    break
                line = line.strip()
                if line:  # 非空行
                    print(f"行{line_number}：{line}")
                line_number += 1
    except FileNotFoundError:
        print(f"檔案 {filename} 不存在")
```

### 3.3 實用的檔案讀取範例
```python
def read_config_file(filename):
    """讀取設定檔案（key=value格式）"""
    config = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                
                # 跳過空行和註解
                if not line or line.startswith('#'):
                    continue
                
                # 解析key=value
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
                else:
                    print(f"警告：第{line_num}行格式錯誤：{line}")
        
        return config
    except Exception as e:
        print(f"讀取設定檔錯誤：{e}")
        return {}

# 使用範例
config = read_config_file("settings.txt")
print("設定檔內容：", config)

def read_csv_simple(filename):
    """簡單讀取CSV檔案"""
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            header = file.readline().strip().split(',')
            
            for line in file:
                values = line.strip().split(',')
                if len(values) == len(header):
                    row_dict = dict(zip(header, values))
                    data.append(row_dict)
        
        return header, data
    except Exception as e:
        print(f"讀取CSV檔案錯誤：{e}")
        return [], []

# 使用範例
header, data = read_csv_simple("students.csv")
print(f"欄位：{header}")
for row in data:
    print(row)
```

## 4. 寫入檔案

### 4.1 寫入文字到檔案
```python
# 基本寫入
def write_text_file(filename, content):
    """寫入文字到檔案（覆蓋模式）"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"內容已寫入 {filename}")
        return True
    except Exception as e:
        print(f"寫入檔案錯誤：{e}")
        return False

# 寫入多行
def write_lines_to_file(filename, lines):
    """寫入多行文字到檔案"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"已寫入{len(lines)}行到 {filename}")
        return True
    except Exception as e:
        print(f"寫入檔案錯誤：{e}")
        return False

# 使用範例
content = "這是檔案的內容\n第二行內容\n第三行內容"
write_text_file("output.txt", content)

lines = ["第一行", "第二行", "第三行"]
write_lines_to_file("lines.txt", lines)
```

### 4.2 追加內容到檔案
```python
def append_to_file(filename, content):
    """追加內容到檔案末尾"""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(content + '\n')
        print(f"內容已追加到 {filename}")
        return True
    except Exception as e:
        print(f"追加檔案錯誤：{e}")
        return False

def log_message(filename, message):
    """記錄日誌訊息"""
    import datetime
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    
    return append_to_file(filename, log_entry)

# 使用範例
log_message("app.log", "程式啟動")
log_message("app.log", "使用者登入成功")
log_message("app.log", "檔案處理完成")
```

### 4.3 安全寫入檔案
```python
def safe_write_file(filename, content, backup=True):
    """安全寫入檔案（可選備份）"""
    import shutil
    import os
    
    try:
        # 如果檔案存在且需要備份
        if backup and os.path.exists(filename):
            backup_filename = f"{filename}.backup"
            shutil.copy2(filename, backup_filename)
            print(f"已創建備份：{backup_filename}")
        
        # 寫入內容
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"檔案 {filename} 寫入成功")
        return True
        
    except Exception as e:
        print(f"安全寫入失敗：{e}")
        return False

def write_data_to_csv(filename, data, header=None):
    """寫入資料到CSV檔案"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # 寫入標頭
            if header:
                file.write(','.join(header) + '\n')
            
            # 寫入資料
            for row in data:
                if isinstance(row, dict) and header:
                    values = [str(row.get(col, '')) for col in header]
                elif isinstance(row, (list, tuple)):
                    values = [str(item) for item in row]
                else:
                    continue
                
                file.write(','.join(values) + '\n')
        
        print(f"CSV檔案 {filename} 寫入完成")
        return True
        
    except Exception as e:
        print(f"寫入CSV錯誤：{e}")
        return False

# 使用範例
students_data = [
    {"name": "小明", "age": 18, "grade": "A"},
    {"name": "小美", "age": 17, "grade": "B"},
    {"name": "小華", "age": 18, "grade": "A"}
]

header = ["name", "age", "grade"]
write_data_to_csv("students_output.csv", students_data, header)
```

## 5. 檔案路徑和目錄操作

### 5.1 路徑處理
```python
import os

def demonstrate_path_operations():
    """展示路徑操作"""
    print("📁 檔案路徑操作示範")
    print("-" * 30)
    
    # 當前工作目錄
    current_dir = os.getcwd()
    print(f"當前目錄：{current_dir}")
    
    # 路徑組合
    file_path = os.path.join("data", "files", "example.txt")
    print(f"組合路徑：{file_path}")
    
    # 路徑分析
    example_path = "/home/user/documents/report.pdf"
    print(f"\n路徑分析：{example_path}")
    print(f"目錄名：{os.path.dirname(example_path)}")
    print(f"檔案名：{os.path.basename(example_path)}")
    print(f"檔案名（無副檔名）：{os.path.splitext(os.path.basename(example_path))[0]}")
    print(f"副檔名：{os.path.splitext(example_path)[1]}")
    
    # 絕對路徑和相對路徑
    print(f"\n路徑類型：")
    print(f"絕對路徑：{os.path.abspath('example.txt')}")
    print(f"相對路徑：example.txt")
    
    # 檢查路徑
    print(f"\n路徑檢查：")
    print(f"當前目錄存在：{os.path.exists('.')}")
    print(f"是目錄：{os.path.isdir('.')}")
    print(f"是檔案：{os.path.isfile('example.txt')}")

def ensure_directory_exists(directory):
    """確保目錄存在"""
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"目錄 {directory} 已準備就緒")
        return True
    except Exception as e:
        print(f"創建目錄失敗：{e}")
        return False

def safe_file_path(filename):
    """生成安全的檔案路徑"""
    # 移除不安全的字元
    unsafe_chars = '<>:"/\\|?*'
    safe_name = filename
    
    for char in unsafe_chars:
        safe_name = safe_name.replace(char, '_')
    
    return safe_name
```

### 5.2 目錄操作和檔案清單
```python
def list_files_in_directory(directory='.', pattern='*'):
    """列出目錄中的檔案"""
    import glob
    
    try:
        search_pattern = os.path.join(directory, pattern)
        files = glob.glob(search_pattern)
        
        print(f"目錄 {directory} 中的檔案（符合 {pattern}）：")
        for i, file in enumerate(files, 1):
            file_size = os.path.getsize(file) if os.path.isfile(file) else 0
            file_type = "目錄" if os.path.isdir(file) else "檔案"
            print(f"{i:2d}. {os.path.basename(file)} ({file_type}, {file_size} bytes)")
        
        return files
    except Exception as e:
        print(f"列出檔案錯誤：{e}")
        return []

def get_file_info(filename):
    """取得檔案資訊"""
    import datetime
    
    try:
        if not os.path.exists(filename):
            print(f"檔案 {filename} 不存在")
            return None
        
        stat = os.stat(filename)
        
        info = {
            "檔案名": os.path.basename(filename),
            "完整路徑": os.path.abspath(filename),
            "大小": stat.st_size,
            "創建時間": datetime.datetime.fromtimestamp(stat.st_ctime),
            "修改時間": datetime.datetime.fromtimestamp(stat.st_mtime),
            "是否為目錄": os.path.isdir(filename)
        }
        
        return info
    except Exception as e:
        print(f"取得檔案資訊錯誤：{e}")
        return None

# 使用範例
demonstrate_path_operations()
files = list_files_in_directory('.', '*.py')
for file in files[:3]:  # 只看前3個
    info = get_file_info(file)
    if info:
        print(f"\n檔案資訊：{info['檔案名']}")
        print(f"大小：{info['大小']} bytes")
        print(f"修改時間：{info['修改時間']}")
```

## 6. 編碼處理

### 6.1 文字編碼概念
```python
def demonstrate_encoding():
    """展示編碼處理"""
    print("🔤 文字編碼處理示範")
    print("-" * 30)
    
    # 不同編碼的測試文字
    test_text = "Hello 世界 🌍 Python程式設計"
    
    # 常見編碼
    encodings = ['utf-8', 'utf-16', 'big5', 'gb2312']
    
    print(f"測試文字：{test_text}")
    print("\n不同編碼的位元組數：")
    
    for encoding in encodings:
        try:
            encoded = test_text.encode(encoding)
            print(f"{encoding:>8}：{len(encoded):3d} bytes")
        except UnicodeEncodeError as e:
            print(f"{encoding:>8}：編碼失敗 - {e}")

def read_with_encoding_detection(filename):
    """嘗試不同編碼讀取檔案"""
    encodings = ['utf-8', 'utf-8-sig', 'big5', 'gb2312', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                content = file.read()
                print(f"使用 {encoding} 編碼成功讀取檔案")
                return content, encoding
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"檔案 {filename} 不存在")
            return None, None
    
    print("嘗試所有編碼都失敗")
    return None, None

def write_with_bom(filename, content):
    """寫入帶有BOM的UTF-8檔案"""
    try:
        with open(filename, 'w', encoding='utf-8-sig') as file:
            file.write(content)
        print(f"已寫入UTF-8 BOM檔案：{filename}")
        return True
    except Exception as e:
        print(f"寫入失敗：{e}")
        return False
```

## 7. 實作項目：數位日記程式

### 7.1 功能需求
1. 寫入日記條目
2. 查看歷史日記
3. 搜尋日記內容
4. 編輯已存在的日記
5. 刪除日記條目
6. 匯出日記到不同格式
7. 日記統計和分析

### 7.2 完整實作
```python
import datetime
import os
import json
import glob

class DigitalDiary:
    """數位日記程式"""
    
    def __init__(self, diary_dir="diary_entries"):
        """初始化日記程式"""
        self.diary_dir = diary_dir
        self.ensure_diary_directory()
        
        # 設定檔
        self.config_file = os.path.join(diary_dir, "config.json")
        self.stats_file = os.path.join(diary_dir, "stats.json")
        
        # 載入配置
        self.config = self.load_config()
        self.stats = self.load_stats()
    
    def ensure_diary_directory(self):
        """確保日記目錄存在"""
        try:
            os.makedirs(self.diary_dir, exist_ok=True)
            print(f"📁 日記目錄：{os.path.abspath(self.diary_dir)}")
        except Exception as e:
            print(f"❌ 創建日記目錄失敗：{e}")
    
    def load_config(self):
        """載入配置"""
        default_config = {
            "author": "日記作者",
            "date_format": "%Y-%m-%d",
            "time_format": "%H:%M:%S",
            "auto_backup": True,
            "default_mood": "普通"
        }
        
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # 合併預設配置
                    for key, value in default_config.items():
                        if key not in config:
                            config[key] = value
                    return config
            else:
                self.save_config(default_config)
                return default_config
        except Exception as e:
            print(f"⚠️ 載入配置失敗：{e}")
            return default_config
    
    def save_config(self, config=None):
        """儲存配置"""
        if config is None:
            config = self.config
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ 儲存配置失敗：{e}")
    
    def load_stats(self):
        """載入統計"""
        default_stats = {
            "total_entries": 0,
            "first_entry_date": None,
            "last_entry_date": None,
            "word_count": 0,
            "mood_counts": {}
        }
        
        try:
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return default_stats
        except Exception as e:
            print(f"⚠️ 載入統計失敗：{e}")
            return default_stats
    
    def save_stats(self):
        """儲存統計"""
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ 儲存統計失敗：{e}")
    
    def get_entry_filename(self, date=None):
        """取得日記檔案名稱"""
        if date is None:
            date = datetime.date.today()
        
        if isinstance(date, str):
            # 如果是字串，嘗試解析
            try:
                date = datetime.datetime.strptime(date, self.config["date_format"]).date()
            except ValueError:
                print(f"❌ 日期格式錯誤：{date}")
                return None
        
        filename = f"diary_{date.strftime('%Y_%m_%d')}.txt"
        return os.path.join(self.diary_dir, filename)
    
    def write_entry(self, content, date=None, mood=None):
        """寫入日記條目"""
        if date is None:
            date = datetime.date.today()
        
        filename = self.get_entry_filename(date)
        if not filename:
            return False
        
        try:
            # 準備日記內容
            now = datetime.datetime.now()
            mood = mood or self.config["default_mood"]
            
            # 檢查檔案是否已存在
            file_exists = os.path.exists(filename)
            mode = 'a' if file_exists else 'w'
            
            with open(filename, mode, encoding='utf-8') as f:
                if not file_exists:
                    # 新檔案，寫入標頭
                    f.write(f"📅 日記 - {date.strftime(self.config['date_format'])}\n")
                    f.write(f"✍️  作者：{self.config['author']}\n")
                    f.write("=" * 50 + "\n\n")
                
                # 寫入條目
                f.write(f"🕒 時間：{now.strftime(self.config['time_format'])}\n")
                f.write(f"😊 心情：{mood}\n")
                f.write("-" * 30 + "\n")
                f.write(content)
                f.write("\n\n" + "=" * 50 + "\n\n")
            
            # 更新統計
            self.update_stats(date, content, mood)
            
            print(f"✅ 日記已儲存：{filename}")
            return True
            
        except Exception as e:
            print(f"❌ 寫入日記失敗：{e}")
            return False
    
    def read_entry(self, date=None):
        """讀取日記條目"""
        if date is None:
            date = datetime.date.today()
        
        filename = self.get_entry_filename(date)
        if not filename:
            return None
        
        try:
            if not os.path.exists(filename):
                print(f"📝 {date.strftime(self.config['date_format'])} 沒有日記條目")
                return None
            
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                return content
                
        except Exception as e:
            print(f"❌ 讀取日記失敗：{e}")
            return None
    
    def list_all_entries(self):
        """列出所有日記條目"""
        try:
            pattern = os.path.join(self.diary_dir, "diary_*.txt")
            diary_files = glob.glob(pattern)
            
            if not diary_files:
                print("📝 還沒有任何日記條目")
                return []
            
            # 解析日期並排序
            entries = []
            for file in diary_files:
                try:
                    filename = os.path.basename(file)
                    date_part = filename.replace('diary_', '').replace('.txt', '')
                    date = datetime.datetime.strptime(date_part, '%Y_%m_%d').date()
                    
                    # 取得檔案資訊
                    stat = os.stat(file)
                    size = stat.st_size
                    modified = datetime.datetime.fromtimestamp(stat.st_mtime)
                    
                    entries.append({
                        'date': date,
                        'filename': file,
                        'size': size,
                        'modified': modified
                    })
                except ValueError:
                    continue
            
            # 按日期排序（最新的在前）
            entries.sort(key=lambda x: x['date'], reverse=True)
            
            return entries
            
        except Exception as e:
            print(f"❌ 列出日記失敗：{e}")
            return []
    
    def search_entries(self, keyword, case_sensitive=False):
        """搜尋日記條目"""
        try:
            results = []
            all_entries = self.list_all_entries()
            
            for entry in all_entries:
                try:
                    with open(entry['filename'], 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        search_content = content if case_sensitive else content.lower()
                        search_keyword = keyword if case_sensitive else keyword.lower()
                        
                        if search_keyword in search_content:
                            # 找出關鍵字所在的行
                            lines = content.split('\n')
                            matching_lines = []
                            
                            for i, line in enumerate(lines, 1):
                                check_line = line if case_sensitive else line.lower()
                                if search_keyword in check_line:
                                    matching_lines.append((i, line.strip()))
                            
                            results.append({
                                'date': entry['date'],
                                'filename': entry['filename'],
                                'matching_lines': matching_lines
                            })
                            
                except Exception:
                    continue
            
            return results
            
        except Exception as e:
            print(f"❌ 搜尋失敗：{e}")
            return []
    
    def delete_entry(self, date):
        """刪除日記條目"""
        filename = self.get_entry_filename(date)
        if not filename:
            return False
        
        try:
            if not os.path.exists(filename):
                print(f"📝 {date.strftime(self.config['date_format'])} 沒有日記可刪除")
                return False
            
            # 詢問確認
            date_str = date.strftime(self.config['date_format'])
            confirm = input(f"確定要刪除 {date_str} 的日記嗎？(y/N): ").strip().lower()
            
            if confirm == 'y':
                # 備份
                if self.config["auto_backup"]:
                    backup_filename = filename + ".backup"
                    import shutil
                    shutil.copy2(filename, backup_filename)
                    print(f"📦 已創建備份：{backup_filename}")
                
                os.remove(filename)
                print(f"🗑️ 已刪除 {date_str} 的日記")
                return True
            else:
                print("❌ 取消刪除")
                return False
                
        except Exception as e:
            print(f"❌ 刪除失敗：{e}")
            return False
    
    def update_stats(self, date, content, mood):
        """更新統計資訊"""
        try:
            self.stats["total_entries"] += 1
            
            # 日期統計
            date_str = date.strftime(self.config["date_format"])
            if not self.stats["first_entry_date"]:
                self.stats["first_entry_date"] = date_str
            self.stats["last_entry_date"] = date_str
            
            # 字數統計
            word_count = len(content.split())
            self.stats["word_count"] += word_count
            
            # 心情統計
            if mood not in self.stats["mood_counts"]:
                self.stats["mood_counts"][mood] = 0
            self.stats["mood_counts"][mood] += 1
            
            self.save_stats()
            
        except Exception as e:
            print(f"⚠️ 更新統計失敗：{e}")
    
    def get_statistics(self):
        """取得統計資訊"""
        return self.stats.copy()
    
    def export_diary(self, format='txt', date_range=None):
        """匯出日記"""
        try:
            all_entries = self.list_all_entries()
            
            if not all_entries:
                print("📝 沒有日記可匯出")
                return None
            
            # 過濾日期範圍
            if date_range:
                start_date, end_date = date_range
                all_entries = [
                    entry for entry in all_entries 
                    if start_date <= entry['date'] <= end_date
                ]
            
            if not all_entries:
                print("📝 指定範圍內沒有日記")
                return None
            
            # 產生匯出檔名
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            export_filename = f"diary_export_{timestamp}.{format}"
            export_path = os.path.join(self.diary_dir, export_filename)
            
            if format == 'txt':
                self._export_txt(all_entries, export_path)
            elif format == 'html':
                self._export_html(all_entries, export_path)
            elif format == 'json':
                self._export_json(all_entries, export_path)
            else:
                print(f"❌ 不支援的格式：{format}")
                return None
            
            print(f"📦 日記已匯出：{export_path}")
            return export_path
            
        except Exception as e:
            print(f"❌ 匯出失敗：{e}")
            return None
    
    def _export_txt(self, entries, filename):
        """匯出為文字檔"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"📚 {self.config['author']} 的日記集\n")
            f.write(f"📅 匯出時間：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            
            for entry in reversed(entries):  # 按時間順序
                try:
                    with open(entry['filename'], 'r', encoding='utf-8') as diary_file:
                        content = diary_file.read()
                        f.write(content)
                        f.write("\n" + "=" * 60 + "\n\n")
                except Exception:
                    continue
    
    def _export_html(self, entries, filename):
        """匯出為HTML檔"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的日記</title>
    <style>
        body { font-family: 'Microsoft JhengHei', Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }
        .diary-entry { background: white; margin-bottom: 20px; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .date { color: #2c3e50; font-size: 18px; font-weight: bold; margin-bottom: 10px; }
        .content { line-height: 1.6; white-space: pre-wrap; }
        .header { text-align: center; margin-bottom: 30px; }
    </style>
</head>
<body>""")
            
            f.write(f"""
    <div class="header">
        <h1>📚 {self.config['author']} 的日記</h1>
        <p>📅 匯出時間：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
""")
            
            for entry in reversed(entries):
                try:
                    with open(entry['filename'], 'r', encoding='utf-8') as diary_file:
                        content = diary_file.read()
                        date_str = entry['date'].strftime('%Y年%m月%d日')
                        
                        f.write(f"""
    <div class="diary-entry">
        <div class="date">{date_str}</div>
        <div class="content">{content}</div>
    </div>
""")
                except Exception:
                    continue
            
            f.write("</body></html>")
    
    def _export_json(self, entries, filename):
        """匯出為JSON檔"""
        export_data = {
            "author": self.config['author'],
            "export_time": datetime.datetime.now().isoformat(),
            "total_entries": len(entries),
            "entries": []
        }
        
        for entry in entries:
            try:
                with open(entry['filename'], 'r', encoding='utf-8') as diary_file:
                    content = diary_file.read()
                    
                    entry_data = {
                        "date": entry['date'].isoformat(),
                        "content": content,
                        "file_size": entry['size'],
                        "modified": entry['modified'].isoformat()
                    }
                    export_data["entries"].append(entry_data)
            except Exception:
                continue
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)

def main():
    """主程式"""
    print("📖 歡迎使用數位日記程式！")
    
    diary = DigitalDiary()
    
    while True:
        print("\n" + "=" * 50)
        print("📚 數位日記選單")
        print("=" * 50)
        print("1. ✍️  寫日記")
        print("2. 📖 讀日記")
        print("3. 📋 列出所有日記")
        print("4. 🔍 搜尋日記")
        print("5. 🗑️  刪除日記")
        print("6. 📊 日記統計")
        print("7. 📦 匯出日記")
        print("8. ⚙️  設定")
        print("0. 🚪 退出")
        print("-" * 50)
        
        try:
            choice = input("請選擇功能 (0-8): ").strip()
            
            if choice == "0":
                print("\n👋 感謝使用數位日記程式！")
                break
            elif choice == "1":
                write_diary_interface(diary)
            elif choice == "2":
                read_diary_interface(diary)
            elif choice == "3":
                list_entries_interface(diary)
            elif choice == "4":
                search_diary_interface(diary)
            elif choice == "5":
                delete_diary_interface(diary)
            elif choice == "6":
                show_statistics_interface(diary)
            elif choice == "7":
                export_diary_interface(diary)
            elif choice == "8":
                settings_interface(diary)
            else:
                print("❌ 無效選擇")
        
        except KeyboardInterrupt:
            print("\n\n程式被中斷")
            break
        except Exception as e:
            print(f"❌ 發生錯誤：{e}")
        
        if choice != "0":
            input("\n按 Enter 繼續...")

# 介面函數
def write_diary_interface(diary):
    """寫日記介面"""
    print("\n✍️ 寫日記")
    print("-" * 20)
    
    # 選擇日期
    date_input = input("日期 (YYYY-MM-DD，直接按 Enter 使用今天): ").strip()
    
    if date_input:
        try:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("❌ 日期格式錯誤")
            return
    else:
        date = datetime.date.today()
    
    # 選擇心情
    moods = ["開心", "普通", "難過", "生氣", "興奮", "焦慮", "平靜", "其他"]
    print(f"\n心情選擇：")
    for i, mood in enumerate(moods, 1):
        print(f"{i}. {mood}")
    
    mood_choice = input("選擇心情 (1-8，直接按 Enter 使用預設): ").strip()
    
    if mood_choice and mood_choice.isdigit():
        mood_index = int(mood_choice) - 1
        if 0 <= mood_index < len(moods):
            mood = moods[mood_index]
        else:
            mood = diary.config["default_mood"]
    else:
        mood = diary.config["default_mood"]
    
    # 輸入內容
    print(f"\n請輸入日記內容 (按 Ctrl+D 或輸入空行結束):")
    
    content_lines = []
    try:
        while True:
            line = input()
            if not line.strip():  # 空行結束
                break
            content_lines.append(line)
    except EOFError:
        pass
    
    if not content_lines:
        print("❌ 沒有輸入內容")
        return
    
    content = "\n".join(content_lines)
    
    # 儲存日記
    success = diary.write_entry(content, date, mood)
    if success:
        print(f"✅ {date.strftime('%Y-%m-%d')} 的日記已儲存")
        print(f"📝 字數：{len(content.split())} 字")
        print(f"😊 心情：{mood}")

def read_diary_interface(diary):
    """讀日記介面"""
    print("\n📖 讀日記")
    print("-" * 20)
    
    date_input = input("請輸入日期 (YYYY-MM-DD，直接按 Enter 使用今天): ").strip()
    
    if date_input:
        try:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("❌ 日期格式錯誤")
            return
    else:
        date = datetime.date.today()
    
    content = diary.read_entry(date)
    if content:
        print(f"\n📖 {date.strftime('%Y-%m-%d')} 的日記：")
        print("=" * 50)
        print(content)
    else:
        print(f"📝 {date.strftime('%Y-%m-%d')} 沒有日記條目")

def list_entries_interface(diary):
    """列出日記介面"""
    print("\n📋 所有日記條目")
    print("-" * 30)
    
    entries = diary.list_all_entries()
    
    if not entries:
        print("📝 還沒有任何日記條目")
        return
    
    print(f"共找到 {len(entries)} 篇日記：\n")
    print(f"{'序號':<4} {'日期':<12} {'大小':<8} {'修改時間'}")
    print("-" * 40)
    
    for i, entry in enumerate(entries, 1):
        date_str = entry['date'].strftime('%Y-%m-%d')
        size_str = f"{entry['size']} B"
        modified_str = entry['modified'].strftime('%m-%d %H:%M')
        
        print(f"{i:<4} {date_str:<12} {size_str:<8} {modified_str}")
    
    # 詢問是否要讀取特定日記
    choice = input(f"\n輸入序號閱讀日記 (1-{len(entries)})，直接按 Enter 返回: ").strip()
    
    if choice and choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(entries):
            selected_entry = entries[index]
            content = diary.read_entry(selected_entry['date'])
            if content:
                print(f"\n📖 {selected_entry['date'].strftime('%Y-%m-%d')} 的日記：")
                print("=" * 50)
                print(content)

def search_diary_interface(diary):
    """搜尋日記介面"""
    print("\n🔍 搜尋日記")
    print("-" * 20)
    
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
    
    print(f"📋 找到 {len(results)} 篇相關日記：\n")
    
    for i, result in enumerate(results, 1):
        date_str = result['date'].strftime('%Y-%m-%d')
        print(f"{i}. {date_str} (找到 {len(result['matching_lines'])} 處)")
        
        # 顯示前3個匹配行
        for line_num, line_content in result['matching_lines'][:3]:
            if line_content.strip():
                print(f"   第{line_num}行: {line_content[:50]}...")
        
        if len(result['matching_lines']) > 3:
            print(f"   ... 還有 {len(result['matching_lines']) - 3} 處匹配")
        print()

def delete_diary_interface(diary):
    """刪除日記介面"""
    print("\n🗑️ 刪除日記")
    print("-" * 20)
    
    date_input = input("請輸入要刪除的日期 (YYYY-MM-DD): ").strip()
    
    if not date_input:
        print("❌ 請輸入日期")
        return
    
    try:
        date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        diary.delete_entry(date)
    except ValueError:
        print("❌ 日期格式錯誤")

def show_statistics_interface(diary):
    """顯示統計介面"""
    print("\n📊 日記統計")
    print("-" * 20)
    
    stats = diary.get_statistics()
    
    if stats["total_entries"] == 0:
        print("📝 還沒有日記條目")
        return
    
    print(f"📈 總體統計：")
    print(f"  📝 總條目數：{stats['total_entries']}")
    print(f"  📅 第一篇：{stats['first_entry_date']}")
    print(f"  📅 最新篇：{stats['last_entry_date']}")
    print(f"  📝 總字數：{stats['word_count']}")
    
    if stats['word_count'] > 0:
        avg_words = stats['word_count'] / stats['total_entries']
        print(f"  📝 平均字數：{avg_words:.1f}")
    
    # 心情統計
    if stats['mood_counts']:
        print(f"\n😊 心情分佈：")
        sorted_moods = sorted(stats['mood_counts'].items(), key=lambda x: x[1], reverse=True)
        for mood, count in sorted_moods:
            percentage = (count / stats['total_entries']) * 100
            print(f"  {mood}: {count} 次 ({percentage:.1f}%)")
    
    # 寫作活躍度（最近7天）
    try:
        recent_entries = 0
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)
        
        all_entries = diary.list_all_entries()
        for entry in all_entries:
            if entry['date'] >= week_ago:
                recent_entries += 1
        
        print(f"\n📈 最近7天活躍度：")
        print(f"  寫作天數：{recent_entries} 天")
        if recent_entries > 0:
            print(f"  平均每天：{recent_entries/7:.1f} 篇")
    except Exception:
        pass

def export_diary_interface(diary):
    """匯出日記介面"""
    print("\n📦 匯出日記")
    print("-" * 20)
    
    # 選擇格式
    formats = ["txt", "html", "json"]
    print("選擇匯出格式：")
    for i, fmt in enumerate(formats, 1):
        print(f"{i}. {fmt.upper()}")
    
    format_choice = input("請選擇 (1-3): ").strip()
    
    if not format_choice.isdigit() or not 1 <= int(format_choice) <= 3:
        print("❌ 無效選擇")
        return
    
    format_type = formats[int(format_choice) - 1]
    
    # 選擇日期範圍
    range_choice = input("是否指定日期範圍？(y/N): ").strip().lower()
    date_range = None
    
    if range_choice == 'y':
        try:
            start_str = input("開始日期 (YYYY-MM-DD): ").strip()
            end_str = input("結束日期 (YYYY-MM-DD): ").strip()
            
            start_date = datetime.datetime.strptime(start_str, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_str, "%Y-%m-%d").date()
            
            if start_date > end_date:
                print("❌ 開始日期不能晚於結束日期")
                return
            
            date_range = (start_date, end_date)
        except ValueError:
            print("❌ 日期格式錯誤")
            return
    
    # 執行匯出
    export_path = diary.export_diary(format_type, date_range)
    
    if export_path:
        print(f"✅ 匯出完成！")
        print(f"📁 檔案位置：{export_path}")

def settings_interface(diary):
    """設定介面"""
    print("\n⚙️ 日記設定")
    print("-" * 20)
    
    config = diary.config
    
    print("目前設定：")
    print(f"1. 作者：{config['author']}")
    print(f"2. 日期格式：{config['date_format']}")
    print(f"3. 時間格式：{config['time_format']}")
    print(f"4. 自動備份：{'是' if config['auto_backup'] else '否'}")
    print(f"5. 預設心情：{config['default_mood']}")
    
    choice = input("\n選擇要修改的設定 (1-5)，直接按 Enter 返回: ").strip()
    
    if not choice:
        return
    
    if choice == "1":
        new_author = input(f"新作者名稱 (目前：{config['author']}): ").strip()
        if new_author:
            config['author'] = new_author
            
    elif choice == "2":
        print("常用日期格式：")
        print("  %Y-%m-%d (2024-01-15)")
        print("  %Y年%m月%d日 (2024年01月15日)")
        print("  %m/%d/%Y (01/15/2024)")
        new_format = input(f"新日期格式 (目前：{config['date_format']}): ").strip()
        if new_format:
            config['date_format'] = new_format
            
    elif choice == "3":
        print("常用時間格式：")
        print("  %H:%M:%S (14:30:00)")
        print("  %H:%M (14:30)")
        print("  %I:%M %p (02:30 PM)")
        new_format = input(f"新時間格式 (目前：{config['time_format']}): ").strip()
        if new_format:
            config['time_format'] = new_format
            
    elif choice == "4":
        backup_choice = input("啟用自動備份？(y/N): ").strip().lower()
        config['auto_backup'] = (backup_choice == 'y')
        
    elif choice == "5":
        moods = ["開心", "普通", "難過", "生氣", "興奮", "焦慮", "平靜"]
        print("心情選項：")
        for i, mood in enumerate(moods, 1):
            print(f"  {i}. {mood}")
        
        mood_choice = input("選擇預設心情 (1-7): ").strip()
        if mood_choice.isdigit():
            mood_index = int(mood_choice) - 1
            if 0 <= mood_index < len(moods):
                config['default_mood'] = moods[mood_index]
    
    else:
        print("❌ 無效選擇")
        return
    
    # 儲存設定
    diary.save_config()
    print("✅ 設定已儲存")

if __name__ == "__main__":
    main()
```

## 8. 今日總結

今天你學會了：
- ✅ 檔案處理的基本概念和重要性
- ✅ 讀取和寫入文字檔案的各種方法
- ✅ 不同檔案開啟模式的使用場景
- ✅ 檔案路徑處理和編碼問題
- ✅ 實作完整的數位日記程式

**關鍵概念回顧：**
- 使用with語句確保檔案正確關閉
- 不同模式適用於不同的檔案操作需求
- 編碼處理對中文內容很重要
- 檔案操作需要適當的錯誤處理

**明天預告：**
我們將學習錯誤處理，了解如何優雅地處理程式中的異常情況，讓檔案操作更加安全可靠！

記住：**檔案處理讓程式能夠持久保存資料，是實用程式的重要基礎！**