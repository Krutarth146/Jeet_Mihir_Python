class A:
    def MA(self):
        print("MA Method Under A class")

    
class B(A):
    def __init__(self):
        self.choco = 9
        print(self.choco)

    def MB(self):
        print("MB method Under B class")

class C(A):
    def __init__(self):
        self.oats = 4
        print(self.oats)

    def MC(self):
        print("MC method Under C class")

class D(C,B):
    def __init__(self):
        super().MB()
        super().MC()

    def MD(self):
        print("MD method Under D class")

d1 = D()
# d1.MA()