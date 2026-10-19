print('Python Dictionary Methods')
print('')

#clear()
A_to_C = {"A": "Alligator","B": "Bear","C": "Cow"}
A_to_C.clear()
print(A_to_C)

#copy()
D_to_F = {"D": "Dog","E": "Elephant","F": "Fox"}
D_to_F.copy()
print(D_to_F)

#fromkeys()
G_to_H = ('G', 'H', 'I')
third_value = "Error"
third_dict=dict.fromkeys(G_to_H, third_value)
print (third_dict)

#get()
J_to_L = {"J": "Jellyfish","K": "Kangaroo","L": "Lion"}
x = J_to_L.get("L")
print (x)

#items()
M_to_O = {"M": "Monkey","N": "Nutria","O": "Ostrich"}
items = M_to_O.items()
print(items)

#keys()
P_to_R = {"P": "Pig","Q": "Quail","R": "Rabbit"}
keys = P_to_R.keys()
print(keys)

#pop()
S_to_U = {"S": "Giraffe","T": "Hippo","U": "Iguana"}
S_to_U.pop("T")
print(S_to_U)

#popitem()
V_to_X = {"V": "Vampire","W": "Walrus","X": "Xerus"}
V_to_X.popitem()
print(V_to_X)

#setdefault()
x = V_to_X.setdefault("X", "Xylophone")
print(x)

#update()
Y_to_Z = {"Y": "Yak","Z": "Zebra",}
Y_to_Z.update({"Z":"Alligator"})
print(Y_to_Z)

#values()
x = Y_to_Z.values()
print(x)