file = open("grades.txt", "r")
data = file.readlines()
file = open('average_grades.txt','w')
for line in data:
    word = line.split()
    name = word[0]
    number = word[1:]
    number = [int(num) for num in number]
    average = sum(number) / len(number)
    file.write (f"{name} {average}\n")
    file.close
file.close