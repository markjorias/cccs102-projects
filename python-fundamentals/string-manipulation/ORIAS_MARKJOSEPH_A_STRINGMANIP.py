string = str(input("Enter a string: "))

letter_count, digit_count, space_count, symbol_count = 0, 0, 0, 0

for letter in string:
    if letter.isalpha():
        letter_count += 1
    elif letter.isdigit():
        digit_count += 1
    elif letter.isspace():
        space_count += 1
    else:
        symbol_count += 1

print("Letters: ", letter_count)
print("Digits: ", digit_count)
print ("Spaces: ", space_count)
print("Special Symbols: ", symbol_count)
