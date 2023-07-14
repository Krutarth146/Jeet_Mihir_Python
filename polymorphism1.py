# Poly - Many
# Morph - Forms

# right ---> right * wrong, right * left
# who -----> Kon, k j

print(len([10,20,30]))  # 3
print(len("Mihir"))  # 5

def royal(num1):
    print("Royal Technosft")

# royal()  # Royal Technosft

def royal(num1, num2):
    print("Royal Techno P. Ltd")

royal(10,20)   # Royal Techno P. Ltd


class RBI():
    def Interest(self):
        print("This is Interest Method Under RBI Class")


class SBI(RBI):  # child class
    def Interest(self):  # Method Overriding
        print("This is Interst Method Under SBI Class")
    

    def Interest(self, num1):  # Method Overloading
        print("This is Interst Method Under SBI Class with args")

# jeet = RBI()

# jeet.Interest()   # This is Interest Method Under RBI Class


# jeet = SBI()

# jeet.Interest(10)  # This is Interst Method Under SBI Class

list1 = [RBI(), SBI()]
print(list1)  # [<__main__.RBI object at 0x0000013DECF19D50>, <__main__.SBI object at 0x0000013DECF1AE30>]


list1[0].Interest()
list1[1].Interest(400)


# This is Interest Method Under RBI Class
# This is Interst Method Under SBI Class with args