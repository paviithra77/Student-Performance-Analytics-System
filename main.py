"""
Student Performance Analytics System
A beginner-friendly Python project using Pandas and NumPy.
Dataset: students.csv (synthetic sample data)
"""

from pathlib import Path
import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).parent / "students.csv"
SUBJECTS = ["Python_Marks", "NumPy_Marks", "Pandas_Marks"]
PASS_MARK = 40  # A student must score at least 40 in every subject to pass.


def load_data(file_path=DATA_FILE):
    """Load student records and validate required columns."""
    df = pd.read_csv(file_path)
    required = [
        "Student_ID", "Name", "Department",
        "Python_Marks", "NumPy_Marks", "Pandas_Marks",
        "Attendance_Percent",
    ]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if df.empty:
        raise ValueError("The dataset contains no student records.")
    return df


def assign_grade(average):
    """Return a grade using the project grading rule."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_performance_columns(df):
    """Calculate total, average, grade, and pass/fail for each student."""
    result = df.copy()
    marks = result[SUBJECTS]
    result["Total_Marks"] = marks.sum(axis=1)
    result["Average_Marks"] = marks.mean(axis=1).round(2)
    result["Grade"] = result["Average_Marks"].apply(assign_grade)

    # Use a loop to determine pass/fail: all three subjects must be >= PASS_MARK.
    pass_status = []
    for _, row in result.iterrows():
        if all(row[subject] >= PASS_MARK for subject in SUBJECTS):
            pass_status.append("Pass")
        else:
            pass_status.append("Fail")
    result["Result"] = pass_status
    return result


def show_basic_information(df):
    """Display dataset size and columns."""
    print("\n" + "=" * 72)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)
    print(f"Total student records : {len(df)}")
    print(f"Departments           : {', '.join(sorted(df['Department'].unique()))}")
    print("\nDataset preview:")
    print(df.head().to_string(index=False))
    print("\nColumn information:")
    df.info()


def show_student_summary(df):
    """Display each student's calculated result."""
    columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance_Percent",
    ]
    print("\nSTUDENT-WISE SUMMARY")
    print(df[columns].sort_values("Average_Marks", ascending=False).to_string(index=False))


def show_class_analysis(df):
    """Display class statistics using Pandas and NumPy."""
    averages = df["Average_Marks"].to_numpy()
    best_student = df.loc[df["Average_Marks"].idxmax()]
    lowest_student = df.loc[df["Average_Marks"].idxmin()]
    pass_count = int((df["Result"] == "Pass").sum())
    fail_count = int((df["Result"] == "Fail").sum())

    print("\nCLASS PERFORMANCE")
    print(f"Overall class average : {np.mean(averages):.2f}")
    print(f"Highest average       : {best_student['Average_Marks']:.2f} ({best_student['Name']})")
    print(f"Lowest average        : {lowest_student['Average_Marks']:.2f} ({lowest_student['Name']})")
    print(f"Passed students       : {pass_count}")
    print(f"Failed students       : {fail_count}")
    print(f"Pass percentage       : {(pass_count / len(df)) * 100:.2f}%")
    print(f"Average attendance    : {np.mean(df['Attendance_Percent'].to_numpy()):.2f}%")


def show_subject_analysis(df):
    """Show mean, highest, and lowest marks for each subject."""
    print("\nSUBJECT-WISE PERFORMANCE")
    subject_averages = df[SUBJECTS].mean()
    for subject in SUBJECTS:
        print(
            f"{subject.replace('_Marks', ''):10} | "
            f"Average: {subject_averages[subject]:6.2f} | "
            f"Highest: {df[subject].max():3.0f} | "
            f"Lowest: {df[subject].min():3.0f}"
        )
    best_subject = subject_averages.idxmax().replace("_Marks", "")
    print(f"Best-performing subject by average: {best_subject}")


def show_department_analysis(df):
    """Compare departments by average marks."""
    print("\nDEPARTMENT-WISE AVERAGE")
    department_average = df.groupby("Department")["Average_Marks"].mean().sort_values(ascending=False)
    print(department_average.round(2).to_string())


def show_top_performers(df, count=5):
    """Display the top students by average marks."""
    print(f"\nTOP {min(count, len(df))} PERFORMING STUDENTS")
    top = df.nlargest(count, "Average_Marks")[["Student_ID", "Name", "Department", "Average_Marks", "Grade"]]
    print(top.to_string(index=False))


def save_results(df):
    """Save calculated student results to a new CSV file."""
    output_file = Path(__file__).parent / "student_performance_results.csv"
    df.to_csv(output_file, index=False)
    print(f"\nFull results saved to: {output_file.name}")


def main():
    try:
        raw_df = load_data()
        show_basic_information(raw_df)
        results_df = add_performance_columns(raw_df)
        show_student_summary(results_df)
        show_class_analysis(results_df)
        show_subject_analysis(results_df)
        show_department_analysis(results_df)
        show_top_performers(results_df)
        save_results(results_df)
    except FileNotFoundError:
        print(f"Error: Could not find {DATA_FILE.name}. Keep it in the same folder as main.py.")
    except (ValueError, pd.errors.ParserError) as error:
        print(f"Could not process the dataset: {error}")


if __name__ == "__main__":
    main()
