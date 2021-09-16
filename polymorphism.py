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






























