from abc import abstractmethod, ABC

class Polygon(ABC):
    def __init__(self, color):
        self.color= color

    
    @abstractmethod
    def printSides(self):
        pass

    def printColor(self):
        print(self.color)


class Traingle(Polygon):
    def __init__(self,color):
        super().__init__(color)

    @abstractmethod
    def printSides(self):
        print("There are 3 Sides")


# p1 = Traingle("Red")
# p1.printColor()  # Red

class Rebisque(Traingle):
    def __init__(self,color):
        super().__init__(color)

    def printSides(self):
        print("There are 4 Sides")


r1 = Rebisque("Purple")

r1.printSides()