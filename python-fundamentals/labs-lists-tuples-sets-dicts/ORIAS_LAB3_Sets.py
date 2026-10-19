print('Python Set Methods')
print('')

#xiaomi = {mi, redmi, poco, mimix, blackshark}
#oppo = {find, reno, f, a}

#add()
xiaomi = {'mi', 'redmi', 'poco', 'mimix'}
xiaomi.add('blackshark')
print(xiaomi)

#clear()
oppo = {'find', 'reno', 'f', 'a'}
oppo.clear()
print(oppo)

#copy()
xiaomi = {'mi', 'redmi', 'poco', 'mimix'}
xiaomi.copy()
print(xiaomi)

#difference()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
series = oppo.difference(samsung) 
print(series)

#difference_update()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
samsung.difference_update(oppo) 
print(samsung)

#discard()
xiaomi = {'mi', 'redmi', 'poco', 'mimix'}
xiaomi.discard('mimix')
print (xiaomi)

#intersection()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
series = samsung.intersection(oppo)
print(series)

#intersection_update()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
oppo.intersection_update(samsung)
print(oppo)

#isdisjoint()
xiaomi = {'mi', 'redmi', 'poco', 'mimix'}
oppo = {'find', 'reno', 'f', 'a'}
series = xiaomi.isdisjoint(oppo)
print(series)

#issubset()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
series = oppo.issubset(samsung)
print(series)

#issuperset()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
series = oppo.issubset(samsung)
print(series)

#pop()
oppo = {'find', 'reno', 'f', 'a'}
oppo.pop()
print (oppo)

#remove()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
samsung.remove('note')
print (samsung)

#symmetric_difference()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
series = oppo.symmetric_difference(samsung)
print(series)

#symmetric_difference_update()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
samsung.symmetric_difference_update(oppo)
print(samsung)

#union()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
series = samsung.union(oppo)
print(series)

#update()
samsung = {'s', 'note', 'zflip', 'a', 'f'}
oppo = {'find', 'reno', 'f', 'a'}
oppo.update(samsung)
print(oppo)