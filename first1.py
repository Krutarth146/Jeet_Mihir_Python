print("""
    Hello, Jeet and Mihir
    Ahm
""")

print("Hello",end='_krutarth_')
print("Good Evening")  # Hello_krutarth_Good Evening


# Python Interpreter, Dynamic Lang.

x = 903232222222222222222222222
print(type(x))   # <class 'int'>

g = 90.67
print(type(g))  # <class 'float'>

y = 'w'
print(type(y))   # <class 'str'>

print(x,g,y,sep='_')   # 903232222222222222222222222_90.67_w

# Input()

# scanf("%d",&num1);

'''
    sdvsd
    vsd
    v
    sdv
    sv
'''


# num1 = int(input("Enter Number: "))
# # print(num1)
# print(type(num1))   # <class 'str'>

# num2 = int(input("ENter num2: "))
# print(num1 + num2)   # 342


# # Arithmetic O/p
# print(num1,'+',num2,'=',num1+num2)
# print(num1,'-',num2,'=',num1-num2)
# print(num1,'*',num2,'=',num1*num2)
# print(num1,'/',num2,'=',num1/num2)   # 25 / 2 = 12.5   (float)
# print(num1,'//',num2,'=',num1//num2)  # 25 // 2 = 12  (floor Division)
# print(num1,'%',num2,'=',num1%num2)    # 25 % 2 = 1  (remainder)
# print(num1,'**',num2,'=',num1**num2)  # Power  25 * 25 = 625


# Typecasting

# To convert one Datatype to another datatype
# 1. Implicit Typecasting
# 2. Explicit Typecasting


_dhiraj_sir = 78.9999999

print(_dhiraj_sir)   # 78.89

print(int(_dhiraj_sir))  # 78   # Explicit Typecasting

import math

print(math.ceil(_dhiraj_sir))   # 79
print(math.floor(_dhiraj_sir))   # 78


h = True   # Bool
w = 90     # int

print(h+w)   # 91 -> Implicit Typecasting

w = 90
q = 88.21

print(w+q)   # 178.20999999999998  # Implicit


e = "31.67"
# print(int(e))   # 3167
print(int(float(e)))   # 31   # Explicit


# Operators

# 1. Arithmetic o/p   + - * / % // **
# 2. Assignment o/p -> Low Priority  += -= *= /= //= %= <<= >>= |= &= ^= =
# 3. Bitwise o/p    & | ^
# 4. Logical o/p   and or not
# 5. Membership o/p    in  not in
# 6. Identity o/p      is    is not
# 7. Relational O/p  (Comparison O/p)   == != < > <= >=

print(2**3**2)   # 64



x = 0

if x > 0:
    print(f"{x} is Positive")   # fstring (Adv. formatted string)
elif x == 0:
    print(f"{x} is zero")     # 0 is zero
else:
    print(f"{x} is Negative")


num1 = 90
num2 = 890

if num1 > num2:
    print("num1 is Max")

else:
    print("num2 is Max")  

max = num1 if num1 > num2 else num2
print(max)

# num1 is Max

num1 = 90
num2 = 56
num3 = 77

if num1 > num2:
    if num1 > num3:
        print("num1 is Max")
    else:
        print("num3 is Max")
else:
    if num2 > num3:
        print("num2 is Max")
    else:
        print("num3 is Max")

# One Liner int his Program
