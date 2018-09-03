print("hello world")

list = ["apple", "orange", "pear"]
print(list)
print(list[0:2])

list[2] = "David"
print(list)

for x in list:
    print(len(x))


print(len(list))

list.append("Minying") # append takes exactly one element
print(list)

list.insert(3, ("Minying"))
print(list)

list.extend(("David", "test", "Open"))
print(list)

list.remove("test") # remove specific item from the list
print(list)

list.pop(2) # remove the specific item by index
print(list)

list.pop() # if not specified, the last item is removed from the list
print(list)

del list[2]
print(list)

# del list # this delete the entire list

list2 = list.copy()
print(list2 + list)

list3 = list + list2
print(list3)

# append() # Adds an element at the end of the list
# clear() # Removes all the elements from the list
# copy() # Returns a copy of the list
# count() # Returns the number of elements with the specified value
# extend() # Add the elements of a list (or any iterable), to the end of the current list
# index() # Returns the index of the first element with the specified value
# insert() # Adds an element at the specified position
# pop() # Removes the element at the specified position
# remove() # Removes the item with the specified value
# reverse() # Reverses the order of the list
# sort() # Sorts the list