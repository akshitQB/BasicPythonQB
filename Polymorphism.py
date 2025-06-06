class Vehicle:
    def __init__(self,model,name):
        self.model =model
        self.name = name 

    def move(self):
        print("Move")

class Car(Vehicle):
    def move(self):
        print("car is moving")
    

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    def move(self):
        print("truck is movimg ")


car1=Car("2020","BMW")
bike1=Bike("2021","Yamaha")
truck1=Truck("2019","Volvo")

for x in (car1,bike1,truck1):
    print(f"{x.name} {x.model}")
    x.move()
    

# in this code we have same mehod name in all the classes with differnt classs 
# we have inherited the Vehicle class in all the classes and we have used the same method name
# this is called polymorphism in python