dict1 = {}   # Dictionary: Ordered, Don't Allow Duplicates (Require Unique Keys Only), values -> Allow's Duplication, Mutable (Changeble)

print(type(dict1))  # <class 'dict'>

set1 = {10}
print(type(set1))  # <class 'set'>

set2 = set()
print(type(set2))  # <class 'set'>


dict1 = {'Name' : "Jeet", 'address' : {'city' : 'V', 'state' : 'New-Jersey'}, 'id' : 90121, 'roll' : [10,20,30,40], 'Name' : "Mihir" }
print(dict1)  # {'Name': 'Jeet', 'address': {'city': 'V', 'state': 'New-Jersey'}, 'id': 90121, 'roll': [10, 20, 30, 40]}

# DIct -> Key - values Pair

print(dict1.keys())  # dict_keys(['Name', 'address', 'id', 'roll'])
print(dict1.values())  # dict_values(['Mihir', {'city': 'V', 'state': 'New-Jersey'}, 90121, [10, 20, 30, 40]])
print(dict1.items())   # dict_items([('Name', 'Mihir'), ('address', {'city': 'V', 'state': 'New-Jersey'}), ('id', 90121), ('roll', [10, 20, 30, 40])])

# print(dict1[0])   # Generates Error

print(dict1['Name'])  # Jeet
print(dict1['address'])  # {'city': 'V', 'state': 'New-Jersey'}
print(dict1['address']['state'])  # {'city': 'V', 'state': 'New-Jersey'}   # New-Jersey

print(len(dict1))  # 4


for e in dict1:
    print(e)

for r in dict1.values():
    print(r)

for t,h in dict1.items():
    print(t,h)


dict1['Name'] = "Krutarth"
print(dict1)   # {'Name': 'Krutarth', 'address': {'city': 'V', 'state': 'New-Jersey'}, 'id': 90121, 'roll': [10, 20, 30, 40]}

dict1.update({'age' : 90})
print(dict1)


del dict1['Name']
print(dict1)

x = ["str1"]
y = 0
print(dict.fromkeys(x,y))


print(dict1['address'])
print(dict1.get('address'))

print(dict1.pop('address'))

print(dict1)

print(dict1.popitem())
print(dict1.popitem())
print(dict1)


dict1.update({"Name" : "Manoj"})


dict1.update({'add' : 90000})
dict1.setdefault("add","3300")
print(dict1)


def demo(x,y,z=0):
    print(x+y+z)


demo(10,20,40)

def demo(x,y,*mihir,v=0):
    sum = 0
    for i in mihir:
        sum += i
    print(sum)


demo(10,20,40,90,89)



def jeet(*kru,**kw):
    # print(kw.values())
    
    print(kru)
    return kw.values()


print(jeet(80,67,12,name='Shivaji', age = 900, salary = 10))   # {'name': 'Shivaji', 'age': 900, 'salary': 10}



# -------------------------------------

def aman(num) :
    for u in range(num):
        yield u
    

# print(aman(5))

for i in aman(5):
    print(i)



def royal(num):
    return num ** 2

print(royal(400))  # 160000

# lambda (Anounomas Function)

royal1 = lambda num : num ** 2


print(royal1(400))


# quadratic Function

# a * (x ** 2) + b * x + c

def quadratic_fun(a,b,c):
    return lambda x : a * (x ** 2) + b * x + c


zafar = quadratic_fun(10,20,30)

print(zafar(5))


list1 = [10,20,30,40,50,70]

print(list(map(lambda x : x**2, list1)))  # [100, 400, 900, 1600, 2500, 4900]

# Powerful function  ---> Map, Reduce, filter


# Dictionary, List Tasks
'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence


Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

    




    # ------------------------------------------------------

    1. Check if a Given Key Already Exists in Dictionary
-> If you have learned about Python dictionaries, you will know that you can check if a given key exists or not in multiple ways. 

D1 = {'first_name' : 'Krutarth', 'age' : 22, 'height' : 5.0 , 'job' : 'Developer', 'company': 'Google'}

2. Handle Missing Keys in Dictionary
-> Dictionary is a collection in python, where the data is stored in the form of a key-value pair, that is, it maps key to its value. Often, you will not know all the keys present in the dictionary and you might end up with a typing error which may lead to runtime error due to missing keys in the dictionary.

D1 = {'first_name' : 'Zafar', 'age' : 21, 'height' : 4.8 , 'job' : 'Engineer', 'company': 'Microsoft'}

3. Extract Unique Values in a Given Dictionary
-> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

D1 = {	'list1': [4, 7, 10, 20], 
      	'list2': [7, 16, 9, 10], 
     	'list3': [13, 10, 4, 8], 
     	'list4': [7, 20, 6, 11]
         }

Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]

4. Print the Sum of Key Value Pairs in a Given Dictionary
-> You need to create a list which has the sum of key-value pairs of a given dictionary. 

D1 = {2: 8, 5: 20, 3: 15}

HINT-> This can be done using a for loop and append() function. 

5. Replace Dictionary Values From Other Dictionary
-> Let’s say you are given two dictionaries. You need to write a python program that will replace the values in the first dictionary with the values from the second dictionary if the key is present in the second dictionary. 

# initializing D1 - first dictionary
D1 = {'first_name' : 'Rutvi', 'age' : 21, 'height' : 4.0 , 'job' : 'Software Engineer', 'company': 'Uber'}
 
# initializing D2 - - first dictionary
D2 = {'age' : 35, 'job' : 'senior data analyst'}

6. Update or Change the Keys in a Given Dictionary
-> try these 2 ways
i)  Using assignment operator
ii) Using pop() method

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

7. Delete a List of Keys in a Given Dictionary 

8. Count the Frequency of List Items Using a Dictionary
-> You can solve this in many ways. Any ideas? Well, you can just use looping constructs or use the list() count method or you can start with an empty dictionary and use the dict.get() method. Probably many other ways!

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

9. Change the Value of a Key in Nested Dictionary
-> Given a nested dictionary, you need to write a program demonstrating how to change the value associated with a particular key of that dictionary. 

#change the value of a key in nested dictionary
#Initializing Dictionary
D1 = {'emp1': {'name' : 'Niraj', 'age' : 21, 'job' : 'developer'}, 
      'emp2': {'name' : 'Zafar', 'age' : 22, 'job' : 'data analyst'}, 
      'emp3': {'name' : 'Rutvi', 'age' : 22, 'job' : 'data scientist'}, 
      'emp4': {'name' : 'Krutarth', 'age' : 60, 'job' : 'python developer'}}

11. Check if the Given Dictionary Is Empty or Not
-> One way to check this using the len() function, which you can try coding; we will achieve this using the bool() function. The bool() function evaluates to standard true or false and is used to return or convert a value to Boolean type. If you pass an empty dictionary, the bool() evaluates to False, as failure to convert something that is empty.

14. Get a Key From Value in a Dictionary
-> You need to write a program, which returns the key for a given value. This can be done in multiple ways. Try doing it using dict.items() function.

#get key for a given value using dict.items()
# Dictionary Initialization
D1 = {'Priyanka Chopra': 23, 'Alia Bhatt': 29, 'Hritik Roshan': 45, 'Ranbir Kapoor': 40}

15. Sort a Given Dictionary by Key
-> You know this so, you got this...

D1 = {'Niraj': 23, 'Jaynam': 29, 'Rutvi': 40, 'Zafar': 45, 'Obama': 34}
    '''