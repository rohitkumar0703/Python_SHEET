# Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Random Number
# Python does not have a random() function to make a random number,
#  but Python has a built-in module called random that can be used to make random numbers:
# Import the random module, and dissplay a random number between 1
import random

print(random.randrange(1, 10))

# TYPE_CASTING
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
# AGAIN
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)