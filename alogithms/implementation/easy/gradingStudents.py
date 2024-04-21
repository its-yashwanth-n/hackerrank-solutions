# https://www.hackerrank.com/challenges/grading/problem

# Time Complexity: O(n)
# Space Complexity O(n)

def gradingStudents(grades):
    final_grades = grades

    for i in range(len(grades)):
        remainder = grades[i] % 5
        if grades[i] >= 38 and remainder > 2:
            final_grades[i] = final_grades[i] + 5 - remainder

    return final_grades


# Using comprehension
def gradingStudents(grades):
    final_grades = [(grade + 5) - (grade % 5) if grade >=
                    38 and (grade % 5) > 2 else grade for grade in grades]
    return final_grades
