'''The word "polymorphism" means "many forms", and in programming it refers to'
 methods/functions/operators with the same name that
 can be executed on many objects or classes.'''

# Function Ploymorphism
# An example of a polymorphism function that can be used on differ can be used on different 
# objects is the len() function.

# String
# For string len() returns the number of character:
x = "Hello World!"
print(len(x))

# Tuple
# for the tuple len() return the number of items in the tuple:
mytuple = ("Rohit" , "Rohan", "Anuj") 
print(len(mytuple))

# Dictionary
# for dictionary len() returns the number of key/value pairs in the dictionary:
thisDict = {
    "Brand" : "Addidas",
    "model no." : "Nine",
    "Year's Old" : 10,
    "Helo" : "Welcome"
}
print(len(thisDict))

# Class Polymosrphism,
# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple
#  classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, 
# and they all have a method called move():

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

# Look at the for loop at the end. Because of polymorphism 
# we can execute the same method for all three classes


'''Inheritance Class Polymorphism
What about classes with child classes with the same name? Can we use polymorphism there?
Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat,
 Plane child classes of Vehicle,the child classes inherits the Vehicle methods, 
 but can override them:'''

# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass
class Boat(Vehicle):
  def move(self):
    print("Sail")
class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1,boat1,plane1):
  print(x.brand)
  print(x.model)
  x.move()