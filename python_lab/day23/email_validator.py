#!/usr/bin/env python3
"""
Day 23: Universal Data Validator and Extractor
A comprehensive data validation and extraction tool using regular expressions

This program showcases:
- Email, phone, and URL validation using regex
- Data extraction from unstructured text
- Pattern-based text cleaning and formatting
- Log file analysis and reporting
- Input validation with detailed feedback
- Multiple data format support

Think of this as your personal data detective and validator!
"""

import re
import json
from datetime import datetime
from pathlib import Path


class DataValidator:
    """
    A comprehensive data validation toolkit using regular expressions
    Like having multiple experts validate different types of data
    """
    
    def __init__(self):
        """Initialize the validator with common patterns"""
        self.patterns = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'phone_us': r'^\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$',
            'url': r'^https?://[^\s<>"{}|\\^`\[\]]+$',
            'ip_address': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
            'date_iso': r'^\d{4}-\d{2}-\d{2}$',
            'date_us': r'^\d{1,2}/\d{1,2}/\d{4}$',
            'credit_card': r'^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$',
            'ssn': r'^\d{3}-\d{2}-\d{4}$',
            'zip_code': r'^\d{5}(-\d{4})?$',
        }
        
        self.validation_history = []
        print("🔍 Universal Data Validator initialized!")
        print(f"📋 Available validators: {len(self.patterns)}")
    
    def validate_email(self, email):
        """
        Comprehensive email validation with detailed feedback
        """
        result = {
            'input': email,
            'type': 'email',
            'valid': False,
            'issues': [],
            'suggestions': []
        }
        
        # Basic format check
        if not email or not isinstance(email, str):
            result['issues'].append("Email cannot be empty")
            return result
        
        # Check basic pattern
        if not re.match(self.patterns['email'], email.strip()):
            result['issues'].append("Invalid email format")
            
            # Specific issue detection
            if '@' not in email:
                result['suggestions'].append("Email must contain @ symbol")
            elif email.count('@') > 1:
                result['suggestions'].append("Email should contain only one @ symbol")
            elif not re.search(r'\.', email):
                result['suggestions'].append("Email must have a domain with extension (.com, .org, etc.)")
            elif email.startswith('@') or email.endswith('@'):
                result['suggestions'].append("@ symbol cannot be at start or end")
            
            return result
        
        # Additional validation
        local_part, domain = email.rsplit('@', 1)
        
        # Check local part (before @)
        if len(local_part) > 64:
            result['issues'].append("Local part too long (max 64 characters)")
        elif len(local_part) == 0:
            result['issues'].append("Local part cannot be empty")
        
        if local_part.startswith('.') or local_part.endswith('.'):
            result['issues'].append("Local part cannot start or end with a dot")
        
        if '..' in local_part:
            result['issues'].append("Local part cannot contain consecutive dots")
        
        # Check domain part
        if len(domain) > 255:
            result['issues'].append("Domain too long (max 255 characters)")
        elif len(domain) == 0:
            result['issues'].append("Domain cannot be empty")
        
        domain_parts = domain.split('.')
        if len(domain_parts) < 2:
            result['issues'].append("Domain must have at least one dot")
        elif len(domain_parts[-1]) < 2:
            result['issues'].append("Top-level domain too short (min 2 characters)")
        
        # If no issues found, it's valid
        if not result['issues']:
            result['valid'] = True
            result['normalized'] = email.lower().strip()
        
        return result
    
    def validate_phone(self, phone):
        """
        Validate phone numbers in various formats
        """
        result = {
            'input': phone,
            'type': 'phone',
            'valid': False,
            'issues': [],
            'suggestions': []
        }
        
        if not phone or not isinstance(phone, str):
            result['issues'].append("Phone number cannot be empty")
            return result
        
        # Clean the phone number
        cleaned_phone = re.sub(r'[^\d+]', '', phone)
        
        # Check if it matches US phone pattern
        if re.match(self.patterns['phone_us'], phone.strip()):
            result['valid'] = True
            # Normalize to standard format
            digits = re.sub(r'\D', '', phone)
            if len(digits) == 10:
                result['normalized'] = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
            elif len(digits) == 11 and digits[0] == '1':
                result['normalized'] = f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
        else:
            result['issues'].append("Invalid phone number format")
            
            if len(cleaned_phone.replace('+', '')) < 10:
                result['suggestions'].append("Phone number too short (need at least 10 digits)")
            elif len(cleaned_phone.replace('+', '')) > 15:
                result['suggestions'].append("Phone number too long (max 15 digits)")
            else:
                result['suggestions'].append("Try format: (555) 123-4567 or 555-123-4567")
        
        return result
    
    def validate_url(self, url):
        """
        Validate URLs with detailed checking
        """
        result = {
            'input': url,
            'type': 'url',
            'valid': False,
            'issues': [],
            'suggestions': []
        }
        
        if not url or not isinstance(url, str):
            result['issues'].append("URL cannot be empty")
            return result
        
        # Check basic pattern
        if not re.match(self.patterns['url'], url.strip()):
            result['issues'].append("Invalid URL format")
            
            if not url.startswith(('http://', 'https://')):
                result['suggestions'].append("URL must start with http:// or https://")
            elif ' ' in url:
                result['suggestions'].append("URLs cannot contain spaces")
            else:
                result['suggestions'].append("Check URL format: https://example.com/path")
        else:
            result['valid'] = True
            result['normalized'] = url.strip()
            
            # Additional info
            if url.startswith('http://'):
                result['warnings'] = ["Consider using HTTPS for security"]
        
        return result
    
    def validate_credit_card(self, card_number):
        """
        Validate credit card numbers and identify card type
        """
        result = {
            'input': card_number,
            'type': 'credit_card',
            'valid': False,
            'issues': [],
            'suggestions': [],
            'card_type': None
        }
        
        if not card_number or not isinstance(card_number, str):
            result['issues'].append("Credit card number cannot be empty")
            return result
        
        # Clean the card number
        cleaned = re.sub(r'[^\d]', '', card_number)
        
        # Check length and format
        if len(cleaned) < 13 or len(cleaned) > 19:
            result['issues'].append("Invalid credit card length (13-19 digits)")
            return result
        
        # Identify card type
        if re.match(r'^4', cleaned):
            result['card_type'] = 'Visa'
            if len(cleaned) not in [13, 16]:
                result['issues'].append("Visa cards must be 13 or 16 digits")
        elif re.match(r'^5[1-5]', cleaned):
            result['card_type'] = 'MasterCard'
            if len(cleaned) != 16:
                result['issues'].append("MasterCard must be 16 digits")
        elif re.match(r'^3[47]', cleaned):
            result['card_type'] = 'American Express'
            if len(cleaned) != 15:
                result['issues'].append("American Express must be 15 digits")
        elif re.match(r'^6(?:011|5)', cleaned):
            result['card_type'] = 'Discover'
            if len(cleaned) != 16:
                result['issues'].append("Discover cards must be 16 digits")
        else:
            result['issues'].append("Unknown card type")
        
        # Luhn algorithm check (simplified)
        if not result['issues']:
            if self.luhn_check(cleaned):
                result['valid'] = True
                result['normalized'] = self.format_credit_card(cleaned)
            else:
                result['issues'].append("Invalid card number (fails checksum)")
        
        return result
    
    def luhn_check(self, card_number):
        """
        Implement Luhn algorithm for credit card validation
        """
        def digits_of(n):
            return [int(d) for d in str(n)]
        
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        
        return checksum % 10 == 0
    
    def format_credit_card(self, card_number):
        """
        Format credit card number with spaces
        """
        if len(card_number) == 15:  # American Express
            return f"{card_number[:4]} {card_number[4:10]} {card_number[10:]}"
        else:  # Most other cards
            return f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
    
    def validate_password(self, password):
        """
        Comprehensive password strength validation
        """
        result = {
            'input': password,
            'type': 'password',
            'valid': False,
            'strength': 'Weak',
            'score': 0,
            'issues': [],
            'suggestions': []
        }
        
        if not password:
            result['issues'].append("Password cannot be empty")
            return result
        
        checks = {
            'length': len(password) >= 8,
            'uppercase': bool(re.search(r'[A-Z]', password)),
            'lowercase': bool(re.search(r'[a-z]', password)),
            'numbers': bool(re.search(r'\d', password)),
            'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
            'no_spaces': not bool(re.search(r'\s', password)),
            'no_common': password.lower() not in ['password', '123456', 'qwerty', 'abc123', 'password123']
        }
        
        score = sum(checks.values())
        result['score'] = score
        result['max_score'] = len(checks)
        
        # Generate suggestions
        if not checks['length']:
            result['suggestions'].append("Use at least 8 characters")
        if not checks['uppercase']:
            result['suggestions'].append("Include uppercase letters (A-Z)")
        if not checks['lowercase']:
            result['suggestions'].append("Include lowercase letters (a-z)")
        if not checks['numbers']:
            result['suggestions'].append("Include numbers (0-9)")
        if not checks['special']:
            result['suggestions'].append("Include special characters (!@#$%^&*)")
        if not checks['no_spaces']:
            result['suggestions'].append("Remove spaces from password")
        if not checks['no_common']:
            result['suggestions'].append("Avoid common passwords")
        
        # Determine strength
        if score >= 6:
            result['strength'] = 'Strong'
            result['valid'] = True
        elif score >= 4:
            result['strength'] = 'Medium'
        else:
            result['strength'] = 'Weak'
        
        return result


class DataExtractor:
    """
    Extract structured data from unstructured text using regex
    Like having a smart assistant who can find needles in haystacks
    """
    
    def __init__(self):
        """Initialize with extraction patterns"""
        self.extraction_patterns = {
            'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phones': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            'urls': r'https?://[^\s<>"{}|\\^`\[\]]+',
            'dates_iso': r'\d{4}-\d{2}-\d{2}',
            'dates_us': r'\d{1,2}/\d{1,2}/\d{4}',
            'dates_written': r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b',
            'money': r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?',
            'times': r'\b\d{1,2}:\d{2}(?:\s*[AaPp][Mm])?\b',
            'ip_addresses': r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
            'social_security': r'\b\d{3}-\d{2}-\d{4}\b',
            'zip_codes': r'\b\d{5}(?:-\d{4})?\b'
        }
    
    def extract_all_data(self, text):
        """
        Extract all types of structured data from text
        """
        if not text:
            return {}
        
        results = {}
        
        for data_type, pattern in self.extraction_patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                # Remove duplicates while preserving order
                unique_matches = []
                for match in matches:
                    if match not in unique_matches:
                        unique_matches.append(match)
                results[data_type] = unique_matches
        
        return results
    
    def extract_contact_info(self, text):
        """
        Extract contact information specifically
        """
        contact_info = {
            'emails': [],
            'phones': [],
            'addresses': []
        }
        
        # Extract emails
        emails = re.findall(self.extraction_patterns['emails'], text)
        contact_info['emails'] = list(set(emails))  # Remove duplicates
        
        # Extract phone numbers
        phones = re.findall(self.extraction_patterns['phones'], text)
        contact_info['phones'] = list(set(phones))
        
        # Extract potential addresses (simplified pattern)
        address_pattern = r'\d+\s+[A-Za-z\s]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Plaza|Pl)'
        addresses = re.findall(address_pattern, text, re.IGNORECASE)
        contact_info['addresses'] = list(set(addresses))
        
        return contact_info
    
    def clean_and_format_data(self, text):
        """
        Clean text data and format consistently
        """
        if not text:
            return ""
        
        # Remove extra whitespace
        cleaned = re.sub(r'\s+', ' ', text.strip())
        
        # Fix common punctuation issues
        cleaned = re.sub(r'\s+([,.!?;:])', r'\1', cleaned)  # Remove space before punctuation
        cleaned = re.sub(r'([.!?])\s*([A-Z])', r'\1 \2', cleaned)  # Ensure space after sentence endings
        
        # Standardize phone numbers
        phone_matches = re.findall(self.extraction_patterns['phones'], cleaned)
        for phone in phone_matches:
            # Format to standard format
            digits = re.sub(r'\D', '', phone)
            if len(digits) == 10:
                formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
                cleaned = cleaned.replace(phone, formatted)
        
        # Standardize email addresses (lowercase)
        email_matches = re.findall(self.extraction_patterns['emails'], cleaned)
        for email in email_matches:
            cleaned = cleaned.replace(email, email.lower())
        
        return cleaned


class LogAnalyzer:
    """
    Analyze log files using regular expressions
    Like having an expert log analyst on your team
    """
    
    def __init__(self):
        """Initialize with common log patterns"""
        # Common log format: IP - - [timestamp] "METHOD /path HTTP/1.1" status size
        self.apache_pattern = r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\].*?"(\w+)\s+(.*?)\s+HTTP/.*?"\s+(\d+)\s+(\d+|-)'
        
        # Error patterns
        self.error_patterns = {
            'critical': r'CRITICAL|FATAL|critical|fatal',
            'error': r'ERROR|error',
            'warning': r'WARNING|WARN|warning|warn',
            'info': r'INFO|info'
        }
    
    def analyze_log_content(self, log_text):
        """
        Comprehensive log analysis
        """
        if not log_text:
            return {'error': 'No log content provided'}
        
        lines = [line.strip() for line in log_text.split('\n') if line.strip()]
        
        analysis = {
            'total_lines': len(lines),
            'structured_entries': 0,
            'ips': set(),
            'http_methods': {},
            'status_codes': {},
            'paths': {},
            'errors_by_level': {level: [] for level in self.error_patterns.keys()},
            'timestamps': [],
            'suspicious_activity': []
        }
        
        for line in lines:
            # Try to parse structured log entries
            apache_match = re.search(self.apache_pattern, line)
            if apache_match:
                analysis['structured_entries'] += 1
                ip, timestamp, method, path, status, size = apache_match.groups()
                
                # Track IPs
                analysis['ips'].add(ip)
                
                # Count HTTP methods
                analysis['http_methods'][method] = analysis['http_methods'].get(method, 0) + 1
                
                # Count status codes
                analysis['status_codes'][status] = analysis['status_codes'].get(status, 0) + 1
                
                # Count popular paths
                analysis['paths'][path] = analysis['paths'].get(path, 0) + 1
                
                # Track timestamps
                analysis['timestamps'].append(timestamp)
                
                # Check for suspicious activity
                if status in ['401', '403', '404'] or method in ['PUT', 'DELETE']:
                    analysis['suspicious_activity'].append({
                        'ip': ip,
                        'method': method,
                        'path': path,
                        'status': status,
                        'timestamp': timestamp
                    })
            
            # Check for error levels
            for level, pattern in self.error_patterns.items():
                if re.search(pattern, line, re.IGNORECASE):
                    analysis['errors_by_level'][level].append(line)
                    break
        
        # Convert sets to lists for JSON serialization
        analysis['ips'] = list(analysis['ips'])
        
        return analysis


def main():
    """
    Main function demonstrating the data validation and extraction tools
    """
    print("🔍" * 20)
    print("    UNIVERSAL DATA VALIDATOR & EXTRACTOR")
    print("🔍" * 20)
    print("Your comprehensive data validation and extraction toolkit!")
    print()
    
    validator = DataValidator()
    extractor = DataExtractor()
    log_analyzer = LogAnalyzer()
    
    while True:
        print("\n" + "=" * 50)
        print("🛠️ MAIN MENU")
        print("=" * 50)
        print("1. Validate single data item")
        print("2. Extract data from text")
        print("3. Clean and format text")
        print("4. Analyze log file")
        print("5. Batch validate from file")
        print("6. Password strength checker")
        print("7. Credit card validator")
        print("8. Demo with sample data")
        print("9. Exit")
        
        try:
            choice = input("\nSelect option (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Goodbye! Keep your data clean and validated!")
            break
        
        if choice == "1":
            # Single data validation
            print("\n📝 Single Data Validation")
            print("-" * 30)
            print("Available validators:")
            print("1. Email address")
            print("2. Phone number")
            print("3. URL")
            print("4. Credit card")
            print("5. Password")
            
            validator_choice = input("Choose validator (1-5): ").strip()
            data_input = input("Enter data to validate: ").strip()
            
            if validator_choice == "1":
                result = validator.validate_email(data_input)
            elif validator_choice == "2":
                result = validator.validate_phone(data_input)
            elif validator_choice == "3":
                result = validator.validate_url(data_input)
            elif validator_choice == "4":
                result = validator.validate_credit_card(data_input)
            elif validator_choice == "5":
                result = validator.validate_password(data_input)
            else:
                print("❌ Invalid validator choice")
                continue
            
            # Display results
            print(f"\n📊 Validation Results:")
            print(f"Input: {result['input']}")
            print(f"Type: {result['type']}")
            print(f"Valid: {'✅ Yes' if result['valid'] else '❌ No'}")
            
            if 'normalized' in result:
                print(f"Normalized: {result['normalized']}")
            
            if 'card_type' in result and result['card_type']:
                print(f"Card Type: {result['card_type']}")
            
            if 'strength' in result:
                print(f"Strength: {result['strength']} ({result['score']}/{result['max_score']})")
            
            if result.get('issues'):
                print("Issues:")
                for issue in result['issues']:
                    print(f"   • {issue}")
            
            if result.get('suggestions'):
                print("Suggestions:")
                for suggestion in result['suggestions']:
                    print(f"   • {suggestion}")
            
            if result.get('warnings'):
                print("Warnings:")
                for warning in result['warnings']:
                    print(f"   ⚠️ {warning}")
        
        elif choice == "2":
            # Data extraction
            print("\n🔍 Data Extraction from Text")
            print("-" * 35)
            print("Paste your text (press Enter twice to finish):")
            
            text_lines = []
            empty_line_count = 0
            while empty_line_count < 2:
                try:
                    line = input()
                    if line == "":
                        empty_line_count += 1
                    else:
                        empty_line_count = 0
                    text_lines.append(line)
                except (EOFError, KeyboardInterrupt):
                    break
            
            text = "\n".join(text_lines).strip()
            
            if text:
                extracted_data = extractor.extract_all_data(text)
                
                if extracted_data:
                    print("\n📊 Extracted Data:")
                    print("-" * 25)
                    for data_type, items in extracted_data.items():
                        if items:
                            print(f"\n{data_type.replace('_', ' ').title()}:")
                            for item in items:
                                print(f"   • {item}")
                else:
                    print("🔍 No structured data found in the text")
            else:
                print("❌ No text provided")
        
        elif choice == "3":
            # Text cleaning
            print("\n🧹 Text Cleaning and Formatting")
            print("-" * 35)
            print("Enter text to clean (press Enter twice to finish):")
            
            text_lines = []
            empty_line_count = 0
            while empty_line_count < 2:
                try:
                    line = input()
                    if line == "":
                        empty_line_count += 1
                    else:
                        empty_line_count = 0
                    text_lines.append(line)
                except (EOFError, KeyboardInterrupt):
                    break
            
            text = "\n".join(text_lines).strip()
            
            if text:
                cleaned_text = extractor.clean_and_format_data(text)
                print(f"\n📝 Original text length: {len(text)} characters")
                print(f"🧹 Cleaned text length: {len(cleaned_text)} characters")
                print(f"\n--- Cleaned Text ---")
                print(cleaned_text)
            else:
                print("❌ No text provided")
        
        elif choice == "4":
            # Log analysis
            print("\n📊 Log File Analysis")
            print("-" * 25)
            print("Paste log content (press Enter twice to finish):")
            
            log_lines = []
            empty_line_count = 0
            while empty_line_count < 2:
                try:
                    line = input()
                    if line == "":
                        empty_line_count += 1
                    else:
                        empty_line_count = 0
                    log_lines.append(line)
                except (EOFError, KeyboardInterrupt):
                    break
            
            log_content = "\n".join(log_lines).strip()
            
            if log_content:
                analysis = log_analyzer.analyze_log_content(log_content)
                
                print(f"\n📊 Log Analysis Results:")
                print("-" * 30)
                print(f"Total lines: {analysis['total_lines']}")
                print(f"Structured entries: {analysis['structured_entries']}")
                print(f"Unique IPs: {len(analysis['ips'])}")
                
                if analysis['http_methods']:
                    print(f"\n🌐 HTTP Methods:")
                    for method, count in analysis['http_methods'].items():
                        print(f"   {method}: {count}")
                
                if analysis['status_codes']:
                    print(f"\n📈 Status Codes:")
                    for code, count in sorted(analysis['status_codes'].items()):
                        print(f"   {code}: {count}")
                
                # Show errors by level
                for level, errors in analysis['errors_by_level'].items():
                    if errors:
                        print(f"\n{level.upper()} Messages ({len(errors)}):")
                        for error in errors[:5]:  # Show first 5
                            print(f"   • {error[:80]}{'...' if len(error) > 80 else ''}")
                        if len(errors) > 5:
                            print(f"   ... and {len(errors) - 5} more")
                
                if analysis['suspicious_activity']:
                    print(f"\n⚠️ Suspicious Activity ({len(analysis['suspicious_activity'])}):")
                    for activity in analysis['suspicious_activity'][:5]:
                        print(f"   • {activity['ip']} - {activity['method']} {activity['path']} → {activity['status']}")
                    if len(analysis['suspicious_activity']) > 5:
                        print(f"   ... and {len(analysis['suspicious_activity']) - 5} more")
            else:
                print("❌ No log content provided")
        
        elif choice == "6":
            # Password strength checker
            print("\n🔐 Password Strength Checker")
            print("-" * 35)
            
            password = input("Enter password to check: ")
            result = validator.validate_password(password)
            
            print(f"\n📊 Password Analysis:")
            print(f"Strength: {result['strength']} ({result['score']}/{result['max_score']})")
            
            if result['suggestions']:
                print("\nSuggestions for improvement:")
                for suggestion in result['suggestions']:
                    print(f"   • {suggestion}")
        
        elif choice == "7":
            # Credit card validator
            print("\n💳 Credit Card Validator")
            print("-" * 30)
            
            card_number = input("Enter credit card number: ")
            result = validator.validate_credit_card(card_number)
            
            print(f"\n📊 Credit Card Analysis:")
            print(f"Valid: {'✅ Yes' if result['valid'] else '❌ No'}")
            
            if result['card_type']:
                print(f"Card Type: {result['card_type']}")
            
            if result.get('normalized'):
                print(f"Formatted: {result['normalized']}")
            
            if result['issues']:
                print("\nIssues:")
                for issue in result['issues']:
                    print(f"   • {issue}")
        
        elif choice == "8":
            # Demo with sample data
            print("\n🎯 Demo with Sample Data")
            print("-" * 30)
            
            sample_data = {
                'emails': [
                    'john.doe@example.com',
                    'invalid.email',
                    'user@domain',
                    'test.user+tag@company.co.uk'
                ],
                'phones': [
                    '(555) 123-4567',
                    '555-987-6543',
                    '123-456-789',  # Invalid
                    '+1 (555) 999-8888'
                ],
                'passwords': [
                    'password123',
                    'MySecureP@ssw0rd!',
                    'weak',
                    'StrongPassword2024!'
                ]
            }
            
            print("📧 Email Validation Demo:")
            for email in sample_data['emails']:
                result = validator.validate_email(email)
                status = "✅" if result['valid'] else "❌"
                print(f"   {status} {email}")
            
            print("\n📞 Phone Validation Demo:")
            for phone in sample_data['phones']:
                result = validator.validate_phone(phone)
                status = "✅" if result['valid'] else "❌"
                formatted = f" → {result.get('normalized', '')}" if result['valid'] else ""
                print(f"   {status} {phone}{formatted}")
            
            print("\n🔐 Password Strength Demo:")
            for password in sample_data['passwords']:
                result = validator.validate_password(password)
                print(f"   '{password}' → {result['strength']} ({result['score']}/7)")
        
        elif choice == "9":
            print("\n🎉 Thank you for using the Universal Data Validator!")
            print("💡 Remember: Clean, validated data is the foundation of great applications!")
            break
        
        else:
            print("❌ Invalid option. Please select 1-9.")


if __name__ == "__main__":
    main()