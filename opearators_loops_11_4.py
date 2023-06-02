# Assignment O/p    -> =  += -= *= /= //= %= <<= >>= &= |= ^=   -> Priority Low

x = 90

x += 10   # x = x + 10  # 100
x -= 5    # x = 95
x %= 2    # x = 1
x *= 9    # x = 9
print(x)   # 9



# Loops
# Entry control Loops
# 1. For    2. While


# 22 to 44 Print

jeet = 22    # Intialization

while jeet <= 44:
    print(jeet,end=' ')
    jeet += 1

print()
# -------- Reverse


# Logical Operators   -> and or not


mihir = 101

while mihir >= 25:
    if mihir % 5 == 0 and mihir % 7 == 0:
        print(mihir,end=' ')   # 70 35
    mihir-=1


print()
print()
print()
mihir = 101

while mihir >= 25:
    if mihir % 5 == 0 and (mihir % 7 == 0 or mihir % 10 == 0):
        print(mihir,end=' ')   # 100 90 80 70 60 50 40 35 30
    mihir-=1




# Continue , Break

j = 10

while j<=20:
    j+=1
    if j==15:
        continue
    print(j)


# Membership o/p     -> in, not in 

# For Loop

for _ in range(10):    # 10 is End Position , Defualt - 0
    print(_,end=' ')   # 0 1 2 3 4 5 6 7 8 9

print()
for kru in range(3,10):   # 3 is Start, 10 is End (n-1)
    print(kru,end=' ')  # 3 4 5 6 7 8 9

print()
for kru in range(10,3,1):   
    print(kru,end=' ')  # blank

print()
for kru in range(3,10,2):   # start -3, end = 10 (10 -1) = 9, step = 2 (2-1) = 1   
    print(kru,end=' ')   # 3 5 7 9 

print()
for kru in range(-8,2,2):   # start -3, end = 10 (10 -1) = 9, step = 2 (2-1) = 1   
    print(kru,end=' ')   # -8 -6 -4 

print()
for kru in range(15,2,-2):   # 
    print(kru,end=' ')   # 15 13 11 9 7 5 3

print()
for kru in range(-2,-8,-3):   # 
    print(kru,end=' ')   # -2 -5


for j in range(3):
    for w in range(5):
        if j == w:
            # print(w)
            break
    print(w)     # 0 1 2
    


list1 = [10,20,30,50,33,22,66,11,90,10,20,30]


# Linear Search

for i in list1:
    print(i,end='\t')  # 10      20      30      50      33      22      66      11      90      10      20      30
user_need = int(input())

counter = 0

for j in list1:
    if j == user_need:
        print(f"{user_need} is Found")
        break
    counter += 1

print(counter)

#  --------- Membership O/p   -> in , not in 

if user_need in list1:
    print(f"{user_need} is Found")
else:
    print(False)


# Identity O/p    -> is , is not

x = 900
y = 900


# if x == y:
#     print("== Same")
# if x is y:
#     print("is Same")

list1 = [10,20,30]
list2 = [10,20,30]

if list1 == list2:   # Element Check
    print("== Same")

if list1 is list2:   # Reference Check
    print("is Same")

list3 = list2

if list3 is list2:
    print("is Same")

    
# While -> Sum of Digits, Sum of Numbers, Find Power, Reverse Number Print, Palindrome (1 to 10000), Armstrong (1 to 10000), Prime (1 to 10000) All Methods, Perfect Number, Twin Number