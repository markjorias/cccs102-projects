colleges = {}
while True:
    try:
        num_colleges = int(input("How many colleges are available? "))
        break
    except ValueError:
        print("Please enter a valid number.")

for i in range(num_colleges):
    college_name = input("Enter the name of the college: ")
    while True:
        try:
            num_programs = int(input(f"How many programs are available at {college_name}? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    programs = []
    for i in range(num_programs):
        program = input("Enter a program: ")
        programs.append(program)
    
    colleges[college_name] = programs

print(f"The created dictionary for all colleges {colleges}")

search_college = input("Enter the name of the college to search: ")
if search_college in colleges:
    print(*colleges[search_college])
else:
    print(f"{search_college} is not found in the list of colleges.")