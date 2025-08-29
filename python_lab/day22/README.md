# Day 22: Date and Time Handling - Working with Time Like a Pro

Welcome to Day 22 of Week 4! Today we're diving into one of Python's most practical modules - handling dates and times. Think of this as learning to be a time wizard who can calculate ages, count down to birthdays, and work with schedules effortlessly.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Work with Python's datetime module to handle dates and times
- Perform date calculations and comparisons
- Format dates and times for different purposes
- Calculate time differences and durations
- Build a birthday countdown program
- Handle time zones and scheduling scenarios

## ⏰ Why Date and Time Handling Matters

### Real-World Applications

Date and time handling is everywhere in programming:
- **Scheduling Apps**: Calendar applications, appointment systems
- **Age Verification**: Checking if someone is old enough for certain services  
- **Data Analysis**: Analyzing trends over time, seasonal patterns
- **Logging Systems**: Recording when events happened
- **Reminders**: Birthday notifications, deadline alerts
- **Financial Systems**: Interest calculations, payment schedules

Think of Python's datetime module as your personal assistant who never forgets important dates!

## 📅 The datetime Module - Your Time Toolkit

### Getting the Current Date and Time

```python
from datetime import datetime, date, time

# Get current date and time
now = datetime.now()
print(f"Right now it is: {now}")

# Get just the current date
today = date.today()
print(f"Today is: {today}")

# Output:
# Right now it is: 2024-03-15 14:30:45.123456
# Today is: 2024-03-15
```

### Creating Specific Dates

```python
from datetime import datetime, date

# Create a specific date
my_birthday = date(1995, 8, 15)  # Year, Month, Day
print(f"My birthday is: {my_birthday}")

# Create a specific datetime
meeting_time = datetime(2024, 12, 25, 14, 30, 0)  # Year, Month, Day, Hour, Minute, Second
print(f"Christmas meeting: {meeting_time}")

# Output:
# My birthday is: 1995-08-15
# Christmas meeting: 2024-12-25 14:30:00
```

## 📊 Date Formatting - Making Dates Look Pretty

### Basic Formatting with strftime()

Think of strftime() as a date formatter that can make your dates look exactly how you want:

```python
from datetime import datetime

now = datetime.now()

# Different ways to format dates
print("American style:", now.strftime("%m/%d/%Y"))           # 03/15/2024
print("European style:", now.strftime("%d/%m/%Y"))           # 15/03/2024
print("Full date:", now.strftime("%A, %B %d, %Y"))          # Friday, March 15, 2024
print("Time only:", now.strftime("%H:%M:%S"))               # 14:30:45
print("12-hour time:", now.strftime("%I:%M %p"))            # 02:30 PM
print("ISO format:", now.strftime("%Y-%m-%d %H:%M:%S"))     # 2024-03-15 14:30:45
```

### Common Format Codes

```python
# Here's your datetime formatting cheat sheet:
format_codes = {
    "%Y": "4-digit year (2024)",
    "%y": "2-digit year (24)", 
    "%m": "Month number (03)",
    "%B": "Full month name (March)",
    "%b": "Short month name (Mar)",
    "%d": "Day of month (15)",
    "%A": "Full day name (Friday)",
    "%a": "Short day name (Fri)",
    "%H": "24-hour format hour (14)",
    "%I": "12-hour format hour (02)",
    "%M": "Minutes (30)",
    "%S": "Seconds (45)",
    "%p": "AM/PM"
}

# Example: Creating a custom format
event_date = datetime(2024, 7, 4, 19, 30)
custom_format = event_date.strftime("Join us on %A, %B %d at %I:%M %p!")
print(custom_format)  # "Join us on Thursday, July 04 at 07:30 PM!"
```

## 🧮 Date Calculations - Time Math Made Easy

### Calculating Age

```python
from datetime import date

def calculate_age(birth_date):
    """
    Calculate someone's age in years
    Like having a calculator that knows about leap years!
    """
    today = date.today()
    
    # Calculate the difference in years
    age = today.year - birth_date.year
    
    # Check if birthday has happened this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

# Test the function
birthday = date(1995, 8, 15)
age = calculate_age(birthday)
print(f"If you were born on {birthday}, you are {age} years old")

# More detailed age calculation
def detailed_age(birth_date):
    """Calculate age in years, months, and days"""
    today = date.today()
    
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    # Adjust for negative days
    if days < 0:
        months -= 1
        # Get days in previous month
        if today.month == 1:
            prev_month = date(today.year - 1, 12, 1)
        else:
            prev_month = date(today.year, today.month - 1, 1)
        days += (date(today.year, today.month, 1) - prev_month).days
    
    # Adjust for negative months
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days

# Example usage
birth = date(2000, 5, 20)
years, months, days = detailed_age(birth)
print(f"You are {years} years, {months} months, and {days} days old")
```

### Working with Time Differences (timedelta)

```python
from datetime import datetime, timedelta

# timedelta represents a duration - like saying "in 3 days" or "2 hours ago"
now = datetime.now()

# Future dates
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_30_days = now + timedelta(days=30)

print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d %H:%M')}")
print(f"Next week: {next_week.strftime('%Y-%m-%d %H:%M')}")
print(f"In 30 days: {in_30_days.strftime('%Y-%m-%d %H:%M')}")

# Past dates
yesterday = now - timedelta(days=1)
last_month = now - timedelta(days=30)

print(f"Yesterday: {yesterday.strftime('%Y-%m-%d %H:%M')}")
print(f"30 days ago: {last_month.strftime('%Y-%m-%d %H:%M')}")

# Calculate difference between two dates
graduation_date = datetime(2024, 6, 15)
time_until_graduation = graduation_date - now

if time_until_graduation.days > 0:
    print(f"Days until graduation: {time_until_graduation.days}")
else:
    print(f"Graduated {abs(time_until_graduation.days)} days ago")
```

## 🎂 Practical Examples

### Birthday Tracker

```python
from datetime import date, datetime

def days_until_birthday(birth_month, birth_day):
    """
    Calculate days until next birthday
    Like a countdown calendar that never forgets!
    """
    today = date.today()
    current_year = today.year
    
    # Create birthday for this year
    birthday_this_year = date(current_year, birth_month, birth_day)
    
    # If birthday already passed this year, calculate for next year
    if birthday_this_year < today:
        birthday_this_year = date(current_year + 1, birth_month, birth_day)
    
    days_left = (birthday_this_year - today).days
    
    return days_left, birthday_this_year

# Example usage
days_left, next_birthday = days_until_birthday(8, 15)
print(f"Days until your birthday: {days_left}")
print(f"Your next birthday is: {next_birthday.strftime('%A, %B %d, %Y')}")

# Birthday reminder system
def birthday_reminder(name, birth_month, birth_day):
    """Generate a personalized birthday reminder message"""
    days_left, next_birthday = days_until_birthday(birth_month, birth_day)
    
    if days_left == 0:
        return f"🎉 Happy Birthday {name}! 🎂"
    elif days_left == 1:
        return f"🎈 {name}'s birthday is TOMORROW! Don't forget! 🎁"
    elif days_left <= 7:
        return f"📅 {name}'s birthday is in {days_left} days ({next_birthday.strftime('%A')})"
    elif days_left <= 30:
        return f"📝 {name}'s birthday is in {days_left} days ({next_birthday.strftime('%B %d')})"
    else:
        return f"📆 {name}'s birthday is on {next_birthday.strftime('%B %d')} ({days_left} days away)"

# Test the reminder system
print(birthday_reminder("Alice", 3, 20))
print(birthday_reminder("Bob", 12, 25))
```

### Meeting Scheduler

```python
from datetime import datetime, timedelta

def schedule_meeting(start_time, duration_minutes):
    """
    Schedule a meeting with start and end times
    Like having a personal assistant who manages your calendar
    """
    end_time = start_time + timedelta(minutes=duration_minutes)
    
    meeting_info = {
        'start': start_time,
        'end': end_time,
        'duration': duration_minutes
    }
    
    return meeting_info

def format_meeting_time(meeting_info):
    """Format meeting information nicely"""
    start = meeting_info['start']
    end = meeting_info['end']
    duration = meeting_info['duration']
    
    date_str = start.strftime("%A, %B %d, %Y")
    time_str = f"{start.strftime('%I:%M %p')} - {end.strftime('%I:%M %p')}"
    
    return f"Meeting scheduled for {date_str}\nTime: {time_str}\nDuration: {duration} minutes"

# Example usage
meeting_start = datetime(2024, 3, 20, 14, 30)  # March 20, 2024 at 2:30 PM
meeting = schedule_meeting(meeting_start, 90)  # 90-minute meeting

print(format_meeting_time(meeting))
```

## 🔄 Working with Different Date Formats

### Parsing Date Strings

```python
from datetime import datetime

def parse_flexible_date(date_string):
    """
    Parse dates from different string formats
    Like a translator that understands many date languages
    """
    formats_to_try = [
        "%Y-%m-%d",          # 2024-03-15
        "%m/%d/%Y",          # 03/15/2024
        "%d/%m/%Y",          # 15/03/2024
        "%B %d, %Y",         # March 15, 2024
        "%d %B %Y",          # 15 March 2024
        "%Y-%m-%d %H:%M:%S", # 2024-03-15 14:30:45
    ]
    
    for date_format in formats_to_try:
        try:
            return datetime.strptime(date_string, date_format)
        except ValueError:
            continue
    
    raise ValueError(f"Could not parse date: {date_string}")

# Test different date formats
test_dates = [
    "2024-03-15",
    "03/15/2024", 
    "March 15, 2024",
    "2024-03-15 14:30:45"
]

for date_str in test_dates:
    try:
        parsed_date = parse_flexible_date(date_str)
        print(f"'{date_str}' → {parsed_date}")
    except ValueError as e:
        print(f"Could not parse: {date_str}")
```

## 📊 Time Analysis Functions

### Working Week Calculator

```python
from datetime import date, timedelta

def get_working_days(start_date, end_date):
    """
    Calculate working days between two dates (excluding weekends)
    Like counting only the days you actually have to work!
    """
    working_days = 0
    current_date = start_date
    
    while current_date <= end_date:
        # Monday is 0, Sunday is 6
        if current_date.weekday() < 5:  # Monday to Friday
            working_days += 1
        current_date += timedelta(days=1)
    
    return working_days

def project_deadline_calculator(start_date, working_days_needed):
    """Calculate when a project will be finished"""
    current_date = start_date
    days_counted = 0
    
    while days_counted < working_days_needed:
        if current_date.weekday() < 5:  # It's a working day
            days_counted += 1
        
        if days_counted < working_days_needed:
            current_date += timedelta(days=1)
    
    return current_date

# Example usage
project_start = date(2024, 3, 15)  # Friday
working_days = get_working_days(project_start, date(2024, 3, 29))
print(f"Working days in period: {working_days}")

deadline = project_deadline_calculator(project_start, 10)
print(f"10 working days from {project_start}: {deadline}")
```

## 🏃‍♂️ Practice Exercises

### Exercise 1: Personal Time Calculator
Create a comprehensive time calculator for your personal life:

```python
def personal_time_calculator():
    """
    Calculate various personal time metrics
    """
    # Calculate your age in different units
    # Days until your next birthday  
    # How many weekends until summer vacation
    # Your age in days, hours, minutes
    pass
```

### Exercise 2: Event Countdown System
Build a system that tracks multiple upcoming events:

```python
def event_countdown_system():
    """
    Manage countdowns to multiple events
    """
    # Store multiple events with dates
    # Show countdowns to each event
    # Identify which event is coming up next
    # Show events happening this week/month
    pass
```

### Exercise 3: Time Zone Converter
Create a basic time zone converter:

```python
def time_zone_converter(local_time, hours_offset):
    """
    Convert time to different time zones
    """
    # Convert local time to another timezone
    # Show multiple timezone times simultaneously 
    # Handle day changes when converting
    pass
```

## 📝 Key Takeaways

1. **datetime module is powerful** - It handles most date/time needs elegantly
2. **strftime() formats dates** - Learn the common format codes for pretty display
3. **timedelta handles durations** - Perfect for calculations like "in 3 days" or "2 weeks ago"
4. **Date parsing needs error handling** - People write dates in many different ways
5. **Consider edge cases** - Leap years, weekends, month boundaries matter
6. **Real-world applications are everywhere** - Scheduling, age calculation, countdowns

## 🎯 Today's Project Preview

Today you'll build a **Birthday Countdown Manager** that demonstrates all these concepts. It will:
- Store multiple birthdays with names
- Calculate ages and days until next birthday
- Show upcoming birthdays in chronological order
- Generate personalized birthday reminders
- Handle different date input formats
- Create birthday statistics and insights

The goal is to create something genuinely useful that showcases Python's date handling capabilities!

## 🔗 Connection to Previous Weeks

### Building on Week 3
- **Functions (Day 15-16)**: All date calculations become reusable functions
- **File Handling (Day 19)**: Store birthday data persistently
- **Error Handling (Day 20)**: Handle invalid date inputs gracefully
- **Built-ins (Day 17)**: Use sorting and filtering for date lists

### Looking Forward to This Week
This foundation in date handling will be crucial for:
- **Data Analysis (Day 26)**: Time-series data analysis
- **Web Scraping (Day 24)**: Handling dates in scraped data
- **GUI Programming (Day 28)**: Date pickers and calendar widgets
- **Final Projects**: Any real-world application needs good date handling

Working with dates and times is one of those fundamental skills that makes your programs feel professional and polished. Let's build something amazing!