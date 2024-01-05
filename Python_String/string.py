# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# Example
# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Slicing String:
b = "Hello, World!"
print(b[2:5])
# Slice From the Start
# By leaving out the start index, the range will start at the first character:

b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[5:12])     # , World
# Slice To the End
# By leaving out the end index, the range will go to the end:

# Example
# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
print(b[5:])       # , World!

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])                       # orl

# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.

# Upper Case
# ExampleGet your own Python Server
# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())                    #HELLO, WORLD!

#Lower Case
a = "HELLO, WORLD!"
print(a.lower())                  # hello, world!


# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Example
# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
# Example
# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

# Example
# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Python - String Concatenation
# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

# ExampleGet your own Python Server
# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

# Example
# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Python - Format - Strings
# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# ExampleGet your own Python Server

age = 36
txt = "My name is John, I am " + age
print(txt)
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Example
# Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

# Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

