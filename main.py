def divide(value):
    if not value:
        return 0

    return sum(value) / len(value)



students = {
    'Alice': {'name': 'Alice', 'grade': [85,90]},
    'Bob': {'name': 'Bob', 'grade': [92, 75]},
    'Charlie': {'name': 'Charlie', 'grade': None},
    'Diana': {'name': 'Diana', 'grade': [78, 85]}
}

try:
    for student in students:
        student = students[student]
        name = student['name']
        grade = student['grade']

        if grade is None:
            print(f"{name} has no grade")
            continue
        average = divide(grade)
        print(f'{name} average {average}')
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")
else:
    print('all students grades are completed')
finally:
    print('Thank you')






