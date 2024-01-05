class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
# Use the Person class to create an object, and then execute
# the printname method:

x = Person("Rohit", "Rohan")
x.printname()

# create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class.

# Create a class named Student, which will inherits the Properties
# and methods from the Person class:

# class Student(Person):
    # pass

# Note: Use the pass keywords when you do not want to add any other
# properties or method to the class.

# Now the Student cladd has the same properties asd method as the Person class.

# Use the Student class to create a Object, and then execute the 
# Printname method

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Rohit", "Nidhi")
x.printname()

# Add the __init__() function 
'''When you add the __init__() function, the child class will
 no longer inherit the parent's __init__() function.
Note: The child's __init__() function overrides the inheritance of the parent's
 __init__() function.'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, 
# and we are ready to add functionality in the __init__() function.

# Use the Super()Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

# By using the super() function, you do not have to use the name of the parent element,
#  it will automatically inherit the methods and properties from its parent.
# add Properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationYear = 2026

x = Student("Mike", "Olsen")
print(x.graduationYear)

# In the example below, the year 2026 should be a variable, and passed into the Student 
# class when creating student objects.To do so, add another parameter in the __init__() function:
# Example
# Add a year parameter, and pass the correct year when creating objects:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2026)
print(x.graduationyear)


# Add Methods
# Example
# Add a method called welcome to the Student class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Rohit", "Kumar", 2026)
x.welcome()

# If you add a method in the child class with the same name as a function in the parent class,
#  the inheritance of the parent method will be overridden.


