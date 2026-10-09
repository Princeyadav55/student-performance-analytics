# Student Performance Analytics System

## Project Overview

Student Performance Analytics System is a Python-based data analysis project developed using Python, NumPy, Pandas and Matplotlib.

The project reads student data from a CSV file and analyzes academic performance, grades, pass/fail results, attendance and department-wise performance.

## Objective

The objective of this project is to analyze student performance and generate useful insights, including:

- Total and average marks
- Student grades
- Pass/fail results
- Class performance
- Subject-wise performance
- Grade distribution
- Top 5 performing students
- Highest and lowest-performing students
- Attendance analysis
- Department-wise performance
- Graphical visualization of results

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- CSV Dataset

## Dataset Description

The project uses the `students.csv` file.

The dataset contains 20 student records and the following columns:

- Student_ID
- Name
- Department
- Python
- Mathematics
- Data_Analysis
- Attendance

## Project Structure

    Student-Performance-Analytics/
    ├── main.py
    ├── functions.py
    ├── students.csv
    ├── main_backup.py
    ├── README.md
    └── .gitignore

## Implementation

### 1. Data Loading

Pandas is used to load student records from `students.csv`.

### 2. Total and Average Marks

The project calculates total and average marks for every student.

Total Marks = Python + Mathematics + Data Analysis

Average Marks = Total Marks / 3

### 3. Grade Calculation

The `calculate_grade()` function assigns grades according to average marks:

- 90 or above: A+
- 80 to below 90: A
- 70 to below 80: B
- 60 to below 70: C
- 50 to below 60: D
- Below 50: F

### 4. Pass/Fail Calculation

The `check_pass_fail()` function marks a student as PASS when all of these conditions are met:

- Python marks are at least 33.
- Mathematics marks are at least 33.
- Data Analysis marks are at least 33.
- Average marks are at least 40.

Otherwise, the student is marked FAIL.

### 5. Performance Analysis

The project calculates:

- Class average, highest average and lowest average
- Subject-wise average marks and best-performing subject
- Grade distribution
- Top 5 performing students
- Pass/fail counts and percentages
- Highest and lowest-performing students
- Average, highest and lowest attendance
- Students with attendance below 75%
- Department-wise average marks

## Visualizations

The project generates four graphs:

1. Subject-wise Average Performance
2. Top 5 Performing Students
3. Student Pass/Fail Distribution
4. Department-wise Average Performance

## Key Results

The following results were obtained from the current dataset:

- Total Students: 20
- Class Average: 71.55
- Passed Students: 19
- Failed Students: 1
- Pass Percentage: 95.00%
- Fail Percentage: 5.00%
- Best Performing Subject: Data Analysis
- Highest-performing Student: Kavita
- Highest Average: 95.33
- Lowest-performing Student: Karan
- Lowest Average: 38.00
- Average Attendance: 83.40%

## How to Run

### Step 1: Install Dependencies

Open PowerShell in the project folder and run:

    pip install pandas numpy matplotlib

### Step 2: Run the Program

Run:

    python main.py

The program displays the analysis results in the terminal and opens the performance graphs.

## Conclusion

The project demonstrates the use of Python functions, CSV file handling, Pandas, NumPy and Matplotlib to analyze student marks and attendance and visualize performance results.
