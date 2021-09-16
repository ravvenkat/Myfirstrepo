 ###########Polymorphism in Class Methods###########
  
  class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
    
###############################################################################





Now in the next example we declare another method under the derived class with the same name as base class but with a different argument. As the base class’s method is now overridden by the derived class, only the derived class’s method will be printed as the output.

Example:
class Vehicle:
    def run(self):
        print("Saves Energy")

class EV(Vehicle):
    def run(self):
        print("Run on Electricity")

ev = EV()
ev.run()

########Output
Run on Electricity


///////////////////Super() Function////////////////////////

Now as if the base class’s method has been overridden, the method from the base class cannot be called normally. So to call the method of base class we have to use the super function in the overridden method under the derived class.

Example:
class Vehicle:
    def run(self):
        print("Saves Energy")
class EV(Vehicle):
    def run(self):
    super().run()//super function is used to call the method of base class 

        print("Run on Electricity")

ev = EV()
ev.run()


##################Output:
Saves Energy
Run on Electricity

######



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

class Dog1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog1. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark2")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
dog2 = Dog1("Fluffy2", 40)

for animal in (cat1, dog1,dog2):
    animal.make_sound()
    animal.info()
    animal.make_sound()

class Vehicle:
    def __init__(self, fare):
        self.fare = fare

    def cost(self):
        return (self.fare)

bus= Vehicle(20)
car= Vehicle(30)
total_fare=bus.cost()+ car.cost()
print(total_fare)



################ METHOD OVERRIDING ####################
class Vehicle:
    def run(self):
        print("Saves Energy")
class EV(Vehicle):
    def run(self):
        #super().run()
        super().__init__()
        print("Run on Electricity  \n")

ev = EV()
ev.run()

##############################ANOTHER EXAMPLE ######################


from math import pi


class Shape:
    def __init__(self, name):
        self.name = name
    #    print(self.name)

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):                  ########used to print string, since by default return type is string for this " __str__" method 
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2
    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("valuesenttoShapeClass") ########################
        self.radius = radius
    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())





















































