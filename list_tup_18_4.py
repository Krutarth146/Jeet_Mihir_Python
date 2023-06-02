list1 = [10,90.34, "Anil", "J", True, 67+90j, [10,20,30,40], (20,303)]

list1.append(5000)
print(list1)   # [10, 90.34, 'Anil', 'J', True, (67+90j), [10, 20, 30, 40], (20, 303), 5000]

print(list1.count("Anil"))   # 1

list1.extend("Jeet")
print(list1)   # [10, 90.34, 'Anil', 'J', True, (67+90j), [10, 20, 30, 40], (20, 303), 5000, 'J', 'e', 'e', 't']


del list1[3:]

list2 = [10,20,30,40]

list1.append(list2)
print(list1)  # [10, 90.34, 'Anil', [10, 20, 30, 40]]

# list1.extend(list2)
# print(list1)   # [10, 90.34, 'Anil', 10, 20, 30, 40]

list1.insert(3,5000)
print(list1)  # [10, 90.34, 'Anil', 5000, [10, 20, 30, 40]]

list1.insert(-1,9000)
print(list1)   # [10, 90.34, 'Anil', 5000, 9000, [10, 20, 30, 40]]

list1[-1] = "Manoj"
print(list1)   # [10, 90.34, 'Anil', 5000, 9000, 'Manoj']



# Remove Elements

list1.pop()
print(list1.pop())
print(list1)   # [10, 90.34, 'Anil', 5000]



list1.pop(2)
print(list1)  # [10, 90.34, 5000]


list1.append(2)
print(list1)   # [10, 90.34, 5000, 2]
list1.remove(2)
print(list1)   # [10, 90.34, 5000]


# list1.clear()
# print(list1)   # []

list2 = list1.copy()   # shallow copy

list3 = list1   # deep copy


list1.append(1000)
print(list2)   # [10, 90.34, 5000]
print(list3)   # [10, 90.34, 5000, 1000]
 


print(list1.index(5000))  # 2

list1.reverse()
print(list1)   # [1000, 5000, 90.34, 10]


list1.sort()
print(list1)  # [10, 90.34, 1000, 5000]

list1.sort(reverse=True)
print(list1)  # [5000, 1000, 90.34, 10]  # Decresing Order


# List -> Ordered (Indexed), Allow's Duplicate Values, Mutable (Changeble)


list1= [90,32,21,56,77]

for i in list1:
    print(i,end=' ')  # 90 32 21 56 77

print()
for j in range(len(list1)):
    print(list1[j])

list1 = [(10,20), (40,59), (90,56), (45,32)]

print()
print()
print()
for i in list1:
    # print(i)  # (10,20)
    for h in i:
        if h % 2 != 0:
            print(h)

list3 = [90,43,21,67,54]

# ans = [[90,90], [90,43], [90,21], [90,67].....]

def Combination(list50):
    ans = [] 
    for i in list50:
        for d in list50: 
            ans.append([i,d])  

    return ans

print(Combination(list3)) # [[90, 90], [90, 43], [90, 21], [90, 67], [90, 54], [43, 90], [43, 43], [43, 21], [43, 67], [43, 54], [21, 90], [21, 43], [21, 21], [21, 67], [21, 54], [67, 90], [67, 43], [67, 21], [67, 67], [67, 54], [54, 90], [54, 43], [54, 21], [54, 67], [54, 54]]


# Tuples : ordered (Indexed), Allow's Duplicates, Immuatble (Not Changeble)


tuple1 = (10,20,304,60,90,90,90,90)
print(tuple1)   # (10, 20, 304, 60, 90, 90, 90, 90)
# Indexing
print(tuple1[0])  # 10
print(tuple1[-2])  # 60
print(type(tuple1[-2]))  # int



# Slicing
print(tuple1[-2:1:2])  # ()
print(tuple1[-2:2:-2]) # (60,)
print(type(tuple1[-2:2:-2]))  # tuple

print(tuple1.count(90))   # 4
print(tuple1.index(20))   # 1

tup2 = (10,290,80)

print(id(tuple1))   # 2207175906736
tuple1 += tup2
print(id(tuple1))   # 2207175629760

print(tuple1)  # (10, 20, 304, 60, 90, 90, 90, 90, 10, 290, 80)

list1 = list(tuple1)

list1.insert(2,10000)

print(tuple(list1))   # (10, 20, 10000, 304, 60, 90, 90, 90, 90, 10, 290, 80)


# Set -> Don't Allow Duplicates

# tuple1 = tuple(set(tuple1))
# print(tuple1)   # (290, 10, 304, 80, 20, 90, 60)

res = []
for u in tuple1:
    if u not in res:
        res.append(u)

res= tuple(res)

print(res)  # (10, 20, 304, 60, 90, 290, 80)

# Bank

# deposit, withdraw --> balance

# Bank ROI --> if Changed Loss


# username, password, email  --> django
