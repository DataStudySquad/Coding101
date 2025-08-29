#!/usr/bin/env python3
"""
Day 20: Error Handling Practice Exercises
Interactive exercises to master exception handling

These exercises will help you practice:
- Using try/except blocks effectively
- Handling different types of exceptions
- Creating user-friendly error messages
- Implementing retry mechanisms
- Building robust input validation
"""

import json
import math
import random
import time


def exercise_1_safe_calculator():
    """
    Exercise 1: Build a safe calculator that handles all possible errors
    """
    print("\n" + "="*50)
    print("EXERCISE 1: SAFE CALCULATOR")
    print("="*50)
    
    def safe_calculator(operation, a, b):
        """
        Perform calculations safely with comprehensive error handling
        """
        try:
            # Convert inputs to numbers if they're strings
            if isinstance(a, str):
                a = float(a)
            if isinstance(b, str):
                b = float(b)
            
            # Perform the operation
            if operation.lower() == 'add':
                result = a + b
            elif operation.lower() == 'subtract':
                result = a - b
            elif operation.lower() == 'multiply':
                result = a * b
            elif operation.lower() == 'divide':
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = a / b
            elif operation.lower() == 'power':
                if a == 0 and b < 0:
                    raise ValueError("Cannot raise 0 to a negative power")
                result = a ** b
                # Check for overflow
                if abs(result) > 1e308:
                    raise OverflowError("Result is too large")
            else:
                raise ValueError(f"Unknown operation: {operation}")
            
            return result
            
        except ValueError as e:
            return f"Value Error: {e}"
        except ZeroDivisionError as e:
            return f"Division Error: {e}"
        except OverflowError as e:
            return f"Overflow Error: {e}"
        except TypeError as e:
            return f"Type Error: Invalid input types - {e}"
        except Exception as e:
            return f"Unexpected Error: {e}"
    
    # Test the calculator
    test_cases = [
        ('add', 10, 5),
        ('divide', 10, 2),
        ('divide', 10, 0),  # Division by zero
        ('power', 2, 1000),  # Potential overflow
        ('invalid_op', 5, 3),  # Invalid operation
        ('multiply', 'hello', 5),  # Invalid input
        ('power', 0, -1),  # Invalid power
    ]
    
    print("Testing calculator with various inputs:")
    for operation, a, b in test_cases:
        result = safe_calculator(operation, a, b)
        print(f"{operation}({a}, {b}) = {result}")
    
    # Interactive mode
    print("\nTry it yourself! (Enter 'quit' to exit)")
    while True:
        try:
            operation = input("\nEnter operation (add/subtract/multiply/divide/power): ").strip()
            if operation.lower() == 'quit':
                break
            
            a = input("Enter first number: ").strip()
            b = input("Enter second number: ").strip()
            
            result = safe_calculator(operation, a, b)
            print(f"Result: {result}")
            
        except (EOFError, KeyboardInterrupt):
            print("\nExiting calculator...")
            break


def exercise_2_file_backup_system():
    """
    Exercise 2: Create a file backup system with error handling
    """
    print("\n" + "="*50)
    print("EXERCISE 2: FILE BACKUP SYSTEM")
    print("="*50)
    
    import os
    import shutil
    from pathlib import Path
    
    def backup_file(source_file, backup_folder="backups"):
        """
        Create a backup copy of a file with comprehensive error handling
        """
        try:
            # Convert to Path objects for better handling
            source_path = Path(source_file)
            backup_dir = Path(backup_folder)
            
            # Check if source file exists
            if not source_path.exists():
                raise FileNotFoundError(f"Source file '{source_file}' does not exist")
            
            # Check if source is actually a file
            if not source_path.is_file():
                raise ValueError(f"'{source_file}' is not a file")
            
            # Create backup directory if it doesn't exist
            try:
                backup_dir.mkdir(parents=True, exist_ok=True)
            except PermissionError:
                raise PermissionError(f"No permission to create backup directory '{backup_folder}'")
            
            # Generate backup filename with timestamp
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{source_path.stem}_{timestamp}{source_path.suffix}"
            backup_path = backup_dir / backup_name
            
            # Check available disk space (simplified check)
            source_size = source_path.stat().st_size
            if source_size > 1024 * 1024 * 1024:  # 1GB limit for demo
                raise ValueError("File too large for backup (>1GB)")
            
            # Perform the backup
            shutil.copy2(source_path, backup_path)
            
            # Verify the backup
            if backup_path.exists() and backup_path.stat().st_size == source_size:
                return str(backup_path)
            else:
                raise RuntimeError("Backup verification failed")
                
        except FileNotFoundError as e:
            return f"File Error: {e}"
        except PermissionError as e:
            return f"Permission Error: {e}"
        except ValueError as e:
            return f"Value Error: {e}"
        except shutil.Error as e:
            return f"Backup Error: {e}"
        except OSError as e:
            return f"System Error: {e}"
        except Exception as e:
            return f"Unexpected Error: {e}"
    
    # Create test files for demonstration
    test_files = ["test1.txt", "test2.json", "test3.py"]
    
    print("Creating test files...")
    for filename in test_files:
        try:
            with open(filename, "w") as f:
                f.write(f"This is test content for {filename}\n")
                f.write(f"Created at: {time.ctime()}\n")
            print(f"Created: {filename}")
        except Exception as e:
            print(f"Could not create {filename}: {e}")
    
    # Test the backup function
    print("\nTesting backup function:")
    test_cases = [
        "test1.txt",           # Should work
        "nonexistent.txt",     # File doesn't exist
        ".",                   # Not a file (directory)
    ]
    
    for test_file in test_cases:
        result = backup_file(test_file)
        if result.startswith("test"):  # Successful backup
            print(f"✓ Successfully backed up '{test_file}' to '{result}'")
        else:  # Error occurred
            print(f"✗ Failed to backup '{test_file}': {result}")
    
    # Cleanup test files
    print("\nCleaning up test files...")
    for filename in test_files:
        try:
            os.remove(filename)
            print(f"Removed: {filename}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Could not remove {filename}: {e}")


def exercise_3_robust_input_validation():
    """
    Exercise 3: Create a robust input validation system
    """
    print("\n" + "="*50)
    print("EXERCISE 3: ROBUST INPUT VALIDATION")
    print("="*50)
    
    def get_valid_age(max_attempts=3):
        """
        Get a valid age from user with retry mechanism
        """
        for attempt in range(max_attempts):
            try:
                age_str = input(f"Enter your age (attempt {attempt + 1}/{max_attempts}): ").strip()
                
                # Check for empty input
                if not age_str:
                    raise ValueError("Age cannot be empty")
                
                # Convert to integer
                age = int(age_str)
                
                # Validate age range
                if age < 0:
                    raise ValueError("Age cannot be negative")
                elif age > 150:
                    raise ValueError("Age cannot be greater than 150")
                elif age == 0:
                    print("Warning: Age 0 (newborn) - is this correct?")
                
                return age
                
            except ValueError as e:
                if "invalid literal" in str(e):
                    print(f"Error: Please enter a valid number, not '{age_str}'")
                else:
                    print(f"Error: {e}")
                
                if attempt < max_attempts - 1:
                    print("Please try again.")
                else:
                    print("Too many invalid attempts.")
                    return None
                    
            except (EOFError, KeyboardInterrupt):
                print("\nInput cancelled by user.")
                return None
    
    def get_valid_email(max_attempts=3):
        """
        Get a valid email with basic validation
        """
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        for attempt in range(max_attempts):
            try:
                email = input(f"Enter email address (attempt {attempt + 1}/{max_attempts}): ").strip()
                
                if not email:
                    raise ValueError("Email cannot be empty")
                
                if not re.match(email_pattern, email):
                    raise ValueError("Invalid email format")
                
                if len(email) > 254:  # RFC 5321 limit
                    raise ValueError("Email address too long")
                
                return email
                
            except ValueError as e:
                print(f"Error: {e}")
                if attempt < max_attempts - 1:
                    print("Please try again.")
                else:
                    print("Too many invalid attempts.")
                    return None
                    
            except (EOFError, KeyboardInterrupt):
                print("\nInput cancelled by user.")
                return None
    
    def get_valid_choice(options, prompt="Select an option", max_attempts=3):
        """
        Get a valid choice from a list of options
        """
        print(f"\nAvailable options:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        for attempt in range(max_attempts):
            try:
                choice_str = input(f"{prompt} (1-{len(options)}) [attempt {attempt + 1}/{max_attempts}]: ").strip()
                
                if not choice_str:
                    raise ValueError("Choice cannot be empty")
                
                choice_num = int(choice_str)
                
                if choice_num < 1 or choice_num > len(options):
                    raise ValueError(f"Choice must be between 1 and {len(options)}")
                
                return options[choice_num - 1]
                
            except ValueError as e:
                if "invalid literal" in str(e):
                    print(f"Error: Please enter a number, not '{choice_str}'")
                else:
                    print(f"Error: {e}")
                
                if attempt < max_attempts - 1:
                    print("Please try again.")
                else:
                    print("Too many invalid attempts.")
                    return None
                    
            except (EOFError, KeyboardInterrupt):
                print("\nInput cancelled by user.")
                return None
    
    # Test the validation functions
    print("Testing robust input validation:")
    print("(You can press Ctrl+C to cancel any input)")
    
    try:
        # Test age validation
        print("\n1. Age Validation Test:")
        age = get_valid_age()
        if age is not None:
            print(f"Valid age entered: {age}")
        else:
            print("Age validation failed or cancelled")
        
        # Test email validation
        print("\n2. Email Validation Test:")
        email = get_valid_email()
        if email is not None:
            print(f"Valid email entered: {email}")
        else:
            print("Email validation failed or cancelled")
        
        # Test choice validation
        print("\n3. Choice Validation Test:")
        colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
        chosen_color = get_valid_choice(colors, "Choose your favorite color")
        if chosen_color is not None:
            print(f"You chose: {chosen_color}")
        else:
            print("Choice validation failed or cancelled")
            
    except KeyboardInterrupt:
        print("\n\nValidation exercises cancelled by user.")


def exercise_4_network_retry_simulation():
    """
    Exercise 4: Simulate network operations with retry logic
    """
    print("\n" + "="*50)
    print("EXERCISE 4: NETWORK RETRY SIMULATION")
    print("="*50)
    
    def simulate_network_request(url, success_rate=0.3):
        """
        Simulate a network request that randomly fails
        """
        import random
        import time
        
        # Simulate network delay
        time.sleep(random.uniform(0.1, 0.5))
        
        if random.random() < success_rate:
            return f"Success: Data retrieved from {url}"
        else:
            # Randomly choose an error type
            errors = [
                ConnectionError("Network timeout"),
                ConnectionError("Connection refused"),
                ValueError("Invalid response"),
                RuntimeError("Server error")
            ]
            raise random.choice(errors)
    
    def robust_network_request(url, max_attempts=3, delay_between_attempts=1):
        """
        Make a network request with retry logic and exponential backoff
        """
        for attempt in range(max_attempts):
            try:
                print(f"  Attempt {attempt + 1}/{max_attempts}: Requesting {url}...")
                result = simulate_network_request(url)
                print(f"  ✓ Success on attempt {attempt + 1}")
                return result
                
            except ConnectionError as e:
                print(f"  ✗ Connection error: {e}")
                if attempt < max_attempts - 1:
                    wait_time = delay_between_attempts * (2 ** attempt)  # Exponential backoff
                    print(f"  Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print(f"  Failed after {max_attempts} attempts")
                    return f"Connection failed: {e}"
                    
            except ValueError as e:
                print(f"  ✗ Data error: {e}")
                # Don't retry for data errors
                return f"Data error: {e}"
                
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")
                if attempt < max_attempts - 1:
                    print(f"  Retrying in {delay_between_attempts} seconds...")
                    time.sleep(delay_between_attempts)
                else:
                    return f"Unexpected error: {e}"
        
        return "All retry attempts failed"
    
    # Test the retry mechanism
    test_urls = [
        "https://api.example.com/data",
        "https://api.service.com/users",
        "https://api.weather.com/forecast"
    ]
    
    print("Testing network requests with retry logic:")
    print("(Simulated network requests with random failures)")
    
    for url in test_urls:
        print(f"\nRequesting: {url}")
        result = robust_network_request(url, max_attempts=3, delay_between_attempts=0.5)
        print(f"Final result: {result}")


def exercise_5_data_processing_with_errors():
    """
    Exercise 5: Process data files with comprehensive error handling
    """
    print("\n" + "="*50)
    print("EXERCISE 5: DATA PROCESSING WITH ERROR HANDLING")
    print("="*50)
    
    def safe_process_json_data(data_list):
        """
        Process a list of JSON data with error handling for each item
        """
        successful_records = []
        failed_records = []
        
        for i, data_item in enumerate(data_list):
            try:
                # Simulate processing each JSON record
                if not isinstance(data_item, dict):
                    raise TypeError(f"Item {i} is not a dictionary")
                
                # Required fields validation
                required_fields = ['id', 'name', 'value']
                for field in required_fields:
                    if field not in data_item:
                        raise KeyError(f"Missing required field: {field}")
                
                # Data type validation
                if not isinstance(data_item['id'], (int, str)):
                    raise ValueError(f"ID must be int or str, got {type(data_item['id'])}")
                
                if not isinstance(data_item['name'], str):
                    raise ValueError(f"Name must be string, got {type(data_item['name'])}")
                
                if not isinstance(data_item['value'], (int, float)):
                    raise ValueError(f"Value must be number, got {type(data_item['value'])}")
                
                # Business logic validation
                if data_item['value'] < 0:
                    raise ValueError("Value cannot be negative")
                
                # Process the record (example: calculate tax)
                processed_record = data_item.copy()
                processed_record['tax'] = data_item['value'] * 0.1
                processed_record['total'] = data_item['value'] * 1.1
                
                successful_records.append(processed_record)
                
            except (KeyError, ValueError, TypeError) as e:
                failed_records.append({
                    'index': i,
                    'data': data_item,
                    'error': str(e),
                    'error_type': type(e).__name__
                })
            except Exception as e:
                failed_records.append({
                    'index': i,
                    'data': data_item,
                    'error': f"Unexpected error: {e}",
                    'error_type': 'UnexpectedError'
                })
        
        return successful_records, failed_records
    
    # Create test data with various error scenarios
    test_data = [
        # Valid records
        {'id': 1, 'name': 'Product A', 'value': 100.0},
        {'id': 2, 'name': 'Product B', 'value': 50.5},
        
        # Error scenarios
        {'id': 3, 'name': 'Product C'},  # Missing 'value' field
        {'id': 4, 'value': 75.0},  # Missing 'name' field
        {'id': '5', 'name': 'Product D', 'value': -10},  # Negative value
        {'id': None, 'name': 'Product E', 'value': 25},  # Invalid ID type
        'invalid_record',  # Not a dictionary
        {'id': 6, 'name': 123, 'value': 80},  # Invalid name type
        {'id': 7, 'name': 'Product F', 'value': 'not_a_number'},  # Invalid value type
    ]
    
    print("Processing test data with error handling:")
    print(f"Total records to process: {len(test_data)}")
    
    successful, failed = safe_process_json_data(test_data)
    
    print(f"\n✓ Successfully processed: {len(successful)} records")
    for record in successful:
        print(f"  ID: {record['id']}, Name: {record['name']}, Total: ${record['total']:.2f}")
    
    print(f"\n✗ Failed to process: {len(failed)} records")
    for failure in failed:
        print(f"  Index {failure['index']}: {failure['error_type']} - {failure['error']}")
    
    # Generate summary report
    print(f"\nPROCESSING SUMMARY:")
    print(f"Success rate: {len(successful)/(len(successful) + len(failed)) * 100:.1f}%")
    
    # Group failures by error type
    error_summary = {}
    for failure in failed:
        error_type = failure['error_type']
        error_summary[error_type] = error_summary.get(error_type, 0) + 1
    
    print(f"Error breakdown:")
    for error_type, count in error_summary.items():
        print(f"  {error_type}: {count} occurrences")


def main():
    """
    Main function to run all error handling exercises
    """
    print("PYTHON ERROR HANDLING PRACTICE EXERCISES")
    print("=" * 60)
    print("These exercises demonstrate various error handling techniques:")
    print("- try/except blocks with specific exception types")
    print("- Input validation and retry mechanisms")  
    print("- File operations with error recovery")
    print("- Network simulation with exponential backoff")
    print("- Data processing with comprehensive error reporting")
    print("=" * 60)
    
    exercises = [
        ("Safe Calculator", exercise_1_safe_calculator),
        ("File Backup System", exercise_2_file_backup_system),
        ("Input Validation", exercise_3_robust_input_validation),
        ("Network Retry Simulation", exercise_4_network_retry_simulation),
        ("Data Processing with Errors", exercise_5_data_processing_with_errors),
    ]
    
    while True:
        print(f"\nAvailable exercises:")
        for i, (name, _) in enumerate(exercises, 1):
            print(f"{i}. {name}")
        print("6. Run all exercises")
        print("7. Exit")
        
        try:
            choice = input("\nSelect exercise (1-7): ").strip()
            
            if choice == '7':
                print("Thank you for practicing error handling!")
                break
            elif choice == '6':
                print("Running all exercises...")
                for name, exercise_func in exercises:
                    print(f"\n{'='*20} {name} {'='*20}")
                    try:
                        exercise_func()
                    except KeyboardInterrupt:
                        print(f"\n{name} interrupted by user")
                        continue
                    except Exception as e:
                        print(f"Error running {name}: {e}")
                        continue
            elif choice in ['1', '2', '3', '4', '5']:
                exercise_num = int(choice) - 1
                name, exercise_func = exercises[exercise_num]
                print(f"\n{'='*20} {name} {'='*20}")
                try:
                    exercise_func()
                except KeyboardInterrupt:
                    print(f"\n{name} interrupted by user")
                except Exception as e:
                    print(f"Error running {name}: {e}")
            else:
                print("Invalid choice. Please select 1-7.")
                
        except (EOFError, KeyboardInterrupt):
            print("\n\nExiting error handling practice...")
            break
        except Exception as e:
            print(f"Unexpected error in main menu: {e}")


if __name__ == "__main__":
    main()