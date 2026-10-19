# SAMPLE OUTPUT: Task Guide #
#Enter student's name: Ryan Bang
#Enter student's age: 23
#Student information successfully recorded:
#Name: Ryan Bang
#Age: 23

class student:
    def __init__(self):
        while True:
            self.name = input("Enter student's name: ")
            if self.name.replace(' ','').isalpha() == True: # This code
                break
            else:
                print("Please input a valid name.")
                
        while True:
            self.age = input("Enter student's age: ")
            if self.age.isdigit() == True:
                break
            else:
                print("Please enter a number only.")

    def displayStudent(self):
        print(f"Student information successfully recorded:\nName: {self.name} \nAge: {self.age}")

stu1 = student()
stu1.displayStudent()