"""
Poly morphism with class example below
"""
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail !")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car   = Car("Honda","civic")
boat  = Boat("Honda","shipx")
plane = Plane("Honda","A300")

for x in (car,boat,plane):
    x.move()



"""
Poly morphism with Inheretence example below
"""


        