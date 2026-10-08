import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from functions import calculate_grade, check_pass_fail

# Load student data from CSV file
df = pd.read_csv("students.csv")

# Display the complete dataset
print("\n===== STUDENT DATA =====")
print(df)

# Display number of rows and columns
print("\n===== DATASET SHAPE =====")
print(df.shape)

# Display column names
print("\n===== COLUMN NAMES =====")
print(df.columns)

# Display basic information about the dataset
print("\n===== DATASET INFORMATION =====")
df.info()
# Calculate total marks for each student
df["Total_Marks"] = df["Python"] + df["Mathematics"] + df["Data_Analysis"]

# Calculate average marks for each student
df["Average_Marks"] = df["Total_Marks"] / 3

# Display total and average marks
print("\n===== TOTAL AND AVERAGE MARKS =====")
print(df[["Student_ID", "Name", "Total_Marks", "Average_Marks"]])    



# NumPy analysis on average marks
average_marks = df["Average_Marks"].to_numpy()

class_average = np.mean(average_marks)
highest_average = np.max(average_marks)
lowest_average = np.min(average_marks)

print("\n===== CLASS PERFORMANCE ANALYSIS =====")
print(f"Class Average: {class_average:.2f}")
print(f"Highest Average: {highest_average:.2f}")
print(f"Lowest Average: {lowest_average:.2f}")

# Assign grades to each student
df["Grade"] = df["Average_Marks"].apply(calculate_grade)

# Determine pass/fail status for each student
df["Result"] = df.apply(
    lambda row: check_pass_fail(
        row["Python"],
        row["Mathematics"],
        row["Data_Analysis"],
        row["Average_Marks"]
    ),
    axis=1
)



# Display grades and results
print("\n===== GRADES AND RESULTS =====")
print(
    df[
        [
            "Student_ID",
            "Name",
            "Average_Marks",
            "Grade",
            "Result"
        ]
    ]
)
# Grade distribution using a loop
grade_counts = {}

for grade in df["Grade"]:
    if grade in grade_counts:
        grade_counts[grade] += 1
    else:
        grade_counts[grade] = 1

print("\n===== GRADE DISTRIBUTION =====")

for grade, count in grade_counts.items():
    print(f"{grade}: {count} students")



# Calculate subject-wise average marks
python_average = np.mean(df["Python"])
mathematics_average = np.mean(df["Mathematics"])
data_analysis_average = np.mean(df["Data_Analysis"])

print("\n===== SUBJECT-WISE PERFORMANCE =====")
print(f"Python Average: {python_average:.2f}")
print(f"Mathematics Average: {mathematics_average:.2f}")
print(f"Data Analysis Average: {data_analysis_average:.2f}")

# Store subject averages in a dictionary
subject_averages = {
    "Python": python_average,
    "Mathematics": mathematics_average,
    "Data Analysis": data_analysis_average
}

# Find the best-performing subject
best_subject = max(subject_averages, key=subject_averages.get)

print(f"Best Performing Subject: {best_subject}")




# Identify the top-performing students
top_students = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)

print("\n===== TOP 5 PERFORMING STUDENTS =====")
print(
    top_students[
        [
            "Student_ID",
            "Name",
            "Department",
            "Total_Marks",
            "Average_Marks",
            "Grade"
        ]
    ]
)




# Calculate pass/fail statistics
pass_count = (df["Result"] == "PASS").sum()
fail_count = (df["Result"] == "FAIL").sum()

total_students = len(df)

pass_percentage = (pass_count / total_students) * 100
fail_percentage = (fail_count / total_students) * 100

print("\n===== PASS/FAIL STATISTICS =====")
print(f"Total Students: {total_students}")
print(f"Passed Students: {pass_count}")
print(f"Failed Students: {fail_count}")
print(f"Pass Percentage: {pass_percentage:.2f}%")
print(f"Fail Percentage: {fail_percentage:.2f}%")



# Identify the highest-performing student
highest_student = df.loc[df["Average_Marks"].idxmax()]

print("\n===== HIGHEST-PERFORMING STUDENT =====")
print(f"Student ID: {highest_student['Student_ID']}")
print(f"Name: {highest_student['Name']}")
print(f"Department: {highest_student['Department']}")
print(f"Total Marks: {highest_student['Total_Marks']}")
print(f"Average Marks: {highest_student['Average_Marks']:.2f}")
print(f"Grade: {highest_student['Grade']}")


# Identify the lowest-performing student
lowest_student = df.loc[df["Average_Marks"].idxmin()]

print("\n===== LOWEST-PERFORMING STUDENT =====")
print(f"Student ID: {lowest_student['Student_ID']}")
print(f"Name: {lowest_student['Name']}")
print(f"Department: {lowest_student['Department']}")
print(f"Total Marks: {lowest_student['Total_Marks']}")
print(f"Average Marks: {lowest_student['Average_Marks']:.2f}")
print(f"Grade: {lowest_student['Grade']}")



# Attendance analysis
average_attendance = np.mean(df["Attendance"])
highest_attendance = np.max(df["Attendance"])
lowest_attendance = np.min(df["Attendance"])

print("\n===== ATTENDANCE ANALYSIS =====")
print(f"Average Attendance: {average_attendance:.2f}%")
print(f"Highest Attendance: {highest_attendance:.2f}%")
print(f"Lowest Attendance: {lowest_attendance:.2f}%")



# Identify students with attendance below 75%
low_attendance_students = df[df["Attendance"] < 75]

print("\n===== LOW ATTENDANCE STUDENTS =====")

if low_attendance_students.empty:
    print("No students have attendance below 75%.")
else:
    print(
        low_attendance_students[
            ["Student_ID", "Name", "Department", "Attendance"]
        ]
    )


    # Subject-wise performance visualization
subjects = ["Python", "Mathematics", "Data Analysis"]
subject_averages = [
    df["Python"].mean(),
    df["Mathematics"].mean(),
    df["Data_Analysis"].mean()
]

plt.figure(figsize=(8, 5))

plt.bar(subjects, subject_averages)

plt.title("Subject-wise Average Performance")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.tight_layout()

plt.show()



# Top 5 students visualization

top_names = top_students["Name"]
top_averages = top_students["Average_Marks"]

plt.figure(figsize=(8, 5))

plt.bar(top_names, top_averages)

plt.title("Top 5 Performing Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.tight_layout()

plt.show()



# PASS/FAIL PIE CHART

pass_count = (df["Result"] == "PASS").sum()
fail_count = (df["Result"] == "FAIL").sum()

labels = ["PASS", "FAIL"]
sizes = [pass_count, fail_count]

plt.figure(figsize=(7, 7))

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Pass/Fail Distribution")
plt.show()


# DEPARTMENT-WISE PERFORMANCE

department_avg = df.groupby("Department")["Average_Marks"].mean()

print("\n===== DEPARTMENT-WISE PERFORMANCE =====")
print(department_avg)

plt.figure(figsize=(8, 5))

department_avg.plot(kind="bar")

plt.title("Department-wise Average Performance")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)

plt.show()