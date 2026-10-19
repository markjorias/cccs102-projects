#resulting output will be the same as the sample output in the prog_exer_2
#first_number: 7
#second_number: 13
#Python 3.11.5

x = int(input("Enter your first number:"))
y = int(input("Enter your second number:"))
x, y = (y, x)
is_even_x = (x % 2 == 0)
is_odd_y = (y % 2 == 1)
z = (x + y)
left_shifted_z = (z << 2)
logical_result = (x > y & y < 10)
remainder = (z % 7)

print ("x: ", x)
print ("y: ", y)
print ("is_even_x: ", is_even_x)
print ("is_odd_y: ", is_odd_y)
print ("z: ", z)
print ("left_shifted_z: ", left_shifted_z)
print ("logical_result: ", logical_result)
print ("remainder: ", remainder)

