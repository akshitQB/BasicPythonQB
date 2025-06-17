#que-1 create a car class with attributes like brand and model. Then create an instance of this class.
#que2 Add a method to the Car class that full name of the car (brand and model)

#inheritance : Create a ElectricCar Class that inherits from the Car class and has an addition attributes battery_size.

# Encapsulation : Modify thr car class to encapsulation the brand attributes , making it private and provide a getter method for it.
# in this code have the set and get method for the private attributes.
# Polymorphism  : Demonstarte polymorephism by defining a method fuel_type in both Car and ElectricCar classes,but with differrent behaviours.
# Class variable : Add a class variable to Car that track of the number of cars craeted 
# Static Method  : Add a static method to the Car that returns a general decription of a car.
# isinstance  : Demonstarate the use of isinstance() to check if my_tesla an instance of Car and ElectricCar.


class Car:
    
    total_car=0
     
    def __init__(self , brand , model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1

    def get_brand(self):
       return self.__brand + "!"
    
    def set_model(self,x):
       self.__brand = x

    def full_name(self):
     return f"{self.model} ,{self.__brand}"


    def fuel_type(self):
       return "Pertol or diesel"
    
 
    def general_desc():
       return " car are .....>>>>...........>>>>>"
    

class ElectricCar(Car):
   def __init__(self,battrysize,brand,model):
      super().__init__(brand,model)
      self.battrysize=battrysize
      print(battrysize)

    
def fuel_type(self):
       return "Electric Charge...:)"

tesla=ElectricCar("22kwh","tesla","T1Pro")


isinstance(tesla,Car)
# print(tesla.set_model("jay"))
# print(tesla.full_name())
# # tata=Car(fuel_type())
# # print(tata)




# s1=Car("BMW", "M4")
# s2=Car("test","test")

# print(s1.brand)
# print(s1.model)


# print(s1.full_name())

# print(Car.total_car)

# print(s1.general_desc)
# print(Car.general_desc())

