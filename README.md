\# Student Performance Analytics System



\## Project Overview



Student Performance Analytics System is a Python-based data analysis project developed using Python, NumPy and Pandas.



The project reads student data from a CSV file and analyzes student academic performance, grades, pass/fail results, attendance and department-wise performance.



\## Objective



The main objective of this project is to analyze student performance and generate meaningful results such as:



\- Total and average marks

\- Student grades

\- Pass/Fail status

\- Class performance

\- Subject-wise performance

\- Top-performing students

\- Highest and lowest-performing students

\- Attendance analysis

\- Department-wise performance

\- Graphical visualization of results



\## Technologies Used



\- Python

\- NumPy

\- Pandas

\- Matplotlib

\- CSV Dataset



\## Dataset



The project uses `students.csv`.



The dataset contains 20 student records with the following columns:



\- Student\_ID

\- Name

\- Department

\- Python

\- Mathematics

\- Data\_Analysis

\- Attendance



\## Project Structure



```text

Student-Performance-Analytics/

│

├── main.py

├── functions.py

├── students.csv

├── main\_backup.py

├── README.md

└── .gitignore
## Implementation

### 1. Data Loading

The student dataset is loaded using Pandas from the `students.csv` file.

### 2. Marks Calculation

Total marks and average marks are calculated for every student.

Total Marks = Python + Mathematics + Data Analysis

Average Marks = Total Marks / 3

### 3. Grade Calculation

Grades are assigned according to the student's average marks:

- 90 or above → A+
- 80–89 → A
- 70–79 → B
- 60–69 → C
- 50–59 → D
- Below 50 → F

### 4. Pass/Fail Calculation

A student is marked PASS when:

- Python marks are at least 33
- Mathematics marks are at least 33
- Data Analysis marks are at least 33
- Average marks are at least 40

Otherwise, the student is marked FAIL.

### 5. Performance Analysis

The project calculates:

- Class average
- Highest average
- Lowest average
- Subject-wise averages
- Top 5 performing students
- Pass percentage
- Fail percentage
- Highest-performing student
- Lowest-performing student
- Average attendance
- Highest attendance
- Lowest attendance
- Students with attendance below 75%
- Department-wise average performance

## Visualizations

The project generates the following visualizations:

1. Subject-wise Average Performance
2. Top 5 Performing Students
3. Student Pass/Fail Distribution
4. Department-wise Average Performance

## Key Results

Based on the current dataset:

- Total Students: 20
- Class Average: 71.55
- Passed Students: 19
- Failed Students: 1
- Pass Percentage: 95%
- Fail Percentage: 5%
- Best Performing Subject: Data Analysis
- Highest-performing Student: Kavita
- Highest Average: 95.33
- Lowest-performing Student: Karan
- Lowest Average: 38.00
- Average Attendance: 83.40%

## How to Run

### Step 1: Install Required Libraries

Open PowerShell in the project folder and run:

```bash
pip install pandas numpy matplotlib
