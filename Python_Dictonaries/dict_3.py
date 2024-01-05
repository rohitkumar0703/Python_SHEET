# Python - Copy Dictionaries
# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# ExampleGet your own Python Server
# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# Another way to make a copy is to use the built-in function dict().
# Example
# Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# -----------------P  Y  T  H  O  N - N E S T E D  DICTIONARIES-----------------------
# Nested Dictionaries 
# A dictionary can contain dictionaries, this is called dictionaries
# Example
#  Create a dictionary that contain three dictionaries :

myfamily ={
    "child1" : {
        "name" : "Rohan",
        "year" : "2000"
    },
    "child2" : {
        "name" : "Anuj",
        "year" : 2001
    }
}
print(myfamily)


# Or, if you want to add three dictionaries into a new dictionary:
# Example
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# Example
# Print the name of child 2:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])
