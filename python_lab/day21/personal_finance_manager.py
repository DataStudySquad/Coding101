#!/usr/bin/env python3
"""
Day 21: Personal Finance Manager
A comprehensive financial management application bringing together all Week 3 concepts

This application demonstrates:
- Functions for code organization and reusability (Day 15-16)
- Built-in functions for data processing and analysis (Day 17)
- Module integration for extended functionality (Day 18)
- File handling for data persistence (Day 19)
- Error handling for robust operation (Day 20)

Features:
- Transaction management (add, edit, delete, search)
- Budget tracking and analysis
- Financial reporting and insights
- Data persistence with automatic backups
- Comprehensive error handling
- User-friendly interface

This is your capstone project for Week 3!
"""

import json
import csv
import datetime
import os
from pathlib import Path
import shutil
import math
from typing import Dict, List, Any, Optional


class PersonalFinanceManager:
    """
    A comprehensive personal finance management system
    
    Think of this as your digital financial assistant that:
    - Tracks all your income and expenses
    - Helps you stick to budgets
    - Provides insights into your spending patterns
    - Keeps your financial data safe and organized
    """
    
    def __init__(self, data_dir="finance_data"):
        """
        Initialize the Finance Manager with error handling
        """
        self.data_dir = Path(data_dir)
        self.transactions_file = self.data_dir / "transactions.json"
        self.budgets_file = self.data_dir / "budgets.json"
        self.config_file = self.data_dir / "config.json"
        self.backup_dir = self.data_dir / "backups"
        
        # Ensure all directories exist
        self.ensure_directories()
        
        # Load data with error handling
        self.transactions = self.load_transactions()
        self.budgets = self.load_budgets()
        self.config = self.load_config()
        
        # Default categories for new users
        self.default_categories = [
            "Food & Dining", "Transportation", "Shopping", "Entertainment",
            "Bills & Utilities", "Healthcare", "Education", "Travel",
            "Groceries", "Gas", "Income", "Investment", "Other"
        ]
        
        print("Personal Finance Manager initialized successfully!")
        print(f"Data directory: {self.data_dir.absolute()}")
    
    def ensure_directories(self):
        """
        Create necessary directories with error handling
        """
        try:
            self.data_dir.mkdir(parents=True, exist_ok=True)
            self.backup_dir.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            raise PermissionError(f"No permission to create directories in {self.data_dir}")
        except Exception as e:
            raise RuntimeError(f"Could not create directories: {e}")
    
    def load_transactions(self):
        """
        Load transaction data with error handling and backup recovery
        """
        try:
            if self.transactions_file.exists():
                with open(self.transactions_file, 'r', encoding='utf-8') as f:
                    transactions = json.load(f)
                    # Validate transaction data structure
                    if isinstance(transactions, list):
                        return transactions
                    else:
                        raise ValueError("Invalid transaction data format")
            else:
                return []
                
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Transaction data corrupted: {e}")
            return self.attempt_backup_recovery("transactions")
        except Exception as e:
            print(f"Error loading transactions: {e}")
            return []
    
    def load_budgets(self):
        """
        Load budget data with error handling
        """
        try:
            if self.budgets_file.exists():
                with open(self.budgets_file, 'r', encoding='utf-8') as f:
                    budgets = json.load(f)
                    return budgets if isinstance(budgets, dict) else {}
            else:
                return {}
                
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Budget data corrupted: {e}")
            return self.attempt_backup_recovery("budgets")
        except Exception as e:
            print(f"Error loading budgets: {e}")
            return {}
    
    def load_config(self):
        """
        Load configuration with defaults
        """
        default_config = {
            "currency": "$",
            "date_format": "%Y-%m-%d",
            "auto_backup": True,
            "backup_frequency": 7,  # days
            "default_category": "Other"
        }
        
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    return {**default_config, **config}
            else:
                self.save_config(default_config)
                return default_config
                
        except Exception as e:
            print(f"Error loading config, using defaults: {e}")
            return default_config
    
    def attempt_backup_recovery(self, data_type):
        """
        Attempt to recover data from backup files
        """
        try:
            backup_pattern = f"{data_type}_backup_*.json"
            backup_files = list(self.backup_dir.glob(backup_pattern))
            
            if backup_files:
                # Get the most recent backup
                latest_backup = max(backup_files, key=lambda x: x.stat().st_mtime)
                print(f"Attempting recovery from backup: {latest_backup.name}")
                
                with open(latest_backup, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print("Successfully recovered from backup!")
                    return data
            else:
                print("No backup files found for recovery")
                return [] if data_type == "transactions" else {}
                
        except Exception as e:
            print(f"Backup recovery failed: {e}")
            return [] if data_type == "transactions" else {}
    
    def save_data(self):
        """
        Save all data with automatic backup
        """
        try:
            # Create backups if auto_backup is enabled
            if self.config.get("auto_backup", True):
                self.create_backups()
            
            # Save transactions
            with open(self.transactions_file, 'w', encoding='utf-8') as f:
                json.dump(self.transactions, f, indent=2, default=str)
            
            # Save budgets
            with open(self.budgets_file, 'w', encoding='utf-8') as f:
                json.dump(self.budgets, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def save_config(self, config=None):
        """
        Save configuration
        """
        try:
            config_to_save = config if config else self.config
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config_to_save, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def create_backups(self):
        """
        Create timestamped backup copies of data files
        """
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Backup transactions
            if self.transactions_file.exists():
                backup_name = f"transactions_backup_{timestamp}.json"
                backup_path = self.backup_dir / backup_name
                shutil.copy2(self.transactions_file, backup_path)
            
            # Backup budgets
            if self.budgets_file.exists():
                backup_name = f"budgets_backup_{timestamp}.json"
                backup_path = self.backup_dir / backup_name
                shutil.copy2(self.budgets_file, backup_path)
            
            # Clean old backups (keep last 10)
            self.cleanup_old_backups()
            
        except Exception as e:
            print(f"Warning: Could not create backups: {e}")
    
    def cleanup_old_backups(self, keep_count=10):
        """
        Remove old backup files, keeping only the most recent ones
        """
        try:
            for pattern in ["transactions_backup_*.json", "budgets_backup_*.json"]:
                backup_files = sorted(
                    self.backup_dir.glob(pattern),
                    key=lambda x: x.stat().st_mtime,
                    reverse=True
                )
                
                # Remove old backups beyond keep_count
                for old_backup in backup_files[keep_count:]:
                    old_backup.unlink()
                    
        except Exception as e:
            print(f"Warning: Could not cleanup old backups: {e}")
    
    # Transaction Management Functions (Day 15-16: Functions)
    
    def add_transaction(self, amount, description, category, transaction_type="expense", date=None):
        """
        Add a new transaction with validation
        
        Args:
            amount (float): Transaction amount (positive number)
            description (str): Transaction description
            category (str): Transaction category
            transaction_type (str): 'income' or 'expense'
            date (str, optional): Transaction date (YYYY-MM-DD format)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Validate inputs
            if not isinstance(amount, (int, float)) or amount <= 0:
                raise ValueError("Amount must be a positive number")
            
            if not description or not description.strip():
                raise ValueError("Description cannot be empty")
            
            if transaction_type not in ["income", "expense"]:
                raise ValueError("Transaction type must be 'income' or 'expense'")
            
            # Use current date if none provided
            if date is None:
                date = datetime.date.today().strftime(self.config["date_format"])
            else:
                # Validate date format
                datetime.datetime.strptime(date, self.config["date_format"])
            
            # Create transaction record
            transaction = {
                "id": self.generate_transaction_id(),
                "date": date,
                "amount": round(float(amount), 2),
                "description": description.strip(),
                "category": category.strip(),
                "type": transaction_type,
                "created_at": datetime.datetime.now().isoformat()
            }
            
            # Add to transactions list
            self.transactions.append(transaction)
            
            # Save data
            if self.save_data():
                print(f"✓ {transaction_type.capitalize()} added: {self.config['currency']}{amount} - {description}")
                return True
            else:
                # Remove from list if save failed
                self.transactions.pop()
                print("✗ Failed to save transaction")
                return False
                
        except ValueError as e:
            print(f"Input Error: {e}")
            return False
        except Exception as e:
            print(f"Error adding transaction: {e}")
            return False
    
    def generate_transaction_id(self):
        """
        Generate a unique transaction ID
        """
        if not self.transactions:
            return 1
        return max(t["id"] for t in self.transactions) + 1
    
    def edit_transaction(self, transaction_id, **updates):
        """
        Edit an existing transaction
        
        Args:
            transaction_id (int): ID of transaction to edit
            **updates: Fields to update (amount, description, category, type, date)
        """
        try:
            # Find transaction
            transaction = self.find_transaction_by_id(transaction_id)
            if not transaction:
                print(f"Transaction with ID {transaction_id} not found")
                return False
            
            # Validate and apply updates
            if 'amount' in updates:
                amount = updates['amount']
                if not isinstance(amount, (int, float)) or amount <= 0:
                    raise ValueError("Amount must be a positive number")
                transaction['amount'] = round(float(amount), 2)
            
            if 'description' in updates:
                desc = updates['description']
                if not desc or not desc.strip():
                    raise ValueError("Description cannot be empty")
                transaction['description'] = desc.strip()
            
            if 'category' in updates:
                transaction['category'] = updates['category'].strip()
            
            if 'type' in updates:
                if updates['type'] not in ["income", "expense"]:
                    raise ValueError("Transaction type must be 'income' or 'expense'")
                transaction['type'] = updates['type']
            
            if 'date' in updates:
                # Validate date format
                datetime.datetime.strptime(updates['date'], self.config["date_format"])
                transaction['date'] = updates['date']
            
            # Add modification timestamp
            transaction['modified_at'] = datetime.datetime.now().isoformat()
            
            # Save data
            if self.save_data():
                print(f"✓ Transaction {transaction_id} updated successfully")
                return True
            else:
                print("✗ Failed to save transaction changes")
                return False
                
        except ValueError as e:
            print(f"Input Error: {e}")
            return False
        except Exception as e:
            print(f"Error editing transaction: {e}")
            return False
    
    def delete_transaction(self, transaction_id):
        """
        Delete a transaction by ID
        """
        try:
            # Find transaction
            transaction = self.find_transaction_by_id(transaction_id)
            if not transaction:
                print(f"Transaction with ID {transaction_id} not found")
                return False
            
            # Show transaction details and confirm
            print(f"\nTransaction to delete:")
            self.display_transaction(transaction)
            
            confirmation = input("\nAre you sure you want to delete this transaction? (y/n): ").strip().lower()
            if confirmation not in ['y', 'yes']:
                print("Delete cancelled")
                return False
            
            # Remove transaction
            self.transactions = [t for t in self.transactions if t["id"] != transaction_id]
            
            # Save data
            if self.save_data():
                print(f"✓ Transaction {transaction_id} deleted successfully")
                return True
            else:
                print("✗ Failed to save after deletion")
                return False
                
        except Exception as e:
            print(f"Error deleting transaction: {e}")
            return False
    
    def find_transaction_by_id(self, transaction_id):
        """
        Find a transaction by its ID
        """
        for transaction in self.transactions:
            if transaction["id"] == transaction_id:
                return transaction
        return None
    
    # Data Analysis Functions (Day 17: Built-in Functions)
    
    def get_spending_by_category(self, start_date=None, end_date=None):
        """
        Calculate total spending by category using built-in functions
        """
        try:
            # Filter transactions by date range if specified
            filtered_transactions = self.filter_transactions_by_date(start_date, end_date)
            
            # Filter only expenses
            expenses = [t for t in filtered_transactions if t["type"] == "expense"]
            
            if not expenses:
                return {}
            
            # Group by category using dictionary comprehension and sum()
            categories = set(t["category"] for t in expenses)
            spending_by_category = {
                category: sum(t["amount"] for t in expenses if t["category"] == category)
                for category in categories
            }
            
            return spending_by_category
            
        except Exception as e:
            print(f"Error calculating spending by category: {e}")
            return {}
    
    def get_monthly_summary(self, year=None, month=None):
        """
        Generate monthly financial summary using built-in functions
        """
        try:
            # Use current month/year if not specified
            if year is None or month is None:
                today = datetime.date.today()
                year = year or today.year
                month = month or today.month
            
            # Filter transactions for the specified month
            month_transactions = [
                t for t in self.transactions
                if datetime.datetime.strptime(t["date"], self.config["date_format"]).year == year
                and datetime.datetime.strptime(t["date"], self.config["date_format"]).month == month
            ]
            
            if not month_transactions:
                return {
                    "period": f"{year}-{month:02d}",
                    "total_income": 0,
                    "total_expenses": 0,
                    "net_income": 0,
                    "transaction_count": 0,
                    "top_expense_category": None,
                    "average_transaction": 0
                }
            
            # Calculate summary statistics using built-in functions
            incomes = [t["amount"] for t in month_transactions if t["type"] == "income"]
            expenses = [t["amount"] for t in month_transactions if t["type"] == "expense"]
            
            total_income = sum(incomes)
            total_expenses = sum(expenses)
            net_income = total_income - total_expenses
            
            # Find top expense category
            expense_by_category = {}
            for t in month_transactions:
                if t["type"] == "expense":
                    category = t["category"]
                    expense_by_category[category] = expense_by_category.get(category, 0) + t["amount"]
            
            top_category = max(expense_by_category.keys(), key=expense_by_category.get) if expense_by_category else None
            
            # Calculate average transaction amount
            all_amounts = [abs(t["amount"]) for t in month_transactions]
            average_transaction = sum(all_amounts) / len(all_amounts) if all_amounts else 0
            
            return {
                "period": f"{year}-{month:02d}",
                "total_income": round(total_income, 2),
                "total_expenses": round(total_expenses, 2),
                "net_income": round(net_income, 2),
                "transaction_count": len(month_transactions),
                "top_expense_category": top_category,
                "top_category_amount": round(expense_by_category.get(top_category, 0), 2) if top_category else 0,
                "average_transaction": round(average_transaction, 2)
            }
            
        except Exception as e:
            print(f"Error generating monthly summary: {e}")
            return {}
    
    def filter_transactions_by_date(self, start_date=None, end_date=None):
        """
        Filter transactions by date range
        """
        try:
            if start_date is None and end_date is None:
                return self.transactions
            
            filtered = []
            for transaction in self.transactions:
                transaction_date = datetime.datetime.strptime(
                    transaction["date"], 
                    self.config["date_format"]
                ).date()
                
                # Check date range
                if start_date and transaction_date < start_date:
                    continue
                if end_date and transaction_date > end_date:
                    continue
                
                filtered.append(transaction)
            
            return filtered
            
        except Exception as e:
            print(f"Error filtering transactions by date: {e}")
            return self.transactions
    
    # Budget Management Functions
    
    def set_budget(self, category, monthly_amount):
        """
        Set a monthly budget for a category
        """
        try:
            if not isinstance(monthly_amount, (int, float)) or monthly_amount <= 0:
                raise ValueError("Budget amount must be a positive number")
            
            self.budgets[category] = {
                "amount": round(float(monthly_amount), 2),
                "created_date": datetime.date.today().isoformat(),
                "last_modified": datetime.datetime.now().isoformat()
            }
            
            if self.save_data():
                print(f"✓ Budget set for {category}: {self.config['currency']}{monthly_amount}/month")
                return True
            else:
                print("✗ Failed to save budget")
                return False
                
        except ValueError as e:
            print(f"Input Error: {e}")
            return False
        except Exception as e:
            print(f"Error setting budget: {e}")
            return False
    
    def get_budget_analysis(self, year=None, month=None):
        """
        Analyze budget performance for a given month
        """
        try:
            # Get monthly spending by category
            if year is None or month is None:
                today = datetime.date.today()
                year = year or today.year
                month = month or today.month
            
            # Filter transactions for the month
            month_start = datetime.date(year, month, 1)
            if month == 12:
                month_end = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
            else:
                month_end = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
            
            monthly_spending = self.get_spending_by_category(month_start, month_end)
            
            # Compare with budgets
            budget_analysis = {}
            for category, budget_info in self.budgets.items():
                spent = monthly_spending.get(category, 0)
                budget_amount = budget_info["amount"]
                
                budget_analysis[category] = {
                    "budget": budget_amount,
                    "spent": spent,
                    "remaining": budget_amount - spent,
                    "percentage_used": (spent / budget_amount * 100) if budget_amount > 0 else 0,
                    "status": "over" if spent > budget_amount else "under"
                }
            
            # Include categories with spending but no budget
            for category, spent in monthly_spending.items():
                if category not in budget_analysis:
                    budget_analysis[category] = {
                        "budget": 0,
                        "spent": spent,
                        "remaining": -spent,
                        "percentage_used": float('inf'),
                        "status": "no_budget"
                    }
            
            return budget_analysis
            
        except Exception as e:
            print(f"Error analyzing budgets: {e}")
            return {}
    
    # Data Export Functions (Day 18: Modules)
    
    def export_to_csv(self, filename=None, start_date=None, end_date=None):
        """
        Export transactions to CSV file
        """
        try:
            if filename is None:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"transactions_export_{timestamp}.csv"
            
            # Get filtered transactions
            transactions_to_export = self.filter_transactions_by_date(start_date, end_date)
            
            if not transactions_to_export:
                print("No transactions to export")
                return False
            
            # Write CSV file
            export_path = self.data_dir / filename
            with open(export_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'date', 'type', 'category', 'description', 'amount']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for transaction in transactions_to_export:
                    writer.writerow({
                        'id': transaction['id'],
                        'date': transaction['date'],
                        'type': transaction['type'],
                        'category': transaction['category'],
                        'description': transaction['description'],
                        'amount': transaction['amount']
                    })
            
            print(f"✓ Exported {len(transactions_to_export)} transactions to {filename}")
            return True
            
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def export_summary_report(self, filename=None):
        """
        Export a comprehensive financial summary report
        """
        try:
            if filename is None:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"financial_summary_{timestamp}.txt"
            
            export_path = self.data_dir / filename
            
            with open(export_path, 'w', encoding='utf-8') as f:
                # Header
                f.write("PERSONAL FINANCE SUMMARY REPORT\n")
                f.write("="*50 + "\n")
                f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # Overall statistics
                f.write("OVERALL STATISTICS\n")
                f.write("-"*30 + "\n")
                f.write(f"Total transactions: {len(self.transactions)}\n")
                
                if self.transactions:
                    total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
                    total_expenses = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
                    f.write(f"Total income: {self.config['currency']}{total_income:.2f}\n")
                    f.write(f"Total expenses: {self.config['currency']}{total_expenses:.2f}\n")
                    f.write(f"Net income: {self.config['currency']}{total_income - total_expenses:.2f}\n\n")
                
                # Monthly summary for current month
                current_summary = self.get_monthly_summary()
                if current_summary:
                    f.write(f"CURRENT MONTH SUMMARY ({current_summary['period']})\n")
                    f.write("-"*30 + "\n")
                    f.write(f"Income: {self.config['currency']}{current_summary['total_income']:.2f}\n")
                    f.write(f"Expenses: {self.config['currency']}{current_summary['total_expenses']:.2f}\n")
                    f.write(f"Net: {self.config['currency']}{current_summary['net_income']:.2f}\n")
                    f.write(f"Transactions: {current_summary['transaction_count']}\n")
                    if current_summary['top_expense_category']:
                        f.write(f"Top expense category: {current_summary['top_expense_category']} "
                               f"({self.config['currency']}{current_summary['top_category_amount']:.2f})\n")
                    f.write("\n")
                
                # Budget analysis
                budget_analysis = self.get_budget_analysis()
                if budget_analysis:
                    f.write("BUDGET ANALYSIS (Current Month)\n")
                    f.write("-"*30 + "\n")
                    for category, analysis in budget_analysis.items():
                        if analysis['status'] != 'no_budget':
                            f.write(f"{category}:\n")
                            f.write(f"  Budget: {self.config['currency']}{analysis['budget']:.2f}\n")
                            f.write(f"  Spent: {self.config['currency']}{analysis['spent']:.2f}\n")
                            f.write(f"  Remaining: {self.config['currency']}{analysis['remaining']:.2f}\n")
                            f.write(f"  Usage: {analysis['percentage_used']:.1f}%\n")
                            f.write(f"  Status: {analysis['status'].upper()}\n\n")
                
                # Category breakdown
                category_spending = self.get_spending_by_category()
                if category_spending:
                    f.write("SPENDING BY CATEGORY (All Time)\n")
                    f.write("-"*30 + "\n")
                    sorted_categories = sorted(category_spending.items(), key=lambda x: x[1], reverse=True)
                    for category, amount in sorted_categories:
                        f.write(f"{category}: {self.config['currency']}{amount:.2f}\n")
                    f.write("\n")
            
            print(f"✓ Summary report exported to {filename}")
            return True
            
        except Exception as e:
            print(f"Error exporting summary report: {e}")
            return False
    
    # Search and Display Functions
    
    def search_transactions(self, **criteria):
        """
        Search transactions based on various criteria
        
        Args:
            category (str): Filter by category
            description (str): Search in description (partial match)
            min_amount (float): Minimum amount
            max_amount (float): Maximum amount
            transaction_type (str): 'income' or 'expense'
            date_from (str): Start date (YYYY-MM-DD)
            date_to (str): End date (YYYY-MM-DD)
        """
        try:
            results = self.transactions.copy()
            
            # Apply filters
            if 'category' in criteria and criteria['category']:
                results = [t for t in results if t['category'].lower() == criteria['category'].lower()]
            
            if 'description' in criteria and criteria['description']:
                search_term = criteria['description'].lower()
                results = [t for t in results if search_term in t['description'].lower()]
            
            if 'min_amount' in criteria and criteria['min_amount'] is not None:
                results = [t for t in results if t['amount'] >= criteria['min_amount']]
            
            if 'max_amount' in criteria and criteria['max_amount'] is not None:
                results = [t for t in results if t['amount'] <= criteria['max_amount']]
            
            if 'transaction_type' in criteria and criteria['transaction_type']:
                results = [t for t in results if t['type'] == criteria['transaction_type']]
            
            if 'date_from' in criteria and criteria['date_from']:
                date_from = datetime.datetime.strptime(criteria['date_from'], self.config["date_format"]).date()
                results = [t for t in results 
                          if datetime.datetime.strptime(t['date'], self.config["date_format"]).date() >= date_from]
            
            if 'date_to' in criteria and criteria['date_to']:
                date_to = datetime.datetime.strptime(criteria['date_to'], self.config["date_format"]).date()
                results = [t for t in results 
                          if datetime.datetime.strptime(t['date'], self.config["date_format"]).date() <= date_to]
            
            return results
            
        except Exception as e:
            print(f"Error searching transactions: {e}")
            return []
    
    def display_transaction(self, transaction):
        """
        Display a single transaction in a formatted way
        """
        print(f"ID: {transaction['id']}")
        print(f"Date: {transaction['date']}")
        print(f"Type: {transaction['type'].title()}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print(f"Amount: {self.config['currency']}{transaction['amount']:.2f}")
    
    def display_transactions(self, transactions, limit=None):
        """
        Display multiple transactions in a table format
        """
        if not transactions:
            print("No transactions to display")
            return
        
        # Sort by date (most recent first)
        sorted_transactions = sorted(
            transactions, 
            key=lambda x: datetime.datetime.strptime(x['date'], self.config["date_format"]), 
            reverse=True
        )
        
        if limit:
            sorted_transactions = sorted_transactions[:limit]
        
        # Display header
        print(f"\n{'ID':<5} {'Date':<12} {'Type':<8} {'Category':<15} {'Description':<25} {'Amount':<10}")
        print("-" * 80)
        
        # Display transactions
        for transaction in sorted_transactions:
            amount_str = f"{self.config['currency']}{transaction['amount']:.2f}"
            if transaction['type'] == 'expense':
                amount_str = f"-{amount_str}"
            
            description = transaction['description'][:22] + "..." if len(transaction['description']) > 22 else transaction['description']
            category = transaction['category'][:12] + "..." if len(transaction['category']) > 12 else transaction['category']
            
            print(f"{transaction['id']:<5} {transaction['date']:<12} {transaction['type']:<8} "
                  f"{category:<15} {description:<25} {amount_str:>10}")
        
        print("-" * 80)
        print(f"Showing {len(sorted_transactions)} of {len(transactions)} transactions")
    
    def get_categories(self):
        """
        Get list of all categories used in transactions
        """
        categories = set(t['category'] for t in self.transactions)
        all_categories = categories.union(set(self.default_categories))
        return sorted(list(all_categories))


def get_user_input(prompt, input_type=str, required=True, validator=None):
    """
    Get validated user input with error handling
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            if required and not user_input:
                print("This field is required. Please enter a value.")
                continue
            
            if not user_input and not required:
                return None
            
            # Convert to appropriate type
            if input_type == int:
                converted_input = int(user_input)
            elif input_type == float:
                converted_input = float(user_input)
            else:
                converted_input = user_input
            
            # Apply custom validator if provided
            if validator and not validator(converted_input):
                print("Invalid input. Please try again.")
                continue
            
            return converted_input
            
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}")
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled")
            return None


def main():
    """
    Main application interface
    """
    print("=" * 60)
    print("    PERSONAL FINANCE MANAGER")
    print("    Week 3 Capstone Project")
    print("=" * 60)
    print("Welcome to your comprehensive financial management system!")
    print("This application demonstrates all concepts from Week 3:")
    print("• Functions for code organization")
    print("• Built-in functions for data analysis") 
    print("• Module integration for extended features")
    print("• File handling for data persistence")
    print("• Error handling for robust operation")
    print()
    
    # Initialize the finance manager
    try:
        fm = PersonalFinanceManager()
    except Exception as e:
        print(f"Failed to initialize Finance Manager: {e}")
        return
    
    # Main application loop
    while True:
        print("\n" + "=" * 40)
        print("PERSONAL FINANCE MANAGER - MAIN MENU")
        print("=" * 40)
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. Search Transactions")
        print("6. Budget Management")
        print("7. Financial Reports")
        print("8. Data Export")
        print("9. Settings")
        print("10. Exit")
        
        try:
            choice = input("\nSelect option (1-10): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye!")
            break
        
        if choice == "1":
            # Add Transaction
            print("\n--- ADD TRANSACTION ---")
            
            # Get transaction type
            trans_type = get_user_input("Transaction type (income/expense): ", str, True,
                                       lambda x: x.lower() in ['income', 'expense'])
            if not trans_type:
                continue
            trans_type = trans_type.lower()
            
            # Get amount
            amount = get_user_input("Amount: ", float, True, lambda x: x > 0)
            if not amount:
                continue
            
            # Get description
            description = get_user_input("Description: ", str, True)
            if not description:
                continue
            
            # Show available categories
            categories = fm.get_categories()
            print("\nAvailable categories:", ", ".join(categories))
            category = get_user_input("Category: ", str, True)
            if not category:
                continue
            
            # Optional date (use current if not provided)
            date_str = get_user_input("Date (YYYY-MM-DD, or press Enter for today): ", str, False)
            
            # Add the transaction
            fm.add_transaction(amount, description, category, trans_type, date_str)
        
        elif choice == "2":
            # View Transactions
            print("\n--- VIEW TRANSACTIONS ---")
            print("1. Recent transactions (last 10)")
            print("2. All transactions")
            print("3. This month's transactions")
            
            view_choice = get_user_input("Select view option (1-3): ", str)
            if not view_choice:
                continue
            
            if view_choice == "1":
                fm.display_transactions(fm.transactions, limit=10)
            elif view_choice == "2":
                fm.display_transactions(fm.transactions)
            elif view_choice == "3":
                today = datetime.date.today()
                month_start = datetime.date(today.year, today.month, 1)
                month_transactions = fm.filter_transactions_by_date(month_start)
                fm.display_transactions(month_transactions)
        
        elif choice == "3":
            # Edit Transaction
            print("\n--- EDIT TRANSACTION ---")
            
            transaction_id = get_user_input("Enter transaction ID to edit: ", int, True)
            if not transaction_id:
                continue
            
            transaction = fm.find_transaction_by_id(transaction_id)
            if not transaction:
                print(f"Transaction {transaction_id} not found")
                continue
            
            print("\nCurrent transaction:")
            fm.display_transaction(transaction)
            
            print("\nEnter new values (press Enter to keep current value):")
            
            updates = {}
            
            # Get updated fields
            new_amount = get_user_input(f"Amount ({transaction['amount']}): ", str, False)
            if new_amount:
                try:
                    updates['amount'] = float(new_amount)
                except ValueError:
                    print("Invalid amount, keeping current value")
            
            new_description = get_user_input(f"Description ({transaction['description']}): ", str, False)
            if new_description:
                updates['description'] = new_description
            
            new_category = get_user_input(f"Category ({transaction['category']}): ", str, False)
            if new_category:
                updates['category'] = new_category
            
            new_type = get_user_input(f"Type ({transaction['type']}): ", str, False,
                                     lambda x: x.lower() in ['income', 'expense', ''])
            if new_type:
                updates['type'] = new_type.lower()
            
            if updates:
                fm.edit_transaction(transaction_id, **updates)
            else:
                print("No changes made")
        
        elif choice == "4":
            # Delete Transaction
            print("\n--- DELETE TRANSACTION ---")
            
            transaction_id = get_user_input("Enter transaction ID to delete: ", int, True)
            if transaction_id:
                fm.delete_transaction(transaction_id)
        
        elif choice == "5":
            # Search Transactions
            print("\n--- SEARCH TRANSACTIONS ---")
            print("Enter search criteria (press Enter to skip):")
            
            search_criteria = {}
            
            category = get_user_input("Category: ", str, False)
            if category:
                search_criteria['category'] = category
            
            description = get_user_input("Description (partial match): ", str, False)
            if description:
                search_criteria['description'] = description
            
            min_amount = get_user_input("Minimum amount: ", str, False)
            if min_amount:
                try:
                    search_criteria['min_amount'] = float(min_amount)
                except ValueError:
                    pass
            
            max_amount = get_user_input("Maximum amount: ", str, False)
            if max_amount:
                try:
                    search_criteria['max_amount'] = float(max_amount)
                except ValueError:
                    pass
            
            trans_type = get_user_input("Transaction type (income/expense): ", str, False)
            if trans_type and trans_type.lower() in ['income', 'expense']:
                search_criteria['transaction_type'] = trans_type.lower()
            
            results = fm.search_transactions(**search_criteria)
            print(f"\nSearch Results: {len(results)} transactions found")
            fm.display_transactions(results)
        
        elif choice == "6":
            # Budget Management
            print("\n--- BUDGET MANAGEMENT ---")
            print("1. Set budget for category")
            print("2. View current budgets")
            print("3. Budget analysis")
            
            budget_choice = get_user_input("Select option (1-3): ", str)
            if not budget_choice:
                continue
            
            if budget_choice == "1":
                categories = fm.get_categories()
                print("\nAvailable categories:", ", ".join(categories))
                category = get_user_input("Category: ", str, True)
                if not category:
                    continue
                
                amount = get_user_input("Monthly budget amount: ", float, True, lambda x: x > 0)
                if amount:
                    fm.set_budget(category, amount)
            
            elif budget_choice == "2":
                if not fm.budgets:
                    print("No budgets set yet")
                else:
                    print("\nCurrent Budgets:")
                    print("-" * 40)
                    for category, budget_info in fm.budgets.items():
                        print(f"{category}: {fm.config['currency']}{budget_info['amount']:.2f}/month")
            
            elif budget_choice == "3":
                analysis = fm.get_budget_analysis()
                if not analysis:
                    print("No budget data available")
                else:
                    today = datetime.date.today()
                    print(f"\nBudget Analysis for {today.strftime('%B %Y')}:")
                    print("-" * 60)
                    
                    for category, data in analysis.items():
                        status_symbol = "🔴" if data['status'] == 'over' else "🟢" if data['status'] == 'under' else "⚪"
                        print(f"{status_symbol} {category}:")
                        
                        if data['status'] != 'no_budget':
                            print(f"   Budget: {fm.config['currency']}{data['budget']:.2f}")
                            print(f"   Spent: {fm.config['currency']}{data['spent']:.2f}")
                            print(f"   Remaining: {fm.config['currency']}{data['remaining']:.2f}")
                            print(f"   Usage: {data['percentage_used']:.1f}%")
                        else:
                            print(f"   Spent: {fm.config['currency']}{data['spent']:.2f} (No budget set)")
                        print()
        
        elif choice == "7":
            # Financial Reports
            print("\n--- FINANCIAL REPORTS ---")
            print("1. Monthly summary")
            print("2. Spending by category")
            print("3. Yearly overview")
            
            report_choice = get_user_input("Select report (1-3): ", str)
            if not report_choice:
                continue
            
            if report_choice == "1":
                summary = fm.get_monthly_summary()
                if summary:
                    print(f"\nMonthly Summary for {summary['period']}:")
                    print("-" * 40)
                    print(f"Total Income: {fm.config['currency']}{summary['total_income']:.2f}")
                    print(f"Total Expenses: {fm.config['currency']}{summary['total_expenses']:.2f}")
                    print(f"Net Income: {fm.config['currency']}{summary['net_income']:.2f}")
                    print(f"Number of Transactions: {summary['transaction_count']}")
                    print(f"Average Transaction: {fm.config['currency']}{summary['average_transaction']:.2f}")
                    if summary['top_expense_category']:
                        print(f"Top Expense Category: {summary['top_expense_category']} "
                              f"({fm.config['currency']}{summary['top_category_amount']:.2f})")
                else:
                    print("No data available for monthly summary")
            
            elif report_choice == "2":
                spending = fm.get_spending_by_category()
                if spending:
                    print("\nSpending by Category:")
                    print("-" * 40)
                    sorted_spending = sorted(spending.items(), key=lambda x: x[1], reverse=True)
                    total_spending = sum(spending.values())
                    
                    for category, amount in sorted_spending:
                        percentage = (amount / total_spending * 100) if total_spending > 0 else 0
                        print(f"{category:<20} {fm.config['currency']}{amount:>8.2f} ({percentage:4.1f}%)")
                    
                    print("-" * 40)
                    print(f"{'TOTAL':<20} {fm.config['currency']}{total_spending:>8.2f}")
                else:
                    print("No spending data available")
            
            elif report_choice == "3":
                # Simple yearly overview
                current_year = datetime.date.today().year
                year_transactions = [
                    t for t in fm.transactions
                    if datetime.datetime.strptime(t['date'], fm.config['date_format']).year == current_year
                ]
                
                if year_transactions:
                    yearly_income = sum(t['amount'] for t in year_transactions if t['type'] == 'income')
                    yearly_expenses = sum(t['amount'] for t in year_transactions if t['type'] == 'expense')
                    
                    print(f"\nYearly Overview for {current_year}:")
                    print("-" * 40)
                    print(f"Total Income: {fm.config['currency']}{yearly_income:.2f}")
                    print(f"Total Expenses: {fm.config['currency']}{yearly_expenses:.2f}")
                    print(f"Net Income: {fm.config['currency']}{yearly_income - yearly_expenses:.2f}")
                    print(f"Total Transactions: {len(year_transactions)}")
                    print(f"Monthly Average Income: {fm.config['currency']}{yearly_income/12:.2f}")
                    print(f"Monthly Average Expenses: {fm.config['currency']}{yearly_expenses/12:.2f}")
                else:
                    print(f"No data available for {current_year}")
        
        elif choice == "8":
            # Data Export
            print("\n--- DATA EXPORT ---")
            print("1. Export transactions to CSV")
            print("2. Export summary report")
            
            export_choice = get_user_input("Select export option (1-2): ", str)
            if not export_choice:
                continue
            
            if export_choice == "1":
                filename = get_user_input("Filename (press Enter for auto-generated): ", str, False)
                fm.export_to_csv(filename)
            
            elif export_choice == "2":
                filename = get_user_input("Filename (press Enter for auto-generated): ", str, False)
                fm.export_summary_report(filename)
        
        elif choice == "9":
            # Settings
            print("\n--- SETTINGS ---")
            print(f"Current currency symbol: {fm.config['currency']}")
            print(f"Date format: {fm.config['date_format']}")
            print(f"Auto backup: {'Enabled' if fm.config['auto_backup'] else 'Disabled'}")
            
            print("\n1. Change currency symbol")
            print("2. Toggle auto backup")
            print("3. Create manual backup")
            print("4. View backup files")
            
            settings_choice = get_user_input("Select option (1-4): ", str)
            if not settings_choice:
                continue
            
            if settings_choice == "1":
                new_currency = get_user_input(f"New currency symbol ({fm.config['currency']}): ", str, False)
                if new_currency:
                    fm.config['currency'] = new_currency
                    fm.save_config()
                    print(f"Currency symbol updated to: {new_currency}")
            
            elif settings_choice == "2":
                fm.config['auto_backup'] = not fm.config['auto_backup']
                fm.save_config()
                status = "enabled" if fm.config['auto_backup'] else "disabled"
                print(f"Auto backup {status}")
            
            elif settings_choice == "3":
                fm.create_backups()
                print("Manual backup created successfully")
            
            elif settings_choice == "4":
                backup_files = list(fm.backup_dir.glob("*.json"))
                if backup_files:
                    print("\nBackup files:")
                    for backup_file in sorted(backup_files, reverse=True):
                        file_time = datetime.datetime.fromtimestamp(backup_file.stat().st_mtime)
                        print(f"  {backup_file.name} - {file_time.strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    print("No backup files found")
        
        elif choice == "10":
            # Exit
            print("\nSaving data before exit...")
            if fm.save_data():
                print("Data saved successfully!")
            else:
                print("Warning: Could not save data!")
            
            print("Thank you for using Personal Finance Manager!")
            print("This project demonstrated all Week 3 concepts:")
            print("• Functions for code organization and reusability")
            print("• Built-in functions for data analysis and processing")
            print("• Modules for extended functionality (datetime, json, csv)")
            print("• File handling for data persistence and backups")
            print("• Error handling for robust, user-friendly operation")
            print("\nCongratulations on completing Week 3! 🎉")
            break
        
        else:
            print("Invalid option. Please select 1-10.")


if __name__ == "__main__":
    main()