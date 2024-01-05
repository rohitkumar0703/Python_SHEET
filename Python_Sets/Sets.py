# Python - Access Set Items
# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Example
# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Example
# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# Once a set is created, you cannot change its items, but you can add new items.

# To add one item to a set use the add() method.
# ExampleGet your own Python Server
# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

# print(thisset)
# Add Sets
# To add items from another set into the current set, use the update() method.

# Example
# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# Example
# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)



# Python - Remove Set Items
# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

# ExampleGet your own Python Server
# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

# Example
# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop() method to remove an item, but this method will remove a random item,
#  so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
# Example
# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# Example
# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()

print(thisset)
# Example
# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# Loop Set
thisset = {"apple","banana","cherry"}
for x in thisset:
  print(x)