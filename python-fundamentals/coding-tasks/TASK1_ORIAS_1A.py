class stud_info:
    def __init__ (self):
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.address = input("Enter Address: ")
        self.year = input("Enter Year: ")
        self.section = input("Enter Section: ")
        self.program = input("Enter Program: ")

    def displayInfo(self):
        print (f"\nStudent Information:\nName: {self.name}\nAge: {self.age}\nAddress: {self.address}\nYear: {self.year}\nSection: {self.section}\nProgram: {self.program}")

student = stud_info()
student.displayInfo()