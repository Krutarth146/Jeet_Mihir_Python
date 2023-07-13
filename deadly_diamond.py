class A:
    def MA(self):
        print("MA Method Under A class")

    
class B(A):
    def __init__(self):
        self.choco = 9
        print(self.choco)

    def MB(self):
        print("MB method Under B class",self.choco)

class C(A):
    def __init__(self):
        self.oats = 4
        print(self.oats)

    def MC(self):
        print("MC method Under C class",self.oats)

class D(C,B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        # pass

        # super().MB()
        # super().MC()

    def MD(self):
        print("MD method Under D class",self.oats, self.choco)

d1 = D()
d1.MD()