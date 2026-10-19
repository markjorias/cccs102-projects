#resulting output will be the same as the sample output in the prog_exer_1
#first_number: 4.6
#second_number: 3.8
#Python 3.11.5

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
add_result = (num1 + num2)
sub_result = (num1 - num2)
mul_result = (num1 * num2)
div_result = (num1 / num2)
equal_result = (num1 == num2)
greater_result = (num1 > num2)
less_equal_result = (num2 <= num2)
bitwise_and_result = int(num1) & int(num2)
bitwise_or_result = int(num1) | int(num2)
logical_and_result = (equal_result < greater_result and greater_result < equal_result)
logical_or_result = (less_equal_result > bitwise_and_result or less_equal_result < bitwise_and_result)

print ("Addition result: ", add_result)
print ("Subtraction result: ", sub_result)
print ("Multiplication result: ", mul_result)
print ("Division result: ", div_result)
print ("Equal result: ", equal_result)
print ("Greater result: ", greater_result)
print ("Less or equal result: ", less_equal_result)
print ("Bitwise AND result: ", bitwise_and_result)
print ("Bitwise OR result: ", bitwise_or_result)
print ("Logical AND result:", logical_and_result)
print ("Logical OR result: ", logical_or_result)
