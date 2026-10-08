def calculate_grade(average):
    """Return a grade based on the student's average marks."""

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


def check_pass_fail(python, mathematics, data_analysis, average):
    """Return PASS or FAIL based on subject and average marks."""

    if (
        python >= 33
        and mathematics >= 33
        and data_analysis >= 33
        and average >= 40
    ):
        return "PASS"
    else:
        return "FAIL"