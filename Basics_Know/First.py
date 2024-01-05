
# Here is the first Code , That Every Coder had did in first time
print("Hello World")

# Lets start from Variables
x = 5
y = "john"
print(x)  #printing value of x
print(y)  #printing value of y

print(type(x))  # Finding the type of data of x 
print(type(y))  # Finding the type of data of y 

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#Create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
    print("Python is " +x)
myfunc()

#If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
#The global variable with the same name will remain as it was, global and with the original value.
    
#Create a variable inside a function, with the same name as the global variable
x = "axtern"
def myfunc():
    x = "Gaming"
    print("Python is "+x)
def func():
    print("python is "+x)

#If you use the global keyword, the variable belongs to the global scope:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

a = 3
b = 3
print(a is b)

a = 300
b = 300
print(a is b)