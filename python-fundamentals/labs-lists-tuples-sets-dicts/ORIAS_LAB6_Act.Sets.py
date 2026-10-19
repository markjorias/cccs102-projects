brands = {'samsung', 'oppo', 'vivo', 'xiaomi', 'redmi', 'poco', 'realme'}
input = {str(input('Please enter a smartphone brand:'))}
check = brands.issuperset(input)

if check == True:
    print('This brand is in the set')
else:
    print('This brand does not exist')