#!/usr/bin/env python3
"""
Day 20: Safe File Manager
A comprehensive file management program demonstrating robust error handling

This program showcases:
- Safe file operations with proper exception handling
- User input validation with retry mechanisms
- Error logging and recovery strategies
- Graceful handling of various file system errors
- Professional-grade error messages and user feedback

Think of this as a bulletproof file manager that never crashes!
"""

import os
import json
import shutil
import datetime
from pathlib import Path


class SafeFileManager:
    """
    A robust file manager that handles errors gracefully
    Like having a professional assistant who never panics
    """
    
    def __init__(self, working_dir="managed_files"):
        """
        Initialize the file manager with error handling
        """
        self.working_dir = Path(working_dir)
        self.log_file = "file_manager_log.txt"
        self.config_file = "file_manager_config.json"
        
        # Ensure working directory exists
        self.ensure_directory_exists(self.working_dir)
        
        # Load configuration with error handling
        self.config = self.load_config()
        
        print(f"Safe File Manager initialized successfully!")
        print(f"Working directory: {self.working_dir.absolute()}")
    
    def ensure_directory_exists(self, directory_path):
        """
        Create directory if it doesn't exist, with error handling
        """
        try:
            directory_path.mkdir(parents=True, exist_ok=True)
            return True
        except PermissionError:
            self.log_error(f"Permission denied creating directory: {directory_path}")
            print(f"Error: No permission to create directory '{directory_path}'")
            return False
        except OSError as e:
            self.log_error(f"OS error creating directory {directory_path}: {e}")
            print(f"Error: Could not create directory '{directory_path}': {e}")
            return False
    
    def log_error(self, message):
        """
        Log errors with timestamp for debugging
        Like keeping a record of what went wrong
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] ERROR: {message}\n"
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as log:
                log.write(log_entry)
        except Exception as e:
            # If we can't write to log file, at least print it
            print(f"Could not write to log file: {log_entry.strip()}")
            print(f"Log write error: {e}")
    
    def log_info(self, message):
        """
        Log information messages
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] INFO: {message}\n"
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as log:
                log.write(log_entry)
        except Exception:
            pass  # Don't worry if info logging fails
    
    def load_config(self):
        """
        Load configuration with fallback to defaults
        """
        default_config = {
            "max_file_size_mb": 100,
            "allowed_extensions": [".txt", ".json", ".csv", ".py", ".md"],
            "backup_enabled": True,
            "auto_backup_interval": 24
        }
        
        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
                self.log_info("Configuration loaded successfully")
                return config
        except FileNotFoundError:
            self.log_info("No config file found, using defaults")
            self.save_config(default_config)
            return default_config
        except json.JSONDecodeError as e:
            self.log_error(f"Config file corrupted: {e}")
            print("Config file is corrupted. Using default settings.")
            return default_config
        except Exception as e:
            self.log_error(f"Error loading config: {e}")
            return default_config
    
    def save_config(self, config=None):
        """
        Save configuration with error handling
        """
        config_to_save = config if config else self.config
        
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(config_to_save, f, indent=2)
            return True
        except PermissionError:
            self.log_error("Permission denied saving config")
            print("Error: No permission to save configuration")
            return False
        except Exception as e:
            self.log_error(f"Error saving config: {e}")
            print(f"Error saving configuration: {e}")
            return False
    
    def safe_read_file(self, filename):
        """
        Safely read a file with comprehensive error handling
        """
        file_path = self.working_dir / filename
        
        try:
            # Check if file exists
            if not file_path.exists():
                print(f"Error: File '{filename}' does not exist")
                return None
            
            # Check file size (prevent reading huge files)
            file_size_mb = file_path.stat().st_size / (1024 * 1024)
            if file_size_mb > self.config.get("max_file_size_mb", 100):
                print(f"Error: File '{filename}' is too large ({file_size_mb:.1f}MB)")
                return None
            
            # Try to read the file
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.log_info(f"Successfully read file: {filename}")
                return content
                
        except PermissionError:
            self.log_error(f"Permission denied reading file: {filename}")
            print(f"Error: No permission to read '{filename}'")
            return None
        except UnicodeDecodeError as e:
            self.log_error(f"Encoding error reading {filename}: {e}")
            print(f"Error: Cannot read '{filename}' - encoding issue")
            
            # Try with different encoding
            try:
                with open(file_path, "r", encoding="latin1") as f:
                    content = f.read()
                    print(f"Warning: Read '{filename}' with latin1 encoding")
                    return content
            except Exception:
                print(f"Could not read '{filename}' with any encoding")
                return None
        except Exception as e:
            self.log_error(f"Unexpected error reading {filename}: {e}")
            print(f"Unexpected error reading '{filename}': {e}")
            return None
    
    def safe_write_file(self, filename, content, overwrite=False):
        """
        Safely write content to a file with error handling
        """
        file_path = self.working_dir / filename
        
        try:
            # Check if file exists and overwrite is not allowed
            if file_path.exists() and not overwrite:
                response = self.get_user_confirmation(
                    f"File '{filename}' already exists. Overwrite? (y/n): "
                )
                if not response:
                    print("Write operation cancelled")
                    return False
            
            # Check file extension
            file_extension = file_path.suffix.lower()
            allowed_extensions = self.config.get("allowed_extensions", [])
            if allowed_extensions and file_extension not in allowed_extensions:
                print(f"Warning: '{file_extension}' is not in allowed extensions")
                response = self.get_user_confirmation("Continue anyway? (y/n): ")
                if not response:
                    print("Write operation cancelled")
                    return False
            
            # Create backup if file exists and backup is enabled
            if file_path.exists() and self.config.get("backup_enabled", True):
                self.create_backup(filename)
            
            # Write the file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            self.log_info(f"Successfully wrote file: {filename}")
            print(f"File '{filename}' written successfully!")
            return True
            
        except PermissionError:
            self.log_error(f"Permission denied writing file: {filename}")
            print(f"Error: No permission to write '{filename}'")
            return False
        except OSError as e:
            self.log_error(f"OS error writing {filename}: {e}")
            print(f"Error: Could not write '{filename}': {e}")
            return False
        except Exception as e:
            self.log_error(f"Unexpected error writing {filename}: {e}")
            print(f"Unexpected error writing '{filename}': {e}")
            return False
    
    def create_backup(self, filename):
        """
        Create a backup copy of a file
        """
        source_path = self.working_dir / filename
        backup_dir = self.working_dir / "backups"
        
        try:
            # Ensure backup directory exists
            if not self.ensure_directory_exists(backup_dir):
                return False
            
            # Create backup filename with timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{source_path.stem}_{timestamp}{source_path.suffix}"
            backup_path = backup_dir / backup_name
            
            # Copy the file
            shutil.copy2(source_path, backup_path)
            self.log_info(f"Created backup: {backup_name}")
            print(f"Backup created: {backup_name}")
            return True
            
        except Exception as e:
            self.log_error(f"Error creating backup for {filename}: {e}")
            print(f"Warning: Could not create backup for '{filename}': {e}")
            return False
    
    def safe_delete_file(self, filename):
        """
        Safely delete a file with confirmation and backup
        """
        file_path = self.working_dir / filename
        
        try:
            # Check if file exists
            if not file_path.exists():
                print(f"Error: File '{filename}' does not exist")
                return False
            
            # Get user confirmation
            print(f"File details:")
            print(f"  Size: {file_path.stat().st_size} bytes")
            print(f"  Modified: {datetime.datetime.fromtimestamp(file_path.stat().st_mtime)}")
            
            confirmation = self.get_user_confirmation(
                f"Are you sure you want to delete '{filename}'? (y/n): "
            )
            if not confirmation:
                print("Delete operation cancelled")
                return False
            
            # Create backup before deleting
            if self.config.get("backup_enabled", True):
                self.create_backup(filename)
            
            # Delete the file
            file_path.unlink()
            self.log_info(f"Successfully deleted file: {filename}")
            print(f"File '{filename}' deleted successfully!")
            return True
            
        except PermissionError:
            self.log_error(f"Permission denied deleting file: {filename}")
            print(f"Error: No permission to delete '{filename}'")
            return False
        except Exception as e:
            self.log_error(f"Error deleting {filename}: {e}")
            print(f"Error deleting '{filename}': {e}")
            return False
    
    def list_files(self):
        """
        List all files in the working directory with error handling
        """
        try:
            files = []
            for item in self.working_dir.iterdir():
                if item.is_file():
                    file_info = {
                        'name': item.name,
                        'size': item.stat().st_size,
                        'modified': datetime.datetime.fromtimestamp(item.stat().st_mtime)
                    }
                    files.append(file_info)
            
            if not files:
                print("No files found in the working directory")
                return []
            
            print(f"\nFiles in {self.working_dir}:")
            print("-" * 60)
            for file_info in sorted(files, key=lambda x: x['name']):
                print(f"{file_info['name']:<30} {file_info['size']:>8} bytes  {file_info['modified'].strftime('%Y-%m-%d %H:%M')}")
            print("-" * 60)
            
            return files
            
        except PermissionError:
            self.log_error("Permission denied listing directory")
            print("Error: No permission to list directory contents")
            return []
        except Exception as e:
            self.log_error(f"Error listing files: {e}")
            print(f"Error listing files: {e}")
            return []
    
    def get_user_confirmation(self, prompt):
        """
        Get user confirmation with input validation
        """
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                response = input(prompt).strip().lower()
                if response in ['y', 'yes']:
                    return True
                elif response in ['n', 'no']:
                    return False
                else:
                    if attempt < max_attempts - 1:
                        print("Please enter 'y' for yes or 'n' for no")
                    else:
                        print("Too many invalid attempts. Assuming 'no'.")
                        return False
            except (EOFError, KeyboardInterrupt):
                print("\nOperation cancelled by user")
                return False
        return False
    
    def get_valid_filename(self, prompt="Enter filename: "):
        """
        Get a valid filename from user with validation
        """
        max_attempts = 3
        invalid_chars = '<>:"/\\|?*'
        
        for attempt in range(max_attempts):
            try:
                filename = input(prompt).strip()
                
                # Check for empty input
                if not filename:
                    if attempt < max_attempts - 1:
                        print("Filename cannot be empty")
                        continue
                    else:
                        return None
                
                # Check for invalid characters
                if any(char in filename for char in invalid_chars):
                    if attempt < max_attempts - 1:
                        print(f"Filename cannot contain: {invalid_chars}")
                        continue
                    else:
                        return None
                
                # Check length
                if len(filename) > 255:
                    if attempt < max_attempts - 1:
                        print("Filename too long (max 255 characters)")
                        continue
                    else:
                        return None
                
                return filename
                
            except (EOFError, KeyboardInterrupt):
                print("\nOperation cancelled by user")
                return None
        
        print("Too many invalid attempts")
        return None
    
    def search_files(self, search_term):
        """
        Search for files containing a specific term
        """
        try:
            matching_files = []
            
            for file_path in self.working_dir.glob("*"):
                if file_path.is_file():
                    try:
                        content = self.safe_read_file(file_path.name)
                        if content and search_term.lower() in content.lower():
                            matching_files.append(file_path.name)
                    except Exception:
                        # Skip files that can't be read
                        continue
            
            if matching_files:
                print(f"\nFiles containing '{search_term}':")
                for filename in matching_files:
                    print(f"  - {filename}")
            else:
                print(f"No files found containing '{search_term}'")
            
            return matching_files
            
        except Exception as e:
            self.log_error(f"Error searching files: {e}")
            print(f"Error during search: {e}")
            return []
    
    def show_file_stats(self):
        """
        Show statistics about managed files
        """
        try:
            files = list(self.working_dir.glob("*"))
            total_files = sum(1 for f in files if f.is_file())
            total_dirs = sum(1 for f in files if f.is_dir())
            
            if total_files == 0:
                print("No files to analyze")
                return
            
            # Calculate total size
            total_size = 0
            file_types = {}
            
            for file_path in files:
                if file_path.is_file():
                    try:
                        size = file_path.stat().st_size
                        total_size += size
                        
                        ext = file_path.suffix.lower() or 'no extension'
                        file_types[ext] = file_types.get(ext, 0) + 1
                    except Exception:
                        continue
            
            print(f"\nFile Statistics:")
            print(f"Total files: {total_files}")
            print(f"Total directories: {total_dirs}")
            print(f"Total size: {total_size:,} bytes ({total_size / (1024*1024):.1f} MB)")
            
            print(f"\nFile types:")
            for ext, count in sorted(file_types.items()):
                print(f"  {ext}: {count} files")
            
        except Exception as e:
            self.log_error(f"Error generating file stats: {e}")
            print(f"Error generating statistics: {e}")


def main():
    """
    Main function demonstrating the Safe File Manager
    """
    print("=" * 60)
    print("    SAFE FILE MANAGER - Error Handling Demo")
    print("=" * 60)
    print("This program demonstrates robust error handling in file operations")
    print("Try various operations to see how errors are handled gracefully!")
    print()
    
    # Initialize the file manager
    try:
        manager = SafeFileManager()
    except Exception as e:
        print(f"Fatal error initializing file manager: {e}")
        return
    
    # Demo operations with error handling
    while True:
        print("\n" + "=" * 40)
        print("SAFE FILE MANAGER MENU")
        print("=" * 40)
        print("1. List files")
        print("2. Read file")
        print("3. Write file")
        print("4. Delete file")
        print("5. Search files")
        print("6. Show file statistics")
        print("7. Create test files (for demo)")
        print("8. Test error scenarios")
        print("9. Exit")
        
        try:
            choice = input("\nSelect option (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye!")
            break
        
        if choice == "1":
            manager.list_files()
        
        elif choice == "2":
            filename = manager.get_valid_filename("Enter filename to read: ")
            if filename:
                content = manager.safe_read_file(filename)
                if content:
                    print(f"\n--- Content of {filename} ---")
                    print(content[:500] + ("..." if len(content) > 500 else ""))
        
        elif choice == "3":
            filename = manager.get_valid_filename("Enter filename to write: ")
            if filename:
                print("Enter content (press Enter twice to finish):")
                content_lines = []
                while True:
                    try:
                        line = input()
                        if line == "" and len(content_lines) > 0 and content_lines[-1] == "":
                            break
                        content_lines.append(line)
                    except (EOFError, KeyboardInterrupt):
                        break
                
                content = "\n".join(content_lines)
                manager.safe_write_file(filename, content)
        
        elif choice == "4":
            filename = manager.get_valid_filename("Enter filename to delete: ")
            if filename:
                manager.safe_delete_file(filename)
        
        elif choice == "5":
            search_term = input("Enter search term: ").strip()
            if search_term:
                manager.search_files(search_term)
        
        elif choice == "6":
            manager.show_file_stats()
        
        elif choice == "7":
            # Create test files for demonstration
            test_files = [
                ("hello.txt", "Hello, World!\nThis is a test file."),
                ("data.json", '{"name": "John", "age": 30, "city": "New York"}'),
                ("notes.md", "# My Notes\n\nThis is a markdown file with some notes."),
                ("script.py", "#!/usr/bin/env python3\nprint('Hello from Python!')")
            ]
            
            for filename, content in test_files:
                if manager.safe_write_file(filename, content, overwrite=True):
                    print(f"Created test file: {filename}")
        
        elif choice == "8":
            # Demonstrate error handling scenarios
            print("\n--- Testing Error Scenarios ---")
            print("1. Trying to read non-existent file...")
            manager.safe_read_file("nonexistent_file.txt")
            
            print("\n2. Trying to write to invalid filename...")
            manager.safe_write_file("invalid<>filename.txt", "test content")
            
            print("\n3. Searching for files...")
            manager.search_files("test")
        
        elif choice == "9":
            print("\nThank you for using Safe File Manager!")
            break
        
        else:
            print("Invalid option. Please select 1-9.")


if __name__ == "__main__":
    main()