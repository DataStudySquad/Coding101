#!/usr/bin/env python3
"""
Day 26: Comprehensive Sales Data Analysis System
A professional CSV processing and data analysis toolkit

This program showcases:
- CSV reading and writing with Python's csv module
- Data cleaning and validation techniques
- Statistical analysis and business insights
- Professional reporting and export capabilities
- Error handling for real-world data issues
- Integration with pandas for advanced analysis

Think of this as your personal business intelligence platform!
"""

import csv
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
import json


class CSVProcessor:
    """
    Basic CSV processing using Python's built-in csv module
    Like having a careful data entry clerk who never makes mistakes
    """
    
    def __init__(self):
        """
        Initialize the CSV processor
        """
        self.data = []
        self.headers = []
        self.filename = None
        print("📄 CSV Processor initialized")
    
    def read_csv(self, filename, has_header=True):
        """
        Read CSV file using csv module
        """
        try:
            self.filename = filename
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                
                if has_header:
                    self.headers = next(csv_reader)
                
                self.data = []
                for row in csv_reader:
                    self.data.append(row)
                
                print(f"✅ Successfully read {len(self.data)} rows from {filename}")
                if self.headers:
                    print(f"📋 Headers: {self.headers}")
                
                return True
                
        except FileNotFoundError:
            print(f"❌ File {filename} not found")
            return False
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return False
    
    def read_as_dictionaries(self, filename):
        """
        Read CSV as list of dictionaries for easier access
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                
                self.headers = csv_reader.fieldnames
                self.data = list(csv_reader)
                
                print(f"✅ Successfully read {len(self.data)} records as dictionaries")
                print(f"📋 Fields: {self.headers}")
                
                return True
                
        except Exception as e:
            print(f"❌ Error reading CSV as dictionaries: {e}")
            return False
    
    def write_csv(self, filename, data=None, headers=None):
        """
        Write data to CSV file
        """
        try:
            data_to_write = data if data is not None else self.data
            headers_to_write = headers if headers is not None else self.headers
            
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                
                if headers_to_write:
                    csv_writer.writerow(headers_to_write)
                
                if isinstance(data_to_write[0], dict):
                    # Writing dictionary data
                    for row in data_to_write:
                        csv_writer.writerow([row.get(header, '') for header in headers_to_write])
                else:
                    # Writing list data
                    csv_writer.writerows(data_to_write)
            
            print(f"✅ Successfully wrote data to {filename}")
            return True
            
        except Exception as e:
            print(f"❌ Error writing CSV: {e}")
            return False
    
    def filter_data(self, filter_func):
        """
        Filter data based on a function
        """
        if not self.data:
            print("❌ No data to filter")
            return []
        
        if isinstance(self.data[0], dict):
            filtered = [row for row in self.data if filter_func(row)]
        else:
            filtered = [row for row in self.data if filter_func(row)]
        
        print(f"🔍 Filtered {len(self.data)} rows to {len(filtered)} rows")
        return filtered
    
    def get_column_stats(self, column_name):
        """
        Get basic statistics for a numeric column
        """
        if not self.data or not isinstance(self.data[0], dict):
            print("❌ Data must be loaded as dictionaries for column stats")
            return None
        
        try:
            values = []
            for row in self.data:
                if column_name in row and row[column_name]:
                    try:
                        values.append(float(row[column_name]))
                    except ValueError:
                        continue
            
            if not values:
                print(f"❌ No numeric values found in column {column_name}")
                return None
            
            stats = {
                'count': len(values),
                'sum': sum(values),
                'mean': sum(values) / len(values),
                'min': min(values),
                'max': max(values),
                'range': max(values) - min(values)
            }
            
            # Calculate median
            sorted_values = sorted(values)
            n = len(sorted_values)
            if n % 2 == 0:
                stats['median'] = (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
            else:
                stats['median'] = sorted_values[n//2]
            
            print(f"📊 Statistics for {column_name}:")
            for key, value in stats.items():
                if key in ['sum', 'mean', 'min', 'max', 'median', 'range']:
                    print(f"   {key.title()}: {value:.2f}")
                else:
                    print(f"   {key.title()}: {value}")
            
            return stats
            
        except Exception as e:
            print(f"❌ Error calculating stats for {column_name}: {e}")
            return None


class SalesDataAnalyzer:
    """
    Comprehensive sales data analysis system
    Like having a complete business intelligence team
    """
    
    def __init__(self, data_file=None):
        """
        Initialize the sales analyzer
        """
        self.sales_data = None
        self.analysis_results = {}
        self.csv_processor = CSVProcessor()
        
        if data_file and Path(data_file).exists():
            self.load_sales_data(data_file)
        else:
            print("📊 Generating sample sales data...")
            self.generate_sample_sales_data()
        
        print(f"💼 Sales Data Analyzer initialized")
    
    def generate_sample_sales_data(self):
        """
        Generate comprehensive sample sales data
        """
        np.random.seed(42)
        
        # Product catalog
        products_catalog = {
            'Electronics': {
                'Laptop': {'price_range': (800, 2000), 'margin': 0.15},
                'Smartphone': {'price_range': (300, 1200), 'margin': 0.20},
                'Tablet': {'price_range': (200, 800), 'margin': 0.18},
                'Headphones': {'price_range': (50, 400), 'margin': 0.25},
                'Smart Watch': {'price_range': (150, 600), 'margin': 0.22}
            },
            'Clothing': {
                'T-Shirt': {'price_range': (15, 60), 'margin': 0.50},
                'Jeans': {'price_range': (40, 150), 'margin': 0.45},
                'Jacket': {'price_range': (60, 300), 'margin': 0.40},
                'Sneakers': {'price_range': (50, 200), 'margin': 0.35},
                'Dress': {'price_range': (30, 250), 'margin': 0.48}
            },
            'Home & Garden': {
                'Coffee Maker': {'price_range': (30, 300), 'margin': 0.30},
                'Vacuum Cleaner': {'price_range': (80, 500), 'margin': 0.25},
                'Garden Tools': {'price_range': (20, 150), 'margin': 0.40},
                'Lamp': {'price_range': (25, 200), 'margin': 0.35},
                'Bed Sheets': {'price_range': (30, 150), 'margin': 0.45}
            },
            'Books': {
                'Fiction Novel': {'price_range': (10, 30), 'margin': 0.40},
                'Cookbook': {'price_range': (15, 50), 'margin': 0.35},
                'Textbook': {'price_range': (50, 300), 'margin': 0.20},
                'Children Book': {'price_range': (8, 25), 'margin': 0.45},
                'Biography': {'price_range': (12, 35), 'margin': 0.38}
            },
            'Sports': {
                'Football': {'price_range': (20, 80), 'margin': 0.30},
                'Basketball': {'price_range': (25, 100), 'margin': 0.28},
                'Yoga Mat': {'price_range': (20, 80), 'margin': 0.40},
                'Dumbbells': {'price_range': (30, 200), 'margin': 0.25},
                'Running Shoes': {'price_range': (60, 250), 'margin': 0.35}
            }
        }
        
        # Sales team and regions
        sales_team = [
            {'name': 'Alice Johnson', 'region': 'North', 'experience': 5},
            {'name': 'Bob Smith', 'region': 'South', 'experience': 8},
            {'name': 'Charlie Brown', 'region': 'East', 'experience': 3},
            {'name': 'Diana Prince', 'region': 'West', 'experience': 6},
            {'name': 'Eve Adams', 'region': 'North', 'experience': 4},
            {'name': 'Frank Wilson', 'region': 'South', 'experience': 7}
        ]
        
        # Generate 18 months of sales data
        start_date = datetime(2023, 6, 1)
        end_date = datetime(2024, 12, 31)
        
        sales_records = []
        customer_counter = 1000
        
        current_date = start_date
        while current_date <= end_date:
            # Seasonal and day-of-week variations
            day_of_week = current_date.weekday()
            month = current_date.month
            
            # Base sales per day
            base_sales = 8
            
            # Weekend boost
            if day_of_week >= 5:
                base_sales *= 1.4
            
            # Seasonal patterns
            if month in [11, 12]:  # Holiday season
                base_sales *= 1.8
            elif month in [6, 7, 8]:  # Summer
                base_sales *= 1.2
            elif month in [1, 2]:  # Post-holiday slump
                base_sales *= 0.7
            
            # Generate sales for the day
            num_sales = max(1, int(np.random.poisson(base_sales)))
            
            for _ in range(num_sales):
                # Select random category and product
                category = np.random.choice(list(products_catalog.keys()))
                product = np.random.choice(list(products_catalog[category].keys()))
                product_info = products_catalog[category][product]
                
                # Generate price within range
                min_price, max_price = product_info['price_range']
                price = round(np.random.uniform(min_price, max_price), 2)
                
                # Quantity (most orders are 1 item)
                quantity = np.random.choice([1, 1, 1, 1, 1, 2, 2, 3], p=[0.6, 0.15, 0.1, 0.05, 0.05, 0.03, 0.015, 0.005])
                
                # Calculate totals
                subtotal = round(price * quantity, 2)
                cost = round(subtotal * (1 - product_info['margin']), 2)
                profit = round(subtotal - cost, 2)
                
                # Select sales rep (with some regional bias)
                if np.random.random() < 0.7:  # 70% chance of regional preference
                    region_reps = [rep for rep in sales_team if rep['region'] == np.random.choice(['North', 'South', 'East', 'West'])]
                    if region_reps:
                        sales_rep_info = np.random.choice(region_reps)
                    else:
                        sales_rep_info = np.random.choice(sales_team)
                else:
                    sales_rep_info = np.random.choice(sales_team)
                
                # Generate customer ID (returning customers sometimes)
                if np.random.random() < 0.3:  # 30% chance of returning customer
                    customer_id = f"CUST_{np.random.randint(customer_counter-200, customer_counter)}"
                else:
                    customer_id = f"CUST_{customer_counter}"
                    customer_counter += 1
                
                # Payment method
                payment_method = np.random.choice(['Credit Card', 'Debit Card', 'Cash', 'PayPal'], 
                                                p=[0.45, 0.25, 0.15, 0.15])
                
                # Discount (occasionally)
                discount_percent = 0
                if np.random.random() < 0.15:  # 15% chance of discount
                    discount_percent = np.random.choice([5, 10, 15, 20], p=[0.4, 0.3, 0.2, 0.1])
                
                discount_amount = round(subtotal * discount_percent / 100, 2)
                final_total = round(subtotal - discount_amount, 2)
                
                sales_record = {
                    'Date': current_date.strftime('%Y-%m-%d'),
                    'Order_ID': f"ORD_{current_date.strftime('%Y%m%d')}_{len(sales_records)+1:04d}",
                    'Customer_ID': customer_id,
                    'Product': product,
                    'Category': category,
                    'Price': price,
                    'Quantity': quantity,
                    'Subtotal': subtotal,
                    'Discount_Percent': discount_percent,
                    'Discount_Amount': discount_amount,
                    'Total_Amount': final_total,
                    'Cost': cost,
                    'Profit': round(final_total - cost, 2),
                    'Sales_Rep': sales_rep_info['name'],
                    'Region': sales_rep_info['region'],
                    'Payment_Method': payment_method,
                    'Day_of_Week': current_date.strftime('%A'),
                    'Month': current_date.strftime('%B'),
                    'Quarter': f"Q{(current_date.month-1)//3 + 1}",
                    'Year': current_date.year
                }
                
                sales_records.append(sales_record)
            
            current_date += timedelta(days=1)
        
        # Save to CSV
        fieldnames = sales_records[0].keys()
        
        with open('comprehensive_sales_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sales_records)
        
        print(f"✅ Generated {len(sales_records)} sales records")
        print(f"📅 Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
        print(f"💾 Saved to 'comprehensive_sales_data.csv'")
        
        # Load the generated data
        self.load_sales_data('comprehensive_sales_data.csv')
        
        return sales_records
    
    def load_sales_data(self, filename):
        """
        Load sales data from CSV file
        """
        try:
            # Use pandas for more advanced operations
            self.sales_data = pd.read_csv(filename)
            
            # Convert date column
            self.sales_data['Date'] = pd.to_datetime(self.sales_data['Date'])
            
            # Also load with basic CSV processor
            self.csv_processor.read_as_dictionaries(filename)
            
            print(f"✅ Sales data loaded: {len(self.sales_data)} records")
            return True
            
        except Exception as e:
            print(f"❌ Error loading sales data: {e}")
            return False
    
    def data_quality_check(self):
        """
        Comprehensive data quality analysis
        """
        if self.sales_data is None:
            print("❌ No sales data loaded")
            return
        
        print("\n🔍 DATA QUALITY ASSESSMENT")
        print("=" * 40)
        
        # Basic info
        print(f"📊 Dataset shape: {self.sales_data.shape}")
        print(f"📅 Date range: {self.sales_data['Date'].min().strftime('%Y-%m-%d')} to {self.sales_data['Date'].max().strftime('%Y-%m-%d')}")
        
        # Missing values
        print(f"\n❓ Missing values:")
        missing = self.sales_data.isnull().sum()
        for col, count in missing.items():
            if count > 0:
                print(f"   {col}: {count} ({count/len(self.sales_data)*100:.1f}%)")
        
        if missing.sum() == 0:
            print("   ✅ No missing values found!")
        
        # Data types
        print(f"\n📋 Data types:")
        for col, dtype in self.sales_data.dtypes.items():
            print(f"   {col}: {dtype}")
        
        # Duplicates
        duplicates = self.sales_data.duplicated().sum()
        print(f"\n🔄 Duplicate rows: {duplicates}")
        if duplicates > 0:
            print("   ⚠️ Consider removing duplicates")
        
        # Value ranges for key numeric columns
        numeric_cols = ['Price', 'Quantity', 'Total_Amount', 'Profit']
        print(f"\n📈 Numeric ranges:")
        for col in numeric_cols:
            if col in self.sales_data.columns:
                col_data = self.sales_data[col]
                print(f"   {col}: ${col_data.min():.2f} - ${col_data.max():.2f} (avg: ${col_data.mean():.2f})")
        
        # Categorical value counts
        categorical_cols = ['Category', 'Region', 'Payment_Method']
        print(f"\n🏷️ Categorical distributions:")
        for col in categorical_cols:
            if col in self.sales_data.columns:
                unique_count = self.sales_data[col].nunique()
                print(f"   {col}: {unique_count} unique values")
                top_values = self.sales_data[col].value_counts().head(3)
                for value, count in top_values.items():
                    print(f"      {value}: {count} ({count/len(self.sales_data)*100:.1f}%)")
    
    def comprehensive_analysis(self):
        """
        Perform comprehensive business analysis
        """
        if self.sales_data is None:
            print("❌ No sales data loaded")
            return
        
        print("\n💼 COMPREHENSIVE SALES ANALYSIS")
        print("=" * 45)
        
        # Overall performance metrics
        total_revenue = self.sales_data['Total_Amount'].sum()
        total_profit = self.sales_data['Profit'].sum()
        total_orders = len(self.sales_data)
        avg_order_value = self.sales_data['Total_Amount'].mean()
        profit_margin = (total_profit / total_revenue) * 100
        
        print(f"📊 OVERALL PERFORMANCE")
        print(f"   💰 Total Revenue: ${total_revenue:,.2f}")
        print(f"   💵 Total Profit: ${total_profit:,.2f}")
        print(f"   📈 Profit Margin: {profit_margin:.1f}%")
        print(f"   🛒 Total Orders: {total_orders:,}")
        print(f"   💳 Average Order Value: ${avg_order_value:.2f}")
        print(f"   👥 Unique Customers: {self.sales_data['Customer_ID'].nunique():,}")
        
        # Monthly trends
        monthly_data = self.sales_data.groupby(self.sales_data['Date'].dt.to_period('M')).agg({
            'Total_Amount': 'sum',
            'Profit': 'sum',
            'Order_ID': 'count'
        }).round(2)
        
        monthly_data.columns = ['Revenue', 'Profit', 'Orders']
        
        # Find growth trends
        monthly_data['Revenue_Growth'] = monthly_data['Revenue'].pct_change() * 100
        monthly_data['Order_Growth'] = monthly_data['Orders'].pct_change() * 100
        
        print(f"\n📅 MONTHLY TRENDS (Last 6 months)")
        print(monthly_data.tail(6).to_string())
        
        # Category performance
        category_perf = self.sales_data.groupby('Category').agg({
            'Total_Amount': ['sum', 'count', 'mean'],
            'Profit': ['sum', 'mean'],
            'Quantity': 'sum'
        }).round(2)
        
        category_perf.columns = ['Revenue', 'Orders', 'Avg_Order_Value', 'Total_Profit', 'Avg_Profit', 'Units_Sold']
        category_perf['Profit_Margin'] = (category_perf['Total_Profit'] / category_perf['Revenue'] * 100).round(1)
        category_perf = category_perf.sort_values('Revenue', ascending=False)
        
        print(f"\n🏷️ CATEGORY PERFORMANCE")
        print(category_perf.to_string())
        
        # Regional analysis
        regional_perf = self.sales_data.groupby('Region').agg({
            'Total_Amount': ['sum', 'count'],
            'Profit': 'sum',
            'Customer_ID': 'nunique'
        }).round(2)
        
        regional_perf.columns = ['Revenue', 'Orders', 'Profit', 'Unique_Customers']
        regional_perf['Avg_Order_Value'] = (regional_perf['Revenue'] / regional_perf['Orders']).round(2)
        regional_perf = regional_perf.sort_values('Revenue', ascending=False)
        
        print(f"\n🌍 REGIONAL PERFORMANCE")
        print(regional_perf.to_string())
        
        # Sales representative performance
        rep_perf = self.sales_data.groupby('Sales_Rep').agg({
            'Total_Amount': ['sum', 'count'],
            'Profit': 'sum',
            'Customer_ID': 'nunique'
        }).round(2)
        
        rep_perf.columns = ['Revenue', 'Orders', 'Profit', 'Unique_Customers']
        rep_perf['Revenue_per_Order'] = (rep_perf['Revenue'] / rep_perf['Orders']).round(2)
        rep_perf = rep_perf.sort_values('Revenue', ascending=False)
        
        print(f"\n👤 SALES REPRESENTATIVE PERFORMANCE")
        print(rep_perf.to_string())
        
        # Store results for export
        self.analysis_results = {
            'overall_metrics': {
                'total_revenue': total_revenue,
                'total_profit': total_profit,
                'profit_margin': profit_margin,
                'total_orders': total_orders,
                'avg_order_value': avg_order_value,
                'unique_customers': self.sales_data['Customer_ID'].nunique()
            },
            'monthly_trends': monthly_data,
            'category_performance': category_perf,
            'regional_performance': regional_perf,
            'rep_performance': rep_perf
        }
        
        return self.analysis_results
    
    def identify_business_insights(self):
        """
        Generate actionable business insights
        """
        if self.sales_data is None:
            return []
        
        insights = []
        
        # Revenue trends
        monthly_revenue = self.sales_data.groupby(self.sales_data['Date'].dt.to_period('M'))['Total_Amount'].sum()
        recent_growth = monthly_revenue.pct_change().tail(3).mean() * 100
        
        if recent_growth > 5:
            insights.append(f"🚀 Strong growth trend: {recent_growth:.1f}% average monthly growth")
        elif recent_growth < -5:
            insights.append(f"📉 Concerning decline: {recent_growth:.1f}% average monthly decline")
        
        # Category insights
        category_revenue = self.sales_data.groupby('Category')['Total_Amount'].sum().sort_values(ascending=False)
        top_category = category_revenue.index[0]
        top_category_share = (category_revenue.iloc[0] / category_revenue.sum()) * 100
        
        insights.append(f"🏆 {top_category} dominates with {top_category_share:.1f}% of revenue")
        
        # Seasonal patterns
        monthly_avg = self.sales_data.groupby(self.sales_data['Date'].dt.month)['Total_Amount'].sum()
        peak_month = monthly_avg.idxmax()
        peak_month_name = datetime(2024, peak_month, 1).strftime('%B')
        
        insights.append(f"📅 {peak_month_name} is the peak sales month")
        
        # Profit margin analysis
        category_margins = self.sales_data.groupby('Category').apply(
            lambda x: (x['Profit'].sum() / x['Total_Amount'].sum()) * 100
        ).sort_values(ascending=False)
        
        best_margin_category = category_margins.index[0]
        best_margin_value = category_margins.iloc[0]
        
        insights.append(f"💰 {best_margin_category} has the best profit margin at {best_margin_value:.1f}%")
        
        # Customer insights
        repeat_customers = self.sales_data['Customer_ID'].value_counts()
        repeat_rate = (repeat_customers[repeat_customers > 1].count() / repeat_customers.count()) * 100
        
        insights.append(f"🔄 Customer retention rate: {repeat_rate:.1f}% make repeat purchases")
        
        # Regional insights
        regional_revenue = self.sales_data.groupby('Region')['Total_Amount'].sum()
        best_region = regional_revenue.idxmax()
        worst_region = regional_revenue.idxmin()
        performance_gap = ((regional_revenue.loc[best_region] / regional_revenue.loc[worst_region]) - 1) * 100
        
        insights.append(f"🌍 {best_region} outperforms {worst_region} by {performance_gap:.0f}%")
        
        print(f"\n💡 KEY BUSINESS INSIGHTS")
        print("=" * 30)
        for i, insight in enumerate(insights, 1):
            print(f"{i}. {insight}")
        
        return insights
    
    def export_comprehensive_report(self, filename="comprehensive_sales_report.txt"):
        """
        Export detailed analysis report
        """
        if not self.analysis_results:
            self.comprehensive_analysis()
        
        insights = self.identify_business_insights()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("COMPREHENSIVE SALES ANALYSIS REPORT\n")
                f.write("=" * 50 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Analysis Period: {self.sales_data['Date'].min().strftime('%Y-%m-%d')} to {self.sales_data['Date'].max().strftime('%Y-%m-%d')}\n\n")
                
                # Executive summary
                metrics = self.analysis_results['overall_metrics']
                f.write("EXECUTIVE SUMMARY\n")
                f.write("-" * 20 + "\n")
                f.write(f"Total Revenue: ${metrics['total_revenue']:,.2f}\n")
                f.write(f"Total Profit: ${metrics['total_profit']:,.2f}\n")
                f.write(f"Profit Margin: {metrics['profit_margin']:.1f}%\n")
                f.write(f"Total Orders: {metrics['total_orders']:,}\n")
                f.write(f"Average Order Value: ${metrics['avg_order_value']:.2f}\n")
                f.write(f"Unique Customers: {metrics['unique_customers']:,}\n\n")
                
                # Key insights
                f.write("KEY BUSINESS INSIGHTS\n")
                f.write("-" * 25 + "\n")
                for i, insight in enumerate(insights, 1):
                    f.write(f"{i}. {insight.replace('🚀', '').replace('📉', '').replace('🏆', '').replace('📅', '').replace('💰', '').replace('🔄', '').replace('🌍', '').strip()}\n")
                f.write("\n")
                
                # Detailed analysis
                f.write("DETAILED ANALYSIS\n")
                f.write("-" * 20 + "\n\n")
                
                f.write("Category Performance:\n")
                f.write(self.analysis_results['category_performance'].to_string())
                f.write("\n\n")
                
                f.write("Regional Performance:\n")
                f.write(self.analysis_results['regional_performance'].to_string())
                f.write("\n\n")
                
                f.write("Sales Representative Performance:\n")
                f.write(self.analysis_results['rep_performance'].to_string())
                f.write("\n\n")
                
                f.write("Monthly Trends:\n")
                f.write(self.analysis_results['monthly_trends'].to_string())
                f.write("\n")
            
            print(f"📄 Comprehensive report exported to {filename}")
            return filename
            
        except Exception as e:
            print(f"❌ Error exporting report: {e}")
            return None
    
    def export_to_multiple_formats(self, base_filename="sales_analysis"):
        """
        Export analysis results to multiple formats
        """
        try:
            # Export cleaned CSV data
            csv_file = f"{base_filename}_cleaned.csv"
            self.sales_data.to_csv(csv_file, index=False)
            print(f"📊 CSV data exported to {csv_file}")
            
            # Export summary statistics as JSON
            json_file = f"{base_filename}_summary.json"
            
            # Prepare JSON-serializable data
            json_data = {
                'generation_timestamp': datetime.now().isoformat(),
                'data_period': {
                    'start': self.sales_data['Date'].min().isoformat(),
                    'end': self.sales_data['Date'].max().isoformat()
                },
                'overall_metrics': self.analysis_results['overall_metrics'],
                'insights': self.identify_business_insights()
            }
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            print(f"📋 JSON summary exported to {json_file}")
            
            # Export comprehensive text report
            txt_file = f"{base_filename}_report.txt"
            self.export_comprehensive_report(txt_file)
            
            return {
                'csv': csv_file,
                'json': json_file, 
                'report': txt_file
            }
            
        except Exception as e:
            print(f"❌ Error in multi-format export: {e}")
            return None


def main():
    """
    Main function demonstrating the comprehensive CSV processing system
    """
    print("📊" * 25)
    print("    COMPREHENSIVE CSV PROCESSING & SALES ANALYSIS")
    print("📊" * 25)
    print("Professional data processing and business intelligence toolkit")
    print()
    
    # Initialize the analyzer
    analyzer = SalesDataAnalyzer()
    
    while True:
        print("\n" + "=" * 60)
        print("💼 CSV PROCESSING & SALES ANALYSIS MENU")
        print("=" * 60)
        print("1. Data quality assessment")
        print("2. Comprehensive sales analysis") 
        print("3. Generate business insights")
        print("4. Export analysis reports")
        print("5. Basic CSV operations demo")
        print("6. Load different data file")
        print("7. Export to multiple formats")
        print("8. Complete analysis workflow")
        print("9. Exit")
        
        try:
            choice = input("\nSelect option (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Thank you for using the CSV Processing System!")
            print("📊 Remember: Good data analysis drives great business decisions!")
            break
        
        if choice == "1":
            print("\n🔍 Running Data Quality Assessment...")
            analyzer.data_quality_check()
        
        elif choice == "2":
            print("\n💼 Running Comprehensive Sales Analysis...")
            analyzer.comprehensive_analysis()
        
        elif choice == "3":
            print("\n💡 Generating Business Insights...")
            insights = analyzer.identify_business_insights()
            
            print(f"\n🎯 Actionable Recommendations:")
            if 'growth' in str(insights).lower():
                print("   • Continue current growth strategies")
            if 'margin' in str(insights).lower():
                print("   • Focus on high-margin categories")
            if 'region' in str(insights).lower():
                print("   • Investigate regional performance differences")
            print("   • Implement customer retention programs")
            print("   • Optimize seasonal inventory planning")
        
        elif choice == "4":
            print("\n📄 Exporting Analysis Reports...")
            
            report_types = input("Export options:\n1. Comprehensive report\n2. Quick summary\n3. Both\nChoice (1-3): ").strip()
            
            if report_types in ["1", "3"]:
                report_file = analyzer.export_comprehensive_report()
                if report_file:
                    print(f"✅ Comprehensive report: {report_file}")
            
            if report_types in ["2", "3"]:
                # Generate quick summary
                summary_file = "sales_summary.txt"
                if analyzer.analysis_results:
                    metrics = analyzer.analysis_results['overall_metrics']
                    with open(summary_file, 'w') as f:
                        f.write("SALES SUMMARY REPORT\n")
                        f.write("=" * 25 + "\n")
                        f.write(f"Revenue: ${metrics['total_revenue']:,.2f}\n")
                        f.write(f"Profit: ${metrics['total_profit']:,.2f}\n")
                        f.write(f"Orders: {metrics['total_orders']:,}\n")
                        f.write(f"Customers: {metrics['unique_customers']:,}\n")
                    print(f"✅ Quick summary: {summary_file}")
        
        elif choice == "5":
            print("\n📄 Basic CSV Operations Demo...")
            
            # Demonstrate basic CSV processor
            csv_demo = CSVProcessor()
            
            print("🔧 Reading CSV with basic processor...")
            if csv_demo.read_as_dictionaries('comprehensive_sales_data.csv'):
                print(f"   📊 Loaded {len(csv_demo.data)} records")
                
                # Show sample operations
                print("\n📈 Sample column statistics:")
                csv_demo.get_column_stats('Total_Amount')
                
                print("\n🔍 Filter example: Orders over $100")
                high_value_orders = csv_demo.filter_data(lambda row: float(row.get('Total_Amount', 0)) > 100)
                print(f"   Found {len(high_value_orders)} high-value orders")
                
                # Export filtered data
                if high_value_orders:
                    csv_demo.write_csv('high_value_orders.csv', high_value_orders, csv_demo.headers)
        
        elif choice == "6":
            print("\n📂 Load Different Data File")
            filename = input("Enter CSV filename: ").strip()
            if filename:
                new_analyzer = SalesDataAnalyzer(filename)
                if new_analyzer.sales_data is not None:
                    analyzer = new_analyzer
                    print("✅ New data loaded successfully!")
            else:
                print("❌ Please enter a valid filename")
        
        elif choice == "7":
            print("\n💾 Exporting to Multiple Formats...")
            
            if analyzer.analysis_results:
                exports = analyzer.export_to_multiple_formats()
                if exports:
                    print("✅ Multi-format export complete!")
                    print(f"   📊 CSV: {exports['csv']}")
                    print(f"   📋 JSON: {exports['json']}")  
                    print(f"   📄 Report: {exports['report']}")
            else:
                print("⚠️ Run analysis first to generate export data")
        
        elif choice == "8":
            print("\n🚀 COMPLETE ANALYSIS WORKFLOW")
            print("=" * 35)
            
            print("Step 1/5: Data Quality Assessment...")
            analyzer.data_quality_check()
            
            print("\nStep 2/5: Comprehensive Analysis...")
            analyzer.comprehensive_analysis()
            
            print("\nStep 3/5: Business Insights...")
            analyzer.identify_business_insights()
            
            print("\nStep 4/5: Export Reports...")
            analyzer.export_comprehensive_report("complete_workflow_report.txt")
            
            print("\nStep 5/5: Multi-format Export...")
            exports = analyzer.export_to_multiple_formats("complete_workflow")
            
            print(f"\n🎉 COMPLETE WORKFLOW FINISHED!")
            print(f"📊 Analyzed {len(analyzer.sales_data)} sales records")
            print(f"💰 Total revenue: ${analyzer.analysis_results['overall_metrics']['total_revenue']:,.2f}")
            print(f"📈 Profit margin: {analyzer.analysis_results['overall_metrics']['profit_margin']:.1f}%")
            print(f"📁 All reports saved with 'complete_workflow' prefix")
        
        elif choice == "9":
            print("\n💼 Thank you for using the CSV Processing & Sales Analysis System!")
            print("\n🎯 Key capabilities demonstrated:")
            print("   • Professional CSV data processing")
            print("   • Comprehensive business analysis")
            print("   • Data quality assessment")
            print("   • Multi-format export capabilities")
            print("   • Actionable business insights")
            print("\n📊 Remember: Great analysis starts with clean data and ends with actionable insights!")
            break
        
        else:
            print("❌ Invalid option. Please select 1-9.")


if __name__ == "__main__":
    main()