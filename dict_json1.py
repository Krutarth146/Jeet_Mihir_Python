import json
# dict1 = {'1001' : {'pName' : "5 Star", 'qn' : 342, 'price' : 10},
#          '1002' : {'pName' : "Parle G", 'qn' : 180, 'price' : 5},
#          '1003' : {'pName' : "Oats", 'qn' : 220, 'price' : 30},
#          '1004' : {'pName' : "kellogs", 'qn' : 112, 'price' : 50}}

# print(dict1)
# print(type(dict1))  # <class 'dict'>

# # print(dict1.values())

# print(dict1['1002']['price'])
# print(dict1['1004']['pName'])

f1 = open('record.txt','r')
f = f1.read()
dict1 = json.loads(f)
f1.close()


# print("----------------Menu-----------------")
# for i in dict1:
#     print(i, dict1[i]['pName'], "      " ,dict1[i]['qn'],"        " ,dict1[i]['price'])




user_need = input("Enter Your product Id: ")
user_qn = int(input("ENter Quantity: "))




if user_qn <= dict1[user_need]['qn']:
    dict1[user_need]['qn'] -= user_qn
    print(dict1[user_need]['qn'])
    print("Total Bill Amount is",dict1[user_need]['price'] * user_qn)
    print("Inventory Updated")
else:
    print("We have only",dict1[user_need]['qn'])
    x = input('Press y for buy product: ')
    if x.lower() == 'y':
        print("Total Bill Amount is",dict1[user_need]['price'] * dict1[user_need]['qn'])
        dict1[user_need]['qn'] = 0
        print("Inventory Updated")
    else:
        print("Thank You!!!")



# Files 

# Modes : 'w', 'r', 'a', 'x', 't', 'b', '+'

# 'w' ---> Write Mode


# 1. Text File     2. Binary File

# fp = open("jeet.txt", 'w')

# fp.write("Hello This is Jeet Popat.")

# list1= ["\nIndia is Good Country Forever.\n","Royal is Best.\n"]
# fp.writelines(list1)

# fp.close()

# fp = open("jeet.txt", 'r')

# # x = fp.read()
# print(fp.tell())
# print(fp.readline())
# print(fp.tell())
# print(fp.readline())

# fp.seek(0)
# print(fp.tell())
# print(fp.readline())
# print(fp.readline())
# print(fp.readline())
# print(fp.readline())
# print(fp.readlines())
# print(fp.tell())
# # print(x)
# fp.close()




f1 = open('record.txt','w')
js = json.dumps(dict1)
f1.write(js)
f1.close()


# Bill.txt ---> Customer Name, Date, Total Bill amount