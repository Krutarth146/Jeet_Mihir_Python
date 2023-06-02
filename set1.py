set1 = {10}
print(set1)
print(type(set1))  # <class 'set'>

set2 = set()
print(type(set2))  # <class 'set'>


# Set ------>  Don't Allow Duplicates, Unordered (Unindexed), Immutable (But u can add or delete Elements)
#  Set items are unchangeable, but you can remove items and add new items.
set3 = {10,20,10,10,90.78, True, 3+5j, (10,20,30)}
print(set3)  # {True, (3+5j), 20, 90.78, 10, (10, 20, 30)}

# print(set3[0])  # TypeError: 'set' object is not subscriptable

# Set Methods

set3.add(5000)
print(set3)  # {True, (3+5j), 20, 90.78, 5000, 10, (10, 20, 30)}

# set3.clear()

# del set3

set4 = set3.copy()   # Shallow Copy

set5 = set3  # Deep Copy

set3 = {10,20,30,40}
set4 = {30,40,50,60,70}

# print(set3.difference(set4))  # {10,20}
# print(id(set3))   # 2149364305696
# set3.difference_update(set4)
# print(id(set3))   # 2149364305696
# print(set3)



# set3.remove(20)   # {10}  # If element is not found then it will generates an Error
# set3.discard(20)  # If element is not found then it ignores error
print(set3)   # {40, 10, 20, 30}


print(set3.intersection(set4))  # {40, 30}


set3 = {7,8,90,121,1,60,70}
set4 = {30,40,50,60,70}
print(set3.isdisjoint(set4)) # True
print(set3.issubset(set4))   # True
print(set4.issuperset(set3))  # True


# set3.pop()
# set3.pop()
print(set3)

print(set3.symmetric_difference(set4))  # {1, 7, 8, 90, 30, 40, 50, 121}
print(set3.difference(set4))  # {1, 7, 8, 121, 90}

set3 = set3.union(set4)
print(set3)

set3.update((40000,21211,"str1"))
print(set3)

# set4 = {[10,20,30]}


# Frozen set -----> Imutable



# String Methods

# oye balle balle oye

# OyE BallE BallE OyE

# String Is Imutable

str1 = "oye belle belle oye"

str1 = str1.title()

print(str1)


list1 = str1.split(' ')

print(list1)
main = []
for i in list1:
    temp = i[::-1].replace('e','E',1)
    temp = temp[::-1]
    main.append(temp)

print(main)


str3 = 'belle'


str3 = str3.title()

print(str3[-1].upper())

main1 = []
for i in list1:
    str4 = i[0:len(i)-1]
    print(str4)
    str4 = str4 + ''.join(i[-1].upper())
    main1.append(str4)
print(main1)   # ['OyE', 'BellE', 'BellE', 'OyE']
