# Encapsulation

class Student:
    school = "HBK"   # class Variable

    def __init__(self, iddd, nameee, marksss):   # Constructor
        self.__id = iddd   # Private
        self.name = nameee   # public
        self._marks = marksss  # protected

    def display(self):   # Instance Method
        print(self.__id,'----',self.name,'----',self._marks)

    @classmethod   # decorator
    def change_school(cls):
        cls.school = input("Enter New School: ")
        print("School record Updated!!")

    @staticmethod
    def show_school():
        print(Student.school)

    
jeet = Student(100, "Jeet Popat", 900)
mihir = Student(200, "Mihir Thakkar", 910)

jeet.display()
mihir.display()

print(jeet.school)
print(mihir.school)

# jeet.marks = 1000
# print(jeet.marks)  # 1000

Student.change_school()
print(mihir.school)   # class Variable
print(jeet.school)    # class Variable
print(Student.school)  # class Variable

# print(Student.id)  # Error

print(jeet._marks)   # 900  # Protected

jeet.show_school()  # static Method

# print(jeet.id)  # Error
# print(jeet.__id)  # Error