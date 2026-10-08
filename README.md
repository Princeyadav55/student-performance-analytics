# Student Performance Analytics System

## Project Overview
A Python-based project that analyzes student marks, grades, pass/fail results, attendance and department-wise performance using Pandas, NumPy and Matplotlib.

## Objective
To calculate student performance statistics and generate meaningful insights from the student dataset.

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- CSV

## Dataset
The project uses `students.csv`, containing 20 student records with these columns:
- Student_ID
- Name
- Department
- Python
- Mathematics
- Data_Analysis
- Attendance

## Project Structure
```text
Student-Performance-Analytics/
├── main.py
├── functions.py
├── students.csv
├── README.md
├── requirements.txt
├── Project_Documentation.txt
└── .gitignore
```

## Key Features
- Loads and examines student data using Pandas
- Calculates total and average marks
- Assigns grades based on average marks
- Calculates PASS/FAIL status
- Identifies top five students
- Calculates class and subject-wise averages
- Analyzes grade distribution
- Reports highest- and lowest-performing students
- Analyzes attendance and identifies attendance below 75%
- Calculates department-wise average performance
- Generates four performance graphs

## Grade Rules
- 90 or above: A+
- 80 to below 90: A
- 70 to below 80: B
- 60 to below 70: C
- 50 to below 60: D
- Below 50: F

## Pass/Fail Rules
A student passes when all three subject marks are at least 33 and the overall average is at least 40. Otherwise, the student fails.

## Visualizations
1. Subject-wise Average Performance
2. Top 5 Performing Students
3. Student Pass/Fail Distribution
4. Department-wise Average Performance

## Results
Based on the current dataset:
- Total students: 20
- Class average: 71.55
- Passed: 19
- Failed: 1
- Pass percentage: 95%
- Fail percentage: 5%
- Best-performing subject: Data Analysis
- Highest-performing student: Kavita (95.33 average)
- Lowest-performing student: Karan (38.00 average)
- Average attendance: 83.40%

## How to Run

Install the dependencies:
```bash
pip install -r requirements.txt
```

Run the project:
```bash
python main.py
```

The program displays the analysis in the terminal and generates performance graphs.

## Project Documentation
See `Project_Documentation.txt` for the objective, implementation, results, learning outcomes and other project details.

## GitHub Repository
https://github.com/Princeyadav55/student-performance-analytics

## Conclusion
This project demonstrates Python functions, conditions, loops, CSV handling, NumPy, Pandas and data visualization for student performance analysis.
