# Day 20: Error Handling - Making Your Code Bulletproof

Welcome to Day 20! Today we're learning about error handling - one of the most important skills for writing reliable, professional code. Think of error handling like having safety nets and emergency procedures in place.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Understand what errors and exceptions are
- Use try/except blocks to handle errors gracefully
- Create user-friendly error messages
- Write robust file operations that won't crash
- Implement proper error logging and recovery

## 🤔 What Are Errors and Why Handle Them?

### The Problem with Unhandled Errors

Imagine you're running a restaurant, and a customer orders something that's out of stock. Without proper procedures:
- The waiter panics and runs away
- The kitchen shuts down completely
- All other customers are left confused

This is what happens when your program encounters an error without proper handling - it crashes completely!

### Types of Errors

```python
# Syntax Error - like speaking broken English
print("Hello World"  # Missing closing parenthesis

# Runtime Error - happens while program is running
number = int("not a number")  # ValueError

# Logic Error - program runs but does wrong thing
def calculate_average(numbers):
    return sum(numbers) / len(numbers) + 1  # Wrong formula!
```

## 🛡️ The try/except Safety Net

### Basic Syntax

Think of try/except like having a backup plan:

```python
try:
    # Try to do something risky
    risky_operation()
except:
    # If anything goes wrong, do this instead
    handle_the_problem()
```

### Real Example: Safe Division

```python
def safe_divide(a, b):
    """
    Safely divide two numbers with error handling
    Like having a calculator that doesn't break when you divide by zero
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers!")
        return None

# Test it out
print(safe_divide(10, 2))    # Works fine: 5.0
print(safe_divide(10, 0))    # Handles zero division gracefully
print(safe_divide(10, "2"))  # Handles wrong type gracefully
```

## 📁 Safe File Operations

File operations are particularly prone to errors. Here's how to handle them:

### The Problem Without Error Handling

```python
# Dangerous code that can crash your program
file = open("nonexistent_file.txt", "r")  # FileNotFoundError!
content = file.read()
file.close()
```

### The Safe Way

```python
def read_file_safely(filename):
    """
    Safely read a file with proper error handling
    Like checking if a door is unlocked before trying to open it
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
        return None
    except UnicodeDecodeError:
        print(f"Error: Cannot read '{filename}' - encoding issue.")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {e}")
        return None

# Usage
content = read_file_safely("my_document.txt")
if content:
    print("File read successfully!")
    print(content)
else:
    print("Could not read the file.")
```

## 🔧 Different Types of Exception Handling

### Specific Exception Handling

```python
def convert_to_number(user_input):
    """
    Convert user input to a number with specific error messages
    Like having different responses for different problems
    """
    try:
        # Try to convert to integer first
        return int(user_input)
    except ValueError:
        try:
            # If that fails, try float
            return float(user_input)
        except ValueError:
            print(f"'{user_input}' is not a valid number.")
            return None

# Test different inputs
print(convert_to_number("42"))        # 42
print(convert_to_number("3.14"))      # 3.14
print(convert_to_number("hello"))     # Error message and None
```

### Using else and finally

```python
def process_data_file(filename):
    """
    Process a data file with complete error handling
    """
    try:
        with open(filename, "r") as file:
            data = file.read()
            processed_data = data.upper()  # Simple processing
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return None
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return None
    else:
        # This runs only if no exception occurred
        print("File processed successfully!")
        return processed_data
    finally:
        # This always runs, whether there was an error or not
        print("Processing attempt completed.")
```

## 🎯 Best Practices for Error Handling

### 1. Be Specific with Exceptions

```python
# Bad - too general
try:
    result = risky_function()
except:  # Catches ALL errors, even programming mistakes
    print("Something went wrong")

# Good - specific error handling
try:
    result = risky_function()
except ValueError as e:
    print(f"Invalid value provided: {e}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

### 2. Provide Helpful Error Messages

```python
def withdraw_money(account_balance, amount):
    """
    Withdraw money with helpful error messages
    """
    try:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > account_balance:
            raise ValueError(f"Insufficient funds. Balance: ${account_balance}, Requested: ${amount}")
        
        new_balance = account_balance - amount
        return new_balance
    
    except ValueError as e:
        print(f"Withdrawal failed: {e}")
        return account_balance  # Return original balance
```

### 3. Log Errors for Debugging

```python
import datetime

def log_error(error_message, filename="error_log.txt"):
    """
    Log errors with timestamp for debugging
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR: {error_message}\n"
    
    try:
        with open(filename, "a", encoding="utf-8") as log_file:
            log_file.write(log_entry)
    except Exception:
        # If we can't log to file, at least print it
        print(f"Could not write to log file: {log_entry.strip()}")

# Usage in error handling
def risky_operation():
    try:
        # Some risky code here
        result = 10 / 0  # This will cause an error
    except ZeroDivisionError as e:
        error_msg = f"Division by zero in risky_operation(): {e}"
        log_error(error_msg)
        print("An error occurred and has been logged.")
```

## 🔄 Error Recovery Strategies

### Retry Mechanism

```python
def download_with_retry(url, max_attempts=3):
    """
    Try to download something with retry logic
    Like knocking on a door multiple times
    """
    import time
    
    for attempt in range(max_attempts):
        try:
            # Simulate download (replace with actual download code)
            if attempt < 2:  # Simulate failure for first 2 attempts
                raise ConnectionError("Network timeout")
            
            print(f"Successfully downloaded on attempt {attempt + 1}")
            return "Downloaded data"
            
        except ConnectionError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_attempts - 1:
                print("Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print("Max attempts reached. Download failed.")
                return None

# Test the retry mechanism
result = download_with_retry("https://example.com/data")
```

### Fallback Options

```python
def get_user_preference(preference_file="preferences.json"):
    """
    Get user preferences with fallback to defaults
    """
    import json
    
    # Default preferences
    default_preferences = {
        "theme": "light",
        "language": "en",
        "notifications": True
    }
    
    try:
        with open(preference_file, "r") as file:
            preferences = json.load(file)
            print("Loaded user preferences successfully")
            return preferences
    except FileNotFoundError:
        print("Preferences file not found. Using defaults.")
        return default_preferences
    except json.JSONDecodeError:
        print("Preferences file corrupted. Using defaults.")
        return default_preferences
    except Exception as e:
        print(f"Error loading preferences: {e}. Using defaults.")
        return default_preferences
```

## 🏃‍♂️ Practice Exercises

### Exercise 1: Safe Calculator
Create a calculator function that handles all possible errors:

```python
def safe_calculator(operation, a, b):
    """
    Perform calculations safely with error handling
    Operations: 'add', 'subtract', 'multiply', 'divide', 'power'
    """
    # Your code here
    pass

# Test cases
print(safe_calculator('divide', 10, 2))     # Should work
print(safe_calculator('divide', 10, 0))     # Handle division by zero
print(safe_calculator('power', 2, 1000))    # Handle overflow
print(safe_calculator('invalid', 5, 3))     # Handle invalid operation
```

### Exercise 2: File Backup System
Create a function that safely backs up files:

```python
def backup_file(source_file, backup_folder="backups"):
    """
    Create a backup copy of a file with error handling
    """
    # Your code here
    pass
```

### Exercise 3: User Input Validator
Create a robust input validation system:

```python
def get_valid_age():
    """
    Keep asking for age until user provides a valid number
    """
    # Your code here
    pass
```

## 📝 Key Takeaways

1. **Always expect the unexpected** - Users will input wrong data, files will be missing, networks will fail
2. **Use specific exception handling** - Catch specific errors rather than using broad except statements
3. **Provide helpful error messages** - Tell users what went wrong and how to fix it
4. **Have fallback strategies** - Default values, retry mechanisms, alternative approaches
5. **Log errors for debugging** - Keep records of what goes wrong for future improvements
6. **Fail gracefully** - When errors occur, handle them elegantly rather than crashing

## 🎯 Today's Project Preview

Today you'll build a **Safe File Manager** that demonstrates all these error handling concepts. It will:
- Safely read and write files
- Handle missing files gracefully
- Validate user input
- Log errors for debugging
- Provide helpful error messages
- Recover from common problems

The goal is to create a robust program that never crashes, no matter what the user throws at it!

## 🔗 Connection to Previous Days

- **Day 15-16 (Functions)**: Error handling makes your functions more reliable
- **Day 17 (Built-ins)**: Many built-in functions can raise exceptions
- **Day 18 (Modules)**: Import errors and module-specific exceptions
- **Day 19 (File Handling)**: File operations are especially prone to errors

Remember: Good error handling is the difference between a program that works in ideal conditions and one that works in the real world!