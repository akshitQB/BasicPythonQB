from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass

class Desk():
    def __init__(self , name , age):
        self.name=name
        self.__age=age


    def get_age(self):
        return self.__age + "You are Eligible "
        
    def wow(self):
        return f"congulation.............{self.name}"

class Desk2(Desk):

    def printDetails(self):
        print(self.name)
        print(self.age)
    
    def sunroof(self):
        print("this is not available right now!....")
              

s1=Desk("jay","2")
s2=Desk2("rudra","15")
print(s2.sunroof())
print(s1.get_age())
print(s1.wow())
