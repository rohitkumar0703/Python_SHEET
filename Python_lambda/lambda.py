# Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5))

# lambda function can take any number of arguments:

# Multiple argument a with argument b and return the result :
x = lambda a, b: a * b
print(x(5,6))

# Summarize argument a,b,and c and return the result :
x = lambda a, b, c : a+b+c
print(x(5,6,2))

# Using as Function
def myfuns(n):
    return lambda a: a * n

n = int(input("Enter no.: "))
result_function = myfuns(n)
a = int(input("Enter another number: "))  # You can input another number to be multiplied
result = result_function(a)
print(f"The result of {a} * {n} is {result}")

#  Use that function definition to make a function that always doubles the number you send in:
def myfun(n):
    return lambda a:a*n
mydoubler = myfun(5)
print(mydoubler(11))
# or use the same function definition to make a function that always triples the number you send in: 
def myfunc(n):
    return lambda a: a*n
mytripler = myfunc(3)
print(mytripler(11))

# Or, use the same function definition to make both functions, in the same program:
def myfunc(n):
    return lambda a: a*n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
# Use lambda functions when an anonymous function is required for a short period of time.