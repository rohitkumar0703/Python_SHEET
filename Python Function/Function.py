# Creating a Function
# calling a Function
# In python a function is defined using the def keyword

def my_function():
    print("Hello From Function")
my_function()

# Arguments

def my_function(fname):
    print(fname + "Refsnes")
my_function("Email")
my_function("Tobias")
my_function("Linus")

# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

# This function expects 2 arguments, but gets only 1:

# def my_function(fname, lname):
#   print(fname + " " + lname)
# my_function("Rohit") 
# 
# Arbitrary Arguments, *arg
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:
# Example
# If the number of arguments is unknown, add a * before the parameter name:
def my_fun(*kids):
   print("The youngest child is" + kids[2])
my_fun("Email","Tobias","Linus")

# keywords Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_fun(child3, child2, child1):
   print("The youngest child is" + child3)
my_fun(child1 = "Rohit", child2 = "Rohan", child3 = "Anuj")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
#  ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:


def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Rohit", lname = "kumar")

# default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# # Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
#  and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# eturn Values
# To let a function return a value, use the return statement:
# Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
# Example
def myfunction():
  pass


# -------------------------R E C U R S I O N--------
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
