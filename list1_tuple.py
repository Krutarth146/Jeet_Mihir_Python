# Bitwise Operator & | ^ << >>

print(20 & 30)   # 20
print(20 | 30)   # 30
print(20 ^ 30)   # 10




# Collections -> List [], Tuple (), Set {}, Dict {} (key - values Pairs), string "" '' '''


# List ---> Allow Duplicates, Ordered

list1 = [10,20,30,90,10,10]
print(list1)   # [10, 20, 30, 90, 10, 10]

print(type(list1))  # <class 'list'>

print(len(list1))   # 6   # Length starts from 1 and Index starts from 0

print(list1.__sizeof__())   # 88
print(id(list1))   # 3135963976128


# Indexing
list1 = [10,20, 90.89, "Manoj", 'R', 67 + 90j, True, [10,20,30], ((10,20,"Str1"), (90,90)), {"set1",'set1'}, {"Name" : "Mihir", "address" : {'city' : "Ahm", 'state' : "USA"}}]
print(list1)  # [10, 20, 90.89, 'Manoj', 'R', (67+90j), True, [10, 20, 30], ((10, 20, 'Str1'), (90, 90)), {'set1'}, {'Name': 'Mihir', 'address': {'city': 'Ahm', 'state': 'USA'}}]


list2 = [10,20,30,40,50,99,22,10]

print(list2[2])  # 30
print(list2[-2])  # 22
print(list2[6])  # 22

# Slicing

# print(list2[start : End(n-1)])
list2 = [10,20,30,40,50,99,22,10]
print(list2[0:5])  # start - 0, End - 4   # [10, 20, 30, 40, 50]
print(list2[5:2])  # []
print(list2[3:6])  # [40,50,99]
print(list2[3:])  # [40, 50, 99, 22, 10]
print(list2[:6])  # [10, 20, 30, 40, 50, 99]
print(type(list2[-5:-4]))  # <class 'list'>
# print(type(list2[start : end : step (n-1) (default - 1)]))  # <class 'list'>


print(list2[3:7:1])  # [40, 50, 99, 22]
print(list2[3:7:2])  # [40, 99]

list2 = [10,20,30,40,50,99,22,10]
print(list2[-5:-1:2])  # [40, 99]

list2 = [10,20,30,40,50,99,22,10]
print(list2[-1:-5:-2])  # [40, 99]
print(list2[-1::-2])  # [10, 99, 40, 20]
print(list2[::-2])  # [10, 99, 40, 20]
print(list2[::])  # [10, 20, 30, 40, 50, 99, 22, 10]
print(list2[:-4:])  # [10, 20, 30, 40]
print(list2[:-4:-1])  # [10, 22, 99]
print(list2[::-1])  # [10, 22, 99, 50, 40, 30, 20, 10]

print(list2[-3:4:2])   # []   blank list
print(list2[-3:4:-2])   # [99]


# ----------------------------------------------------

# list Methods : ------------------------


list3 = [10,20,30,40,"Manoj"]

print(list3.index(40))  # 3   # Gives Index of Particular Element
print(list3.count(40))   # 1  # Gives Total NO. Of frequency

list4 = [10,20]

list3 += list4
print(list3)  # [10, 20, 30, 40, 'Manoj', 10, 20]

list3.append(900)
print(list3)   # [10, 20, 30, 40, 'Manoj', 10, 20, 900]

list3.append("Jeet")
print(list3)  # [10, 20, 30, 40, 'Manoj', 10, 20, 900, 'Jeet']


# list3.extend(1000)   # Does nOt support Int object
list3.extend("Ashok")
print(list3)  # [10, 20, 30, 40, 'Manoj', 10, 20, 900, 'Jeet', 'A', 's', 'h', 'o', 'k']


list6 = [10,20,30,40]

list3.append(list6)
print(list3)  # [10, 20, 30, 40, 'Manoj', 10, 20, 900, 'Jeet', 'A', 's', 'h', 'o', 'k', [10, 20, 30, 40]]

# list3.extend(list6)
# print(list3)  # [10, 20, 30, 40, 'Manoj', 10, 20, 900, 'Jeet', 'A', 's', 'h', 'o', 'k', 10, 20, 30, 40]


list3.insert(3,6000)
print(list3)  # [10, 20, 30, 6000, 40, 'Manoj', 10, 20, 900, 'Jeet', 'A', 's', 'h', 'o', 'k', [10, 20, 30, 40]]

list3.insert(-1,9000)
print(list3)  # [10, 20, 30, 6000, 40, 'Manoj', 10, 20, 900, 'Jeet', 'A', 's', 'h', 'o', 'k', 9000, [10, 20, 30, 40]]

list3[-1] = 8000
print(list3)  # [10, 20, 30, 6000, 40, 'Manoj', 10, 20, 900, 'Jeet', 'A', 's', 'h', 'o', 'k', 9000, 8000]