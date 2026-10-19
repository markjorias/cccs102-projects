print('Python List Methods:')
print('')

#append()
deciduous = ['narra', 'mahogany', 'acacia']
deciduous.append('molave')
print(deciduous)

#clear()
angiosperms = ['mango', 'coconut', 'papaya']
angiosperms.clear()
print(angiosperms)

#copy()
deciduous = ['narra', 'mahogany', 'acacia']
deciduous.copy()
print(deciduous)

#count()
deciduous = ['narra', 'mahogany', 'acacia']
x = deciduous.count("narra")
print(x)

#extend()
angiosperms = ['mango', 'coconut', 'papaya']
deciduous = ['narra', 'mahogany', 'acacia']
angiosperms.extend(deciduous)
print(angiosperms)

#index()
deciduous = ['narra', 'mahogany', 'acacia']
x = deciduous.index('mahogany')
print(x)

#insert()
angiosperms = ['mango', 'coconut', 'papaya']
angiosperms.insert(0, "guava")
print(angiosperms)

#pop()
deciduous = ['narra', 'mahogany', 'acacia']
deciduous.pop(1)
print(deciduous)

#remove()
angiosperms = ['mango', 'coconut', 'papaya']
angiosperms.remove("mango")
print(angiosperms)

#reverse()
deciduous = ['narra', 'mahogany', 'acacia']
deciduous.reverse()
print(deciduous)

#sort()
angiosperms = ['mango', 'coconut', 'papaya']
angiosperms.sort()
print(angiosperms)