# Day 23: Regular Expressions - Pattern Matching Like a Detective

Welcome to Day 23! Today we're diving into Regular Expressions (regex) - one of Python's most powerful text processing tools. Think of regex as becoming a text detective who can find any pattern in any amount of text, no matter how complex or hidden it might be.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Understand what regular expressions are and why they're useful
- Write basic regex patterns to match text
- Use Python's `re` module for pattern matching
- Validate email addresses, phone numbers, and other formats
- Extract specific information from large text documents
- Build a comprehensive email and data validator

## 🔍 What Are Regular Expressions?

### The Detective Analogy

Imagine you're a detective searching through thousands of documents for specific clues:
- **Manual Search**: Reading every document word by word (slow and error-prone)
- **Simple Search**: Using Ctrl+F to find exact words (limited and inflexible)  
- **Regex Search**: Having a super-smart assistant who can find any pattern you describe (powerful and efficient!)

Regular expressions are like having that super-smart assistant who understands pattern descriptions like:
- "Find all email addresses"
- "Find all phone numbers, regardless of format"
- "Find all dates, whether written as 2024-01-15 or January 15, 2024"
- "Find all social security numbers"

### Real-World Applications

```python
# Without regex (painful):
def find_emails_manually(text):
    # You'd have to write hundreds of lines of code
    # to handle all possible email formats!
    pass

# With regex (elegant):
import re
def find_emails_with_regex(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)
```

## 🚀 Getting Started with the `re` Module

### Basic Pattern Matching

```python
import re

# Basic string search
text = "Hello World! This is a test message."

# Check if pattern exists
if re.search("World", text):
    print("Found 'World' in the text!")

# Find all occurrences
words = re.findall(r"\w+", text)  # Find all words
print(f"Words found: {words}")

# Replace patterns
new_text = re.sub("World", "Python", text)
print(f"After replacement: {new_text}")
```

### Understanding Regex Patterns

Think of regex patterns as a special language for describing text patterns:

```python
# Literal characters - match exactly
pattern = "hello"  # Matches exactly "hello"

# Special characters (metacharacters) - have special meaning
pattern = "."      # Matches any single character
pattern = "*"      # Matches 0 or more of the previous character
pattern = "+"      # Matches 1 or more of the previous character
pattern = "?"      # Matches 0 or 1 of the previous character

# Examples:
text = "cat, bat, rat, at"
print(re.findall(r".at", text))    # ['cat', 'bat', 'rat']
print(re.findall(r"c.*t", text))   # ['cat, bat, rat'] (greedy)
print(re.findall(r"c.+t", text))   # ['cat, bat, rat']
```

## 📝 Essential Regex Patterns

### Character Classes

```python
import re

text = "Hello123 World456! Contact: john.doe@email.com or call 555-1234"

# Character classes - match specific types of characters
patterns = {
    r"\d": "Any digit (0-9)",
    r"\D": "Any non-digit",
    r"\w": "Any word character (letters, digits, underscore)",
    r"\W": "Any non-word character",
    r"\s": "Any whitespace (space, tab, newline)",
    r"\S": "Any non-whitespace"
}

for pattern, description in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{pattern:<4} ({description}): {matches[:10]}")  # Show first 10 matches

# Custom character classes
print("\nCustom character classes:")
print("Vowels:", re.findall(r"[aeiou]", text.lower()))
print("Digits 1-5:", re.findall(r"[1-5]", text))
print("Not digits:", re.findall(r"[^0-9]", text)[:10])  # ^ means NOT
```

### Quantifiers - How Many Times?

```python
import re

# Quantifiers specify how many times a pattern should match
examples = [
    ("hello", r"l+"),           # One or more 'l'
    ("helo", r"l+"),            # One or more 'l'
    ("heo", r"l+"),             # One or more 'l'
    ("hello", r"l*"),           # Zero or more 'l'
    ("heo", r"l*"),             # Zero or more 'l'
    ("hello", r"l?"),           # Zero or one 'l'
    ("hello", r"l{2}"),         # Exactly 2 'l's
    ("hello", r"l{1,3}"),       # Between 1 and 3 'l's
]

print("Quantifier Examples:")
for text, pattern in examples:
    matches = re.findall(pattern, text)
    print(f"'{text}' with pattern '{pattern}': {matches}")
```

### Anchors - Position Matters

```python
import re

lines = [
    "python is awesome",
    "I love python programming", 
    "learning python",
    "python",
    "not about python here"
]

# Anchors specify position in string
print("Anchor Examples:")
for line in lines:
    if re.search(r"^python", line):  # ^ means start of string
        print(f"Starts with 'python': {line}")
    if re.search(r"python$", line):  # $ means end of string
        print(f"Ends with 'python': {line}")
    if re.search(r"\bpython\b", line):  # \b means word boundary
        print(f"Contains word 'python': {line}")
```

## 🎯 Practical Examples

### Email Validation

```python
import re

def validate_email(email):
    """
    Validate email addresses with regex
    Like having a smart bouncer who knows what real emails look like
    """
    # Basic email pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

def detailed_email_validation(email):
    """
    More detailed email validation with specific checks
    """
    # Check basic format first
    if not validate_email(email):
        return False, "Invalid email format"
    
    # Additional checks
    local_part, domain = email.split('@')
    
    # Check local part (before @)
    if len(local_part) > 64:
        return False, "Local part too long (max 64 characters)"
    
    if local_part.startswith('.') or local_part.endswith('.'):
        return False, "Local part cannot start or end with a dot"
    
    # Check domain part
    if len(domain) > 255:
        return False, "Domain part too long (max 255 characters)"
    
    # Check for valid TLD
    tld_pattern = r'\.[a-zA-Z]{2,}$'
    if not re.search(tld_pattern, domain):
        return False, "Invalid top-level domain"
    
    return True, "Valid email address"

# Test email validation
test_emails = [
    "user@example.com",
    "first.last@subdomain.example.org", 
    "user+tag@example.co.uk",
    "invalid.email",
    "@example.com",
    "user@",
    "user..double.dot@example.com",
    "user@example",
    "valid.email@example.museum"
]

print("Email Validation Results:")
print("-" * 50)
for email in test_emails:
    is_valid, message = detailed_email_validation(email)
    status = "✅ VALID" if is_valid else "❌ INVALID"
    print(f"{email:<35} | {status} - {message}")
```

### Phone Number Extraction

```python
import re

def extract_phone_numbers(text):
    """
    Extract various phone number formats
    Like a multilingual assistant who understands phone numbers from anywhere
    """
    # Different phone number patterns
    patterns = [
        r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # (123) 456-7890, 123-456-7890, 123.456.7890
        r'\+1[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # +1 (123) 456-7890
        r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',       # 123 456 7890
        r'\(\d{3}\)\d{3}-\d{4}',                 # (123)456-7890
    ]
    
    all_numbers = []
    for pattern in patterns:
        numbers = re.findall(pattern, text)
        all_numbers.extend(numbers)
    
    # Remove duplicates while preserving order
    unique_numbers = []
    for num in all_numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    
    return unique_numbers

def format_phone_number(phone):
    """
    Standardize phone number format
    """
    # Extract just the digits
    digits = re.sub(r'\D', '', phone)
    
    # Handle different lengths
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return phone  # Return original if can't format

# Test phone number extraction
sample_text = """
Contact information:
- Main office: (555) 123-4567
- Sales: 555.987.6543
- Support: 555 111 2222
- International: +1 (555) 999-8888
- Alternative: 5551234567
- Invalid: 123-45-67890
"""

print("Phone Number Extraction:")
print("-" * 30)
phone_numbers = extract_phone_numbers(sample_text)
for phone in phone_numbers:
    formatted = format_phone_number(phone)
    print(f"Found: {phone:<20} → Formatted: {formatted}")
```

### Data Extraction from Text

```python
import re

def extract_data_from_text(text):
    """
    Extract various types of data from free-form text
    Like having multiple specialists analyze a document
    """
    results = {}
    
    # Extract email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    results['emails'] = re.findall(email_pattern, text)
    
    # Extract phone numbers (simplified)
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    results['phones'] = re.findall(phone_pattern, text)
    
    # Extract dates (various formats)
    date_patterns = [
        r'\d{1,2}/\d{1,2}/\d{2,4}',          # MM/DD/YYYY or MM/DD/YY
        r'\d{4}-\d{1,2}-\d{1,2}',            # YYYY-MM-DD
        r'\b\w+ \d{1,2}, \d{4}\b',           # Month DD, YYYY
    ]
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))
    results['dates'] = dates
    
    # Extract URLs
    url_pattern = r'https?://[^\s<>"{}|\\^`[\]]+'
    results['urls'] = re.findall(url_pattern, text)
    
    # Extract monetary amounts
    money_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    results['money'] = re.findall(money_pattern, text)
    
    # Extract time (HH:MM format)
    time_pattern = r'\b\d{1,2}:\d{2}(?:\s*[AaPp][Mm])?\b'
    results['times'] = re.findall(time_pattern, text)
    
    return results

# Test data extraction
sample_document = """
Meeting Summary - March 15, 2024

Attendees can contact us at:
- John Smith: john.smith@company.com, (555) 123-4567
- Sarah Johnson: sarah.j@company.org, 555.987.6543

Meeting scheduled for 03/20/2024 at 2:30 PM
Budget approved: $15,000.00 for Q2
Next review: April 1st, 2024

Resources:
- Project site: https://project.company.com/dashboard
- Documentation: https://docs.company.com/api

Follow-up meeting: 4/15/2024 at 10:00 AM
Additional funding: $2,500.50 requested
"""

print("Data Extraction Results:")
print("=" * 50)
extracted_data = extract_data_from_text(sample_document)

for data_type, items in extracted_data.items():
    if items:
        print(f"\n📋 {data_type.upper()}:")
        for item in items:
            print(f"   - {item}")
    else:
        print(f"\n📋 {data_type.upper()}: None found")
```

## 🛡️ Input Validation with Regex

### Password Strength Checker

```python
import re

def check_password_strength(password):
    """
    Check password strength using multiple regex patterns
    Like having a security expert evaluate password quality
    """
    checks = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'numbers': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        'no_spaces': not bool(re.search(r'\s', password)),
        'no_common': password.lower() not in ['password', '123456', 'qwerty', 'abc123']
    }
    
    # Calculate strength score
    score = sum(checks.values())
    
    # Determine strength level
    if score >= 6:
        strength = "Strong"
        color = "🟢"
    elif score >= 4:
        strength = "Medium"
        color = "🟡"
    else:
        strength = "Weak"
        color = "🔴"
    
    return {
        'score': score,
        'max_score': len(checks),
        'strength': strength,
        'color': color,
        'checks': checks,
        'suggestions': get_password_suggestions(checks)
    }

def get_password_suggestions(checks):
    """Generate suggestions based on failed checks"""
    suggestions = []
    
    if not checks['length']:
        suggestions.append("Use at least 8 characters")
    if not checks['uppercase']:
        suggestions.append("Include uppercase letters (A-Z)")
    if not checks['lowercase']:
        suggestions.append("Include lowercase letters (a-z)")
    if not checks['numbers']:
        suggestions.append("Include numbers (0-9)")
    if not checks['special']:
        suggestions.append("Include special characters (!@#$%^&*)")
    if not checks['no_spaces']:
        suggestions.append("Remove spaces")
    if not checks['no_common']:
        suggestions.append("Avoid common passwords")
    
    return suggestions

# Test password checker
test_passwords = [
    "password",
    "Password123",
    "MySecureP@ssw0rd!",
    "weak",
    "StrongPassword2024!",
    "abc123",
    "Hello World"
]

print("Password Strength Analysis:")
print("=" * 60)

for pwd in test_passwords:
    result = check_password_strength(pwd)
    print(f"\nPassword: '{pwd}'")
    print(f"Strength: {result['color']} {result['strength']} ({result['score']}/{result['max_score']})")
    
    if result['suggestions']:
        print("Suggestions:")
        for suggestion in result['suggestions']:
            print(f"   • {suggestion}")
```

## 🔍 Advanced Pattern Matching

### Log File Analysis

```python
import re
from datetime import datetime

def analyze_log_file(log_text):
    """
    Analyze log files to extract useful information
    Like having an expert who can read server logs instantly
    """
    results = {
        'total_lines': len(log_text.split('\n')),
        'errors': [],
        'warnings': [],
        'ips': set(),
        'timestamps': [],
        'http_methods': {},
        'status_codes': {}
    }
    
    # Common log format pattern (Apache/Nginx style)
    # IP - - [timestamp] "METHOD /path HTTP/1.1" status size
    log_pattern = r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\].*?"(\w+) (.*?) HTTP/.*?" (\d+) (\d+)'
    
    # Error patterns
    error_pattern = r'.*ERROR.*|.*error.*|.*Error.*'
    warning_pattern = r'.*WARNING.*|.*warning.*|.*Warning.*'
    
    lines = log_text.split('\n')
    
    for line in lines:
        if not line.strip():
            continue
            
        # Check for errors and warnings
        if re.search(error_pattern, line):
            results['errors'].append(line.strip())
        elif re.search(warning_pattern, line):
            results['warnings'].append(line.strip())
        
        # Extract structured log data
        match = re.search(log_pattern, line)
        if match:
            ip, timestamp, method, path, status, size = match.groups()
            
            results['ips'].add(ip)
            results['timestamps'].append(timestamp)
            
            # Count HTTP methods
            results['http_methods'][method] = results['http_methods'].get(method, 0) + 1
            
            # Count status codes
            results['status_codes'][status] = results['status_codes'].get(status, 0) + 1
    
    return results

# Sample log data
sample_log = """
192.168.1.100 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.101 - - [15/Mar/2024:10:31:02 +0000] "POST /api/login HTTP/1.1" 401 89
192.168.1.100 - - [15/Mar/2024:10:31:15 +0000] "GET /dashboard HTTP/1.1" 200 5678
ERROR: Database connection failed at 10:31:30
192.168.1.102 - - [15/Mar/2024:10:32:01 +0000] "GET /nonexistent HTTP/1.1" 404 156
WARNING: High memory usage detected
192.168.1.101 - - [15/Mar/2024:10:32:45 +0000] "POST /api/data HTTP/1.1" 200 2345
"""

print("Log File Analysis Results:")
print("=" * 40)

log_analysis = analyze_log_file(sample_log)

print(f"📊 Summary:")
print(f"   Total lines: {log_analysis['total_lines']}")
print(f"   Unique IPs: {len(log_analysis['ips'])}")
print(f"   Errors: {len(log_analysis['errors'])}")
print(f"   Warnings: {len(log_analysis['warnings'])}")

if log_analysis['http_methods']:
    print(f"\n🌐 HTTP Methods:")
    for method, count in log_analysis['http_methods'].items():
        print(f"   {method}: {count}")

if log_analysis['status_codes']:
    print(f"\n📈 Status Codes:")
    for code, count in log_analysis['status_codes'].items():
        print(f"   {code}: {count}")

if log_analysis['errors']:
    print(f"\n❌ Errors found:")
    for error in log_analysis['errors']:
        print(f"   • {error}")

if log_analysis['warnings']:
    print(f"\n⚠️ Warnings found:")
    for warning in log_analysis['warnings']:
        print(f"   • {warning}")
```

## 🏃‍♂️ Practice Exercises

### Exercise 1: Social Media Handle Validator
Create a validator for social media handles:

```python
def validate_social_handle(handle, platform):
    """
    Validate social media handles for different platforms
    Twitter: @username (letters, numbers, underscore, 1-15 chars)
    Instagram: @username (letters, numbers, underscore, period, 1-30 chars)
    """
    # Your code here
    pass
```

### Exercise 2: Credit Card Number Validator
Build a credit card number validator:

```python
def validate_credit_card(card_number):
    """
    Validate credit card numbers and identify card type
    Visa: starts with 4, 16 digits
    MasterCard: starts with 5, 16 digits
    American Express: starts with 34 or 37, 15 digits
    """
    # Your code here
    pass
```

### Exercise 3: Text Cleaner
Create a text cleaning function:

```python
def clean_text_data(text):
    """
    Clean text data by:
    - Removing extra whitespace
    - Fixing common formatting issues
    - Extracting and formatting phone numbers and emails
    - Standardizing date formats
    """
    # Your code here
    pass
```

## 📝 Key Takeaways

1. **Regex is powerful but complex** - Start simple and build up complexity gradually
2. **Test your patterns thoroughly** - Edge cases will surprise you
3. **Use raw strings (r"pattern")** - Prevents Python from interpreting backslashes
4. **Be specific rather than greedy** - Overly broad patterns match too much
5. **Document complex patterns** - Future you will thank you
6. **Performance matters** - Complex regex on large text can be slow
7. **Sometimes simple string methods are better** - Don't use regex for everything

## 🎯 Today's Project Preview

Today you'll build a **Universal Data Validator and Extractor** that demonstrates regex mastery. It will:
- Validate email addresses, phone numbers, and other formats
- Extract structured data from unstructured text
- Clean and standardize various data formats
- Analyze text files and generate reports
- Provide detailed feedback on validation failures
- Handle multiple input formats gracefully

The goal is to create a professional-grade tool that showcases regex capabilities!

## 🔗 Connection to Previous Days

### Building on Previous Weeks
- **String Operations (Day 4)**: Regex extends string manipulation capabilities
- **Functions (Day 15-16)**: Regex validation becomes reusable functions
- **File Handling (Day 19)**: Process text files with regex patterns
- **Error Handling (Day 20)**: Handle invalid regex patterns gracefully

### Looking Forward
Regex skills will be essential for:
- **Web Scraping (Day 24)**: Extract data from HTML content
- **Data Processing (Day 26)**: Clean and validate CSV data
- **Final Projects**: Any real application needs input validation

Regular expressions are like learning a superpower for text processing. Once you master them, you'll wonder how you ever lived without them!