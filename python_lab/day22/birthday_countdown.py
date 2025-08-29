#!/usr/bin/env python3
"""
Day 22: Birthday Countdown Manager
A comprehensive birthday management system demonstrating date and time handling

This program showcases:
- Working with Python's datetime module
- Date calculations and formatting
- Age calculations and birthday countdowns
- File persistence for birthday data
- Error handling for date inputs
- Time-based sorting and filtering

Think of this as your personal birthday assistant that never forgets!
"""

import json
import os
from datetime import datetime, date, timedelta
from pathlib import Path


class BirthdayManager:
    """
    A comprehensive birthday management system
    Like having a personal assistant who remembers every birthday!
    """
    
    def __init__(self, data_file="birthdays.json"):
        """
        Initialize the birthday manager
        """
        self.data_file = Path(data_file)
        self.birthdays = self.load_birthdays()
        print("🎂 Birthday Countdown Manager Initialized!")
        print(f"📁 Data file: {self.data_file.absolute()}")
        print(f"👥 Currently tracking {len(self.birthdays)} birthdays")
    
    def load_birthdays(self):
        """
        Load birthday data from file with error handling
        """
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Convert date strings back to date objects
                    for birthday in data:
                        birthday['birth_date'] = datetime.strptime(
                            birthday['birth_date'], '%Y-%m-%d'
                        ).date()
                    return data
            else:
                print("📝 No existing birthday data found. Starting fresh!")
                return []
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"⚠️ Error loading birthday data: {e}")
            print("📝 Starting with empty birthday list")
            return []
    
    def save_birthdays(self):
        """
        Save birthday data to file
        """
        try:
            # Convert date objects to strings for JSON serialization
            data_to_save = []
            for birthday in self.birthdays:
                birthday_copy = birthday.copy()
                birthday_copy['birth_date'] = birthday['birth_date'].strftime('%Y-%m-%d')
                data_to_save.append(birthday_copy)
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ Error saving birthday data: {e}")
            return False
    
    def parse_date(self, date_string):
        """
        Parse various date formats flexibly
        Like a translator that understands many date languages
        """
        # Remove common separators and try different formats
        date_string = date_string.strip()
        
        formats_to_try = [
            "%Y-%m-%d",          # 2024-03-15
            "%m/%d/%Y",          # 03/15/2024
            "%d/%m/%Y",          # 15/03/2024
            "%B %d, %Y",         # March 15, 2024
            "%b %d, %Y",         # Mar 15, 2024
            "%d %B %Y",          # 15 March 2024
            "%d %b %Y",          # 15 Mar 2024
            "%Y/%m/%d",          # 2024/03/15
            "%d-%m-%Y",          # 15-03-2024
            "%m-%d-%Y",          # 03-15-2024
        ]
        
        for date_format in formats_to_try:
            try:
                return datetime.strptime(date_string, date_format).date()
            except ValueError:
                continue
        
        raise ValueError(f"Could not parse date: '{date_string}'")
    
    def calculate_age(self, birth_date):
        """
        Calculate someone's current age in years
        """
        today = date.today()
        age = today.year - birth_date.year
        
        # Check if birthday has occurred this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def days_until_birthday(self, birth_date):
        """
        Calculate days until next birthday
        """
        today = date.today()
        current_year = today.year
        
        # Create birthday for this year
        birthday_this_year = date(current_year, birth_date.month, birth_date.day)
        
        # If birthday already passed, calculate for next year
        if birthday_this_year < today:
            birthday_this_year = date(current_year + 1, birth_date.month, birth_date.day)
        
        days_left = (birthday_this_year - today).days
        return days_left, birthday_this_year
    
    def add_birthday(self, name, birth_date_string):
        """
        Add a new birthday to the system
        """
        try:
            # Parse the birth date
            birth_date = self.parse_date(birth_date_string)
            
            # Check if person already exists
            for birthday in self.birthdays:
                if birthday['name'].lower() == name.lower():
                    print(f"⚠️ {name} already exists in the system!")
                    response = input("Update their birthday? (y/n): ").strip().lower()
                    if response in ['y', 'yes']:
                        birthday['birth_date'] = birth_date
                        birthday['added_date'] = date.today()
                        print(f"✅ Updated {name}'s birthday!")
                        self.save_birthdays()
                        return True
                    else:
                        return False
            
            # Add new birthday
            new_birthday = {
                'name': name.title(),  # Capitalize properly
                'birth_date': birth_date,
                'added_date': date.today()
            }
            
            self.birthdays.append(new_birthday)
            self.save_birthdays()
            
            # Show confirmation with age info
            age = self.calculate_age(birth_date)
            days_left, next_birthday = self.days_until_birthday(birth_date)
            
            print(f"🎉 Added {name} to birthday list!")
            print(f"📅 Birthday: {birth_date.strftime('%B %d, %Y')}")
            print(f"🎂 Current age: {age} years old")
            print(f"⏰ Next birthday in {days_left} days")
            
            return True
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("💡 Try formats like: 2024-03-15, 03/15/2024, March 15 2024")
            return False
        except Exception as e:
            print(f"❌ Unexpected error adding birthday: {e}")
            return False
    
    def remove_birthday(self, name):
        """
        Remove a birthday from the system
        """
        for i, birthday in enumerate(self.birthdays):
            if birthday['name'].lower() == name.lower():
                removed = self.birthdays.pop(i)
                self.save_birthdays()
                print(f"🗑️ Removed {removed['name']} from birthday list")
                return True
        
        print(f"❌ Could not find '{name}' in birthday list")
        return False
    
    def list_all_birthdays(self):
        """
        List all birthdays with details
        """
        if not self.birthdays:
            print("📭 No birthdays stored yet!")
            return
        
        print(f"\n🎂 All Birthdays ({len(self.birthdays)} people)")
        print("=" * 60)
        
        # Sort by upcoming birthdays
        birthday_info = []
        for birthday in self.birthdays:
            age = self.calculate_age(birthday['birth_date'])
            days_left, next_birthday = self.days_until_birthday(birthday['birth_date'])
            birthday_info.append({
                'name': birthday['name'],
                'birth_date': birthday['birth_date'],
                'age': age,
                'days_left': days_left,
                'next_birthday': next_birthday
            })
        
        # Sort by days until next birthday
        birthday_info.sort(key=lambda x: x['days_left'])
        
        for info in birthday_info:
            print(f"👤 {info['name']:<20} | Born: {info['birth_date'].strftime('%B %d, %Y')}")
            print(f"   Age: {info['age']} years old | Next birthday: {info['days_left']} days")
            print(f"   📅 {info['next_birthday'].strftime('%A, %B %d, %Y')}")
            print("-" * 60)
    
    def upcoming_birthdays(self, days_ahead=30):
        """
        Show birthdays coming up in the next specified days
        """
        if not self.birthdays:
            print("📭 No birthdays stored yet!")
            return
        
        upcoming = []
        for birthday in self.birthdays:
            days_left, next_birthday = self.days_until_birthday(birthday['birth_date'])
            if days_left <= days_ahead:
                age_next = self.calculate_age(birthday['birth_date']) + 1
                upcoming.append({
                    'name': birthday['name'],
                    'days_left': days_left,
                    'next_birthday': next_birthday,
                    'age_next': age_next
                })
        
        if not upcoming:
            print(f"🎉 No birthdays in the next {days_ahead} days!")
            return
        
        # Sort by days until birthday
        upcoming.sort(key=lambda x: x['days_left'])
        
        print(f"\n🎈 Upcoming Birthdays (next {days_ahead} days)")
        print("=" * 50)
        
        for person in upcoming:
            days_left = person['days_left']
            if days_left == 0:
                print(f"🎉 TODAY: {person['name']} turns {person['age_next']}!")
            elif days_left == 1:
                print(f"🎈 TOMORROW: {person['name']} turns {person['age_next']}")
            else:
                day_name = person['next_birthday'].strftime('%A')
                print(f"📅 {days_left} days ({day_name}): {person['name']} turns {person['age_next']}")
    
    def birthday_reminders(self):
        """
        Generate personalized birthday reminder messages
        """
        if not self.birthdays:
            print("📭 No birthdays to remind about!")
            return
        
        reminders = []
        for birthday in self.birthdays:
            days_left, next_birthday = self.days_until_birthday(birthday['birth_date'])
            age_next = self.calculate_age(birthday['birth_date']) + 1
            name = birthday['name']
            
            if days_left == 0:
                message = f"🎉 {name}'s birthday is TODAY! They're turning {age_next}! 🎂"
            elif days_left == 1:
                message = f"🎈 {name}'s birthday is TOMORROW! Don't forget the gift! 🎁"
            elif days_left <= 7:
                day_name = next_birthday.strftime('%A')
                message = f"📅 {name}'s birthday is this {day_name} ({days_left} days) - turning {age_next}"
            elif days_left <= 30:
                message = f"📝 {name}'s birthday is in {days_left} days ({next_birthday.strftime('%B %d')})"
            else:
                continue  # Skip distant birthdays
            
            reminders.append((days_left, message))
        
        if not reminders:
            print("😊 No immediate birthday reminders!")
            return
        
        # Sort by urgency (days left)
        reminders.sort(key=lambda x: x[0])
        
        print("\n🔔 Birthday Reminders")
        print("=" * 40)
        for _, message in reminders:
            print(message)
    
    def birthday_statistics(self):
        """
        Show interesting statistics about birthdays
        """
        if not self.birthdays:
            print("📭 No birthday data for statistics!")
            return
        
        print("\n📊 Birthday Statistics")
        print("=" * 40)
        
        # Age statistics
        ages = [self.calculate_age(b['birth_date']) for b in self.birthdays]
        print(f"👥 Total people: {len(self.birthdays)}")
        print(f"🎂 Average age: {sum(ages) / len(ages):.1f} years")
        print(f"👶 Youngest: {min(ages)} years old")
        print(f"👴 Oldest: {max(ages)} years old")
        
        # Month distribution
        months = {}
        for birthday in self.birthdays:
            month_name = birthday['birth_date'].strftime('%B')
            months[month_name] = months.get(month_name, 0) + 1
        
        print("\n📅 Birthdays by month:")
        for month, count in sorted(months.items()):
            print(f"   {month}: {count} {'person' if count == 1 else 'people'}")
        
        # Zodiac signs (simplified)
        zodiac_signs = self.calculate_zodiac_distribution()
        if zodiac_signs:
            print("\n⭐ Zodiac sign distribution:")
            for sign, count in zodiac_signs.items():
                print(f"   {sign}: {count}")
    
    def calculate_zodiac_distribution(self):
        """
        Calculate zodiac sign distribution (simplified)
        """
        zodiac_signs = {}
        
        for birthday in self.birthdays:
            birth_date = birthday['birth_date']
            sign = self.get_zodiac_sign(birth_date.month, birth_date.day)
            zodiac_signs[sign] = zodiac_signs.get(sign, 0) + 1
        
        return zodiac_signs
    
    def get_zodiac_sign(self, month, day):
        """
        Determine zodiac sign based on birth month and day
        """
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "♈ Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "♉ Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "♊ Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "♋ Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "♌ Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "♍ Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "♎ Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "♏ Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "♐ Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "♑ Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "♒ Aquarius"
        else:
            return "♓ Pisces"
    
    def search_birthdays(self, search_term):
        """
        Search for birthdays by name
        """
        matches = []
        search_term = search_term.lower()
        
        for birthday in self.birthdays:
            if search_term in birthday['name'].lower():
                matches.append(birthday)
        
        if not matches:
            print(f"❌ No birthdays found matching '{search_term}'")
            return
        
        print(f"\n🔍 Search results for '{search_term}':")
        print("-" * 40)
        
        for birthday in matches:
            age = self.calculate_age(birthday['birth_date'])
            days_left, next_birthday = self.days_until_birthday(birthday['birth_date'])
            
            print(f"👤 {birthday['name']}")
            print(f"   Born: {birthday['birth_date'].strftime('%B %d, %Y')} (age {age})")
            print(f"   Next birthday: {days_left} days ({next_birthday.strftime('%A, %B %d')})")
            print()


def demonstrate_date_functions():
    """
    Demonstrate various date and time functions
    """
    print("\n🔧 Date & Time Function Demonstrations")
    print("=" * 50)
    
    # Current date/time
    now = datetime.now()
    today = date.today()
    
    print(f"📅 Current date: {today}")
    print(f"⏰ Current time: {now.strftime('%I:%M:%S %p')}")
    print(f"🌍 Full timestamp: {now.strftime('%A, %B %d, %Y at %I:%M %p')}")
    
    # Date formatting examples
    print(f"\n📋 Date formatting examples:")
    print(f"   American format: {today.strftime('%m/%d/%Y')}")
    print(f"   European format: {today.strftime('%d/%m/%Y')}")
    print(f"   ISO format: {today.strftime('%Y-%m-%d')}")
    print(f"   Full format: {today.strftime('%A, %B %d, %Y')}")
    
    # Date calculations
    print(f"\n🧮 Date calculations:")
    print(f"   Tomorrow: {(today + timedelta(days=1)).strftime('%B %d, %Y')}")
    print(f"   One week from now: {(today + timedelta(weeks=1)).strftime('%B %d, %Y')}")
    print(f"   30 days ago: {(today - timedelta(days=30)).strftime('%B %d, %Y')}")
    
    # Age calculation example
    sample_birth_date = date(1990, 5, 15)
    years_old = today.year - sample_birth_date.year
    if (today.month, today.day) < (sample_birth_date.month, sample_birth_date.day):
        years_old -= 1
    print(f"   If born May 15, 1990, you'd be {years_old} years old")


def main():
    """
    Main function demonstrating the Birthday Manager
    """
    print("🎂" * 20)
    print("    BIRTHDAY COUNTDOWN MANAGER")
    print("🎂" * 20)
    print("Your personal birthday assistant that never forgets!")
    print()
    
    # Initialize birthday manager
    manager = BirthdayManager()
    
    # Demo some date functions first
    demonstrate_date_functions()
    
    while True:
        print("\n" + "=" * 40)
        print("🎂 BIRTHDAY MANAGER MENU")
        print("=" * 40)
        print("1. Add birthday")
        print("2. List all birthdays")
        print("3. Upcoming birthdays")
        print("4. Birthday reminders")
        print("5. Birthday statistics")
        print("6. Search birthdays")
        print("7. Remove birthday")
        print("8. Add sample birthdays (for demo)")
        print("9. Exit")
        
        try:
            choice = input("\nSelect option (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Goodbye! Keep celebrating birthdays!")
            break
        
        if choice == "1":
            print("\n➕ Add New Birthday")
            print("-" * 20)
            name = input("Enter name: ").strip()
            if name:
                birth_date = input("Enter birth date (e.g., 1995-08-15, March 15 1995): ").strip()
                if birth_date:
                    manager.add_birthday(name, birth_date)
                else:
                    print("❌ Birth date cannot be empty")
            else:
                print("❌ Name cannot be empty")
        
        elif choice == "2":
            manager.list_all_birthdays()
        
        elif choice == "3":
            try:
                days = int(input("Show birthdays in next how many days? (default 30): ") or "30")
                manager.upcoming_birthdays(days)
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == "4":
            manager.birthday_reminders()
        
        elif choice == "5":
            manager.birthday_statistics()
        
        elif choice == "6":
            search_term = input("Enter name to search for: ").strip()
            if search_term:
                manager.search_birthdays(search_term)
            else:
                print("❌ Search term cannot be empty")
        
        elif choice == "7":
            name = input("Enter name to remove: ").strip()
            if name:
                manager.remove_birthday(name)
            else:
                print("❌ Name cannot be empty")
        
        elif choice == "8":
            # Add sample birthdays for demonstration
            sample_birthdays = [
                ("Alice Johnson", "1995-03-15"),
                ("Bob Smith", "1988-07-22"),
                ("Charlie Brown", "2000-12-01"),
                ("Diana Prince", "1992-09-30"),
                ("Eve Adams", "1985-06-18")
            ]
            
            print("\n📝 Adding sample birthdays...")
            for name, birth_date in sample_birthdays:
                try:
                    manager.add_birthday(name, birth_date)
                except:
                    pass  # Skip if already exists
        
        elif choice == "9":
            print("\n🎉 Thank you for using Birthday Manager!")
            print("💝 Remember: The best gift is remembering someone's special day!")
            break
        
        else:
            print("❌ Invalid option. Please select 1-9.")


if __name__ == "__main__":
    main()