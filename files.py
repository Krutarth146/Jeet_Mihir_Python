# Files 

# File Types  1. Text File  2. Binary File

# Modes

# 'w' --> Write Mode (Overwrite) If file is not exist then it will create new one.
    # if file is already exists then ignores.

# 'r' --> Read Mode # If file does not exist then it will give Error

# 'a' --> Append Mode # If file Does not Exist then it will create new one.
# [Add the data from last line of code] 

# '+' --> Read + Write Both

# 'x' --> If file does not Exist then It will create a new one, if file already Exist then it will generate an Error


fp = open("first.txt",'w')
# fp = open("first.txt",'a')

print(fp.tell())   # 0
fp.write("Hello Jeet How are You???\nMihir, How Are??")
print(fp.tell())   # 43
list1 = ["\nRoyal Institute\n", "Best Institute\n", "India Country\n"]

fp.writelines(list1)
fp.close()

f1 = open("first.txt","rt+")

print(f1.tell())  # 0
x = f1.read()
print(type(x))  # str
print(x)

print(f1.tell())  # 93

f1.seek(0)
print(f1.readline())
print(f1.readline())
print(f1.readline())
print(f1.readline())
print(f1.readline())
print(f1.readline())

f1.seek(0)
print(f1.readlines())   # ['Hello Jeet How are You???\n', 'Mihir, How Are??\n', 'Royal Institute\n', 'Best Institute\n', 'India Country\n']


f1.close()



# f2 = open("first1.txt",'x')   
# f2.close()  


import pickle
f3 = open("img1.txt","wb")

pickle.dump(list1,f3)
f3.close()


f4 = open("img1.txt",'rb')
x1 = pickle.load(f4)
print(x1)   # ['\nRoyal Institute\n', 'Best Institute\n', 'India Country\n']
f4.close()  

# Task : Image write, Read 

# Next Topic: Exception Handling