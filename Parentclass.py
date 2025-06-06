class Parent():
    def __init__(self , name , age):
        self.name =name
        self.age=age 

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


s1=Parent("Akshit",60 )
s1.display()