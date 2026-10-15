import streamlit as st
import pandas as pd
from functions import calculate_grade, check_pass_fail

# Page settings
st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("students.csv")

df = load_data()

# Calculate student results
df["Total"] = df[
    ["Python", "Mathematics", "Data_Analysis"]
].sum(axis=1)

df["Average"] = df[
    ["Python", "Mathematics", "Data_Analysis"]
].mean(axis=1).round(2)

df["Grade"] = df["Average"].apply(calculate_grade)

df["Result"] = df.apply(
    lambda row: check_pass_fail(
        row["Python"],
        row["Mathematics"],
        row["Data_Analysis"],
        row["Average"]
    ),
    axis=1
)

# Page heading
st.title("📊 Student Performance Analytics System")
st.write("Analyze student marks, grades, results, and attendance.")

st.divider()

# Summary metrics
total_students = len(df)
class_average = round(df["Average"].mean(), 2)
passed = int((df["Result"] == "PASS").sum())
failed = int((df["Result"] == "FAIL").sum())

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", total_students)
col2.metric("Class Average", class_average)
col3.metric("Passed", passed)
col4.metric("Failed", failed)

st.divider()

# Student records
st.subheader("Student Records")

search = st.text_input("Search student by name")

display_df = df.copy()

if search:
    display_df = display_df[
        display_df["Name"].astype(str).str.contains(
            search, case=False, na=False
        )
    ]

st.dataframe(display_df, use_container_width=True, hide_index=True)

# Subject analysis
st.subheader("Subject-wise Average Marks")

subject_averages = df[
    ["Python", "Mathematics", "Data_Analysis"]
].mean().round(2)

st.bar_chart(subject_averages)

# Result analysis
st.subheader("Pass and Fail Analysis")

result_counts = df["Result"].value_counts()

st.bar_chart(result_counts)

# Top students
st.subheader("Top 5 Students")

top_students = df.nlargest(5, "Average")[
    ["Student_ID", "Name", "Average", "Grade", "Result"]
]

st.dataframe(top_students, use_container_width=True, hide_index=True)

# Attendance analysis
st.subheader("Student Attendance")

st.bar_chart(
    df.set_index("Name")["Attendance"]
)

st.caption("Student Performance Analytics System | Python, Pandas, NumPy and Streamlit")