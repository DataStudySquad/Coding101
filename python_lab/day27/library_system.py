#!/usr/bin/env python3
"""
Day 27: Comprehensive Library Management System
A complete Object-Oriented Programming demonstration

This program showcases:
- Class design and object creation
- Encapsulation with private attributes and public methods
- Inheritance and polymorphism
- Complex object relationships and interactions
- Professional software architecture patterns
- Real-world business logic implementation

Think of this as a complete software system built with OOP principles!
"""

from datetime import datetime, timedelta
import json
from pathlib import Path
import random


class Person:
    """
    Base class for all people in the system
    Demonstrates inheritance foundation
    """
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.created_date = datetime.now()
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def contact_info(self):
        """
        Get formatted contact information
        """
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}"


class Book:
    """
    Represents a book in the library system
    Demonstrates encapsulation and data modeling
    """
    
    def __init__(self, title, author, isbn, category, publication_year, copies=1):
        # Public attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.publication_year = publication_year
        
        # Private attributes (encapsulation)
        self._total_copies = copies
        self._available_copies = copies
        self._borrow_history = []
        self._total_borrows = 0
        
        # Metadata
        self.added_date = datetime.now()
        self.last_borrowed = None
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year})"
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"
    
    @property
    def available_copies(self):
        """
        Property to safely access available copies
        """
        return self._available_copies
    
    @property
    def total_copies(self):
        """
        Property to safely access total copies
        """
        return self._total_copies
    
    @property
    def is_available(self):
        """
        Check if any copies are available
        """
        return self._available_copies > 0
    
    def add_copies(self, count):
        """
        Add more copies of the book
        """
        if count > 0:
            self._total_copies += count
            self._available_copies += count
            return True, f"Added {count} copies. Total: {self._total_copies}"
        return False, "Count must be positive"
    
    def borrow_copy(self, member):
        """
        Borrow a copy of this book
        """
        if not self.is_available:
            return False, "No copies available"
        
        self._available_copies -= 1
        self._total_borrows += 1
        self.last_borrowed = datetime.now()
        
        # Record borrow history
        borrow_record = {
            'member_id': member.member_id,
            'member_name': member.name,
            'borrow_date': datetime.now(),
            'due_date': datetime.now() + timedelta(days=14)
        }
        self._borrow_history.append(borrow_record)
        
        return True, f"Book borrowed successfully. Due: {borrow_record['due_date'].strftime('%Y-%m-%d')}"
    
    def return_copy(self):
        """
        Return a copy of this book
        """
        if self._available_copies >= self._total_copies:
            return False, "All copies are already available"
        
        self._available_copies += 1
        return True, "Book returned successfully"
    
    def get_popularity_score(self):
        """
        Calculate popularity based on borrow history
        """
        if not self._borrow_history:
            return 0
        
        # Consider both total borrows and recent activity
        recent_borrows = len([b for b in self._borrow_history 
                            if (datetime.now() - b['borrow_date']).days <= 90])
        
        return self._total_borrows * 0.7 + recent_borrows * 0.3
    
    def get_info(self):
        """
        Get comprehensive book information
        """
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'category': self.category,
            'publication_year': self.publication_year,
            'total_copies': self._total_copies,
            'available_copies': self._available_copies,
            'total_borrows': self._total_borrows,
            'popularity_score': self.get_popularity_score(),
            'added_date': self.added_date.strftime('%Y-%m-%d')
        }


class Member(Person):
    """
    Library member class, inherits from Person
    Demonstrates inheritance and specialized behavior
    """
    
    def __init__(self, name, email, phone, member_type="Standard"):
        super().__init__(name, email, phone)
        
        # Member-specific attributes
        self.member_id = self._generate_member_id()
        self.member_type = member_type  # Standard, Premium, Student
        self.membership_date = datetime.now()
        
        # Borrowing limits based on membership type
        self._borrow_limits = {
            "Standard": 3,
            "Premium": 5,
            "Student": 2,
            "Faculty": 10
        }
        
        # Private tracking attributes
        self._borrowed_books = []
        self._borrow_history = []
        self._fine_amount = 0.0
        self._total_books_borrowed = 0
    
    def _generate_member_id(self):
        """
        Generate unique member ID
        """
        return f"M{datetime.now().strftime('%Y')}{random.randint(1000, 9999)}"
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}, Type: {self.member_type})"
    
    @property
    def borrowed_books(self):
        """
        Safe access to borrowed books list
        """
        return self._borrowed_books.copy()
    
    @property
    def borrow_limit(self):
        """
        Get borrowing limit for this member type
        """
        return self._borrow_limits.get(self.member_type, 3)
    
    @property
    def fine_amount(self):
        """
        Get current fine amount
        """
        return self._fine_amount
    
    def can_borrow(self):
        """
        Check if member can borrow more books
        """
        if len(self._borrowed_books) >= self.borrow_limit:
            return False, f"Borrow limit reached ({self.borrow_limit} books)"
        
        if self._fine_amount > 10.00:
            return False, f"Outstanding fine: ${self._fine_amount:.2f}. Please pay before borrowing."
        
        return True, "Can borrow"
    
    def borrow_book(self, book):
        """
        Attempt to borrow a book
        """
        # Check if can borrow
        can_borrow, reason = self.can_borrow()
        if not can_borrow:
            return False, reason
        
        # Check if book is available
        success, message = book.borrow_copy(self)
        if not success:
            return False, message
        
        # Add to member's borrowed books
        borrow_record = {
            'book': book,
            'borrow_date': datetime.now(),
            'due_date': datetime.now() + timedelta(days=14),
            'returned': False
        }
        
        self._borrowed_books.append(borrow_record)
        self._borrow_history.append(borrow_record.copy())
        self._total_books_borrowed += 1
        
        return True, f"Successfully borrowed '{book.title}'. Due: {borrow_record['due_date'].strftime('%Y-%m-%d')}"
    
    def return_book(self, book):
        """
        Return a borrowed book
        """
        # Find the book in borrowed books
        book_record = None
        for record in self._borrowed_books:
            if record['book'].isbn == book.isbn and not record['returned']:
                book_record = record
                break
        
        if not book_record:
            return False, "You haven't borrowed this book or it's already returned"
        
        # Check for overdue fine
        fine_added = 0
        if datetime.now() > book_record['due_date']:
            days_overdue = (datetime.now() - book_record['due_date']).days
            fine_added = days_overdue * 0.50  # $0.50 per day
            self._fine_amount += fine_added
        
        # Return the book
        success, message = book.return_copy()
        if not success:
            return False, f"Error returning book: {message}"
        
        # Update records
        book_record['returned'] = True
        book_record['return_date'] = datetime.now()
        book_record['fine_added'] = fine_added
        
        self._borrowed_books.remove(book_record)
        
        fine_message = f" Fine added: ${fine_added:.2f}" if fine_added > 0 else ""
        return True, f"Book returned successfully.{fine_message}"
    
    def get_overdue_books(self):
        """
        Get list of overdue books
        """
        overdue = []
        for record in self._borrowed_books:
            if datetime.now() > record['due_date'] and not record['returned']:
                days_overdue = (datetime.now() - record['due_date']).days
                overdue.append({
                    'book': record['book'],
                    'days_overdue': days_overdue,
                    'fine_amount': days_overdue * 0.50
                })
        return overdue
    
    def pay_fine(self, amount):
        """
        Pay outstanding fine
        """
        if amount <= 0:
            return False, "Payment amount must be positive"
        
        if amount > self._fine_amount:
            return False, f"Payment exceeds fine amount (${self._fine_amount:.2f})"
        
        self._fine_amount -= amount
        return True, f"Payment of ${amount:.2f} processed. Remaining fine: ${self._fine_amount:.2f}"
    
    def get_member_stats(self):
        """
        Get comprehensive member statistics
        """
        return {
            'member_id': self.member_id,
            'name': self.name,
            'member_type': self.member_type,
            'membership_date': self.membership_date.strftime('%Y-%m-%d'),
            'total_books_borrowed': self._total_books_borrowed,
            'currently_borrowed': len(self._borrowed_books),
            'borrow_limit': self.borrow_limit,
            'fine_amount': self._fine_amount,
            'overdue_books': len(self.get_overdue_books())
        }


class Librarian(Person):
    """
    Librarian class with administrative privileges
    Demonstrates role-based access and specialized methods
    """
    
    def __init__(self, name, email, phone, employee_id, hire_date=None):
        super().__init__(name, email, phone)
        self.employee_id = employee_id
        self.hire_date = hire_date or datetime.now()
        self.access_level = "Librarian"
    
    def __str__(self):
        return f"Librarian: {self.name} (ID: {self.employee_id})"
    
    def add_book_to_library(self, library, book):
        """
        Add a book to the library (librarian privilege)
        """
        return library.add_book(book, added_by=self.employee_id)
    
    def remove_book_from_library(self, library, isbn, reason=""):
        """
        Remove a book from the library (librarian privilege)
        """
        return library.remove_book(isbn, removed_by=self.employee_id, reason=reason)
    
    def generate_reports(self, library):
        """
        Generate administrative reports
        """
        return library.generate_admin_reports()


class Library:
    """
    Main library management system
    Demonstrates composition and system architecture
    """
    
    def __init__(self, name, address="", phone=""):
        self.name = name
        self.address = address
        self.phone = phone
        self.established_date = datetime.now()
        
        # Collections
        self._books = {}  # ISBN -> Book object
        self._members = {}  # Member ID -> Member object
        self._librarians = {}  # Employee ID -> Librarian object
        
        # System statistics
        self._total_books_added = 0
        self._total_members_registered = 0
        self._total_books_borrowed = 0
        self._total_books_returned = 0
        
        # Transaction log
        self._transaction_log = []
        
        print(f"🏛️ Library system '{name}' initialized successfully!")
    
    def _log_transaction(self, action, details):
        """
        Log system transactions for audit trail
        """
        log_entry = {
            'timestamp': datetime.now(),
            'action': action,
            'details': details
        }
        self._transaction_log.append(log_entry)
    
    def add_book(self, book, added_by="System"):
        """
        Add a book to the library collection
        """
        if book.isbn in self._books:
            return False, f"Book with ISBN {book.isbn} already exists"
        
        self._books[book.isbn] = book
        self._total_books_added += 1
        
        self._log_transaction("ADD_BOOK", {
            'isbn': book.isbn,
            'title': book.title,
            'added_by': added_by
        })
        
        return True, f"Book '{book.title}' added successfully (ISBN: {book.isbn})"
    
    def remove_book(self, isbn, removed_by="System", reason=""):
        """
        Remove a book from the library collection
        """
        if isbn not in self._books:
            return False, "Book not found"
        
        book = self._books[isbn]
        
        # Check if book is currently borrowed
        if book.available_copies < book.total_copies:
            return False, "Cannot remove book that is currently borrowed"
        
        del self._books[isbn]
        
        self._log_transaction("REMOVE_BOOK", {
            'isbn': isbn,
            'title': book.title,
            'removed_by': removed_by,
            'reason': reason
        })
        
        return True, f"Book '{book.title}' removed successfully"
    
    def register_member(self, member):
        """
        Register a new library member
        """
        if member.member_id in self._members:
            return False, f"Member ID {member.member_id} already exists"
        
        self._members[member.member_id] = member
        self._total_members_registered += 1
        
        self._log_transaction("REGISTER_MEMBER", {
            'member_id': member.member_id,
            'name': member.name,
            'member_type': member.member_type
        })
        
        return True, f"Member {member.name} registered successfully (ID: {member.member_id})"
    
    def register_librarian(self, librarian):
        """
        Register a new librarian
        """
        if librarian.employee_id in self._librarians:
            return False, f"Employee ID {librarian.employee_id} already exists"
        
        self._librarians[librarian.employee_id] = librarian
        
        self._log_transaction("REGISTER_LIBRARIAN", {
            'employee_id': librarian.employee_id,
            'name': librarian.name
        })
        
        return True, f"Librarian {librarian.name} registered successfully"
    
    def search_books(self, query, search_type="title", category=None):
        """
        Search for books with multiple criteria
        """
        results = []
        query = query.lower() if query else ""
        
        for book in self._books.values():
            # Category filter
            if category and book.category.lower() != category.lower():
                continue
            
            # Search criteria
            match = False
            if search_type == "title" and query in book.title.lower():
                match = True
            elif search_type == "author" and query in book.author.lower():
                match = True
            elif search_type == "isbn" and query in book.isbn.lower():
                match = True
            elif search_type == "category" and query in book.category.lower():
                match = True
            elif search_type == "all":
                if (query in book.title.lower() or 
                    query in book.author.lower() or 
                    query in book.category.lower()):
                    match = True
            
            if match:
                results.append(book)
        
        return results
    
    def borrow_book(self, member_id, isbn):
        """
        Process book borrowing transaction
        """
        # Validate member
        if member_id not in self._members:
            return False, "Member not found"
        
        # Validate book
        if isbn not in self._books:
            return False, "Book not found"
        
        member = self._members[member_id]
        book = self._books[isbn]
        
        # Process borrowing
        success, message = member.borrow_book(book)
        
        if success:
            self._total_books_borrowed += 1
            self._log_transaction("BORROW_BOOK", {
                'member_id': member_id,
                'isbn': isbn,
                'title': book.title
            })
        
        return success, message
    
    def return_book(self, member_id, isbn):
        """
        Process book return transaction
        """
        if member_id not in self._members:
            return False, "Member not found"
        
        if isbn not in self._books:
            return False, "Book not found"
        
        member = self._members[member_id]
        book = self._books[isbn]
        
        success, message = member.return_book(book)
        
        if success:
            self._total_books_returned += 1
            self._log_transaction("RETURN_BOOK", {
                'member_id': member_id,
                'isbn': isbn,
                'title': book.title
            })
        
        return success, message
    
    def get_popular_books(self, limit=10):
        """
        Get most popular books based on borrowing history
        """
        books_with_scores = [(book, book.get_popularity_score()) 
                            for book in self._books.values()]
        books_with_scores.sort(key=lambda x: x[1], reverse=True)
        
        return [book for book, score in books_with_scores[:limit]]
    
    def get_overdue_books(self):
        """
        Get all overdue books in the system
        """
        overdue_info = []
        
        for member in self._members.values():
            member_overdue = member.get_overdue_books()
            for overdue in member_overdue:
                overdue_info.append({
                    'member': member,
                    'book': overdue['book'],
                    'days_overdue': overdue['days_overdue'],
                    'fine_amount': overdue['fine_amount']
                })
        
        return overdue_info
    
    def generate_system_report(self):
        """
        Generate comprehensive system report
        """
        total_books = len(self._books)
        total_available = sum(book.available_copies for book in self._books.values())
        total_copies = sum(book.total_copies for book in self._books.values())
        currently_borrowed = total_copies - total_available
        
        overdue_books = self.get_overdue_books()
        total_fines = sum(member.fine_amount for member in self._members.values())
        
        popular_books = self.get_popular_books(5)
        
        report = f"""
🏛️ LIBRARY SYSTEM REPORT: {self.name}
{'='*60}
📊 COLLECTION OVERVIEW
   📚 Unique Titles: {total_books:,}
   📖 Total Copies: {total_copies:,}
   ✅ Available Copies: {total_available:,}
   📋 Currently Borrowed: {currently_borrowed:,}

👥 MEMBERSHIP
   🎫 Total Members: {len(self._members):,}
   👨‍🏫 Librarians: {len(self._librarians):,}

📈 ACTIVITY STATISTICS
   📚 Books Ever Borrowed: {self._total_books_borrowed:,}
   🔄 Books Returned: {self._total_books_returned:,}
   ⏰ Currently Overdue: {len(overdue_books):,}
   💰 Total Outstanding Fines: ${total_fines:.2f}

🏆 TOP 5 POPULAR BOOKS:
"""
        
        for i, book in enumerate(popular_books, 1):
            report += f"   {i}. {book.title} by {book.author}\n"
            report += f"      Popularity Score: {book.get_popularity_score():.1f}\n"
        
        # Category breakdown
        categories = {}
        for book in self._books.values():
            categories[book.category] = categories.get(book.category, 0) + 1
        
        report += f"\n📚 COLLECTION BY CATEGORY:\n"
        for category, count in sorted(categories.items()):
            percentage = (count / total_books) * 100
            report += f"   {category}: {count} books ({percentage:.1f}%)\n"
        
        return report
    
    def export_data(self, filename="library_data.json"):
        """
        Export library data to JSON file
        """
        try:
            export_data = {
                'library_info': {
                    'name': self.name,
                    'address': self.address,
                    'phone': self.phone,
                    'established_date': self.established_date.isoformat()
                },
                'books': [book.get_info() for book in self._books.values()],
                'members': [member.get_member_stats() for member in self._members.values()],
                'statistics': {
                    'total_books_added': self._total_books_added,
                    'total_members_registered': self._total_members_registered,
                    'total_books_borrowed': self._total_books_borrowed,
                    'total_books_returned': self._total_books_returned
                },
                'export_date': datetime.now().isoformat()
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            return True, f"Library data exported to {filename}"
            
        except Exception as e:
            return False, f"Export failed: {str(e)}"


def create_sample_library():
    """
    Create a sample library with books and members for demonstration
    """
    print("📚 Creating sample library system...")
    
    # Create library
    library = Library("Central City Library", "123 Main St", "555-LIBRARY")
    
    # Create librarian
    librarian = Librarian("Sarah Wilson", "sarah@library.com", "555-0100", "EMP001")
    library.register_librarian(librarian)
    
    # Add sample books
    sample_books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", "Fiction", 1925, 3),
        Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", "Fiction", 1960, 2),
        Book("1984", "George Orwell", "978-0-452-28423-4", "Dystopian Fiction", 1949, 4),
        Book("Pride and Prejudice", "Jane Austen", "978-0-14-143951-8", "Romance", 1813, 2),
        Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0", "Fiction", 1951, 2),
        Book("Python Programming", "John Smith", "978-1-23456-789-0", "Technology", 2020, 5),
        Book("Data Science Handbook", "Jake VanderPlas", "978-1-49191-205-8", "Technology", 2016, 3),
        Book("The Art of War", "Sun Tzu", "978-0-486-42557-1", "Philosophy", -500, 1),
        Book("Sapiens", "Yuval Noah Harari", "978-0-06-231609-7", "History", 2011, 4),
        Book("Atomic Habits", "James Clear", "978-0-73521-129-2", "Self-Help", 2018, 3)
    ]
    
    print("📖 Adding books to library...")
    for book in sample_books:
        success, message = library.add_book(book)
        if success:
            print(f"   ✅ {book.title}")
    
    # Register sample members
    sample_members = [
        Member("Alice Johnson", "alice@email.com", "555-0101", "Premium"),
        Member("Bob Smith", "bob@email.com", "555-0102", "Standard"),
        Member("Carol Davis", "carol@email.com", "555-0103", "Student"),
        Member("David Wilson", "david@email.com", "555-0104", "Faculty"),
        Member("Emily Brown", "emily@email.com", "555-0105", "Standard")
    ]
    
    print("\n👥 Registering members...")
    for member in sample_members:
        success, message = library.register_member(member)
        if success:
            print(f"   ✅ {member.name} ({member.member_type})")
    
    return library, librarian


def main():
    """
    Main function demonstrating the library management system
    """
    print("🏛️" * 20)
    print("    COMPREHENSIVE LIBRARY MANAGEMENT SYSTEM")
    print("🏛️" * 20)
    print("Object-Oriented Programming Demonstration")
    print()
    
    # Create sample library
    library, librarian = create_sample_library()
    
    while True:
        print("\n" + "=" * 60)
        print("📚 LIBRARY MANAGEMENT SYSTEM MENU")
        print("=" * 60)
        print("1. Search books")
        print("2. Borrow book")
        print("3. Return book") 
        print("4. View member information")
        print("5. View book information")
        print("6. Popular books report")
        print("7. Overdue books report")
        print("8. Complete system report")
        print("9. Add new book (Librarian)")
        print("10. Register new member")
        print("11. Export library data")
        print("12. Demo automated transactions")
        print("13. Exit")
        
        try:
            choice = input("\nSelect option (1-13): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Thank you for using the Library Management System!")
            print("📚 Remember: Knowledge is the only treasure that increases when shared!")
            break
        
        if choice == "1":
            # Search books
            print("\n🔍 Book Search")
            query = input("Enter search term: ").strip()
            search_type = input("Search by (title/author/category/all): ").strip().lower()
            if search_type not in ['title', 'author', 'category', 'all']:
                search_type = 'title'
            
            results = library.search_books(query, search_type)
            
            if results:
                print(f"\n📚 Found {len(results)} books:")
                for book in results:
                    availability = f"({book.available_copies}/{book.total_copies} available)"
                    print(f"   • {book} - {book.category} {availability}")
            else:
                print("❌ No books found matching your search")
        
        elif choice == "2":
            # Borrow book
            print("\n📋 Borrow Book")
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            
            success, message = library.borrow_book(member_id, isbn)
            if success:
                print(f"✅ {message}")
            else:
                print(f"❌ {message}")
        
        elif choice == "3":
            # Return book
            print("\n🔄 Return Book")
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            
            success, message = library.return_book(member_id, isbn)
            if success:
                print(f"✅ {message}")
            else:
                print(f"❌ {message}")
        
        elif choice == "4":
            # View member information
            print("\n👤 Member Information")
            member_id = input("Enter member ID (or 'all' for all members): ").strip()
            
            if member_id.lower() == 'all':
                print(f"\n👥 All Members ({len(library._members)}):")
                for member in library._members.values():
                    stats = member.get_member_stats()
                    print(f"   • {member.name} (ID: {member.member_id})")
                    print(f"     Type: {stats['member_type']}, Borrowed: {stats['currently_borrowed']}")
                    if stats['fine_amount'] > 0:
                        print(f"     Fine: ${stats['fine_amount']:.2f}")
            elif member_id in library._members:
                member = library._members[member_id]
                stats = member.get_member_stats()
                
                print(f"\n📋 Member Details:")
                print(f"   Name: {stats['name']}")
                print(f"   ID: {stats['member_id']}")
                print(f"   Type: {stats['member_type']}")
                print(f"   Member since: {stats['membership_date']}")
                print(f"   Books borrowed (lifetime): {stats['total_books_borrowed']}")
                print(f"   Currently borrowed: {stats['currently_borrowed']}/{member.borrow_limit}")
                print(f"   Fine amount: ${stats['fine_amount']:.2f}")
                print(f"   Overdue books: {stats['overdue_books']}")
                
                if member.borrowed_books:
                    print(f"\n📚 Currently Borrowed Books:")
                    for record in member.borrowed_books:
                        book = record['book']
                        due_date = record['due_date'].strftime('%Y-%m-%d')
                        status = "⏰ OVERDUE" if datetime.now() > record['due_date'] else "✅ On time"
                        print(f"   • {book.title} - Due: {due_date} {status}")
            else:
                print("❌ Member not found")
        
        elif choice == "5":
            # View book information
            print("\n📖 Book Information")
            isbn = input("Enter book ISBN: ").strip()
            
            if isbn in library._books:
                book = library._books[isbn]
                info = book.get_info()
                
                print(f"\n📚 Book Details:")
                print(f"   Title: {info['title']}")
                print(f"   Author: {info['author']}")
                print(f"   ISBN: {info['isbn']}")
                print(f"   Category: {info['category']}")
                print(f"   Published: {info['publication_year']}")
                print(f"   Copies: {info['available_copies']}/{info['total_copies']} available")
                print(f"   Times borrowed: {info['total_borrows']}")
                print(f"   Popularity score: {info['popularity_score']:.1f}")
                print(f"   Added to library: {info['added_date']}")
            else:
                print("❌ Book not found")
        
        elif choice == "6":
            # Popular books report
            print("\n🏆 Popular Books Report")
            popular_books = library.get_popular_books(10)
            
            if popular_books:
                print(f"\n📈 Top {len(popular_books)} Most Popular Books:")
                for i, book in enumerate(popular_books, 1):
                    score = book.get_popularity_score()
                    print(f"   {i}. {book.title} by {book.author}")
                    print(f"      Popularity Score: {score:.1f}")
                    print(f"      Available: {book.available_copies}/{book.total_copies}")
            else:
                print("❌ No borrowing data available")
        
        elif choice == "7":
            # Overdue books report
            print("\n⏰ Overdue Books Report")
            overdue_books = library.get_overdue_books()
            
            if overdue_books:
                print(f"\n📋 {len(overdue_books)} Overdue Books:")
                total_fines = 0
                for overdue in overdue_books:
                    member = overdue['member']
                    book = overdue['book']
                    days = overdue['days_overdue']
                    fine = overdue['fine_amount']
                    total_fines += fine
                    
                    print(f"   • '{book.title}' borrowed by {member.name}")
                    print(f"     {days} days overdue, Fine: ${fine:.2f}")
                
                print(f"\n💰 Total outstanding fines: ${total_fines:.2f}")
            else:
                print("✅ No overdue books!")
        
        elif choice == "8":
            # Complete system report
            print("\n📊 Generating comprehensive system report...")
            report = library.generate_system_report()
            print(report)
        
        elif choice == "9":
            # Add new book (librarian function)
            print("\n📚 Add New Book (Librarian Access)")
            
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN: ").strip()
            category = input("Category: ").strip()
            
            try:
                year = int(input("Publication year: ").strip())
                copies = int(input("Number of copies: ").strip() or "1")
            except ValueError:
                print("❌ Invalid year or copies number")
                continue
            
            new_book = Book(title, author, isbn, category, year, copies)
            success, message = librarian.add_book_to_library(library, new_book)
            
            if success:
                print(f"✅ {message}")
            else:
                print(f"❌ {message}")
        
        elif choice == "10":
            # Register new member
            print("\n👥 Register New Member")
            
            name = input("Full name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()
            member_type = input("Member type (Standard/Premium/Student/Faculty): ").strip()
            
            if member_type not in ["Standard", "Premium", "Student", "Faculty"]:
                member_type = "Standard"
            
            new_member = Member(name, email, phone, member_type)
            success, message = library.register_member(new_member)
            
            if success:
                print(f"✅ {message}")
            else:
                print(f"❌ {message}")
        
        elif choice == "11":
            # Export library data
            print("\n💾 Export Library Data")
            filename = input("Enter filename (default: library_data.json): ").strip()
            if not filename:
                filename = "library_data.json"
            
            success, message = library.export_data(filename)
            if success:
                print(f"✅ {message}")
            else:
                print(f"❌ {message}")
        
        elif choice == "12":
            # Demo automated transactions
            print("\n🤖 Running Automated Demo Transactions...")
            
            # Get some members and books for demo
            member_ids = list(library._members.keys())[:3]
            book_isbns = list(library._books.keys())[:5]
            
            print(f"📋 Simulating borrowing transactions...")
            for i, member_id in enumerate(member_ids):
                for j in range(min(2, len(book_isbns))):  # Each member borrows 2 books
                    isbn = book_isbns[(i * 2 + j) % len(book_isbns)]
                    success, message = library.borrow_book(member_id, isbn)
                    member_name = library._members[member_id].name
                    book_title = library._books[isbn].title
                    status = "✅" if success else "❌"
                    print(f"   {status} {member_name} borrowing '{book_title}'")
            
            print(f"\n📊 System status after demo transactions:")
            print(f"   📚 Total books borrowed: {library._total_books_borrowed}")
            print(f"   👥 Active borrowers: {sum(1 for m in library._members.values() if m.borrowed_books)}")
            
            # Show some member statuses
            print(f"\n👤 Member Status Examples:")
            for member_id in member_ids:
                member = library._members[member_id]
                stats = member.get_member_stats()
                print(f"   • {member.name}: {stats['currently_borrowed']} books borrowed")
        
        elif choice == "13":
            print("\n📚 Thank you for using the Library Management System!")
            print("\n🎯 OOP Concepts Demonstrated:")
            print("   • Classes and Objects: Book, Member, Library, Librarian")
            print("   • Encapsulation: Private attributes with public interfaces")
            print("   • Inheritance: Member and Librarian inherit from Person")
            print("   • Polymorphism: Different behaviors for different object types")
            print("   • Composition: Library contains Books and Members")
            print("\n💡 This system showcases professional software architecture!")
            break
        
        else:
            print("❌ Invalid option. Please select 1-13.")


if __name__ == "__main__":
    main()