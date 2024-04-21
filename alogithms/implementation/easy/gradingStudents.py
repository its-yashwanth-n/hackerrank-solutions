def gradingStudents(grades):
    final_grades = grades

    for i in range(len(grades)):
        remainder = grades[i] % 5
        if grades[i] >= 38 and remainder > 2:
            final_grades[i] = final_grades[i] + 5 - remainder
    
    return final_grades
