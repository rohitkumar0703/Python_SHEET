print(10 > 9)
print(10 == 9)
print(10 < 9)

# Example
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables
# # The bool() function allows you to evaluate any value, and give you True or False in return,
# Example
# Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))

# Example
# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("abc"))                                          # True                                       
print(bool(123))                                            # True
print(bool(["apple", "cherry", "banana"]))                  # True 
print(bool(0))                                              # False               
print(bool())                                               #False


# Some values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


print(bool(23))  # For Checking Position


'''One more value, or object in this case, evaluates to False,
 and that is if you have an object that is made from a class with
 a __len__ function that returns 0 or False:'''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:

# Example
# Print the answer of a function:

def myFunction() :
  return True

print(myFunction())

# You can execute code based on the Boolean answer of a function:

# Example
# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#   Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:
# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
