# Student Performance Analytics System

| Detail | Information |
|---|---|
| **Student Name** | Pavithra |
| **Course** | EWB Courses, Python with AI |
| **College / Batch** | [East Point College Of Engineering and Technology/ 2023-2027] |
| **Submission Date** | 16 October 2026 |

---

## 1. Project Title

**Student Performance Analytics System**: a Python data-analysis project built with Pandas and NumPy.

## 2. Objective

Teachers often hold student marks in spreadsheets and have to work out totals, grades and pass/fail status by hand, which is slow and easy to get wrong. This project automates that work. It reads student records from a CSV file, calculates each student's total, average, grade and result, and produces class-level, subject-wise and department-wise analysis, plus a list of top performers.

## 3. Technologies Used

- **Python 3**: core language (functions, loops, conditions, file handling)
- **Pandas**: loading the CSV, DataFrame operations, grouping and sorting
- **NumPy**: numerical calculations (class mean, array conversion)
- **Git and GitHub**: version control and submission
- No other libraries are used.

## 4. Dataset Description

- **File:** `students.csv` (synthetic sample data, created for this project)
- **Records:** 20 students across 4 departments (CSE, ECE, IT, ME)
- **Marks:** each subject is scored out of 100

| Column | Description |
|---|---|
| `Student_ID` | Unique ID (S001 to S020) |
| `Name` | Student name |
| `Department` | CSE, ECE, IT or ME |
| `Python_Marks` | Marks in Python (out of 100) |
| `NumPy_Marks` | Marks in NumPy (out of 100) |
| `Pandas_Marks` | Marks in Pandas (out of 100) |
| `Attendance_Percent` | Attendance percentage |

## 5. Implementation

1. **Load the data:** `load_data()` reads `students.csv` with Pandas and checks that all required columns exist and the file is not empty.
2. **Inspect the data:** `show_basic_information()` prints the record count, departments, a preview and `df.info()`.
3. **Process the data:** `add_performance_columns()` adds four new columns:
   - `Total_Marks`: sum of the three subjects (`sum(axis=1)`)
   - `Average_Marks`: mean of the three subjects, rounded to 2 decimals
   - `Grade`: assigned by `assign_grade()` using the grading rule below
   - `Result`: Pass/Fail decided inside a **loop** over every student
4. **Analyse the data:** separate functions compute class statistics (NumPy mean, highest and lowest average, pass count, attendance), subject-wise statistics, department averages (`groupby`) and top performers (`nlargest`).
5. **Output:** results are printed in clearly labelled sections and also saved to `student_performance_results.csv`.

### Grading rule (based on average marks)

| Average | Grade |
|---|---|
| 90 and above | A+ |
| 80 to 89.99 | A |
| 70 to 79.99 | B |
| 60 to 69.99 | C |
| 50 to 59.99 | D |
| Below 50 | F |

### Pass/Fail rule

A student **passes only if they score at least 40 in every subject**. Grade and result are calculated separately. For example, a student with an average of 48 gets grade F but still passes if all three subjects are 40 or above (student S017 in the sample data).

## 6. Key Features

- `load_data()`: reads the CSV and validates columns
- `assign_grade()`: converts an average into a grade
- `add_performance_columns()`: total, average, grade and pass/fail for each student
- `show_student_summary()`: student-wise table sorted by average
- `show_class_analysis()`: class average, highest and lowest average, pass/fail counts, pass percentage, average attendance
- `show_subject_analysis()`: average, highest and lowest marks per subject, plus the best subject
- `show_department_analysis()`: department-wise average
- `show_top_performers()`: top 5 students
- `save_results()`: exports the full results to CSV
- Error handling for a missing file, missing columns and an empty dataset

## 7. Output / Screenshots

Sample output from running `python main.py`:

```
CLASS PERFORMANCE
Overall class average : 70.47
Highest average       : 95.67 (Isha Kapoor)
Lowest average        : 41.00 (Harsh Mehta)
Passed students       : 17
Failed students       : 3
Pass percentage       : 85.00%
Average attendance    : 83.95%

SUBJECT-WISE PERFORMANCE
Python     | Average:  70.70 | Highest:  97 | Lowest:  35
NumPy      | Average:  69.15 | Highest:  94 | Lowest:  38
Pandas     | Average:  71.55 | Highest:  96 | Lowest:  38
Best-performing subject by average: Pandas

DEPARTMENT-WISE AVERAGE
CSE    82.50
IT     76.20
ECE    64.73
ME     52.42

TOP 5 PERFORMING STUDENTS
Student_ID          Name Department  Average_Marks Grade
      S020   Isha Kapoor        CSE          95.67    A+
      S004  Ananya Reddy         IT          93.33    A+
      S001  Aarav Sharma        CSE          90.00    A+
      S014 Neha Kulkarni         IT          88.67     A
      S008   Divya Menon        CSE          88.00     A
```

Screenshots of the program running:

![Program output](screenshots/output1.png)

## 8. Final Outcome

The program runs without errors and answers the key questions about the dataset:

- Highest average: **Isha Kapoor (95.67)**
- Best subject by average: **Pandas (71.55)**
- Students passed: **17 of 20 (85%)**
- Overall class average: **70.47**
- Best department: **CSE (82.50)**

It turns raw marks into a clear report that can be read without opening the code.

## 9. Challenges & Learning

- **Challenge:** Deciding the pass rule. **Solution:** I required at least 40 marks in every subject so a strong subject cannot hide a failing one.
- **Challenge:** Keeping the code readable. **Solution:** I split the work into small functions, one for each calculation or report section.
- **Challenge:** Pushing the project to GitHub for the first time. **Solution:** I created the repository, then used `git init`, `git add`, `git commit` and `git push` to upload the files.
- **Learning:** I practised DataFrame operations (`groupby`, `nlargest`, `idxmax`), NumPy calculations, loops with conditions, and using Git and GitHub.

## 10. GitHub Repository

https://github.com/paviithra77/Student-Performance-Analytics-System

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

Keep `students.csv` in the same folder as `main.py`.

## Project Structure

```
Student-Performance-Analytics-System/
├── main.py                           # program and analysis functions
├── students.csv                      # dataset (20 records)
├── student_performance_results.csv   # generated results
├── requirements.txt                  # dependencies
├── Project_Documentation.md          # project documentation
├── screenshots/                      # output screenshots
└── README.md                         # this file
```
