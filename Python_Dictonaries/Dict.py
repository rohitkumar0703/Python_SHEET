# Python - Access Dictionary Items
# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Example
# Get the value of the "model" key:

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisDict["model"]
print(x)

# There is also a method called get() that will give you the same result:
# Example
# Get the value of the "brand" key:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisDict.get("brand")
print(x)
# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisDict.keys()
print(x)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.keys()
print(x)   #before the change 
car["color"] = "White"
print(x)   #after change 
x = car.get("color")
print(x)

# Get Values
# The values() method will return a list of all the values in the dictionary.
# Example

x = thisDict.values()
print(x)

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

# Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

# get all element 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# Example
# Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes")
else:
    print("nope")
