
# return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable Objects, Contaning a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# Looping through an Iterator
# We can also use a for loop to iterate through an iterable Objects:
# Iterate the value of a tuple:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

# Also
mystr = "banana"
for x in mystr:
    print(x)

# The for loop actually creates an iterator oibject and execute the next() method for each loop.

# Create an Iterator
# create an Iterator that returns numberm starting with 1, and each sequence will increase by
# one (returning 1,2,3,4,5 etc)


class myNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myClass = myNumber()
myiter = iter(myClass)

for x in myiter:
    print(x)
