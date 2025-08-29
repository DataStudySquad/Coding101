#!/usr/bin/env python3
"""
Day 25: Comprehensive Grade Analysis and Visualization System
A professional data visualization tool for academic performance analysis

This program showcases:
- Multiple chart types (bar, line, pie, scatter, histogram, heatmap)
- Professional styling and color schemes
- Statistical analysis and correlations
- Interactive dashboard creation
- Data export and reporting capabilities
- Educational insights and recommendations

Think of this as your personal academic performance consultant!
"""

import matplotlib.pyplot as plt
import numpy as np
import json
import csv
from datetime import datetime, timedelta
from pathlib import Path
import seaborn as sns


class GradeAnalyzer:
    """
    A comprehensive grade analysis and visualization system
    Like having a team of data analysts and educational consultants
    """
    
    def __init__(self, data_file=None):
        """
        Initialize the grade analyzer
        """
        self.students_data = []
        self.analysis_results = {}
        
        if data_file and Path(data_file).exists():
            self.load_data(data_file)
        else:
            self.students_data = self.generate_sample_data()
        
        print(f"📊 Grade Analyzer initialized with {len(self.students_data)} students")
        
        # Set up matplotlib styling
        self.setup_plot_style()
    
    def setup_plot_style(self):
        """
        Configure matplotlib for professional-looking plots
        """
        plt.style.use('default')  # Reset to default first
        
        # Set global parameters
        plt.rcParams.update({
            'figure.figsize': (12, 8),
            'figure.dpi': 100,
            'savefig.dpi': 300,
            'font.size': 10,
            'axes.labelsize': 12,
            'axes.titlesize': 14,
            'xtick.labelsize': 10,
            'ytick.labelsize': 10,
            'legend.fontsize': 10,
            'axes.grid': True,
            'grid.alpha': 0.3,
            'axes.spines.top': False,
            'axes.spines.right': False,
            'figure.autolayout': True
        })
    
    def generate_sample_data(self):
        """
        Generate realistic sample student data for demonstration
        """
        np.random.seed(42)  # For reproducible results
        
        # Realistic student names
        first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 
                      'Iris', 'Jack', 'Kate', 'Liam', 'Maya', 'Noah', 'Olivia', 'Peter',
                      'Quinn', 'Ruby', 'Sam', 'Tina', 'Uma', 'Victor', 'Wendy', 'Xavier', 'Yara', 'Zoe']
        last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
                     'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Garcia', 'Martinez']
        
        students = []
        
        for i in range(60):  # 60 students for better statistical analysis
            # Generate unique name combinations
            first_name = np.random.choice(first_names)
            last_name = np.random.choice(last_names)
            
            # Student's base ability (affects all subjects)
            base_ability = np.random.normal(77, 15)  # Mean 77, SD 15
            base_ability = max(50, min(95, base_ability))  # Constrain to realistic range
            
            # Generate subject grades with realistic patterns
            subjects = {}
            subject_list = ['Mathematics', 'Science', 'English', 'History', 'Art']
            
            for subject in subject_list:
                # Some students are better at certain subjects
                if subject in ['Mathematics', 'Science']:
                    # STEM correlation
                    stem_modifier = np.random.normal(0, 5)
                    grade = base_ability + stem_modifier + np.random.normal(0, 8)
                elif subject in ['English', 'History']:
                    # Humanities correlation
                    humanities_modifier = np.random.normal(0, 5)
                    grade = base_ability + humanities_modifier + np.random.normal(0, 8)
                else:
                    # Art is more variable
                    grade = base_ability + np.random.normal(0, 12)
                
                # Ensure grades are within realistic bounds
                subjects[subject] = max(40, min(100, round(grade, 1)))
            
            # Generate semester-long assignment data
            assignments = []
            current_performance = base_ability
            
            for week in range(1, 17):  # 16-week semester
                # Performance can drift over time (improvement/decline)
                performance_drift = np.random.normal(0, 2)
                current_performance += performance_drift * 0.1
                
                # 2-3 assignments per week
                num_assignments = np.random.randint(2, 4)
                
                for assignment_num in range(num_assignments):
                    # Assignment difficulty varies
                    difficulty_factor = np.random.normal(0, 5)
                    assignment_grade = current_performance + difficulty_factor + np.random.normal(0, 8)
                    assignment_grade = max(0, min(100, round(assignment_grade, 1)))
                    
                    assignments.append({
                        'week': week,
                        'assignment': assignment_num + 1,
                        'grade': assignment_grade,
                        'type': np.random.choice(['Quiz', 'Homework', 'Test', 'Project'], 
                                                p=[0.3, 0.4, 0.2, 0.1])
                    })
            
            # Additional student attributes
            student = {
                'id': i + 1,
                'name': f"{first_name} {last_name}",
                'grade_level': np.random.choice(['9th', '10th', '11th', '12th']),
                'subjects': subjects,
                'assignments': assignments,
                'attendance': max(75, min(100, np.random.normal(90, 8))),
                'participation': max(1, min(5, np.random.normal(3.5, 1.0))),
                'study_hours_per_week': max(2, min(25, np.random.normal(8, 4))),
                'extracurricular_hours': max(0, min(15, np.random.normal(3, 3))),
                'parent_education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 
                                                   p=[0.2, 0.4, 0.3, 0.1])
            }
            
            students.append(student)
        
        return students
    
    def calculate_statistics(self):
        """
        Calculate comprehensive statistics about the class
        """
        if not self.students_data:
            return {}
        
        # Collect all grades
        all_grades = []
        subject_grades = {subject: [] for subject in ['Mathematics', 'Science', 'English', 'History', 'Art']}
        
        for student in self.students_data:
            student_grades = list(student['subjects'].values())
            all_grades.extend(student_grades)
            
            for subject, grade in student['subjects'].items():
                subject_grades[subject].append(grade)
        
        # Calculate overall statistics
        stats = {
            'total_students': len(self.students_data),
            'overall_mean': np.mean(all_grades),
            'overall_median': np.median(all_grades),
            'overall_std': np.std(all_grades),
            'grade_distribution': {
                'A (90+)': len([g for g in all_grades if g >= 90]) / len(all_grades) * 100,
                'B (80-89)': len([g for g in all_grades if 80 <= g < 90]) / len(all_grades) * 100,
                'C (70-79)': len([g for g in all_grades if 70 <= g < 80]) / len(all_grades) * 100,
                'D/F (<70)': len([g for g in all_grades if g < 70]) / len(all_grades) * 100
            },
            'subject_stats': {}
        }
        
        # Subject-specific statistics
        for subject, grades in subject_grades.items():
            stats['subject_stats'][subject] = {
                'mean': np.mean(grades),
                'median': np.median(grades),
                'std': np.std(grades),
                'min': np.min(grades),
                'max': np.max(grades)
            }
        
        # Student-level statistics
        student_gpas = []
        attendance_rates = []
        study_hours = []
        
        for student in self.students_data:
            gpa = np.mean(list(student['subjects'].values()))
            student_gpas.append(gpa)
            attendance_rates.append(student['attendance'])
            study_hours.append(student['study_hours_per_week'])
        
        stats['student_performance'] = {
            'mean_gpa': np.mean(student_gpas),
            'median_gpa': np.median(student_gpas),
            'gpa_std': np.std(student_gpas),
            'mean_attendance': np.mean(attendance_rates),
            'mean_study_hours': np.mean(study_hours)
        }
        
        # Correlations
        stats['correlations'] = {
            'attendance_gpa': np.corrcoef(attendance_rates, student_gpas)[0, 1],
            'study_hours_gpa': np.corrcoef(study_hours, student_gpas)[0, 1]
        }
        
        self.analysis_results = stats
        return stats
    
    def create_grade_distribution_charts(self):
        """
        Create comprehensive grade distribution visualizations
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('📊 Grade Distribution Analysis', fontsize=20, fontweight='bold', y=0.98)
        
        subjects = ['Mathematics', 'Science', 'English', 'History', 'Art']
        colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
        
        # Individual subject distributions
        for i, (subject, color) in enumerate(zip(subjects, colors)):
            if i < 3:
                ax = axes[0, i]
            else:
                ax = axes[1, i-3]
            
            grades = [student['subjects'][subject] for student in self.students_data]
            
            # Create histogram with grade boundaries
            bins = [0, 60, 70, 80, 90, 100]
            n, bin_edges, patches = ax.hist(grades, bins=bins, alpha=0.7, edgecolor='black', linewidth=1)
            
            # Color bars based on grade ranges
            grade_colors = ['#8e44ad', '#e74c3c', '#f39c12', '#2ecc71']  # F, D/C, B, A
            for patch, grade_color in zip(patches, grade_colors):
                patch.set_facecolor(grade_color)
            
            # Add statistics
            mean_grade = np.mean(grades)
            median_grade = np.median(grades)
            
            ax.axvline(mean_grade, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_grade:.1f}')
            ax.axvline(median_grade, color='blue', linestyle='--', linewidth=2, label=f'Median: {median_grade:.1f}')
            
            ax.set_title(f'{subject}\nDistribution', fontsize=12, fontweight='bold')
            ax.set_xlabel('Grade')
            ax.set_ylabel('Number of Students')
            ax.legend(fontsize=9)
            ax.grid(True, alpha=0.3)
        
        # Overall GPA distribution
        ax_gpa = axes[1, 2]
        gpas = [np.mean(list(student['subjects'].values())) for student in self.students_data]
        
        n, bin_edges, patches = ax_gpa.hist(gpas, bins=15, alpha=0.7, color='steelblue', 
                                           edgecolor='black', linewidth=1)
        
        # Color bars based on GPA ranges
        for i, patch in enumerate(patches):
            bin_center = (bin_edges[i] + bin_edges[i+1]) / 2
            if bin_center >= 90:
                patch.set_facecolor('#2ecc71')  # A
            elif bin_center >= 80:
                patch.set_facecolor('#f39c12')  # B  
            elif bin_center >= 70:
                patch.set_facecolor('#e74c3c')  # C
            else:
                patch.set_facecolor('#8e44ad')  # D/F
        
        mean_gpa = np.mean(gpas)
        median_gpa = np.median(gpas)
        
        ax_gpa.axvline(mean_gpa, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_gpa:.1f}')
        ax_gpa.axvline(median_gpa, color='blue', linestyle='--', linewidth=2, label=f'Median: {median_gpa:.1f}')
        
        ax_gpa.set_title('Overall GPA\nDistribution', fontsize=12, fontweight='bold')
        ax_gpa.set_xlabel('GPA')
        ax_gpa.set_ylabel('Number of Students')
        ax_gpa.legend(fontsize=9)
        
        plt.tight_layout()
        return fig
    
    def create_performance_trends(self):
        """
        Create performance trend analysis over the semester
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('📈 Performance Trends Analysis', fontsize=18, fontweight='bold')
        
        # 1. Weekly class average trend
        weeks = range(1, 17)
        weekly_averages = []
        weekly_std = []
        
        for week in weeks:
            week_grades = []
            for student in self.students_data:
                week_assignments = [a['grade'] for a in student['assignments'] if a['week'] == week]
                if week_assignments:
                    week_grades.extend(week_assignments)
            
            if week_grades:
                weekly_averages.append(np.mean(week_grades))
                weekly_std.append(np.std(week_grades))
            else:
                weekly_averages.append(0)
                weekly_std.append(0)
        
        ax1.plot(weeks, weekly_averages, marker='o', linewidth=2.5, markersize=6, 
                color='steelblue', label='Class Average')
        
        # Add confidence band
        weekly_averages = np.array(weekly_averages)
        weekly_std = np.array(weekly_std)
        ax1.fill_between(weeks, weekly_averages - weekly_std/2, weekly_averages + weekly_std/2, 
                        alpha=0.2, color='steelblue')
        
        # Add trend line
        z = np.polyfit(weeks, weekly_averages, 1)
        trend = np.poly1d(z)
        ax1.plot(weeks, trend(weeks), '--', color='red', linewidth=2, 
                label=f'Trend: {"+" if z[0] > 0 else ""}{z[0]:.2f}/week')
        
        ax1.set_title('Weekly Performance Trend')
        ax1.set_xlabel('Week')
        ax1.set_ylabel('Average Grade')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Performance by grade level
        grade_levels = ['9th', '10th', '11th', '12th']
        grade_level_data = []
        
        for level in grade_levels:
            students_in_level = [s for s in self.students_data if s['grade_level'] == level]
            if students_in_level:
                level_gpas = [np.mean(list(s['subjects'].values())) for s in students_in_level]
                grade_level_data.append(level_gpas)
            else:
                grade_level_data.append([])
        
        # Create box plot
        bp = ax2.boxplot(grade_level_data, labels=grade_levels, patch_artist=True)
        
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        ax2.set_title('GPA Distribution by Grade Level')
        ax2.set_xlabel('Grade Level')
        ax2.set_ylabel('GPA')
        ax2.grid(True, alpha=0.3)
        
        # 3. Subject performance comparison
        subjects = ['Mathematics', 'Science', 'English', 'History', 'Art']
        subject_means = []
        subject_stds = []
        
        for subject in subjects:
            grades = [student['subjects'][subject] for student in self.students_data]
            subject_means.append(np.mean(grades))
            subject_stds.append(np.std(grades))
        
        bars = ax3.bar(subjects, subject_means, yerr=subject_stds, 
                      color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6'],
                      alpha=0.7, capsize=5)
        
        # Add value labels
        for bar, mean_val in zip(bars, subject_means):
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    f'{mean_val:.1f}', ha='center', va='bottom', fontweight='bold')
        
        ax3.set_title('Average Performance by Subject')
        ax3.set_ylabel('Average Grade')
        ax3.tick_params(axis='x', rotation=45)
        ax3.grid(True, axis='y', alpha=0.3)
        
        # 4. Performance vs Study Hours scatter plot
        study_hours = [s['study_hours_per_week'] for s in self.students_data]
        gpas = [np.mean(list(s['subjects'].values())) for s in self.students_data]
        attendance = [s['attendance'] for s in self.students_data]
        
        # Color points by attendance rate
        scatter = ax4.scatter(study_hours, gpas, c=attendance, cmap='RdYlGn', 
                            alpha=0.6, s=60, edgecolors='black', linewidth=0.5)
        
        # Add trend line
        z = np.polyfit(study_hours, gpas, 1)
        trend = np.poly1d(z)
        ax4.plot(sorted(study_hours), trend(sorted(study_hours)), '--', 
                color='red', linewidth=2)
        
        # Add correlation
        correlation = np.corrcoef(study_hours, gpas)[0, 1]
        ax4.text(0.05, 0.95, f'Correlation: {correlation:.3f}', transform=ax4.transAxes,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8),
                fontweight='bold')
        
        ax4.set_title('Study Hours vs GPA')
        ax4.set_xlabel('Study Hours per Week')
        ax4.set_ylabel('GPA')
        
        # Add colorbar
        cbar = plt.colorbar(scatter, ax=ax4)
        cbar.set_label('Attendance %')
        
        plt.tight_layout()
        return fig
    
    def create_subject_correlation_heatmap(self):
        """
        Create a correlation heatmap between subjects
        """
        subjects = ['Mathematics', 'Science', 'English', 'History', 'Art']
        
        # Create correlation matrix
        grade_data = []
        for subject in subjects:
            subject_grades = [student['subjects'][subject] for student in self.students_data]
            grade_data.append(subject_grades)
        
        correlation_matrix = np.corrcoef(grade_data)
        
        # Create the heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create heatmap
        im = ax.imshow(correlation_matrix, cmap='RdYlBu_r', vmin=-1, vmax=1)
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax, shrink=0.8)
        cbar.set_label('Correlation Coefficient', fontsize=12, fontweight='bold')
        
        # Set labels
        ax.set_xticks(range(len(subjects)))
        ax.set_yticks(range(len(subjects)))
        ax.set_xticklabels(subjects, rotation=45, ha='right')
        ax.set_yticklabels(subjects)
        
        # Add correlation values to cells
        for i in range(len(subjects)):
            for j in range(len(subjects)):
                text = ax.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                              ha="center", va="center", fontweight='bold', fontsize=12,
                              color='white' if abs(correlation_matrix[i, j]) > 0.6 else 'black')
        
        ax.set_title('Subject Grade Correlations\n(How related are performances across subjects?)', 
                    fontsize=16, fontweight='bold', pad=20)
        
        plt.tight_layout()
        return fig
    
    def create_comprehensive_dashboard(self):
        """
        Create a comprehensive performance dashboard
        """
        fig = plt.figure(figsize=(20, 16))
        gs = fig.add_gridspec(4, 4, hspace=0.35, wspace=0.3)
        
        # Calculate statistics if not done
        if not self.analysis_results:
            self.calculate_statistics()
        
        stats = self.analysis_results
        
        # 1. Class Overview (top-left)
        ax1 = fig.add_subplot(gs[0, :2])
        
        overview_text = f"""
📊 CLASS PERFORMANCE OVERVIEW
{'='*45}
👥 Total Students: {stats['total_students']}
📈 Class Average: {stats['overall_mean']:.1f}
📊 Median Grade: {stats['overall_median']:.1f}
📏 Standard Deviation: {stats['overall_std']:.1f}
📋 Mean GPA: {stats['student_performance']['mean_gpa']:.1f}
📅 Average Attendance: {stats['student_performance']['mean_attendance']:.1f}%

🎯 GRADE DISTRIBUTION:
🟢 A Students (90+): {stats['grade_distribution']['A (90+)']:.1f}%
🟡 B Students (80-89): {stats['grade_distribution']['B (80-89)']:.1f}%
🟠 C Students (70-79): {stats['grade_distribution']['C (70-79)']:.1f}%
🔴 At Risk (<70): {stats['grade_distribution']['D/F (<70)']:.1f}%

🔗 KEY CORRELATIONS:
📚 Study Hours ↔ GPA: {stats['correlations']['study_hours_gpa']:.3f}
🏫 Attendance ↔ GPA: {stats['correlations']['attendance_gpa']:.3f}
        """
        
        ax1.text(0.05, 0.95, overview_text, transform=ax1.transAxes, fontsize=11,
                verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.axis('off')
        
        # 2. Grade Distribution Pie Chart (top-right)
        ax2 = fig.add_subplot(gs[0, 2:])
        
        grade_labels = ['A (90+)', 'B (80-89)', 'C (70-79)', 'D/F (<70)']
        grade_sizes = [stats['grade_distribution'][label] for label in grade_labels]
        colors = ['#2ecc71', '#f39c12', '#e74c3c', '#8e44ad']
        
        wedges, texts, autotexts = ax2.pie(grade_sizes, labels=grade_labels, colors=colors,
                                          autopct='%1.1f%%', startangle=90, textprops={'fontweight': 'bold'})
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(11)
        
        ax2.set_title('Overall Grade Distribution', fontsize=14, fontweight='bold')
        
        # 3. Subject Performance Bar Chart (second row, left)
        ax3 = fig.add_subplot(gs[1, :2])
        
        subjects = ['Mathematics', 'Science', 'English', 'History', 'Art']
        subject_means = [stats['subject_stats'][subject]['mean'] for subject in subjects]
        subject_stds = [stats['subject_stats'][subject]['std'] for subject in subjects]
        
        colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
        bars = ax3.bar(subjects, subject_means, yerr=subject_stds, 
                      color=colors, alpha=0.7, capsize=5)
        
        # Add value labels
        for bar, mean_val in zip(bars, subject_means):
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{mean_val:.1f}', ha='center', va='bottom', fontweight='bold')
        
        ax3.set_title('Average Performance by Subject', fontsize=14, fontweight='bold')
        ax3.set_ylabel('Average Grade')
        ax3.tick_params(axis='x', rotation=45)
        ax3.grid(True, axis='y', alpha=0.3)
        ax3.set_ylim(60, 85)
        
        # 4. Top and Bottom Performers (second row, right)
        ax4 = fig.add_subplot(gs[1, 2:])
        
        # Sort students by GPA
        sorted_students = sorted(self.students_data, 
                               key=lambda x: np.mean(list(x['subjects'].values())), reverse=True)
        
        top_5 = sorted_students[:5]
        bottom_5 = sorted_students[-5:]
        
        performers_text = "🏆 TOP 5 PERFORMERS\n" + "="*25 + "\n"
        for i, student in enumerate(top_5, 1):
            gpa = np.mean(list(student['subjects'].values()))
            performers_text += f"{i}. {student['name']}: {gpa:.1f}\n"
        
        performers_text += "\n⚠️ STUDENTS NEEDING SUPPORT\n" + "="*30 + "\n"
        for i, student in enumerate(bottom_5, 1):
            gpa = np.mean(list(student['subjects'].values()))
            performers_text += f"{i}. {student['name']}: {gpa:.1f}\n"
        
        ax4.text(0.05, 0.95, performers_text, transform=ax4.transAxes, fontsize=10,
                verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)
        ax4.axis('off')
        
        # 5. Attendance vs Performance Scatter (third row, left)
        ax5 = fig.add_subplot(gs[2, :2])
        
        attendance_data = [student['attendance'] for student in self.students_data]
        gpa_data = [np.mean(list(student['subjects'].values())) for student in self.students_data]
        study_hours = [student['study_hours_per_week'] for student in self.students_data]
        
        scatter = ax5.scatter(attendance_data, gpa_data, c=study_hours, cmap='viridis', 
                             alpha=0.6, s=60, edgecolors='black', linewidth=0.5)
        
        # Add trend line
        z = np.polyfit(attendance_data, gpa_data, 1)
        trend = np.poly1d(z)
        ax5.plot(sorted(attendance_data), trend(sorted(attendance_data)), 
                '--', color='red', linewidth=2)
        
        ax5.set_xlabel('Attendance (%)')
        ax5.set_ylabel('GPA')
        ax5.set_title('Attendance vs Academic Performance', fontsize=14, fontweight='bold')
        
        # Add correlation text
        correlation = np.corrcoef(attendance_data, gpa_data)[0, 1]
        ax5.text(0.05, 0.95, f'Correlation: {correlation:.3f}', transform=ax5.transAxes,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8),
                fontweight='bold')
        
        # Add colorbar
        cbar = plt.colorbar(scatter, ax=ax5, shrink=0.8)
        cbar.set_label('Study Hours/Week')
        
        # 6. Weekly Performance Trend (third row, right) 
        ax6 = fig.add_subplot(gs[2, 2:])
        
        weeks = range(1, 17)
        weekly_averages = []
        
        for week in weeks:
            week_grades = []
            for student in self.students_data:
                week_assignments = [a['grade'] for a in student['assignments'] if a['week'] == week]
                if week_assignments:
                    week_grades.extend(week_assignments)
            weekly_averages.append(np.mean(week_grades) if week_grades else 0)
        
        ax6.plot(weeks, weekly_averages, marker='o', linewidth=2.5, markersize=6, 
                color='steelblue')
        
        # Add trend line
        z = np.polyfit(weeks, weekly_averages, 1)
        trend = np.poly1d(z)
        ax6.plot(weeks, trend(weeks), '--', color='red', linewidth=2,
                label=f'Trend: {"+" if z[0] > 0 else ""}{z[0]:.2f}/week')
        
        ax6.set_xlabel('Week')
        ax6.set_ylabel('Average Grade')
        ax6.set_title('Weekly Performance Trend', fontsize=14, fontweight='bold')
        ax6.legend()
        ax6.grid(True, alpha=0.3)
        
        # 7. Subject Correlation Mini-Heatmap (bottom left)
        ax7 = fig.add_subplot(gs[3, :2])
        
        subjects = ['Math', 'Science', 'English', 'History', 'Art']
        
        # Create simplified correlation matrix
        grade_data = []
        for subject in ['Mathematics', 'Science', 'English', 'History', 'Art']:
            subject_grades = [student['subjects'][subject] for student in self.students_data]
            grade_data.append(subject_grades)
        
        correlation_matrix = np.corrcoef(grade_data)
        
        im = ax7.imshow(correlation_matrix, cmap='RdYlBu_r', vmin=-1, vmax=1)
        
        ax7.set_xticks(range(len(subjects)))
        ax7.set_yticks(range(len(subjects)))
        ax7.set_xticklabels(subjects, rotation=45, ha='right')
        ax7.set_yticklabels(subjects)
        
        # Add correlation values
        for i in range(len(subjects)):
            for j in range(len(subjects)):
                ax7.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                        ha="center", va="center", fontweight='bold',
                        color='white' if abs(correlation_matrix[i, j]) > 0.5 else 'black')
        
        ax7.set_title('Subject Correlations', fontsize=14, fontweight='bold')
        
        # 8. Recommendations (bottom right)
        ax8 = fig.add_subplot(gs[3, 2:])
        
        # Generate recommendations based on analysis
        recommendations = self.generate_recommendations()
        
        rec_text = "💡 EDUCATIONAL RECOMMENDATIONS\n" + "="*35 + "\n"
        for i, rec in enumerate(recommendations[:8], 1):
            rec_text += f"{i}. {rec}\n"
        
        ax8.text(0.05, 0.95, rec_text, transform=ax8.transAxes, fontsize=10,
                verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.8))
        ax8.set_xlim(0, 1)
        ax8.set_ylim(0, 1)
        ax8.axis('off')
        
        # Main title
        fig.suptitle('🎓 COMPREHENSIVE ACADEMIC PERFORMANCE DASHBOARD', 
                    fontsize=24, fontweight='bold', y=0.98)
        
        return fig
    
    def generate_recommendations(self):
        """
        Generate educational recommendations based on data analysis
        """
        if not self.analysis_results:
            self.calculate_statistics()
        
        stats = self.analysis_results
        recommendations = []
        
        # Attendance-based recommendations
        if stats['correlations']['attendance_gpa'] > 0.3:
            recommendations.append("Strong attendance correlation - implement attendance incentives")
        
        # Study hours recommendations
        if stats['correlations']['study_hours_gpa'] > 0.2:
            recommendations.append("Study hours impact performance - promote study skills workshops")
        
        # Subject-specific recommendations
        worst_subject = min(stats['subject_stats'].keys(), 
                           key=lambda x: stats['subject_stats'][x]['mean'])
        recommendations.append(f"Focus additional resources on {worst_subject} (lowest average)")
        
        # Grade distribution recommendations
        if stats['grade_distribution']['D/F (<70)'] > 20:
            recommendations.append("High at-risk population - implement early intervention program")
        
        if stats['grade_distribution']['A (90+)'] > 30:
            recommendations.append("Many high achievers - consider advanced/honors programs")
        
        # Performance trend recommendations
        recommendations.append("Monitor weekly trends for early identification of struggling students")
        recommendations.append("Implement peer tutoring program for consistent support")
        recommendations.append("Regular parent-teacher conferences for at-risk students")
        
        return recommendations
    
    def export_analysis_report(self, filename="grade_analysis_report.txt"):
        """
        Export a comprehensive text report of the analysis
        """
        if not self.analysis_results:
            self.calculate_statistics()
        
        stats = self.analysis_results
        
        report = f"""
COMPREHENSIVE GRADE ANALYSIS REPORT
{'='*50}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERVIEW
--------
Total Students Analyzed: {stats['total_students']}
Analysis Period: 16-week semester
Subjects Analyzed: Mathematics, Science, English, History, Art

CLASS PERFORMANCE STATISTICS
-----------------------------
Overall Class Average: {stats['overall_mean']:.2f}
Overall Median Grade: {stats['overall_median']:.2f}
Standard Deviation: {stats['overall_std']:.2f}
Mean GPA: {stats['student_performance']['mean_gpa']:.2f}

GRADE DISTRIBUTION
------------------
A Students (90-100): {stats['grade_distribution']['A (90+)']:.1f}%
B Students (80-89):  {stats['grade_distribution']['B (80-89)']:.1f}%
C Students (70-79):  {stats['grade_distribution']['C (70-79)']:.1f}%
At Risk (<70):       {stats['grade_distribution']['D/F (<70)']:.1f}%

SUBJECT PERFORMANCE BREAKDOWN
-----------------------------
"""
        
        for subject, subject_stats in stats['subject_stats'].items():
            report += f"""
{subject}:
  Mean: {subject_stats['mean']:.2f}
  Median: {subject_stats['median']:.2f}
  Std Dev: {subject_stats['std']:.2f}
  Range: {subject_stats['min']:.1f} - {subject_stats['max']:.1f}
"""
        
        report += f"""
CORRELATION ANALYSIS
--------------------
Attendance ↔ GPA: {stats['correlations']['attendance_gpa']:.3f}
Study Hours ↔ GPA: {stats['correlations']['study_hours_gpa']:.3f}

ADDITIONAL METRICS
------------------
Average Attendance Rate: {stats['student_performance']['mean_attendance']:.1f}%
Average Study Hours/Week: {stats['student_performance']['mean_study_hours']:.1f}

RECOMMENDATIONS
---------------
"""
        
        recommendations = self.generate_recommendations()
        for i, rec in enumerate(recommendations, 1):
            report += f"{i}. {rec}\n"
        
        # Save report
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"📄 Analysis report saved to {filename}")
            return filename
        except Exception as e:
            print(f"❌ Error saving report: {e}")
            return None
    
    def save_data(self, filename="grade_data.json"):
        """
        Save student data to JSON file
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.students_data, f, indent=2, ensure_ascii=False)
            print(f"💾 Student data saved to {filename}")
            return filename
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return None
    
    def load_data(self, filename):
        """
        Load student data from JSON file
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.students_data = json.load(f)
            print(f"📂 Student data loaded from {filename}")
            return True
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False


def main():
    """
    Main function demonstrating the Grade Analysis System
    """
    print("🎓" * 25)
    print("    COMPREHENSIVE GRADE ANALYSIS SYSTEM")
    print("🎓" * 25)
    print("Professional academic performance analysis and visualization")
    print()
    
    # Initialize the analyzer
    analyzer = GradeAnalyzer()
    
    while True:
        print("\n" + "=" * 60)
        print("📊 GRADE ANALYSIS MENU")
        print("=" * 60)
        print("1. Calculate class statistics")
        print("2. Create grade distribution charts")
        print("3. Analyze performance trends")
        print("4. Show subject correlations")
        print("5. Generate comprehensive dashboard")
        print("6. Export analysis report")
        print("7. Save/Load data")
        print("8. Quick demo - Generate all visualizations")
        print("9. Exit")
        
        try:
            choice = input("\nSelect option (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Thank you for using the Grade Analysis System!")
            print("📚 Keep making data-driven educational decisions!")
            break
        
        if choice == "1":
            print("\n📊 Calculating Class Statistics...")
            stats = analyzer.calculate_statistics()
            
            print(f"\n✅ Analysis Complete!")
            print(f"📈 Class Average: {stats['overall_mean']:.1f}")
            print(f"📊 Students Analyzed: {stats['total_students']}")
            print(f"🎯 A Students: {stats['grade_distribution']['A (90+)']:.1f}%")
            print(f"⚠️ At Risk: {stats['grade_distribution']['D/F (<70)']:.1f}%")
        
        elif choice == "2":
            print("\n📊 Creating Grade Distribution Charts...")
            fig = analyzer.create_grade_distribution_charts()
            plt.show()
            
            save_choice = input("\nSave chart? (y/n): ").strip().lower()
            if save_choice in ['y', 'yes']:
                fig.savefig('grade_distributions.png', dpi=300, bbox_inches='tight')
                print("✅ Chart saved as 'grade_distributions.png'")
        
        elif choice == "3":
            print("\n📈 Analyzing Performance Trends...")
            fig = analyzer.create_performance_trends()
            plt.show()
            
            save_choice = input("\nSave chart? (y/n): ").strip().lower()
            if save_choice in ['y', 'yes']:
                fig.savefig('performance_trends.png', dpi=300, bbox_inches='tight')
                print("✅ Chart saved as 'performance_trends.png'")
        
        elif choice == "4":
            print("\n🔗 Creating Subject Correlation Analysis...")
            fig = analyzer.create_subject_correlation_heatmap()
            plt.show()
            
            save_choice = input("\nSave chart? (y/n): ").strip().lower()
            if save_choice in ['y', 'yes']:
                fig.savefig('subject_correlations.png', dpi=300, bbox_inches='tight')
                print("✅ Chart saved as 'subject_correlations.png'")
        
        elif choice == "5":
            print("\n📋 Generating Comprehensive Dashboard...")
            fig = analyzer.create_comprehensive_dashboard()
            plt.show()
            
            save_choice = input("\nSave dashboard? (y/n): ").strip().lower()
            if save_choice in ['y', 'yes']:
                fig.savefig('academic_dashboard.png', dpi=300, bbox_inches='tight')
                print("✅ Dashboard saved as 'academic_dashboard.png'")
        
        elif choice == "6":
            print("\n📄 Exporting Analysis Report...")
            report_file = analyzer.export_analysis_report()
            if report_file:
                print(f"✅ Report exported successfully!")
                print(f"📁 File: {report_file}")
        
        elif choice == "7":
            print("\n💾 Data Management")
            print("1. Save current data")
            print("2. Load data from file")
            
            data_choice = input("Choose option (1-2): ").strip()
            
            if data_choice == "1":
                filename = input("Enter filename (default: grade_data.json): ").strip()
                if not filename:
                    filename = "grade_data.json"
                analyzer.save_data(filename)
            
            elif data_choice == "2":
                filename = input("Enter filename to load: ").strip()
                if filename:
                    if analyzer.load_data(filename):
                        print("✅ Data loaded successfully!")
                    else:
                        print("❌ Failed to load data")
        
        elif choice == "8":
            print("\n🎯 COMPREHENSIVE ANALYSIS DEMO")
            print("=" * 35)
            print("Generating all visualizations and reports...")
            
            # Calculate statistics
            print("📊 1/5 Calculating statistics...")
            analyzer.calculate_statistics()
            
            # Generate all visualizations
            print("📊 2/5 Creating grade distributions...")
            dist_fig = analyzer.create_grade_distribution_charts()
            dist_fig.savefig('demo_grade_distributions.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            print("📈 3/5 Creating performance trends...")
            trend_fig = analyzer.create_performance_trends()
            trend_fig.savefig('demo_performance_trends.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            print("🔗 4/5 Creating correlation analysis...")
            corr_fig = analyzer.create_subject_correlation_heatmap()
            corr_fig.savefig('demo_subject_correlations.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            print("📋 5/5 Creating comprehensive dashboard...")
            dashboard_fig = analyzer.create_comprehensive_dashboard()
            dashboard_fig.savefig('demo_academic_dashboard.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            # Export report
            print("📄 Exporting analysis report...")
            analyzer.export_analysis_report("demo_analysis_report.txt")
            
            # Save data
            print("💾 Saving student data...")
            analyzer.save_data("demo_grade_data.json")
            
            print(f"\n🎉 Demo Complete!")
            print(f"✅ All visualizations saved with 'demo_' prefix")
            print(f"📊 {len(analyzer.students_data)} students analyzed")
            print(f"📈 Multiple chart types generated")
            print(f"📄 Comprehensive report created")
            print(f"💾 Data saved for future analysis")
        
        elif choice == "9":
            print("\n🎓 Thank you for using the Grade Analysis System!")
            print("📊 Key features demonstrated:")
            print("   • Statistical analysis and reporting")
            print("   • Multiple visualization types") 
            print("   • Correlation analysis")
            print("   • Performance trend tracking")
            print("   • Data export capabilities")
            print("\n💡 Remember: Good visualizations tell stories that lead to better decisions!")
            break
        
        else:
            print("❌ Invalid option. Please select 1-9.")


if __name__ == "__main__":
    main()