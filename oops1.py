# Object Oriented Programming

# object, class, Polymorphism, Encapsulation, Inheritance, Data Abstraction

# structure  ---> User Defined Datatype

# class Student
# {
#     int id;
#     char name[10];
#     float marks;

        # void set_data(id, name, marks)
    # {
    #     this->id = id;
    #     this->name = name;
    #     this->marks = marks;
    # }

    # void dislay()
    # {
    #     cout<<id<<name<<marks;
    # }
# };


# Constructor ---> Special Method, NO return Type, class name
# Constructor Solves Intialization Problem
# self ----> This Pointer in CPP, Java

# class  ---> Blueprint of any Object
# Object ----> Instance of class

class Bank:
    ROI = 4   # Class memeber Variable

    def __init__(self):
        self.name = None   # Instance Memeber Variable
        self.balance = 0

    def set_name(self):
        self.name = input()

    def deposit(self, money):   # Instance Method
        if money > 0:
            self.balance += money

    def withdraw(self,money):
        self.amount = 0   # Local Variable
        if money <= 0 or (self.balance - money) <= 5000:
            print("Not Allowed")

        else:
            self.balance -= money

    def check_balance(self):
        print(f"Your Ac. Bal is {self.balance}")


    @classmethod   # decorator
    def Increase_ROI(cls):
        cls.ROI += 2


    def Give_interest(self):
        self.balance += (self.balance * Bank.ROI) / 100
        print("Interst Credited")


# Bank b1 in CPP

jeet = Bank()
mihir = Bank()


jeet.set_name()
jeet.deposit(20000)
jeet.withdraw(18000)
jeet.withdraw(1000)
jeet.check_balance()
jeet.Increase_ROI()
jeet.Give_interest()
jeet.check_balance()    

jeet.address = "Gnr"   # Instance Varibale
print(jeet.address)
# print(mihir.address)


print(jeet.ROI)

jeet.ROI = 90

print(Bank.ROI)   # 6    # Class Variable
print(jeet.ROI)   # 90   # Instance Variable
print(mihir.ROI)  # 6    # Class Variable