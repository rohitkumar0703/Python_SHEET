# The length of an Array

# Use the len() method to return the length of an array (the number of elements in an array).
# Return the number of elements in the cars array:
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# looping Array Elemnents 
# You can use the for in the loop to loop through all the elements of an array.
# Print each item in the cars array:
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# adding array elements 
# you can use the append() method to add an element to an array.
# Add one more element to the cars array :
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
cars = ["Ford", "Volvo", "BMW","Honda"]
cars.remove("Volvo")
print(cars)
