# Day 25: Data Visualization - Turning Numbers into Stories

Welcome to Day 25! Today we're diving into data visualization - the art of turning boring numbers into compelling visual stories. Think of it as becoming a visual storyteller who can make any dataset speak to your audience clearly and beautifully.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Understand the importance of data visualization in communication
- Use matplotlib to create various types of charts and graphs
- Design effective visualizations that tell clear stories
- Create interactive and customizable plots
- Build a grade analysis system with comprehensive charts
- Apply color theory and design principles to data visualization

## 📊 Why Data Visualization Matters

### The Power of Visual Communication

Imagine trying to understand these two presentations of the same data:

**Text Version:**
"Sales in Q1 were $125,000, Q2 was $180,000, Q3 was $145,000, and Q4 was $220,000. Product A sold 500 units in January, 750 in February, 600 in March..."

**Visual Version:**
📈 A beautiful chart showing the clear upward trend with seasonal dips and peaks, instantly revealing the story.

Our brains process visual information 60,000 times faster than text! Data visualization is like having a universal translator that turns complex data into instant insights.

### Real-World Applications

```python
visualization_uses = {
    "Business": "Sales dashboards, performance metrics, market analysis",
    "Science": "Research findings, experimental results, trend analysis", 
    "Education": "Grade distributions, student performance, learning outcomes",
    "Healthcare": "Patient data, treatment outcomes, epidemic tracking",
    "Finance": "Stock prices, portfolio performance, risk analysis",
    "Marketing": "Campaign effectiveness, customer behavior, A/B testing",
    "Sports": "Player statistics, game analysis, performance tracking",
    "Personal": "Fitness tracking, budget analysis, habit monitoring"
}
```

## 📈 Getting Started with matplotlib

### Installation and Setup

```bash
pip install matplotlib numpy seaborn
```

### Your First Plot

```python
import matplotlib.pyplot as plt
import numpy as np

# Create simple data
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 7]

# Create a basic line plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)
plt.title('My First Plot', fontsize=16, fontweight='bold')
plt.xlabel('X Values', fontsize=12)
plt.ylabel('Y Values', fontsize=12)
plt.grid(True, alpha=0.3)

# Show the plot
plt.show()

# Save the plot
plt.savefig('my_first_plot.png', dpi=300, bbox_inches='tight')
print("📊 Plot saved as 'my_first_plot.png'")
```

### Understanding Plot Anatomy

```python
import matplotlib.pyplot as plt

# Think of a plot like a well-organized presentation
def demonstrate_plot_anatomy():
    """
    Show all the components that make up a professional plot
    Like learning the parts of a well-designed poster
    """
    
    # Create sample data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [15000, 18000, 22000, 17000, 25000, 28000]
    
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Main plot
    bars = ax.bar(months, sales, color='steelblue', alpha=0.7, edgecolor='navy')
    
    # Title and labels
    ax.set_title('Monthly Sales Performance', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Month', fontsize=12, fontweight='semibold')
    ax.set_ylabel('Sales ($)', fontsize=12, fontweight='semibold')
    
    # Add value labels on bars
    for bar, value in zip(bars, sales):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500, 
                f'${value:,}', ha='center', va='bottom', fontweight='bold')
    
    # Formatting
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_facecolor('whitesmoke')
    
    # Tight layout
    plt.tight_layout()
    
    return fig

# Create and display the demonstration
demo_fig = demonstrate_plot_anatomy()
plt.show()
```

## 📊 Essential Chart Types

### Line Charts - Showing Trends Over Time

```python
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

def create_trend_analysis():
    """
    Create line charts to show trends over time
    Like drawing a path that shows where you've been and where you're going
    """
    
    # Generate sample time series data
    dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(365)]
    
    # Simulate different trend patterns
    np.random.seed(42)
    
    # Website visitors (with weekly pattern)
    base_visitors = 1000
    weekly_pattern = np.sin(np.arange(365) * 2 * np.pi / 7) * 200
    growth_trend = np.arange(365) * 2
    noise = np.random.normal(0, 50, 365)
    visitors = base_visitors + weekly_pattern + growth_trend + noise
    
    # Sales (with seasonal pattern)
    base_sales = 5000
    seasonal_pattern = np.sin(np.arange(365) * 2 * np.pi / 365) * 1500
    sales_growth = np.arange(365) * 1.5
    sales_noise = np.random.normal(0, 200, 365)
    sales = base_sales + seasonal_pattern + sales_growth + sales_noise
    
    # Create the plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Visitors plot
    ax1.plot(dates, visitors, color='dodgerblue', linewidth=1.5, alpha=0.8)
    ax1.set_title('Daily Website Visitors', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Visitors', fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Add trend line
    z = np.polyfit(range(365), visitors, 1)
    trend_line = np.poly1d(z)
    ax1.plot(dates, trend_line(range(365)), '--', color='red', 
             linewidth=2, label=f'Trend: +{z[0]:.1f} visitors/day')
    ax1.legend()
    
    # Sales plot
    ax2.plot(dates, sales, color='forestgreen', linewidth=1.5, alpha=0.8)
    ax2.set_title('Daily Sales Revenue', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Sales ($)', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    # Format y-axis as currency
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # Add seasonal trend
    z_sales = np.polyfit(range(365), sales, 1)
    sales_trend = np.poly1d(z_sales)
    ax2.plot(dates, sales_trend(range(365)), '--', color='red', 
             linewidth=2, label=f'Trend: +${z_sales[0]:.0f}/day')
    ax2.legend()
    
    plt.tight_layout()
    return fig

# Create the trend analysis
trend_fig = create_trend_analysis()
plt.show()
```

### Bar Charts - Comparing Categories

```python
import matplotlib.pyplot as plt
import numpy as np

def create_comparison_charts():
    """
    Create various bar charts for comparing different categories
    Like organizing items on shelves for easy comparison
    """
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Simple vertical bar chart
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    sales_q1 = [23000, 17000, 35000, 29000, 15000]
    
    bars1 = ax1.bar(products, sales_q1, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    ax1.set_title('Q1 Sales by Product', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Sales ($)', fontsize=12)
    ax1.tick_params(axis='x', rotation=45)
    
    # Add value labels
    for bar, value in zip(bars1, sales_q1):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
                f'${value:,}', ha='center', va='bottom', fontweight='bold')
    
    # 2. Horizontal bar chart
    departments = ['Marketing', 'Engineering', 'Sales', 'HR', 'Finance']
    employees = [25, 45, 30, 12, 18]
    
    bars2 = ax2.barh(departments, employees, color='steelblue', alpha=0.7)
    ax2.set_title('Employees by Department', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Number of Employees', fontsize=12)
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars2, employees)):
        ax2.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                str(value), ha='left', va='center', fontweight='bold')
    
    # 3. Grouped bar chart
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    product_a = [23000, 25000, 22000, 30000]
    product_b = [17000, 19000, 24000, 26000]
    product_c = [35000, 32000, 28000, 31000]
    
    x_pos = np.arange(len(quarters))
    width = 0.25
    
    ax3.bar(x_pos - width, product_a, width, label='Product A', color='#FF6B6B', alpha=0.8)
    ax3.bar(x_pos, product_b, width, label='Product B', color='#4ECDC4', alpha=0.8)
    ax3.bar(x_pos + width, product_c, width, label='Product C', color='#45B7D1', alpha=0.8)
    
    ax3.set_title('Quarterly Sales by Product', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Quarter', fontsize=12)
    ax3.set_ylabel('Sales ($)', fontsize=12)
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(quarters)
    ax3.legend()
    ax3.grid(True, axis='y', alpha=0.3)
    
    # 4. Stacked bar chart
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
    segment_1 = [20, 35, 30, 35]
    segment_2 = [25, 25, 15, 30]
    segment_3 = [15, 20, 25, 20]
    
    ax4.bar(categories, segment_1, label='Segment 1', color='#96CEB4')
    ax4.bar(categories, segment_2, bottom=segment_1, label='Segment 2', color='#FFEAA7')
    ax4.bar(categories, segment_3, bottom=np.array(segment_1) + np.array(segment_2), 
            label='Segment 3', color='#DDA0DD')
    
    ax4.set_title('Market Share by Category', fontsize=14, fontweight='bold')
    ax4.set_ylabel('Percentage (%)', fontsize=12)
    ax4.legend()
    ax4.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig

# Create comparison charts
comparison_fig = create_comparison_charts()
plt.show()
```

### Pie Charts - Showing Proportions

```python
import matplotlib.pyplot as plt

def create_pie_charts():
    """
    Create pie charts to show proportions and percentages
    Like cutting a pizza to show how much each person gets
    """
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Basic pie chart
    budget_categories = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Savings', 'Other']
    budget_amounts = [1200, 400, 300, 200, 500, 150]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
    
    wedges1, texts1, autotexts1 = ax1.pie(budget_amounts, labels=budget_categories, colors=colors,
                                          autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
    ax1.set_title('Monthly Budget Distribution', fontsize=14, fontweight='bold')
    
    # Make percentage text bold
    for autotext in autotexts1:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    # 2. Exploded pie chart (emphasizing largest segment)
    market_share = [35, 25, 20, 15, 5]
    companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Others']
    explode = (0.1, 0, 0, 0, 0)  # Explode the largest segment
    
    wedges2, texts2, autotexts2 = ax2.pie(market_share, labels=companies, explode=explode,
                                          colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'],
                                          autopct='%1.1f%%', startangle=45, shadow=True)
    ax2.set_title('Market Share Analysis', fontsize=14, fontweight='bold')
    
    # 3. Donut chart
    skills = ['Python', 'JavaScript', 'SQL', 'Excel', 'R']
    proficiency = [85, 70, 60, 90, 45]
    
    # Create donut by adding a white circle in the center
    wedges3, texts3, autotexts3 = ax3.pie(proficiency, labels=skills, 
                                          colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'],
                                          autopct='%1.0f%%', startangle=90, pctdistance=0.85)
    
    # Add center circle for donut effect
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    ax3.add_artist(centre_circle)
    ax3.set_title('Skill Proficiency Levels', fontsize=14, fontweight='bold')
    
    # 4. Nested pie chart (two levels)
    # Outer ring - categories
    outer_labels = ['Technology', 'Healthcare', 'Finance', 'Education']
    outer_sizes = [40, 25, 20, 15]
    outer_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    # Inner ring - subcategories
    inner_labels = ['Software', 'Hardware', 'Hospitals', 'Pharma', 'Banking', 'Insurance', 'K-12', 'Higher Ed']
    inner_sizes = [25, 15, 15, 10, 12, 8, 8, 7]
    inner_colors = ['#FFB3BA', '#FF6B6B', '#B3E5D1', '#4ECDC4', '#B3D7FF', '#45B7D1', '#C9E4CA', '#96CEB4']
    
    # Create nested pies
    wedges4_outer = ax4.pie(outer_sizes, labels=outer_labels, colors=outer_colors,
                           radius=1, startangle=90, labeldistance=1.1)
    wedges4_inner = ax4.pie(inner_sizes, labels=inner_labels, colors=inner_colors,
                           radius=0.7, startangle=90, labeldistance=0.7, textprops={'fontsize': 8})
    
    ax4.set_title('Industry Breakdown (Nested View)', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig

# Create pie charts
pie_fig = create_pie_charts()
plt.show()
```

### Scatter Plots - Exploring Relationships

```python
import matplotlib.pyplot as plt
import numpy as np

def create_scatter_plots():
    """
    Create scatter plots to explore relationships between variables
    Like plotting stars in the sky to find constellations of meaning
    """
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Generate sample data
    np.random.seed(42)
    
    # 1. Basic scatter plot - Study hours vs Test scores
    study_hours = np.random.uniform(1, 10, 50)
    test_scores = 60 + study_hours * 8 + np.random.normal(0, 10, 50)
    test_scores = np.clip(test_scores, 0, 100)  # Keep scores between 0-100
    
    scatter1 = ax1.scatter(study_hours, test_scores, c='dodgerblue', alpha=0.6, s=60, edgecolors='navy')
    ax1.set_xlabel('Study Hours', fontsize=12)
    ax1.set_ylabel('Test Score', fontsize=12)
    ax1.set_title('Study Hours vs Test Scores', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Add trend line
    z = np.polyfit(study_hours, test_scores, 1)
    p = np.poly1d(z)
    ax1.plot(study_hours, p(study_hours), "r--", alpha=0.8, linewidth=2)
    
    # Add correlation coefficient
    correlation = np.corrcoef(study_hours, test_scores)[0, 1]
    ax1.text(0.05, 0.95, f'Correlation: {correlation:.3f}', transform=ax1.transAxes,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
             fontsize=10, fontweight='bold')
    
    # 2. Color-coded scatter plot - Height, Weight, Gender
    n_points = 100
    
    # Generate data for males and females
    male_height = np.random.normal(175, 8, n_points//2)  # cm
    male_weight = 2.3 * male_height - 300 + np.random.normal(0, 10, n_points//2)  # kg
    
    female_height = np.random.normal(165, 7, n_points//2)  # cm
    female_weight = 2.3 * female_height - 280 + np.random.normal(0, 8, n_points//2)  # kg
    
    ax2.scatter(male_height, male_weight, c='steelblue', alpha=0.6, s=60, 
               label='Male', edgecolors='navy')
    ax2.scatter(female_height, female_weight, c='coral', alpha=0.6, s=60, 
               label='Female', edgecolors='darkred')
    
    ax2.set_xlabel('Height (cm)', fontsize=12)
    ax2.set_ylabel('Weight (kg)', fontsize=12)
    ax2.set_title('Height vs Weight by Gender', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Bubble chart - Sales performance
    sales_reps = 20
    experience_years = np.random.uniform(1, 15, sales_reps)
    sales_amount = 50000 + experience_years * 8000 + np.random.normal(0, 20000, sales_reps)
    customer_satisfaction = np.random.uniform(3.5, 5.0, sales_reps)
    
    # Bubble size represents customer satisfaction
    bubble_sizes = (customer_satisfaction - 3.5) * 400 + 50
    
    scatter3 = ax3.scatter(experience_years, sales_amount, s=bubble_sizes, 
                          c=customer_satisfaction, alpha=0.6, cmap='RdYlGn', 
                          edgecolors='black', linewidth=1)
    
    ax3.set_xlabel('Years of Experience', fontsize=12)
    ax3.set_ylabel('Annual Sales ($)', fontsize=12)
    ax3.set_title('Sales Performance Analysis\n(Bubble size = Customer Satisfaction)', 
                  fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # Add colorbar
    cbar = plt.colorbar(scatter3, ax=ax3)
    cbar.set_label('Customer Satisfaction Rating', fontsize=10)
    
    # Format y-axis as currency
    ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # 4. Multi-variable scatter plot
    departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Finance']
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    
    for i, (dept, color) in enumerate(zip(departments, colors)):
        n_employees = np.random.randint(15, 40)
        salaries = np.random.normal(60000 + i*10000, 15000, n_employees)
        satisfaction = np.random.normal(3.8 - i*0.1, 0.5, n_employees)
        satisfaction = np.clip(satisfaction, 1, 5)
        
        ax4.scatter(salaries, satisfaction, c=color, alpha=0.6, s=60, 
                   label=dept, edgecolors='black', linewidth=0.5)
    
    ax4.set_xlabel('Annual Salary ($)', fontsize=12)
    ax4.set_ylabel('Job Satisfaction (1-5)', fontsize=12)
    ax4.set_title('Salary vs Job Satisfaction by Department', fontsize=14, fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    plt.tight_layout()
    return fig

# Create scatter plots
scatter_fig = create_scatter_plots()
plt.show()
```

## 🎓 Building a Grade Analysis System

### Comprehensive Student Performance Visualizer

```python
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime
import seaborn as sns

class GradeAnalyzer:
    """
    A comprehensive grade analysis and visualization system
    Like having a personal academic performance consultant
    """
    
    def __init__(self):
        """
        Initialize the grade analyzer with sample student data
        """
        self.students_data = self.generate_sample_data()
        print(f"📊 Grade Analyzer initialized with {len(self.students_data)} students")
    
    def generate_sample_data(self):
        """
        Generate realistic sample student data
        """
        np.random.seed(42)
        
        # Student names
        first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 
                      'Iris', 'Jack', 'Kate', 'Liam', 'Maya', 'Noah', 'Olivia', 'Peter',
                      'Quinn', 'Ruby', 'Sam', 'Tina', 'Uma', 'Victor', 'Wendy', 'Xavier', 'Yara', 'Zoe']
        last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
                     'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Garcia', 'Martinez']
        
        students = []
        
        for i in range(50):  # 50 students
            first_name = np.random.choice(first_names)
            last_name = np.random.choice(last_names)
            
            # Generate grades with some realistic patterns
            base_performance = np.random.normal(78, 12)  # Overall student ability
            
            # Subject-specific performance (some students better at certain subjects)
            subjects = {
                'Math': max(0, min(100, base_performance + np.random.normal(0, 8))),
                'Science': max(0, min(100, base_performance + np.random.normal(0, 8))),
                'English': max(0, min(100, base_performance + np.random.normal(0, 8))),
                'History': max(0, min(100, base_performance + np.random.normal(0, 8))),
                'Art': max(0, min(100, base_performance + np.random.normal(0, 10)))
            }
            
            # Assignment grades throughout the semester
            assignments = []
            for week in range(12):  # 12 weeks
                # Performance might improve or decline over time
                time_factor = np.random.normal(0, 3)
                for assignment in range(2):  # 2 assignments per week
                    grade = max(0, min(100, base_performance + time_factor + np.random.normal(0, 10)))
                    assignments.append({
                        'week': week + 1,
                        'assignment': assignment + 1,
                        'grade': round(grade, 1)
                    })
            
            student = {
                'id': i + 1,
                'name': f"{first_name} {last_name}",
                'grade_level': np.random.choice(['9th', '10th', '11th', '12th']),
                'subjects': subjects,
                'assignments': assignments,
                'attendance': max(75, min(100, np.random.normal(92, 8))),
                'participation': max(1, min(5, np.random.normal(3.5, 1)))
            }
            
            students.append(student)
        
        return students
    
    def create_grade_distribution(self):
        """
        Create histograms showing grade distributions
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Grade Distribution Analysis', fontsize=20, fontweight='bold', y=0.98)
        
        subjects = ['Math', 'Science', 'English', 'History', 'Art']
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
        
        # Subject grade distributions
        for i, (subject, color) in enumerate(zip(subjects, colors)):
            ax = axes[0, i] if i < 3 else axes[1, i-3]
            
            grades = [student['subjects'][subject] for student in self.students_data]
            
            # Create histogram
            n, bins, patches = ax.hist(grades, bins=10, alpha=0.7, color=color, 
                                      edgecolor='black', linewidth=1)
            
            # Color bars based on grade ranges
            for j, patch in enumerate(patches):
                bin_center = (bins[j] + bins[j+1]) / 2
                if bin_center >= 90:
                    patch.set_color('#2ECC71')  # Green for A
                elif bin_center >= 80:
                    patch.set_color('#F39C12')  # Orange for B
                elif bin_center >= 70:
                    patch.set_color('#E74C3C')  # Red for C
                else:
                    patch.set_color('#8E44AD')  # Purple for D/F
            
            ax.set_title(f'{subject} Grade Distribution', fontsize=14, fontweight='bold')
            ax.set_xlabel('Grade', fontsize=12)
            ax.set_ylabel('Number of Students', fontsize=12)
            ax.grid(True, alpha=0.3)
            
            # Add statistics
            mean_grade = np.mean(grades)
            std_grade = np.std(grades)
            ax.axvline(mean_grade, color='red', linestyle='--', linewidth=2, 
                      label=f'Mean: {mean_grade:.1f}')
            ax.legend()
        
        # Overall GPA distribution
        ax_overall = axes[1, 2]
        overall_grades = []
        for student in self.students_data:
            gpa = np.mean(list(student['subjects'].values()))
            overall_grades.append(gpa)
        
        n, bins, patches = ax_overall.hist(overall_grades, bins=12, alpha=0.7, 
                                         color='steelblue', edgecolor='black', linewidth=1)
        
        # Color bars based on GPA ranges
        for j, patch in enumerate(patches):
            bin_center = (bins[j] + bins[j+1]) / 2
            if bin_center >= 90:
                patch.set_color('#2ECC71')  # Green for A
            elif bin_center >= 80:
                patch.set_color('#F39C12')  # Orange for B
            elif bin_center >= 70:
                patch.set_color('#E74C3C')  # Red for C
            else:
                patch.set_color('#8E44AD')  # Purple for D/F
        
        ax_overall.set_title('Overall GPA Distribution', fontsize=14, fontweight='bold')
        ax_overall.set_xlabel('GPA', fontsize=12)
        ax_overall.set_ylabel('Number of Students', fontsize=12)
        ax_overall.grid(True, alpha=0.3)
        
        mean_gpa = np.mean(overall_grades)
        ax_overall.axvline(mean_gpa, color='red', linestyle='--', linewidth=2, 
                          label=f'Mean GPA: {mean_gpa:.1f}')
        ax_overall.legend()
        
        plt.tight_layout()
        return fig
    
    def create_performance_trends(self):
        """
        Create line charts showing performance trends over time
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Calculate weekly averages
        weeks = range(1, 13)
        weekly_averages = []
        
        for week in weeks:
            week_grades = []
            for student in self.students_data:
                week_assignments = [a['grade'] for a in student['assignments'] if a['week'] == week]
                if week_assignments:
                    week_grades.extend(week_assignments)
            weekly_averages.append(np.mean(week_grades) if week_grades else 0)
        
        # Class average trend
        ax1.plot(weeks, weekly_averages, marker='o', linewidth=3, markersize=8, 
                color='steelblue', label='Class Average')
        
        # Add trend lines for top and bottom performers
        top_students = sorted(self.students_data, 
                             key=lambda x: np.mean(list(x['subjects'].values())), reverse=True)[:5]
        bottom_students = sorted(self.students_data, 
                                key=lambda x: np.mean(list(x['subjects'].values())))[:5]
        
        # Top performers trend
        top_weekly = []
        for week in weeks:
            week_grades = []
            for student in top_students:
                week_assignments = [a['grade'] for a in student['assignments'] if a['week'] == week]
                week_grades.extend(week_assignments)
            top_weekly.append(np.mean(week_grades) if week_grades else 0)
        
        # Bottom performers trend
        bottom_weekly = []
        for week in weeks:
            week_grades = []
            for student in bottom_students:
                week_assignments = [a['grade'] for a in student['assignments'] if a['week'] == week]
                week_grades.extend(week_assignments)
            bottom_weekly.append(np.mean(week_grades) if week_grades else 0)
        
        ax1.plot(weeks, top_weekly, marker='s', linewidth=2, markersize=6, 
                color='green', alpha=0.7, label='Top 5 Students')
        ax1.plot(weeks, bottom_weekly, marker='^', linewidth=2, markersize=6, 
                color='red', alpha=0.7, label='Bottom 5 Students')
        
        ax1.set_title('Academic Performance Trends Over Semester', fontsize=16, fontweight='bold')
        ax1.set_xlabel('Week', fontsize=12)
        ax1.set_ylabel('Average Grade', fontsize=12)
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(60, 95)
        
        # Grade level comparison
        grade_levels = ['9th', '10th', '11th', '12th']
        grade_level_averages = []
        
        for grade_level in grade_levels:
            students_in_grade = [s for s in self.students_data if s['grade_level'] == grade_level]
            if students_in_grade:
                avg = np.mean([np.mean(list(s['subjects'].values())) for s in students_in_grade])
                grade_level_averages.append(avg)
            else:
                grade_level_averages.append(0)
        
        bars = ax2.bar(grade_levels, grade_level_averages, 
                      color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'], alpha=0.8)
        
        # Add value labels on bars
        for bar, value in zip(bars, grade_level_averages):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    f'{value:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=12)
        
        ax2.set_title('Average GPA by Grade Level', fontsize=16, fontweight='bold')
        ax2.set_xlabel('Grade Level', fontsize=12)
        ax2.set_ylabel('Average GPA', fontsize=12)
        ax2.grid(True, axis='y', alpha=0.3)
        ax2.set_ylim(70, 85)
        
        plt.tight_layout()
        return fig
    
    def create_subject_correlation(self):
        """
        Create correlation heatmap between subjects
        """
        # Prepare data for correlation
        subjects = ['Math', 'Science', 'English', 'History', 'Art']
        
        # Create matrix of grades
        grade_matrix = []
        for subject in subjects:
            subject_grades = [student['subjects'][subject] for student in self.students_data]
            grade_matrix.append(subject_grades)
        
        grade_matrix = np.array(grade_matrix)
        
        # Calculate correlation matrix
        correlation_matrix = np.corrcoef(grade_matrix)
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create heatmap with custom colormap
        im = ax.imshow(correlation_matrix, cmap='RdYlBu_r', aspect='auto', vmin=-1, vmax=1)
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax, shrink=0.8)
        cbar.set_label('Correlation Coefficient', fontsize=12, fontweight='bold')
        
        # Set ticks and labels
        ax.set_xticks(range(len(subjects)))
        ax.set_yticks(range(len(subjects)))
        ax.set_xticklabels(subjects, fontsize=12)
        ax.set_yticklabels(subjects, fontsize=12)
        
        # Add correlation values to cells
        for i in range(len(subjects)):
            for j in range(len(subjects)):
                text = ax.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                              ha="center", va="center", fontweight='bold',
                              color='white' if abs(correlation_matrix[i, j]) > 0.5 else 'black')
        
        ax.set_title('Subject Grade Correlations\n(How closely related are subject performances?)', 
                    fontsize=16, fontweight='bold', pad=20)
        
        plt.tight_layout()
        return fig
    
    def create_performance_dashboard(self):
        """
        Create a comprehensive performance dashboard
        """
        fig = plt.figure(figsize=(20, 16))
        
        # Create a complex layout
        gs = fig.add_gridspec(4, 4, hspace=0.3, wspace=0.3)
        
        # 1. Overall class statistics (top left)
        ax1 = fig.add_subplot(gs[0, :2])
        
        # Calculate key statistics
        all_grades = []
        for student in self.students_data:
            all_grades.extend(list(student['subjects'].values()))
        
        stats = {
            'Class Average': np.mean(all_grades),
            'Median Grade': np.median(all_grades),
            'Standard Deviation': np.std(all_grades),
            'A Students (90+)': len([g for g in all_grades if g >= 90]) / len(all_grades) * 100,
            'At Risk (<70)': len([g for g in all_grades if g < 70]) / len(all_grades) * 100
        }
        
        # Create text summary
        summary_text = f"""
CLASS PERFORMANCE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Class Average: {stats['Class Average']:.1f}
📈 Median Grade: {stats['Median Grade']:.1f}
📏 Standard Deviation: {stats['Standard Deviation']:.1f}
🌟 A Students (90+): {stats['A Students (90+)']:.1f}%
⚠️ At Risk (<70): {stats['At Risk (<70)']:.1f}%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Students: {len(self.students_data)}
Subjects Analyzed: 5
        """
        
        ax1.text(0.05, 0.95, summary_text, transform=ax1.transAxes, fontsize=12,
                verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.axis('off')
        ax1.set_title('📊 CLASS OVERVIEW', fontsize=16, fontweight='bold')
        
        # 2. Grade distribution pie chart (top right)
        ax2 = fig.add_subplot(gs[0, 2:])
        
        grade_ranges = ['A (90-100)', 'B (80-89)', 'C (70-79)', 'D/F (<70)']
        grade_counts = [
            len([g for g in all_grades if g >= 90]),
            len([g for g in all_grades if 80 <= g < 90]),
            len([g for g in all_grades if 70 <= g < 80]),
            len([g for g in all_grades if g < 70])
        ]
        
        colors = ['#2ECC71', '#F39C12', '#E74C3C', '#8E44AD']
        wedges, texts, autotexts = ax2.pie(grade_counts, labels=grade_ranges, colors=colors,
                                          autopct='%1.1f%%', startangle=90)
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax2.set_title('Grade Distribution', fontsize=16, fontweight='bold')
        
        # 3. Subject performance bar chart (middle left)
        ax3 = fig.add_subplot(gs[1, :2])
        
        subjects = ['Math', 'Science', 'English', 'History', 'Art']
        subject_averages = []
        
        for subject in subjects:
            avg = np.mean([student['subjects'][subject] for student in self.students_data])
            subject_averages.append(avg)
        
        bars = ax3.bar(subjects, subject_averages, 
                      color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
        
        # Add value labels
        for bar, value in zip(bars, subject_averages):
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    f'{value:.1f}', ha='center', va='bottom', fontweight='bold')
        
        ax3.set_title('Average Grades by Subject', fontsize=14, fontweight='bold')
        ax3.set_ylabel('Average Grade')
        ax3.grid(True, axis='y', alpha=0.3)
        ax3.set_ylim(70, 85)
        
        # 4. Top and bottom performers (middle right)
        ax4 = fig.add_subplot(gs[1, 2:])
        
        # Sort students by overall performance
        sorted_students = sorted(self.students_data, 
                               key=lambda x: np.mean(list(x['subjects'].values())), reverse=True)
        
        top_5 = sorted_students[:5]
        bottom_5 = sorted_students[-5:]
        
        performers_text = "🏆 TOP 5 PERFORMERS\n"
        performers_text += "━━━━━━━━━━━━━━━━━━━━\n"
        for i, student in enumerate(top_5, 1):
            gpa = np.mean(list(student['subjects'].values()))
            performers_text += f"{i}. {student['name']}: {gpa:.1f}\n"
        
        performers_text += "\n⚠️ STUDENTS NEEDING SUPPORT\n"
        performers_text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        for i, student in enumerate(bottom_5, 1):
            gpa = np.mean(list(student['subjects'].values()))
            performers_text += f"{i}. {student['name']}: {gpa:.1f}\n"
        
        ax4.text(0.05, 0.95, performers_text, transform=ax4.transAxes, fontsize=10,
                verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)
        ax4.axis('off')
        ax4.set_title('🎯 PERFORMANCE HIGHLIGHTS', fontsize=14, fontweight='bold')
        
        # 5. Attendance vs Performance scatter (bottom left)
        ax5 = fig.add_subplot(gs[2:, :2])
        
        attendance_data = [student['attendance'] for student in self.students_data]
        gpa_data = [np.mean(list(student['subjects'].values())) for student in self.students_data]
        
        scatter = ax5.scatter(attendance_data, gpa_data, alpha=0.6, s=60, 
                             c=gpa_data, cmap='RdYlGn', edgecolors='black')
        
        ax5.set_xlabel('Attendance (%)')
        ax5.set_ylabel('GPA')
        ax5.set_title('Attendance vs Academic Performance', fontsize=14, fontweight='bold')
        ax5.grid(True, alpha=0.3)
        
        # Add trend line
        z = np.polyfit(attendance_data, gpa_data, 1)
        p = np.poly1d(z)
        ax5.plot(sorted(attendance_data), p(sorted(attendance_data)), "r--", alpha=0.8, linewidth=2)
        
        # Add correlation
        correlation = np.corrcoef(attendance_data, gpa_data)[0, 1]
        ax5.text(0.05, 0.95, f'Correlation: {correlation:.3f}', transform=ax5.transAxes,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
                fontweight='bold')
        
        plt.colorbar(scatter, ax=ax5, shrink=0.8, label='GPA')
        
        # 6. Weekly performance trend (bottom right)
        ax6 = fig.add_subplot(gs[2:, 2:])
        
        weeks = range(1, 13)
        weekly_averages = []
        
        for week in weeks:
            week_grades = []
            for student in self.students_data:
                week_assignments = [a['grade'] for a in student['assignments'] if a['week'] == week]
                week_grades.extend(week_assignments)
            weekly_averages.append(np.mean(week_grades) if week_grades else 0)
        
        ax6.plot(weeks, weekly_averages, marker='o', linewidth=3, markersize=8, 
                color='steelblue')
        
        # Add moving average
        if len(weekly_averages) >= 3:
            moving_avg = np.convolve(weekly_averages, np.ones(3)/3, mode='valid')
            ax6.plot(weeks[1:-1], moving_avg, '--', color='red', linewidth=2, 
                    label='3-week moving average')
            ax6.legend()
        
        ax6.set_xlabel('Week')
        ax6.set_ylabel('Average Grade')
        ax6.set_title('Weekly Performance Trend', fontsize=14, fontweight='bold')
        ax6.grid(True, alpha=0.3)
        
        # Main title
        fig.suptitle('🎓 COMPREHENSIVE ACADEMIC PERFORMANCE DASHBOARD', 
                    fontsize=24, fontweight='bold', y=0.98)
        
        return fig

# Create the grade analyzer instance
analyzer = GradeAnalyzer()

# Generate all visualizations
print("📊 Creating grade distribution analysis...")
dist_fig = analyzer.create_grade_distribution()
plt.show()

print("📈 Creating performance trends...")
trend_fig = analyzer.create_performance_trends()
plt.show()

print("🔗 Creating subject correlation analysis...")
corr_fig = analyzer.create_subject_correlation()
plt.show()

print("📋 Creating comprehensive dashboard...")
dashboard_fig = analyzer.create_performance_dashboard()
plt.show()
```

## 🎨 Design Principles for Effective Visualizations

### Color Theory and Accessibility

```python
import matplotlib.pyplot as plt
import numpy as np

def demonstrate_color_principles():
    """
    Show good and bad examples of color usage in data visualization
    """
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Color Theory in Data Visualization', fontsize=18, fontweight='bold')
    
    # Sample data
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    values = [23, 45, 56, 78, 32]
    
    # 1. BAD: Too many bright colors (overwhelming)
    ax1 = axes[0, 0]
    bad_colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']
    ax1.bar(categories, values, color=bad_colors)
    ax1.set_title('❌ BAD: Too Many Bright Colors', fontsize=14, color='red')
    ax1.tick_params(axis='x', rotation=45)
    
    # 2. GOOD: Harmonious color palette
    ax2 = axes[0, 1]
    good_colors = ['#2C3E50', '#34495E', '#5D6D7E', '#85929E', '#AEB6BF']
    ax2.bar(categories, values, color=good_colors)
    ax2.set_title('✅ GOOD: Harmonious Color Palette', fontsize=14, color='green')
    ax2.tick_params(axis='x', rotation=45)
    
    # 3. BAD: Colors don't match data meaning
    ax3 = axes[1, 0]
    # Using red for positive values (confusing)
    bars3 = ax3.bar(categories, values, color='red')
    ax3.set_title('❌ BAD: Red for Positive Values', fontsize=14, color='red')
    ax3.tick_params(axis='x', rotation=45)
    
    # 4. GOOD: Colors match data meaning
    ax4 = axes[1, 1]
    # Green gradient for positive values
    colors_gradient = plt.cm.Greens(np.linspace(0.4, 0.8, len(categories)))
    bars4 = ax4.bar(categories, values, color=colors_gradient)
    ax4.set_title('✅ GOOD: Meaningful Color Mapping', fontsize=14, color='green')
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    return fig

# Color accessibility example
def create_colorblind_friendly_chart():
    """
    Create a chart that works for colorblind users
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    product_a = [20, 25, 30, 35, 40, 45]
    product_b = [15, 20, 25, 30, 35, 40]
    product_c = [10, 15, 20, 25, 30, 35]
    
    # Standard colors (problematic for colorblind users)
    ax1.plot(months, product_a, 'r-o', linewidth=3, markersize=8, label='Product A')
    ax1.plot(months, product_b, 'g-s', linewidth=3, markersize=8, label='Product B')
    ax1.plot(months, product_c, 'b-^', linewidth=3, markersize=8, label='Product C')
    ax1.set_title('Standard Colors (Not Colorblind-Friendly)', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Colorblind-friendly version
    # Use different line styles and markers, not just colors
    ax2.plot(months, product_a, color='#1f77b4', linestyle='-', marker='o', 
             linewidth=3, markersize=8, label='Product A')
    ax2.plot(months, product_b, color='#ff7f0e', linestyle='--', marker='s', 
             linewidth=3, markersize=8, label='Product B')
    ax2.plot(months, product_c, color='#2ca02c', linestyle=':', marker='^', 
             linewidth=3, markersize=8, label='Product C')
    
    ax2.set_title('✅ Colorblind-Friendly Version', fontsize=14)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

# Create examples
color_fig = demonstrate_color_principles()
plt.show()

colorblind_fig = create_colorblind_friendly_chart()
plt.show()
```

## 🏃‍♂️ Practice Exercises

### Exercise 1: Personal Fitness Dashboard
Create a comprehensive fitness tracking visualization:

```python
def create_fitness_dashboard():
    """
    Create a personal fitness tracking dashboard
    Include: weight progress, workout frequency, calories burned, goals vs actual
    """
    # Your code here
    pass
```

### Exercise 2: Stock Market Analysis
Build a financial data visualization system:

```python
def create_stock_analysis():
    """
    Create stock market analysis charts
    Include: price trends, volume analysis, moving averages, comparison charts
    """
    # Your code here
    pass
```

### Exercise 3: Social Media Analytics
Design social media performance charts:

```python
def create_social_media_dashboard():
    """
    Create social media analytics dashboard
    Include: engagement rates, follower growth, post performance, best posting times
    """
    # Your code here
    pass
```

## 📝 Key Takeaways

1. **Choose the right chart type** - Line for trends, bars for comparisons, pie for proportions
2. **Keep it simple** - Don't overwhelm with too much information
3. **Use meaningful colors** - Green for good, red for bad, consistent throughout
4. **Label everything clearly** - Titles, axes, legends should be self-explanatory
5. **Consider your audience** - Technical vs. general audience requires different approaches
6. **Tell a story** - Every chart should have a clear message or insight
7. **Make it accessible** - Consider colorblind users and screen readers

## 🎯 Today's Project Preview

Today you built a **Comprehensive Grade Analysis System** that demonstrates professional data visualization. It includes:
- Multiple chart types for different insights
- Professional styling and color schemes
- Interactive analysis capabilities
- Statistical summaries and correlations
- Dashboard-style comprehensive views
- Educational insights and recommendations

The goal was to create a tool that transforms raw data into actionable insights through beautiful, clear visualizations!

## 🔗 Connection to Previous Days

### Building on Previous Skills
- **Functions (Day 15-16)**: All visualization logic is organized in functions
- **Data Structures (Week 2)**: Using lists and dictionaries to organize data
- **File Handling (Day 19)**: Loading and saving visualization data
- **Error Handling (Day 20)**: Robust plotting with error handling

### Looking Forward
Data visualization skills will enhance:
- **CSV Processing (Day 26)**: Visualizing tabular data
- **Final Projects**: Professional presentation of results

Data visualization is the bridge between raw data and human understanding. Master this skill, and you can make any dataset tell its story clearly and compellingly!