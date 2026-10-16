# Project Documentation: Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**

Student Name: [Enter your name]  
Student ID/Roll Number: [Enter your ID]  
Course: Python with AI  
Department/Class: [Enter your department/class]

## 2. Objective
The objective of this project is to analyze student marks and attendance using Python, NumPy and Pandas. It automates the calculation of total marks, average marks, grades and pass/fail status, and summarizes overall, subject-wise and department-wise performance.

## 3. Technologies Used
- **Python:** variables, data types, conditions, loops and functions.
- **Pandas:** reads the CSV file into a DataFrame, processes columns, groups data and creates summaries.
- **NumPy:** calculates numerical statistics such as averages.
- **CSV:** stores the input student dataset.

## 4. Dataset Description
The included `students.csv` file contains 20 synthetic sample student records. The columns are:
- Student_ID
- Name
- Department
- Python_Marks
- NumPy_Marks
- Pandas_Marks
- Attendance_Percent

Marks are assumed to be out of 100. The sample data is for demonstration and is not real student information.

## 5. Implementation
1. Import Pandas and NumPy and define the input file path.
2. Read `students.csv` into a Pandas DataFrame.
3. Validate the required column names and check that the dataset is not empty.
4. Calculate total marks by adding the three subject marks.
5. Calculate average marks for each student.
6. Assign grades using the grading scale below.
7. Use a loop and condition to mark a student Pass only when all three subject marks are at least 40; otherwise mark Fail.
8. Use NumPy and Pandas to calculate class average, highest and lowest student averages, pass/fail counts and average attendance.
9. Calculate subject averages and identify the subject with the highest average.
10. Group records by department to compare average performance.
11. Display the top five students by average marks.
12. Save the processed table to `student_performance_results.csv`.

### Grading rule
| Average marks | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

### Pass/fail rule
A student passes only if they score 40 or more in **each** of Python, NumPy and Pandas. A score below 40 in any one of these subjects results in Fail.

## 6. Key Features
- CSV data loading and basic dataset information
- Student-wise total and average marks
- Automatic grade assignment
- Pass/fail classification
- Class-level statistics and pass percentage
- Subject-wise highest, lowest and average marks
- Department-wise average marks
- Top-five performer list
- Export of calculated results to a CSV file

## 7. Output / Screenshots
After running `python main.py`, capture screenshots of:
1. Dataset preview and column information
2. Student-wise summary
3. Class performance statistics
4. Subject-wise and department-wise analysis
5. Top-five performers and confirmation that the results CSV was saved

**Insert your actual screenshots here before final submission.** The screenshots are not included because they should show the program running in your own environment.

## 8. Final Outcome
The program turns raw student records into an organized performance report. It identifies grades and pass/fail status, summarizes class and subject performance, compares departments, identifies top performers and exports the calculated results for later use.

## 9. Challenges & Learning
Suggested points to personalize after testing:
- Learned to load and inspect CSV data using Pandas.
- Practiced reusable functions, loops and conditional statements.
- Used NumPy and Pandas for numerical analysis.
- Defined clear rules for grades and pass/fail decisions.
- Tested file paths and verified that output files were created.

Replace or edit these points to reflect the challenges you actually faced and how you solved them.

## 10. GitHub Repository
Repository URL: [Paste your public GitHub repository URL here after uploading the project]

## How to run
Install dependencies:
```bash
python -m pip install -r requirements.txt
```
Run:
```bash
python main.py
```

## Submission checklist
- [ ] Run the program successfully
- [ ] Review the dataset and grading/pass rules with your trainer's requirements
- [ ] Add your name and student details
- [ ] Capture and insert actual output screenshots
- [ ] Create a GitHub repository and upload all project files
- [ ] Verify README and documentation are visible
- [ ] Paste the repository URL into the EWB Google Form
