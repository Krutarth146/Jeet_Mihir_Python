# Inheritance ----> one class Inherits the features of Another class

# Types ---> Single, Multilevel, Multiple, Heirarchical, Hybrid

# IS-A Relationship

# Banana is a Fruit.

class Alto:
    def __init__(self):
        self.brake_types = 4
        print("Alto 800")

    def Brake(self):
        print(self.brake_types)
        print("Alto has Brake Method")
    
    def Seats(self):
        print("Alto has 4 Seats")


# class Ferari : public Alto
class Ferari(Alto):
    def __init__(self):
        super().__init__()
        print("Ferari")

    def Sensor(self):
        print("Ferari has Sensor Method")

    def Safety(self):
        print("Ferari has also Safety Features")


class BYD(Ferari):
    def __init__(self):
        super().__init__()
        print("BYD Chinese")

    def Sonar(self):
        print("BYD has SOnar System")

# f1 = Ferari()   # Ferari
 
# # f1.Sensor()
# # f1.Safety()
# f1.Brake()
# # f1.Seats()


b1 = BYD()
b1.Brake()