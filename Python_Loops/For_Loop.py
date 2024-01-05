# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# The for loop does not require an indexing variable to set beforehand.
# Looping through a String 
# Even strings are iterable objects, they contain a sequence of characters:
# Loop through the letters in the word "Banana"

fruits = ["apple", "banana", "cherry"]
for x in "banana":
  print(x)

# The Break-Statement
# The Break Statement we can stop the loop it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# The continue Statement 
# with the continue statement we can stop the current iteration of the loop,
# and continue with the next:

# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments
#  by 1 (by default), and ends at a specified number.

# Using the range() function:
for x in range(6):
  print(x)
#   Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# Using the start parameter:
for x in range (0,21):
  print(x)
print("------------------------------")
# The range() function defaults to increment the sequence by 1, however it is possible 
# to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(1,21,2):
  print(x)
print("...................................................")
# Else in For loop:
# The else keyword in a for loop sepecifies a block of code to be execute when the loop
# is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally Finished!")
print("........................")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finished")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Example
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x,y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass