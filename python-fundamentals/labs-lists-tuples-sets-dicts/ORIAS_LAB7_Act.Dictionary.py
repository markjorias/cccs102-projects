number_of_students = int(input("Enter the number of students: "))

students = dict()
for _ in range(number_of_students):
    while True:
        name = input('Please input the name of the student: ')
        if name.isalpha():
            break
        else:
            print('That is not a name!')

    while True:
        try:
            average = float(input("Please input the average of the student: "))
            break
        except ValueError:
            print('That is not a number!')

    students[name] = average

print('{:<15} {:<15}'.format('Name of Students', 'Average'))
for name, average in students.items():
    print('{:<15} {:<15}'.format(name, average))