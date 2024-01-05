# Example
# create a class named person, use the __init__() function to assign values for name and age:

from typing import Any


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p = Person("Rohit",21)
print(p.name)
print(p.age)

# Note: The __init__() function is called automatically every time 
#       the class is being used to create a new object.
# # The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
# Example
# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("Nidhi" , 20)
print(p)

#Example
# The string representation of an object WITH the __str__() function:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p = Person("Rohit",21)
print(p)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:
# Example
# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello My name is " + self.name)

p = Person("Rohit",21)
p.myfunc()
#Note: The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

# The self Parameter------------------------------
class person:
    def __init__(mysillyObject, name, age):
        mysillyObject.name = name
        mysillyObject.age = age

    def myfun(abc):
        print("Hello my name is " + abc.name)


p2 = person("Rohit",22)
p2.myfun()

# Modify Object Properties
# you can modify properties on object like this:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Rohit", 21)

p1.age = 20
print(p1.age)
p1.myfunc()

# DELETE Object
# del p1

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1
print(p1)

