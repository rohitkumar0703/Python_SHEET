def myfunc():
    x = 300
    print(x)
myfunc()

# The local variable can be accessed from a function within the function:
def myfinc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

# A variable created outside of a function is global and can be used by anyone:
x = 200
def myfunc():
    print(x)
myfunc()
print(x)

# The function will print the local x, and then the code will print the global x:
x = 200
def myfunc():
    x = 300
    print(x)
myfunc()
print(x)

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = 340
    print(x)

myfunc()
print(x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.
# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)