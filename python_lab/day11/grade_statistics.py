# 成績統計分析程式 - Day 11主要項目
# 完整的學生成績管理與分析系統

import json
import os
from datetime import datetime
import statistics

class GradeAnalyzer:
    def __init__(self):
        self.students_data = []
        self.subjects = ["國文", "英文", "數學", "自然", "社會"]
        self.data_file = "grades_data.json"
        self.load_data()
    
    def save_data(self):
        """儲存資料到檔案"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.students_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ 儲存資料失敗：{e}")
    
    def load_data(self):
        """載入資料"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.students_data = json.load(f)
        except Exception as e:
            print(f"⚠️ 載入資料失敗：{e}")
            self.load_sample_data()
    
    def load_sample_data(self):
        """載入示例資料"""
        self.students_data = [
            ["小明", "男", 85, 92, 78, 88, 91],
            ["小美", "女", 96, 88, 91, 94, 89],
            ["小華", "男", 79, 85, 83, 87, 82],
            ["小強", "男", 88, 91, 85, 90, 87],
            ["小雅", "女", 92, 87, 89, 85, 91],
            ["小杰", "男", 76, 82, 79, 83, 80],
            ["小慧", "女", 94, 90, 92, 88, 93],
            ["小峰", "男", 81, 78, 84, 86, 83]
        ]
    
    def display_header(self):
        """顯示程式標題"""
        print("\n" + "="*60)
        print("📊              學生成績統計分析系統              📊")
        print("="*60)
        print(f"📅 分析時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"👥 學生人數：{len(self.students_data)}")
        print(f"📚 科目數量：{len(self.subjects)}")
    
    def display_menu(self):
        """顯示選單"""
        print("\n" + "─"*40)
        print("🏠 主選單")
        print("─"*40)
        print("1. 📋 查看成績表")
        print("2. ➕ 新增學生")
        print("3. 📝 修改成績")
        print("4. 📊 個人分析")
        print("5. 📚 科目統計")
        print("6. 🏆 排名分析")
        print("7. 📈 等第分析")
        print("8. 🔍 進階分析")
        print("9. 📄 匯出報告")
        print("0. 🚪 離開系統")
        print("─"*40)
    
    def display_grade_table(self):
        """顯示成績表"""
        if not self.students_data:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n📋 學生成績表")
        print("="*80)
        
        # 表頭
        header = f"{'姓名':<6} {'性別':<4}"
        for subject in self.subjects:
            header += f" {subject:<4}"
        header += f" {'總分':<4} {'平均':<6} {'排名':<4}"
        print(header)
        print("-" * 80)
        
        # 計算排名
        student_totals = []
        for i, student in enumerate(self.students_data):
            total = sum(student[2:])
            student_totals.append((i, total))
        student_totals.sort(key=lambda x: x[1], reverse=True)
        
        ranks = [0] * len(self.students_data)
        for rank, (index, _) in enumerate(student_totals):
            ranks[index] = rank + 1
        
        # 顯示資料
        for i, student in enumerate(self.students_data):
            name, gender = student[0], student[1]
            scores = student[2:]
            total = sum(scores)
            average = total / len(scores)
            rank = ranks[i]
            
            row = f"{name:<6} {gender:<4}"
            for score in scores:
                row += f" {score:<4}"
            row += f" {total:<4} {average:<6.1f} {rank:<4}"
            print(row)
    
    def add_student(self):
        """新增學生"""
        print("\n➕ 新增學生")
        print("─"*20)
        
        name = input("學生姓名：").strip()
        if not name:
            print("❌ 姓名不能為空！")
            return
        
        # 檢查是否已存在
        if any(student[0] == name for student in self.students_data):
            print("❌ 該學生已存在！")
            return
        
        gender = input("性別（男/女）：").strip()
        if gender not in ["男", "女"]:
            print("❌ 性別請輸入'男'或'女'！")
            return
        
        scores = []
        print(f"\n請輸入{name}的各科成績：")
        for subject in self.subjects:
            while True:
                try:
                    score = int(input(f"{subject}："))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("❌ 成績必須在0-100之間！")
                except ValueError:
                    print("❌ 請輸入有效數字！")
        
        new_student = [name, gender] + scores
        self.students_data.append(new_student)
        self.save_data()
        
        print(f"✅ 成功新增學生：{name}")
        self.display_student_summary(new_student)
    
    def display_student_summary(self, student):
        """顯示學生簡要資訊"""
        name, gender = student[0], student[1]
        scores = student[2:]
        total = sum(scores)
        average = total / len(scores)
        
        print(f"\n👤 {name}（{gender}）")
        print(f"各科成績：{scores}")
        print(f"總分：{total}，平均：{average:.1f}")
    
    def modify_grade(self):
        """修改成績"""
        if not self.students_data:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n📝 修改成績")
        print("─"*20)
        
        # 顯示學生清單
        print("學生清單：")
        for i, student in enumerate(self.students_data, 1):
            print(f"{i:2}. {student[0]}（{student[1]}）")
        
        try:
            choice = int(input("\n請選擇學生編號：")) - 1
            if 0 <= choice < len(self.students_data):
                student = self.students_data[choice]
                self.display_student_summary(student)
                
                # 顯示科目選單
                print(f"\n科目清單：")
                for i, subject in enumerate(self.subjects, 1):
                    current_score = student[i+1]
                    print(f"{i}. {subject}：{current_score}")
                
                subject_choice = int(input("\n請選擇要修改的科目編號：")) - 1
                if 0 <= subject_choice < len(self.subjects):
                    subject_name = self.subjects[subject_choice]
                    current_score = student[subject_choice + 2]
                    print(f"目前{subject_name}成績：{current_score}")
                    
                    new_score = int(input("請輸入新成績（0-100）："))
                    if 0 <= new_score <= 100:
                        old_score = student[subject_choice + 2]
                        student[subject_choice + 2] = new_score
                        self.save_data()
                        print(f"✅ {student[0]}的{subject_name}成績：{old_score} → {new_score}")
                    else:
                        print("❌ 成績必須在0-100之間！")
                else:
                    print("❌ 無效的科目編號！")
            else:
                print("❌ 無效的學生編號！")
        except ValueError:
            print("❌ 請輸入有效的數字！")
    
    def individual_analysis(self):
        """個人分析"""
        if not self.students_data:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n📊 個人成績分析")
        print("─"*30)
        
        # 顯示學生清單
        for i, student in enumerate(self.students_data, 1):
            print(f"{i:2}. {student[0]}（{student[1]}）")
        
        try:
            choice = int(input("\n請選擇學生編號：")) - 1
            if 0 <= choice < len(self.students_data):
                student = self.students_data[choice]
                self.analyze_individual_student(student)
            else:
                print("❌ 無效的學生編號！")
        except ValueError:
            print("❌ 請輸入有效的數字！")
    
    def analyze_individual_student(self, student):
        """分析個別學生"""
        name, gender = student[0], student[1]
        scores = student[2:]
        
        print(f"\n👤 {name}的詳細分析")
        print("="*40)
        
        # 基本統計
        total = sum(scores)
        average = total / len(scores)
        highest = max(scores)
        lowest = min(scores)
        
        print(f"📊 基本統計：")
        print(f"  總分：{total}")
        print(f"  平均：{average:.2f}")
        print(f"  最高分：{highest}")
        print(f"  最低分：{lowest}")
        print(f"  分數差距：{highest - lowest}")
        
        # 科目詳細分析
        print(f"\n📚 科目分析：")
        for i, subject in enumerate(self.subjects):
            score = scores[i]
            # 計算該科目在所有學生中的排名
            all_subject_scores = [s[i+2] for s in self.students_data]
            all_subject_scores.sort(reverse=True)
            rank = all_subject_scores.index(score) + 1
            
            # 等第判定
            if score >= 90:
                grade = "優秀"
            elif score >= 80:
                grade = "良好"
            elif score >= 70:
                grade = "普通"
            elif score >= 60:
                grade = "及格"
            else:
                grade = "不及格"
            
            print(f"  {subject}：{score}分 | 等第：{grade} | 排名：{rank}/{len(self.students_data)}")
        
        # 優勢與劣勢分析
        best_subject_index = scores.index(highest)
        worst_subject_index = scores.index(lowest)
        best_subject = self.subjects[best_subject_index]
        worst_subject = self.subjects[worst_subject_index]
        
        print(f"\n🎯 優劣勢分析：")
        print(f"  最強科目：{best_subject}（{highest}分）")
        print(f"  最弱科目：{worst_subject}（{lowest}分）")
        print(f"  建議：加強{worst_subject}，保持{best_subject}的優勢")
        
        # 與班級平均比較
        print(f"\n📈 與班級比較：")
        class_averages = self.get_subject_averages()
        for i, subject in enumerate(self.subjects):
            student_score = scores[i]
            class_avg = class_averages[i]
            diff = student_score - class_avg
            comparison = "高於" if diff > 0 else "低於" if diff < 0 else "等於"
            print(f"  {subject}：{comparison}班級平均 {abs(diff):.1f}分")
    
    def get_subject_averages(self):
        """計算各科目平均分"""
        if not self.students_data:
            return [0] * len(self.subjects)
        
        averages = []
        for i in range(len(self.subjects)):
            subject_scores = [student[i+2] for student in self.students_data]
            avg = sum(subject_scores) / len(subject_scores)
            averages.append(avg)
        return averages
    
    def subject_statistics(self):
        """科目統計"""
        if not self.students_data:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n📚 科目統計分析")
        print("="*60)
        
        averages = self.get_subject_averages()
        
        print(f"{'科目':<6} {'平均分':<8} {'最高分':<8} {'最低分':<8} {'標準差':<8} {'最高分學生':<10}")
        print("-" * 60)
        
        for i, subject in enumerate(self.subjects):
            subject_scores = [student[i+2] for student in self.students_data]
            
            avg = averages[i]
            max_score = max(subject_scores)
            min_score = min(subject_scores)
            std_dev = statistics.stdev(subject_scores) if len(subject_scores) > 1 else 0
            
            # 找出最高分學生
            max_student_index = next(j for j, student in enumerate(self.students_data) if student[i+2] == max_score)
            max_student_name = self.students_data[max_student_index][0]
            
            print(f"{subject:<6} {avg:<8.1f} {max_score:<8} {min_score:<8} {std_dev:<8.2f} {max_student_name:<10}")
        
        # 各科目分佈分析
        print(f"\n📊 各科目成績分佈：")
        for i, subject in enumerate(self.subjects):
            subject_scores = [student[i+2] for student in self.students_data]
            
            excellent = len([s for s in subject_scores if s >= 90])
            good = len([s for s in subject_scores if 80 <= s < 90])
            fair = len([s for s in subject_scores if 70 <= s < 80])
            poor = len([s for s in subject_scores if s < 70])
            
            print(f"\n{subject}：")
            print(f"  優秀（90+）：{excellent}人 ({excellent/len(subject_scores)*100:.1f}%)")
            print(f"  良好（80-89）：{good}人 ({good/len(subject_scores)*100:.1f}%)")
            print(f"  普通（70-79）：{fair}人 ({fair/len(subject_scores)*100:.1f}%)")
            print(f"  待加強（<70）：{poor}人 ({poor/len(subject_scores)*100:.1f}%)")
    
    def ranking_analysis(self):
        """排名分析"""
        if not self.students_data:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n🏆 排名分析")
        print("="*50)
        
        # 總分排名
        student_totals = []
        for student in self.students_data:
            name = student[0]
            scores = student[2:]
            total = sum(scores)
            average = total / len(scores)
            student_totals.append((name, total, average, scores))
        
        student_totals.sort(key=lambda x: x[1], reverse=True)
        
        print("📈 總分排名：")
        print(f"{'排名':<4} {'姓名':<8} {'總分':<6} {'平均':<8} {'各科成績'}")
        print("-" * 50)
        
        for rank, (name, total, average, scores) in enumerate(student_totals, 1):
            scores_str = " ".join([str(s) for s in scores])
            print(f"{rank:<4} {name:<8} {total:<6} {average:<8.1f} {scores_str}")
        
        # 各科排名前三
        print(f"\n🥇 各科排名前三：")
        for i, subject in enumerate(self.subjects):
            subject_ranking = []
            for student in self.students_data:
                name = student[0]
                score = student[i+2]
                subject_ranking.append((name, score))
            
            subject_ranking.sort(key=lambda x: x[1], reverse=True)
            
            print(f"\n{subject}：")
            for rank, (name, score) in enumerate(subject_ranking[:3], 1):
                medal = ["🥇", "🥈", "🥉"][rank-1]
                print(f"  {medal} 第{rank}名：{name}（{score}分）")
    
    def grade_distribution_analysis(self):
        """等第分析"""
        if not self.students_data:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n📈 等第分析")
        print("="*40)
        
        # 收集所有成績
        all_scores = []
        for student in self.students_data:
            all_scores.extend(student[2:])
        
        total_scores = len(all_scores)
        excellent = len([s for s in all_scores if s >= 90])
        good = len([s for s in all_scores if 80 <= s < 90])
        fair = len([s for s in all_scores if 70 <= s < 80])
        poor = len([s for s in all_scores if s < 70])
        
        print(f"📊 全班總體等第分佈：")
        print(f"總成績數：{total_scores}")
        print(f"優秀（90+）：{excellent} 項（{excellent/total_scores*100:.1f}%）")
        print(f"良好（80-89）：{good} 項（{good/total_scores*100:.1f}%）")
        print(f"普通（70-79）：{fair} 項（{fair/total_scores*100:.1f}%）")
        print(f"待加強（<70）：{poor} 項（{poor/total_scores*100:.1f}%）")
        
        # 繪製簡單的長條圖
        print(f"\n📊 視覺化分佈：")
        max_count = max(excellent, good, fair, poor)
        scale = 20  # 最大長條長度
        
        categories = [("優秀", excellent), ("良好", good), ("普通", fair), ("待加強", poor)]
        for category, count in categories:
            if max_count > 0:
                bar_length = int(count / max_count * scale)
                bar = "█" * bar_length + "░" * (scale - bar_length)
                print(f"{category:<6} [{bar}] {count}")
        
        # 個人等第統計
        print(f"\n👥 個人等第統計：")
        student_grades = []
        for student in self.students_data:
            name = student[0]
            scores = student[2:]
            avg = sum(scores) / len(scores)
            
            if avg >= 90:
                grade = "優秀"
            elif avg >= 80:
                grade = "良好"
            elif avg >= 70:
                grade = "普通"
            else:
                grade = "待加強"
            
            student_grades.append((name, grade, avg))
        
        # 按等第分組
        grade_groups = {"優秀": [], "良好": [], "普通": [], "待加強": []}
        for name, grade, avg in student_grades:
            grade_groups[grade].append((name, avg))
        
        for grade, students in grade_groups.items():
            if students:
                print(f"\n{grade}學生：")
                for name, avg in students:
                    print(f"  {name}：{avg:.1f}")
    
    def advanced_analysis(self):
        """進階分析"""
        if not self.students_data:
            print("\n❌ 目前沒有學生資料！")
            return
        
        print("\n🔍 進階分析")
        print("="*40)
        
        # 1. 進步潛力分析
        print("📈 進步潛力分析：")
        potential_ranking = []
        for student in self.students_data:
            name = student[0]
            scores = student[2:]
            highest = max(scores)
            lowest = min(scores)
            potential = highest - lowest
            potential_ranking.append((name, potential, lowest, highest))
        
        potential_ranking.sort(key=lambda x: x[1], reverse=True)
        top_potential = potential_ranking[0]
        print(f"最有潛力：{top_potential[0]}（分差{top_potential[1]}分，最低{top_potential[2]}→最高{top_potential[3]}）")
        
        most_stable = min(potential_ranking, key=lambda x: x[1])
        print(f"最穩定：{most_stable[0]}（分差僅{most_stable[1]}分）")
        
        # 2. 科目相關性分析
        print(f"\n📚 科目表現關聯分析：")
        correlations = []
        for i in range(len(self.subjects)):
            for j in range(i+1, len(self.subjects)):
                subject1, subject2 = self.subjects[i], self.subjects[j]
                scores1 = [student[i+2] for student in self.students_data]
                scores2 = [student[j+2] for student in self.students_data]
                
                # 簡單的相關性計算（皮爾森相關係數的簡化版）
                mean1 = sum(scores1) / len(scores1)
                mean2 = sum(scores2) / len(scores2)
                
                numerator = sum((scores1[k] - mean1) * (scores2[k] - mean2) for k in range(len(scores1)))
                denominator1 = sum((s - mean1) ** 2 for s in scores1) ** 0.5
                denominator2 = sum((s - mean2) ** 2 for s in scores2) ** 0.5
                
                if denominator1 > 0 and denominator2 > 0:
                    correlation = numerator / (denominator1 * denominator2)
                    correlations.append((subject1, subject2, correlation))
        
        correlations.sort(key=lambda x: abs(x[2]), reverse=True)
        print(f"最相關的科目組合：")
        for subject1, subject2, corr in correlations[:3]:
            strength = "強" if abs(corr) > 0.7 else "中" if abs(corr) > 0.4 else "弱"
            direction = "正" if corr > 0 else "負"
            print(f"  {subject1} ↔ {subject2}：{direction}相關（{strength}度，{corr:.3f}）")
        
        # 3. 性別差異分析
        print(f"\n👥 性別表現分析：")
        male_students = [s for s in self.students_data if s[1] == "男"]
        female_students = [s for s in self.students_data if s[1] == "女"]
        
        if male_students and female_students:
            print(f"男學生（{len(male_students)}人）vs 女學生（{len(female_students)}人）：")
            
            for i, subject in enumerate(self.subjects):
                male_scores = [s[i+2] for s in male_students]
                female_scores = [s[i+2] for s in female_students]
                
                male_avg = sum(male_scores) / len(male_scores)
                female_avg = sum(female_scores) / len(female_scores)
                
                diff = female_avg - male_avg
                advantage = "女生較優" if diff > 2 else "男生較優" if diff < -2 else "相當"
                
                print(f"  {subject}：男{male_avg:.1f} vs 女{female_avg:.1f} ({advantage})")
    
    def export_report(self):
        """匯出報告"""
        if not self.students_data:
            print("\n❌ 目前沒有學生資料！")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"grade_report_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("📊 學生成績分析報告\n")
                f.write("="*60 + "\n")
                f.write(f"報告生成時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"學生人數：{len(self.students_data)}人\n")
                f.write(f"科目：{', '.join(self.subjects)}\n\n")
                
                # 成績表
                f.write("📋 成績表：\n")
                f.write("-" * 60 + "\n")
                for student in self.students_data:
                    name, gender = student[0], student[1]
                    scores = student[2:]
                    total = sum(scores)
                    average = total / len(scores)
                    f.write(f"{name}（{gender}）：{scores} | 總分：{total} | 平均：{average:.1f}\n")
                
                # 科目統計
                f.write(f"\n📚 科目統計：\n")
                f.write("-" * 60 + "\n")
                averages = self.get_subject_averages()
                for i, subject in enumerate(self.subjects):
                    subject_scores = [student[i+2] for student in self.students_data]
                    f.write(f"{subject}：平均{averages[i]:.1f}，最高{max(subject_scores)}，最低{min(subject_scores)}\n")
                
                # 排名
                f.write(f"\n🏆 總分排名：\n")
                f.write("-" * 60 + "\n")
                student_totals = [(s[0], sum(s[2:])) for s in self.students_data]
                student_totals.sort(key=lambda x: x[1], reverse=True)
                for rank, (name, total) in enumerate(student_totals, 1):
                    f.write(f"第{rank}名：{name}（{total}分）\n")
            
            print(f"✅ 報告已匯出：{filename}")
        except Exception as e:
            print(f"❌ 匯出失敗：{e}")
    
    def run(self):
        """執行主程式"""
        self.display_header()
        
        while True:
            self.display_menu()
            choice = input("\n請選擇功能 (0-9): ").strip()
            
            if choice == "1":
                self.display_grade_table()
            elif choice == "2":
                self.add_student()
            elif choice == "3":
                self.modify_grade()
            elif choice == "4":
                self.individual_analysis()
            elif choice == "5":
                self.subject_statistics()
            elif choice == "6":
                self.ranking_analysis()
            elif choice == "7":
                self.grade_distribution_analysis()
            elif choice == "8":
                self.advanced_analysis()
            elif choice == "9":
                self.export_report()
            elif choice == "0":
                self.save_data()
                print("\n👋 感謝使用成績統計分析系統！")
                print("💾 資料已自動儲存")
                break
            else:
                print("❌ 無效選擇，請輸入0-9！")
            
            input("\n按Enter鍵繼續...")

# 執行程式
if __name__ == "__main__":
    analyzer = GradeAnalyzer()
    try:
        analyzer.run()
    except KeyboardInterrupt:
        print("\n\n👋 程式被中斷，資料已儲存！")
        analyzer.save_data()