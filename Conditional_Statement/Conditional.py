# Elif
# The elif keyword is python's way of saying "if the previous conditions were not true,
# then try this condition".
a = 33
b = 33
if b>a:
    print("B is greater than a")
elif a == b:
    print("a and b are equal")

# In this example a is equal to b, so the first condition is not true, 
# but the elif condition is true, so we print to screen that "a and b are equal".

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b>a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# In this example a is greater than b, so the first condition is not true, 
# also the elif condition is not true, so we go to the else condition and print 
# to screen that "a is greater than b".
# You can also have an else without the elif:

a = 200
b = 33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# Short HAnd IF
# If you have only one statement to execute, you can put it in the same line as the if statement.
# One line if statement :
a = 200
b = 33
if a>b:print("a is greater than b")

# Short Hand IF...Else
#  If you have only one statement to execute, one for if, and one for else, you can put it all on 
# the same line:
a = 200
b = 33
print("A") if a>b else print("B")

# Also
a = 200
b = 330
print("A") if a>b else print("B")

# This technique is known as Ternary Operators, or Conditional Expressions.
# You can also have multiple else statements on the same line:
# One line if else statement, with 3 conditions:
a = 330
C = 330
print("A") if a>b else print("=") if a == C else print("C")


# AND
# The AND Keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a>b and c>a:
    print("Both conditions are True")

# Or
# The Or keyword is a logical Operator, and is used to combine conditional statements:
# Test if a is greater than b, Or if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Not 
# The not keyword is a logical operator, amd is used is used to reverse the result of the conditional 
# statements:
# test if a is NOT greater than b:
b = 200
a = 33
if not a >b :
    print("a is Not greater than b")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
    print("Above ten")
if x>20:
    print("and also above 20!")
else:
    print("But not above 20")


# # The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
a = 33
b = 200
if b>a:
    pass
# having an empty if statement like this, would raise an error without the pass statement






