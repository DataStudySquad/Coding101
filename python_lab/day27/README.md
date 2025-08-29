# Day 27: Object-Oriented Programming - Building with Classes and Objects

Welcome to Day 27! Today we're diving into Object-Oriented Programming (OOP) - one of the most powerful programming paradigms. Think of OOP as learning to build with LEGO blocks, where you create reusable components (classes) that can be combined to build complex, organized, and maintainable programs.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Understand the core concepts of Object-Oriented Programming
- Create classes and objects in Python
- Work with attributes (data) and methods (functions) in classes
- Understand encapsulation, inheritance, and polymorphism
- Build a comprehensive Library Management System
- Apply OOP principles to solve real-world problems

## 🧱 What is Object-Oriented Programming?

### The Building Blocks Analogy

Imagine you're building a city:

**Without OOP (Procedural Programming):**
- You have individual functions scattered everywhere
- Hard to organize and maintain
- Difficult to reuse components
- Changes in one place can break other places

**With OOP:**
- You have blueprints (classes) for different building types
- Each building (object) has its own properties and behaviors
- Easy to create multiple similar buildings
- Well-organized and maintainable city structure

### Real-World Examples

```python
# Think of these real-world objects and their properties/behaviors:

class Car:
    # Properties (attributes): color, model, speed, fuel_level
    # Behaviors (methods): start(), stop(), accelerate(), brake()

class BankAccount:
    # Properties: account_number, balance, owner
    # Behaviors: deposit(), withdraw(), check_balance()

class Student:
    # Properties: name, student_id, grades, courses
    # Behaviors: enroll(), study(), take_exam(), graduate()
```

## 🏗️ Classes and Objects - The Foundation

### Creating Your First Class

```python
class Dog:
    """
    A simple Dog class demonstrating basic OOP concepts
    Think of this as a blueprint for creating dogs
    """
    
    # Class attribute (shared by all dogs)
    species = "Canis familiaris"
    
    def __init__(self, name, breed, age):
        """
        Constructor method - called when creating a new dog
        Like filling out a birth certificate for each puppy
        """
        # Instance attributes (unique to each dog)
        self.name = name
        self.breed = breed
        self.age = age
        self.is_sleeping = False
    
    def bark(self):
        """
        Instance method - behavior that all dogs can do
        """
        return f"{self.name} says Woof! Woof!"
    
    def sleep(self):
        """
        Change the dog's state
        """
        self.is_sleeping = True
        return f"{self.name} is now sleeping... 😴"
    
    def wake_up(self):
        """
        Wake up the dog
        """
        self.is_sleeping = False
        return f"{self.name} is now awake and ready to play!"
    
    def describe(self):
        """
        Return a description of the dog
        """
        status = "sleeping" if self.is_sleeping else "awake"
        return f"{self.name} is a {self.age}-year-old {self.breed} who is currently {status}"
    
    def have_birthday(self):
        """
        Age the dog by one year
        """
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old! 🎂"

# Creating objects (instances) from the class
print("🐕 Creating some dogs...")

# Create individual dog objects
buddy = Dog("Buddy", "Golden Retriever", 3)
max_dog = Dog("Max", "German Shepherd", 5)
bella = Dog("Bella", "Poodle", 2)

# Use the objects
print(buddy.describe())
print(buddy.bark())
print(buddy.sleep())
print(buddy.describe())

print("\n" + max_dog.bark())
print(max_dog.have_birthday())

print("\n" + bella.describe())
print(bella.wake_up())
```

### Understanding `self` - The Key to Instance Methods

```python
class Person:
    """
    Understanding 'self' - it refers to the specific instance
    Like saying "this particular person" vs "people in general"
    """
    
    def __init__(self, name, age):
        self.name = name  # This specific person's name
        self.age = age    # This specific person's age
        self.friends = []  # This person's friend list
    
    def introduce(self):
        # 'self' lets us access THIS person's attributes
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def make_friend(self, other_person):
        # 'self' is the person making the friend
        # 'other_person' is the person being befriended
        if other_person not in self.friends:
            self.friends.append(other_person)
            other_person.friends.append(self)  # Add friendship both ways
            return f"{self.name} and {other_person.name} are now friends!"
        else:
            return f"{self.name} and {other_person.name} are already friends"
    
    def list_friends(self):
        if not self.friends:
            return f"{self.name} has no friends yet"
        
        friend_names = [friend.name for friend in self.friends]
        return f"{self.name}'s friends: {', '.join(friend_names)}"

# Demonstrate 'self' in action
alice = Person("Alice", 25)
bob = Person("Bob", 30)
charlie = Person("Charlie", 28)

print(alice.introduce())  # 'self' refers to alice
print(bob.introduce())    # 'self' refers to bob

print(alice.make_friend(bob))    # alice is 'self', bob is 'other_person'
print(charlie.make_friend(alice)) # charlie is 'self', alice is 'other_person'

print(alice.list_friends())
print(bob.list_friends())
print(charlie.list_friends())
```

## 🏛️ The Four Pillars of OOP

### 1. Encapsulation - Data Protection

```python
class BankAccount:
    """
    Encapsulation: Keeping data safe and controlling access
    Like having a safe with specific ways to open it
    """
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._account_number = self._generate_account_number()  # Protected attribute
        self.__balance = initial_balance  # Private attribute (name mangling)
        self.__transaction_history = []   # Private list
    
    def _generate_account_number(self):
        """
        Protected method (single underscore) - internal use
        """
        import random
        return f"ACC-{random.randint(100000, 999999)}"
    
    def deposit(self, amount):
        """
        Public method - anyone can use this
        """
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        """
        Controlled access to private balance
        """
        if amount <= 0:
            return "Withdrawal amount must be positive"
        elif amount > self.__balance:
            return f"Insufficient funds. Current balance: ${self.__balance}"
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
    
    def get_balance(self):
        """
        Safe way to access private balance
        """
        return self.__balance
    
    def get_transaction_history(self):
        """
        Safe way to access transaction history
        """
        return self.__transaction_history.copy()  # Return a copy, not the original
    
    def account_info(self):
        """
        Public interface to account information
        """
        return f"Account holder: {self.account_holder}\nAccount: {self._account_number}\nBalance: ${self.__balance}"

# Demonstrate encapsulation
account = BankAccount("John Doe", 1000)

print(account.account_info())
print(account.deposit(500))
print(account.withdraw(200))
print(f"Current balance: ${account.get_balance()}")

# Try to access private attributes (this shows why encapsulation matters)
print(f"Account holder (public): {account.account_holder}")  # This works
# print(account.__balance)  # This would cause an AttributeError!

# The "correct" way to access the balance:
print(f"Balance (through method): ${account.get_balance()}")
```

### 2. Inheritance - Building on Existing Code

```python
class Animal:
    """
    Base class (parent class)
    Like a general blueprint that other classes can build upon
    """
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self, food):
        return f"{self.name} is eating {food}"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Mammal(Animal):
    """
    Derived class (child class) that inherits from Animal
    Gets all Animal capabilities plus its own
    """
    
    def __init__(self, name, species, fur_color):
        # Call parent constructor
        super().__init__(name, species)
        self.fur_color = fur_color
        self.body_temperature = "warm-blooded"
    
    def give_birth(self):
        return f"{self.name} gives birth to live young"

class Bird(Animal):
    """
    Another child class with different specializations
    """
    
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span
        self.can_fly = True
    
    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying with a {self.wing_span} wingspan!"
        else:
            return f"{self.name} cannot fly"
    
    def make_sound(self):
        # Override parent method
        return f"{self.name} chirps and sings"

class Fish(Animal):
    """
    Third child class - aquatic specialization
    """
    
    def __init__(self, name, species, water_type):
        super().__init__(name, species)
        self.water_type = water_type  # "freshwater" or "saltwater"
    
    def swim(self):
        return f"{self.name} swims gracefully in {self.water_type}"
    
    def make_sound(self):
        # Fish are typically quiet
        return f"{self.name} makes bubbles"

# Demonstrate inheritance
print("🦁 Creating animals with inheritance...")

# Create instances of each class
lion = Mammal("Simba", "Lion", "golden")
eagle = Bird("Eddie", "Eagle", "6 feet")
salmon = Fish("Sally", "Salmon", "freshwater")

# All can use Animal methods
print(lion.eat("meat"))
print(eagle.sleep())
print(salmon.eat("algae"))

# Each has their specialized methods
print(lion.give_birth())
print(eagle.fly())
print(salmon.swim())

# Polymorphism - same method name, different behavior
print("\n🎵 Listen to the different sounds:")
print(lion.make_sound())  # Uses Animal's default
print(eagle.make_sound()) # Uses Bird's override
print(salmon.make_sound()) # Uses Fish's override
```

### 3. Polymorphism - One Interface, Many Forms

```python
class Shape:
    """
    Base class for all shapes
    """
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        # This will be overridden by child classes
        return 0
    
    def perimeter(self):
        return 0
    
    def describe(self):
        return f"This is a {self.name} with area {self.area()} and perimeter {self.perimeter():.2f}"

class Rectangle(Shape):
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    
    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Demonstrate polymorphism
def print_shape_info(shape):
    """
    This function can work with ANY shape object!
    This is polymorphism - one interface, many implementations
    """
    print(shape.describe())

# Create different shapes
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5)
]

print("📐 Demonstrating polymorphism with shapes:")
for shape in shapes:
    print_shape_info(shape)  # Same function, different behaviors!

# Calculate total area of all shapes
total_area = sum(shape.area() for shape in shapes)
print(f"\n📊 Total area of all shapes: {total_area:.2f}")
```

## 📚 Building a Library Management System

Let's create a comprehensive example that demonstrates all OOP concepts:

```python
from datetime import datetime, timedelta

class Book:
    """
    Represents a book in the library system
    """
    
    def __init__(self, title, author, isbn, category, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.publication_year = publication_year
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None
        self.borrow_count = 0
    
    def __str__(self):
        """
        String representation of the book
        """
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"'{self.title}' by {self.author} ({self.publication_year}) - {status}"
    
    def borrow(self, member, loan_period_days=14):
        """
        Borrow the book to a member
        """
        if not self.is_available:
            return False, f"Book is already borrowed by {self.borrowed_by}"
        
        self.is_available = False
        self.borrowed_by = member.name
        self.due_date = datetime.now() + timedelta(days=loan_period_days)
        self.borrow_count += 1
        
        return True, f"Book borrowed successfully. Due date: {self.due_date.strftime('%Y-%m-%d')}"
    
    def return_book(self):
        """
        Return the book to the library
        """
        if self.is_available:
            return False, "Book is already available"
        
        borrower = self.borrowed_by
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None
        
        return True, f"Book returned successfully by {borrower}"
    
    def is_overdue(self):
        """
        Check if the book is overdue
        """
        if self.is_available or not self.due_date:
            return False
        return datetime.now() > self.due_date

class Member:
    """
    Represents a library member
    """
    
    def __init__(self, name, member_id, email, phone):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.phone = phone
        self.borrowed_books = []
        self.membership_date = datetime.now()
        self.fine_amount = 0.0
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}) - {len(self.borrowed_books)} books borrowed"
    
    def borrow_book(self, book):
        """
        Attempt to borrow a book
        """
        if len(self.borrowed_books) >= 5:  # Borrow limit
            return False, "Cannot borrow more than 5 books"
        
        success, message = book.borrow(self)
        if success:
            self.borrowed_books.append(book)
        
        return success, message
    
    def return_book(self, book):
        """
        Return a borrowed book
        """
        if book not in self.borrowed_books:
            return False, "You haven't borrowed this book"
        
        # Check for overdue fine
        if book.is_overdue():
            days_overdue = (datetime.now() - book.due_date).days
            fine = days_overdue * 0.50  # $0.50 per day
            self.fine_amount += fine
        
        success, message = book.return_book()
        if success:
            self.borrowed_books.remove(book)
        
        return success, message
    
    def get_overdue_books(self):
        """
        Get list of overdue books
        """
        return [book for book in self.borrowed_books if book.is_overdue()]

class Library:
    """
    Main library management system
    """
    
    def __init__(self, name):
        self.name = name
        self.books = {}  # ISBN -> Book object
        self.members = {}  # Member ID -> Member object
        self.total_books_borrowed = 0
    
    def add_book(self, book):
        """
        Add a book to the library collection
        """
        if book.isbn in self.books:
            return False, "Book with this ISBN already exists"
        
        self.books[book.isbn] = book
        return True, f"Book '{book.title}' added successfully"
    
    def register_member(self, member):
        """
        Register a new library member
        """
        if member.member_id in self.members:
            return False, "Member ID already exists"
        
        self.members[member.member_id] = member
        return True, f"Member {member.name} registered successfully"
    
    def search_books(self, query, search_by="title"):
        """
        Search for books by title, author, or category
        """
        results = []
        query = query.lower()
        
        for book in self.books.values():
            if search_by == "title" and query in book.title.lower():
                results.append(book)
            elif search_by == "author" and query in book.author.lower():
                results.append(book)
            elif search_by == "category" and query in book.category.lower():
                results.append(book)
        
        return results
    
    def borrow_book(self, member_id, isbn):
        """
        Process book borrowing
        """
        if member_id not in self.members:
            return False, "Member not found"
        
        if isbn not in self.books:
            return False, "Book not found"
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        success, message = member.borrow_book(book)
        if success:
            self.total_books_borrowed += 1
        
        return success, message
    
    def return_book(self, member_id, isbn):
        """
        Process book return
        """
        if member_id not in self.members:
            return False, "Member not found"
        
        if isbn not in self.books:
            return False, "Book not found"
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        return member.return_book(book)
    
    def get_overdue_books(self):
        """
        Get all overdue books in the system
        """
        overdue_books = []
        for book in self.books.values():
            if not book.is_available and book.is_overdue():
                overdue_books.append(book)
        return overdue_books
    
    def generate_report(self):
        """
        Generate library statistics report
        """
        total_books = len(self.books)
        available_books = sum(1 for book in self.books.values() if book.is_available)
        borrowed_books = total_books - available_books
        total_members = len(self.members)
        overdue_books = len(self.get_overdue_books())
        
        report = f"""
📚 LIBRARY REPORT: {self.name}
{'='*50}
📖 Total Books: {total_books}
✅ Available Books: {available_books}
📋 Currently Borrowed: {borrowed_books}
⏰ Overdue Books: {overdue_books}
👥 Total Members: {total_members}
📊 Total Books Ever Borrowed: {self.total_books_borrowed}

📈 Most Popular Books:
"""
        
        # Get most borrowed books
        popular_books = sorted(self.books.values(), key=lambda b: b.borrow_count, reverse=True)[:5]
        for i, book in enumerate(popular_books, 1):
            report += f"   {i}. {book.title} ({book.borrow_count} times)\n"
        
        return report

# Create and demonstrate the library system
def demo_library_system():
    """
    Demonstrate the complete library management system
    """
    print("📚" * 20)
    print("    LIBRARY MANAGEMENT SYSTEM DEMO")
    print("📚" * 20)
    
    # Create library
    library = Library("City Public Library")
    
    # Add books
    books_to_add = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", "Fiction", 1925),
        Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", "Fiction", 1960),
        Book("1984", "George Orwell", "978-0-452-28423-4", "Dystopian Fiction", 1949),
        Book("Pride and Prejudice", "Jane Austen", "978-0-14-143951-8", "Romance", 1813),
        Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0", "Fiction", 1951),
        Book("Python Programming", "John Smith", "978-1-23456-789-0", "Technology", 2020)
    ]
    
    print("\n📖 Adding books to library...")
    for book in books_to_add:
        success, message = library.add_book(book)
        if success:
            print(f"✅ {message}")
    
    # Register members
    members_to_register = [
        Member("Alice Johnson", "M001", "alice@email.com", "555-0101"),
        Member("Bob Smith", "M002", "bob@email.com", "555-0102"),
        Member("Carol Davis", "M003", "carol@email.com", "555-0103")
    ]
    
    print("\n👥 Registering members...")
    for member in members_to_register:
        success, message = library.register_member(member)
        if success:
            print(f"✅ {message}")
    
    # Demonstrate borrowing
    print("\n📋 Borrowing books...")
    
    # Alice borrows some books
    success, message = library.borrow_book("M001", "978-0-7432-7356-5")
    print(f"Alice borrowing Gatsby: {message}")
    
    success, message = library.borrow_book("M001", "978-0-452-28423-4")
    print(f"Alice borrowing 1984: {message}")
    
    # Bob borrows a book
    success, message = library.borrow_book("M002", "978-0-06-112008-4")
    print(f"Bob borrowing Mockingbird: {message}")
    
    # Try to borrow unavailable book
    success, message = library.borrow_book("M003", "978-0-7432-7356-5")
    print(f"Carol trying to borrow Gatsby: {message}")
    
    # Search functionality
    print("\n🔍 Searching books...")
    fiction_books = library.search_books("fiction", "category")
    print(f"Fiction books found: {len(fiction_books)}")
    for book in fiction_books:
        print(f"   - {book}")
    
    # Generate report
    print(library.generate_report())
    
    # Demonstrate return
    print("\n🔄 Returning books...")
    alice = library.members["M001"]
    if alice.borrowed_books:
        book_to_return = alice.borrowed_books[0]
        success, message = library.return_book("M001", book_to_return.isbn)
        print(f"Alice returning book: {message}")
    
    # Final report
    print(library.generate_report())

# Run the demonstration
demo_library_system()
```

## 🏃‍♂️ Practice Exercises

### Exercise 1: Student Grade Management
```python
class Student:
    """
    Create a Student class with grade management capabilities
    """
    # Your implementation here
    pass

class Course:
    """
    Create a Course class that manages students and grades
    """
    # Your implementation here
    pass
```

### Exercise 2: E-commerce System
```python
class Product:
    """
    Create a Product class for an online store
    """
    # Your implementation here
    pass

class ShoppingCart:
    """
    Create a ShoppingCart class that manages products
    """
    # Your implementation here
    pass
```

### Exercise 3: Vehicle Management
```python
class Vehicle:
    """
    Base class for all vehicles
    """
    # Your implementation here
    pass

class Car(Vehicle):
    """
    Car class inheriting from Vehicle
    """
    # Your implementation here
    pass
```

## 📝 Key Takeaways

1. **Classes are blueprints** - They define the structure and behavior of objects
2. **Objects are instances** - Specific examples created from class blueprints
3. **Encapsulation protects data** - Use private attributes and public methods
4. **Inheritance enables reuse** - Build new classes based on existing ones
5. **Polymorphism provides flexibility** - Same interface, different implementations
6. **`self` refers to the instance** - Essential for accessing object attributes
7. **OOP organizes complex code** - Makes large programs manageable

## 🎯 Today's Project Preview

Today you built a **Comprehensive Library Management System** that demonstrates professional OOP design. It includes:
- Multiple interacting classes (Book, Member, Library)
- Encapsulation with private data and public interfaces
- Inheritance principles and method overriding
- Polymorphic behavior across different object types
- Real-world business logic and error handling
- Professional system design patterns

## 🔗 Connection to Previous Days

### Building on Previous Skills
- **Functions (Day 15-16)**: Methods are functions within classes
- **Data Structures (Week 2)**: Classes organize data more effectively
- **File Handling (Day 19)**: Could add persistence to library system
- **Error Handling (Day 20)**: Robust object methods with exception handling

### Looking Forward
OOP skills will enhance:
- **GUI Programming (Day 28)**: Classes are essential for GUI components
- **Final Projects**: Professional software architecture and design

Object-Oriented Programming is the foundation of modern software development. Master these concepts, and you'll be able to build complex, maintainable, and professional applications!