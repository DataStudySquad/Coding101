# Day 26: CSV File Processing - Working with Tabular Data

Welcome to Day 26! Today we're diving into CSV (Comma-Separated Values) file processing - one of the most common data formats you'll encounter in the real world. Think of CSV files as the universal language of spreadsheets and databases, and Python as your personal data translator and analyst.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Understand CSV files and their importance in data processing
- Use Python's built-in `csv` module for reading and writing CSV files
- Get introduced to pandas for advanced data manipulation
- Clean and validate CSV data programmatically
- Perform data analysis on tabular datasets
- Build a comprehensive sales data analysis system

## 📄 What are CSV Files?

### The Universal Data Format

CSV (Comma-Separated Values) files are like the "plain text" of data storage:

```
Name,Age,City,Salary
Alice,25,New York,75000
Bob,30,Los Angeles,82000
Charlie,28,Chicago,78000
```

**Why CSV files are everywhere:**
- **Simple**: Human-readable text format
- **Universal**: Every spreadsheet program can open them
- **Lightweight**: Small file sizes, fast processing
- **Cross-platform**: Works on any operating system
- **Database-friendly**: Easy to import/export from databases

### Real-World Applications

```python
csv_use_cases = {
    "Business": "Sales reports, customer data, financial records",
    "Science": "Experimental data, survey results, sensor readings",
    "Web Analytics": "User behavior data, traffic statistics",
    "E-commerce": "Product catalogs, order history, inventory",
    "Education": "Student grades, attendance records, survey data",
    "Government": "Census data, economic indicators, public records"
}
```

## 📊 Python's CSV Module - Your Data Toolkit

### Basic CSV Reading

```python
import csv
from pathlib import Path

def read_csv_basic(filename):
    """
    Read CSV file using Python's built-in csv module
    Like having a careful librarian who reads every line precisely
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Create CSV reader
            csv_reader = csv.reader(file)
            
            # Read header row
            headers = next(csv_reader)
            print(f"📋 Headers: {headers}")
            
            # Read data rows
            data_rows = []
            for row_num, row in enumerate(csv_reader, start=1):
                data_rows.append(row)
                if row_num <= 3:  # Show first 3 rows
                    print(f"Row {row_num}: {row}")
            
            print(f"📊 Total rows read: {len(data_rows)}")
            return headers, data_rows
            
    except FileNotFoundError:
        print(f"❌ File {filename} not found")
        return None, None
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None, None

# Example usage with sample data
sample_csv_content = """Name,Age,Department,Salary,Years_Experience
Alice Johnson,28,Engineering,85000,5
Bob Smith,32,Marketing,72000,8
Charlie Brown,25,Engineering,78000,3
Diana Prince,30,Sales,81000,6
Eve Adams,27,Marketing,69000,4"""

# Create sample CSV file
with open('employees.csv', 'w') as f:
    f.write(sample_csv_content)

print("📄 Reading CSV file with csv.reader:")
headers, data = read_csv_basic('employees.csv')
```

### Advanced CSV Reading with DictReader

```python
import csv

def read_csv_as_dictionaries(filename):
    """
    Read CSV as dictionaries for easier data access
    Like having each row as a labeled filing cabinet
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # DictReader treats first row as headers
            csv_reader = csv.DictReader(file)
            
            print(f"📋 Field names: {csv_reader.fieldnames}")
            
            employees = []
            for row_num, row in enumerate(csv_reader, start=1):
                employees.append(row)
                if row_num <= 3:  # Show first 3 rows
                    print(f"Employee {row_num}:")
                    for key, value in row.items():
                        print(f"   {key}: {value}")
                    print()
            
            return employees
            
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return []

# Read as dictionaries
print("📚 Reading CSV as dictionaries:")
employees = read_csv_as_dictionaries('employees.csv')

# Now you can access data by field name
if employees:
    print(f"First employee's name: {employees[0]['Name']}")
    print(f"First employee's salary: ${employees[0]['Salary']}")
```

### Writing CSV Files

```python
import csv

def write_csv_from_data(filename, headers, data_rows):
    """
    Write data to CSV file
    Like organizing messy papers into a neat filing system
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            
            # Write header
            csv_writer.writerow(headers)
            
            # Write data rows
            csv_writer.writerows(data_rows)
        
        print(f"✅ CSV file '{filename}' written successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error writing CSV: {e}")
        return False

def write_csv_from_dictionaries(filename, dict_data):
    """
    Write dictionaries to CSV file
    """
    if not dict_data:
        print("❌ No data to write")
        return False
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            # Get field names from first dictionary
            fieldnames = dict_data[0].keys()
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write header
            csv_writer.writeheader()
            
            # Write data rows
            csv_writer.writerows(dict_data)
        
        print(f"✅ Dictionary data written to '{filename}'")
        return True
        
    except Exception as e:
        print(f"❌ Error writing CSV: {e}")
        return False

# Example: Create and write new CSV data
new_employees = [
    {'Name': 'Frank Wilson', 'Age': '35', 'Department': 'Finance', 'Salary': '89000', 'Years_Experience': '10'},
    {'Name': 'Grace Lee', 'Age': '29', 'Department': 'Engineering', 'Salary': '92000', 'Years_Experience': '7'},
    {'Name': 'Henry Clark', 'Age': '26', 'Department': 'Marketing', 'Salary': '67000', 'Years_Experience': '3'}
]

write_csv_from_dictionaries('new_employees.csv', new_employees)
```

## 🐼 Introduction to Pandas - Data Analysis Powerhouse

### Why Pandas?

While Python's csv module is great for basic operations, pandas is like upgrading from a bicycle to a sports car for data analysis:

```python
import pandas as pd
import numpy as np

def demonstrate_pandas_power():
    """
    Show why pandas is amazing for CSV processing
    """
    print("🐼 Pandas CSV Processing Demo")
    print("-" * 35)
    
    # Read CSV with pandas (so much easier!)
    df = pd.read_csv('employees.csv')
    
    print("📊 Basic Info:")
    print(f"   Shape: {df.shape} (rows, columns)")
    print(f"   Columns: {list(df.columns)}")
    print(f"   Data types:\n{df.dtypes}")
    
    print("\n📋 First 3 rows:")
    print(df.head(3))
    
    print("\n📈 Quick Statistics:")
    print(df.describe())
    
    print("\n💰 Salary Analysis:")
    print(f"   Average salary: ${df['Salary'].mean():,.2f}")
    print(f"   Median salary: ${df['Salary'].median():,.2f}")
    print(f"   Salary range: ${df['Salary'].min():,} - ${df['Salary'].max():,}")
    
    print("\n🏢 Department Breakdown:")
    dept_counts = df['Department'].value_counts()
    for dept, count in dept_counts.items():
        print(f"   {dept}: {count} employees")
    
    return df

# Demonstrate pandas capabilities
df = demonstrate_pandas_power()
```

### Data Cleaning and Validation

```python
import pandas as pd
import numpy as np

class CSVDataCleaner:
    """
    A comprehensive CSV data cleaning toolkit
    Like having a professional data janitor
    """
    
    def __init__(self, filename):
        """
        Initialize with CSV file
        """
        self.filename = filename
        self.df = None
        self.original_shape = None
        self.cleaning_log = []
        
        self.load_data()
    
    def load_data(self):
        """
        Load CSV data with error handling
        """
        try:
            self.df = pd.read_csv(self.filename)
            self.original_shape = self.df.shape
            self.log(f"✅ Loaded {self.filename}: {self.original_shape[0]} rows, {self.original_shape[1]} columns")
        except Exception as e:
            self.log(f"❌ Error loading {self.filename}: {e}")
    
    def log(self, message):
        """
        Log cleaning operations
        """
        self.cleaning_log.append(message)
        print(message)
    
    def inspect_data(self):
        """
        Comprehensive data inspection
        """
        if self.df is None:
            return
        
        print("\n🔍 DATA INSPECTION REPORT")
        print("=" * 40)
        
        print(f"📊 Dataset shape: {self.df.shape}")
        print(f"📋 Columns: {list(self.df.columns)}")
        
        print(f"\n📈 Data types:")
        for col, dtype in self.df.dtypes.items():
            print(f"   {col}: {dtype}")
        
        print(f"\n❓ Missing values:")
        missing = self.df.isnull().sum()
        for col, count in missing.items():
            if count > 0:
                print(f"   {col}: {count} missing ({count/len(self.df)*100:.1f}%)")
        
        print(f"\n🔢 Numeric columns summary:")
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print(self.df[numeric_cols].describe())
        
        print(f"\n📝 Text columns info:")
        text_cols = self.df.select_dtypes(include=['object']).columns
        for col in text_cols:
            unique_count = self.df[col].nunique()
            print(f"   {col}: {unique_count} unique values")
            if unique_count <= 10:  # Show values if not too many
                print(f"      Values: {list(self.df[col].unique())}")
    
    def clean_missing_values(self, strategy='auto'):
        """
        Handle missing values intelligently
        """
        if self.df is None:
            return
        
        missing_before = self.df.isnull().sum().sum()
        
        for col in self.df.columns:
            missing_count = self.df[col].isnull().sum()
            if missing_count > 0:
                if strategy == 'auto':
                    if self.df[col].dtype in ['int64', 'float64']:
                        # Fill numeric with median
                        fill_value = self.df[col].median()
                        self.df[col].fillna(fill_value, inplace=True)
                        self.log(f"🔧 Filled {missing_count} missing values in {col} with median ({fill_value})")
                    else:
                        # Fill text with mode (most common)
                        fill_value = self.df[col].mode()[0] if not self.df[col].mode().empty else 'Unknown'
                        self.df[col].fillna(fill_value, inplace=True)
                        self.log(f"🔧 Filled {missing_count} missing values in {col} with mode ('{fill_value}')")
        
        missing_after = self.df.isnull().sum().sum()
        self.log(f"✅ Missing values reduced from {missing_before} to {missing_after}")
    
    def remove_duplicates(self):
        """
        Remove duplicate rows
        """
        if self.df is None:
            return
        
        before_count = len(self.df)
        self.df.drop_duplicates(inplace=True)
        after_count = len(self.df)
        
        removed = before_count - after_count
        if removed > 0:
            self.log(f"🗑️ Removed {removed} duplicate rows")
        else:
            self.log("✅ No duplicates found")
    
    def standardize_text(self):
        """
        Standardize text columns
        """
        if self.df is None:
            return
        
        text_cols = self.df.select_dtypes(include=['object']).columns
        
        for col in text_cols:
            # Strip whitespace and standardize case
            original_values = self.df[col].unique()
            self.df[col] = self.df[col].astype(str).str.strip().str.title()
            new_values = self.df[col].unique()
            
            if len(original_values) != len(new_values):
                self.log(f"🧹 Standardized text in {col}: {len(original_values)} → {len(new_values)} unique values")
    
    def validate_numeric_ranges(self, column_ranges):
        """
        Validate that numeric columns are within expected ranges
        """
        if self.df is None:
            return
        
        for col, (min_val, max_val) in column_ranges.items():
            if col in self.df.columns:
                outliers = self.df[(self.df[col] < min_val) | (self.df[col] > max_val)]
                if len(outliers) > 0:
                    self.log(f"⚠️ Found {len(outliers)} outliers in {col} (outside {min_val}-{max_val})")
                else:
                    self.log(f"✅ All values in {col} are within expected range ({min_val}-{max_val})")
    
    def export_cleaned_data(self, output_filename=None):
        """
        Export cleaned data to new CSV
        """
        if self.df is None:
            return None
        
        if output_filename is None:
            output_filename = self.filename.replace('.csv', '_cleaned.csv')
        
        try:
            self.df.to_csv(output_filename, index=False)
            self.log(f"✅ Cleaned data exported to {output_filename}")
            return output_filename
        except Exception as e:
            self.log(f"❌ Error exporting data: {e}")
            return None
    
    def generate_cleaning_report(self):
        """
        Generate comprehensive cleaning report
        """
        print("\n📋 DATA CLEANING SUMMARY")
        print("=" * 35)
        print(f"Original data: {self.original_shape[0]} rows, {self.original_shape[1]} columns")
        if self.df is not None:
            print(f"Final data: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
            rows_changed = self.original_shape[0] - self.df.shape[0]
            if rows_changed != 0:
                print(f"Net change: {rows_changed:+d} rows")
        
        print(f"\n🔧 Cleaning operations performed:")
        for i, operation in enumerate(self.cleaning_log, 1):
            print(f"   {i}. {operation}")

# Create sample data with issues for demonstration
messy_data = """Name,Age,Department,Salary,Years_Experience
Alice Johnson,28,engineering,85000,5
Bob Smith,,Marketing,72000,8
Charlie Brown,25,ENGINEERING,78000,3
Diana Prince,30,sales,81000,6
Eve Adams,27, marketing ,69000,4
Frank Wilson,35,Finance,,10
Alice Johnson,28,engineering,85000,5
Grace Lee,29,Engineering,92000,7"""

with open('messy_employees.csv', 'w') as f:
    f.write(messy_data)

# Demonstrate data cleaning
print("🧹 CSV Data Cleaning Demo:")
cleaner = CSVDataCleaner('messy_employees.csv')
cleaner.inspect_data()
cleaner.clean_missing_values()
cleaner.remove_duplicates() 
cleaner.standardize_text()
cleaner.validate_numeric_ranges({
    'Age': (18, 70),
    'Salary': (30000, 200000),
    'Years_Experience': (0, 50)
})
cleaned_file = cleaner.export_cleaned_data()
cleaner.generate_cleaning_report()
```

## 📊 Sales Data Analysis Project

Let me create a comprehensive sales analysis system:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import csv

class SalesDataAnalyzer:
    """
    Comprehensive sales data analysis system
    Like having a team of business analysts at your fingertips
    """
    
    def __init__(self, sales_file=None):
        """
        Initialize the sales analyzer
        """
        self.sales_data = None
        self.analysis_results = {}
        
        if sales_file:
            self.load_sales_data(sales_file)
        else:
            self.generate_sample_sales_data()
        
        print(f"💼 Sales Data Analyzer initialized")
        if self.sales_data is not None:
            print(f"📊 Loaded {len(self.sales_data)} sales records")
    
    def generate_sample_sales_data(self):
        """
        Generate realistic sample sales data for demonstration
        """
        np.random.seed(42)
        
        # Product categories and names
        categories = {
            'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera'],
            'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Sneakers', 'Dress'],
            'Home & Garden': ['Coffee Maker', 'Vacuum', 'Plant Pot', 'Lamp', 'Cushion'],
            'Books': ['Fiction Novel', 'Cookbook', 'Biography', 'Textbook', 'Comic'],
            'Sports': ['Football', 'Basketball', 'Tennis Racket', 'Yoga Mat', 'Dumbbells']
        }
        
        # Generate sales data for 12 months
        sales_records = []
        
        start_date = datetime(2024, 1, 1)
        
        for day in range(365):
            current_date = start_date + timedelta(days=day)
            
            # Vary sales volume by day of week and season
            day_of_week = current_date.weekday()
            sales_multiplier = 1.0
            
            # Weekends have more sales
            if day_of_week >= 5:
                sales_multiplier *= 1.3
            
            # Holiday season boost
            if current_date.month in [11, 12]:
                sales_multiplier *= 1.5
            
            # Generate 1-8 sales per day
            num_sales = max(1, int(np.random.poisson(3) * sales_multiplier))
            
            for _ in range(num_sales):
                # Random category and product
                category = np.random.choice(list(categories.keys()))
                product = np.random.choice(categories[category])
                
                # Price based on category
                if category == 'Electronics':
                    base_price = np.random.uniform(200, 1500)
                elif category == 'Clothing':
                    base_price = np.random.uniform(20, 200)
                elif category == 'Home & Garden':
                    base_price = np.random.uniform(30, 300)
                elif category == 'Books':
                    base_price = np.random.uniform(10, 80)
                else:  # Sports
                    base_price = np.random.uniform(25, 400)
                
                # Quantity (usually 1, sometimes more)
                quantity = np.random.choice([1, 1, 1, 1, 2, 2, 3], p=[0.4, 0.3, 0.2, 0.05, 0.03, 0.015, 0.005])
                
                # Customer info
                customer_id = f"CUST_{np.random.randint(1000, 9999)}"
                
                # Sales rep
                sales_rep = np.random.choice(['Alice Johnson', 'Bob Smith', 'Charlie Brown', 
                                            'Diana Prince', 'Eve Adams', 'Frank Wilson'])
                
                # Region
                region = np.random.choice(['North', 'South', 'East', 'West'], p=[0.3, 0.2, 0.25, 0.25])
                
                sales_records.append({
                    'Date': current_date.strftime('%Y-%m-%d'),
                    'Product': product,
                    'Category': category,
                    'Price': round(base_price, 2),
                    'Quantity': quantity,
                    'Total_Amount': round(base_price * quantity, 2),
                    'Customer_ID': customer_id,
                    'Sales_Rep': sales_rep,
                    'Region': region
                })
        
        # Convert to DataFrame
        self.sales_data = pd.DataFrame(sales_records)
        
        # Convert date column to datetime
        self.sales_data['Date'] = pd.to_datetime(self.sales_data['Date'])
        
        # Save to CSV
        self.sales_data.to_csv('sample_sales_data.csv', index=False)
        print(f"💾 Sample sales data saved to 'sample_sales_data.csv'")
        
        return self.sales_data
    
    def load_sales_data(self, filename):
        """
        Load sales data from CSV file
        """
        try:
            self.sales_data = pd.read_csv(filename)
            
            # Ensure Date column is datetime
            if 'Date' in self.sales_data.columns:
                self.sales_data['Date'] = pd.to_datetime(self.sales_data['Date'])
            
            print(f"✅ Sales data loaded from {filename}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading sales data: {e}")
            return False
    
    def basic_statistics(self):
        """
        Calculate basic sales statistics
        """
        if self.sales_data is None:
            return
        
        stats = {
            'total_records': len(self.sales_data),
            'date_range': {
                'start': self.sales_data['Date'].min(),
                'end': self.sales_data['Date'].max()
            },
            'total_revenue': self.sales_data['Total_Amount'].sum(),
            'average_order_value': self.sales_data['Total_Amount'].mean(),
            'median_order_value': self.sales_data['Total_Amount'].median(),
            'total_quantity_sold': self.sales_data['Quantity'].sum(),
            'unique_customers': self.sales_data['Customer_ID'].nunique(),
            'unique_products': self.sales_data['Product'].nunique(),
            'categories': self.sales_data['Category'].unique(),
            'regions': self.sales_data['Region'].unique(),
            'sales_reps': self.sales_data['Sales_Rep'].unique()
        }
        
        print("\n💰 SALES STATISTICS OVERVIEW")
        print("=" * 40)
        print(f"📊 Total Records: {stats['total_records']:,}")
        print(f"📅 Date Range: {stats['date_range']['start'].strftime('%Y-%m-%d')} to {stats['date_range']['end'].strftime('%Y-%m-%d')}")
        print(f"💵 Total Revenue: ${stats['total_revenue']:,.2f}")
        print(f"🛒 Average Order Value: ${stats['average_order_value']:.2f}")
        print(f"📈 Median Order Value: ${stats['median_order_value']:.2f}")
        print(f"📦 Total Quantity Sold: {stats['total_quantity_sold']:,}")
        print(f"👥 Unique Customers: {stats['unique_customers']:,}")
        print(f"🛍️ Unique Products: {stats['unique_products']:,}")
        print(f"🏷️ Categories: {', '.join(stats['categories'])}")
        print(f"🌍 Regions: {', '.join(stats['regions'])}")
        print(f"👤 Sales Reps: {len(stats['sales_reps'])} people")
        
        self.analysis_results['basic_stats'] = stats
        return stats
    
    def monthly_analysis(self):
        """
        Analyze sales by month
        """
        if self.sales_data is None:
            return
        
        # Group by month
        monthly_data = self.sales_data.groupby(self.sales_data['Date'].dt.to_period('M')).agg({
            'Total_Amount': ['sum', 'count', 'mean'],
            'Quantity': 'sum',
            'Customer_ID': 'nunique'
        }).round(2)
        
        # Flatten column names
        monthly_data.columns = ['Revenue', 'Orders', 'Avg_Order_Value', 'Quantity_Sold', 'Unique_Customers']
        
        print("\n📅 MONTHLY SALES ANALYSIS")
        print("=" * 60)
        print(monthly_data.to_string())
        
        # Find best and worst months
        best_month = monthly_data['Revenue'].idxmax()
        worst_month = monthly_data['Revenue'].idxmin()
        
        print(f"\n🏆 Best Month: {best_month} (${monthly_data.loc[best_month, 'Revenue']:,.2f})")
        print(f"📉 Worst Month: {worst_month} (${monthly_data.loc[worst_month, 'Revenue']:,.2f})")
        
        self.analysis_results['monthly'] = monthly_data
        return monthly_data
    
    def category_analysis(self):
        """
        Analyze sales by category
        """
        if self.sales_data is None:
            return
        
        category_analysis = self.sales_data.groupby('Category').agg({
            'Total_Amount': ['sum', 'count', 'mean'],
            'Quantity': 'sum',
            'Price': 'mean'
        }).round(2)
        
        category_analysis.columns = ['Revenue', 'Orders', 'Avg_Order_Value', 'Quantity_Sold', 'Avg_Price']
        
        # Calculate percentages
        total_revenue = self.sales_data['Total_Amount'].sum()
        category_analysis['Revenue_Percentage'] = (category_analysis['Revenue'] / total_revenue * 100).round(1)
        
        # Sort by revenue
        category_analysis = category_analysis.sort_values('Revenue', ascending=False)
        
        print("\n🏷️ CATEGORY PERFORMANCE ANALYSIS")
        print("=" * 70)
        print(category_analysis.to_string())
        
        self.analysis_results['categories'] = category_analysis
        return category_analysis
    
    def sales_rep_performance(self):
        """
        Analyze performance by sales representative
        """
        if self.sales_data is None:
            return
        
        rep_performance = self.sales_data.groupby('Sales_Rep').agg({
            'Total_Amount': ['sum', 'count', 'mean'],
            'Quantity': 'sum',
            'Customer_ID': 'nunique'
        }).round(2)
        
        rep_performance.columns = ['Total_Sales', 'Orders', 'Avg_Order_Value', 'Units_Sold', 'Unique_Customers']
        
        # Sort by total sales
        rep_performance = rep_performance.sort_values('Total_Sales', ascending=False)
        
        print("\n👤 SALES REPRESENTATIVE PERFORMANCE")
        print("=" * 65)
        print(rep_performance.to_string())
        
        # Top performer
        top_rep = rep_performance.index[0]
        print(f"\n🏆 Top Performer: {top_rep} (${rep_performance.loc[top_rep, 'Total_Sales']:,.2f})")
        
        self.analysis_results['sales_reps'] = rep_performance
        return rep_performance
    
    def export_analysis_report(self, filename="sales_analysis_report.txt"):
        """
        Export comprehensive analysis report
        """
        if not self.analysis_results:
            print("❌ No analysis results to export. Run analyses first.")
            return None
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("COMPREHENSIVE SALES ANALYSIS REPORT\n")
                f.write("=" * 50 + "\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # Basic statistics
                if 'basic_stats' in self.analysis_results:
                    stats = self.analysis_results['basic_stats']
                    f.write("OVERVIEW\n")
                    f.write("-" * 20 + "\n")
                    f.write(f"Total Records: {stats['total_records']:,}\n")
                    f.write(f"Date Range: {stats['date_range']['start'].strftime('%Y-%m-%d')} to {stats['date_range']['end'].strftime('%Y-%m-%d')}\n")
                    f.write(f"Total Revenue: ${stats['total_revenue']:,.2f}\n")
                    f.write(f"Average Order Value: ${stats['average_order_value']:.2f}\n")
                    f.write(f"Total Customers: {stats['unique_customers']:,}\n\n")
                
                # Monthly analysis
                if 'monthly' in self.analysis_results:
                    f.write("MONTHLY PERFORMANCE\n")
                    f.write("-" * 25 + "\n")
                    f.write(self.analysis_results['monthly'].to_string())
                    f.write("\n\n")
                
                # Category analysis
                if 'categories' in self.analysis_results:
                    f.write("CATEGORY PERFORMANCE\n")
                    f.write("-" * 25 + "\n")
                    f.write(self.analysis_results['categories'].to_string())
                    f.write("\n\n")
                
                # Sales rep analysis
                if 'sales_reps' in self.analysis_results:
                    f.write("SALES REPRESENTATIVE PERFORMANCE\n")
                    f.write("-" * 35 + "\n")
                    f.write(self.analysis_results['sales_reps'].to_string())
                    f.write("\n\n")
            
            print(f"📄 Analysis report exported to {filename}")
            return filename
            
        except Exception as e:
            print(f"❌ Error exporting report: {e}")
            return None

# Create and demonstrate the sales analyzer
print("💼 Sales Data Analysis Demo")
print("=" * 30)

analyzer = SalesDataAnalyzer()
analyzer.basic_statistics()
analyzer.monthly_analysis()
analyzer.category_analysis()
analyzer.sales_rep_performance()
analyzer.export_analysis_report()
```

## 🏃‍♂️ Practice Exercises

### Exercise 1: Customer Data Processor
```python
def create_customer_processor():
    """
    Build a system to process customer data from CSV
    Include: data validation, duplicate detection, segmentation
    """
    # Your code here
    pass
```

### Exercise 2: Inventory Management
```python
def create_inventory_system():
    """
    Create inventory management from CSV data
    Include: stock levels, reorder points, supplier analysis
    """
    # Your code here
    pass
```

### Exercise 3: Financial Report Generator
```python
def create_financial_analyzer():
    """
    Analyze financial data from CSV files
    Include: profit/loss, trend analysis, forecasting
    """
    # Your code here
    pass
```

## 📝 Key Takeaways

1. **CSV is universal** - Master this format and you can work with data anywhere
2. **pandas is powerful** - Essential for serious data analysis
3. **Clean data first** - Garbage in, garbage out
4. **Validate everything** - Assume data has issues until proven otherwise
5. **Document your process** - Keep track of cleaning and analysis steps
6. **Export results** - Make your analysis shareable and actionable
7. **Think like an analyst** - Ask good questions of your data

## 🎯 Today's Project Preview

Today you built a **Comprehensive Sales Data Analysis System** that demonstrates professional CSV processing. It includes:
- Realistic sample data generation
- Data cleaning and validation
- Multiple analysis perspectives (time, category, performance)
- Professional reporting and export capabilities
- Error handling and data integrity checks
- Statistical insights and recommendations

## 🔗 Connection to Previous Days

### Building on Previous Skills
- **File Handling (Day 19)**: Reading and writing CSV files
- **Error Handling (Day 20)**: Robust data processing
- **Data Visualization (Day 25)**: Could add charts to analysis
- **Functions (Day 15-16)**: Organized analysis logic

### Looking Forward
CSV processing skills will enhance:
- **Final Projects**: Real-world data analysis capabilities
- **Web Development**: Data import/export features

CSV processing is a fundamental skill in the data-driven world. Master it, and you'll be able to extract insights from almost any dataset!