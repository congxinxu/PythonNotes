# Day 3 of Learning Python

# Tuple
# Tuple are unchangable
# We cannot add/edit/remove
tuple = ("apple", "orange", "banana")
print(tuple)

# Sets
# Sets are not ordered
tmp_set = {"apple", "David", "banana"}
for i in tmp_set:
    print(i) # this for loop print the element of the set backwords


tmp_set.add("orange")
print(tmp_set)

thisset = {"apple", "banana", "cherry"}
thisset.update({"orange", "mango", "grapes"})
print(thisset)

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict['model']
print(x)
print('------')
y = thisdict.get('model')
print(y)
print('------')
thisdict['year'] = 2018
print(thisdict["year"])

print('------')

for i in thisdict:
    print(i)

print('------')
for i in thisdict:
    print(thisdict[i])
print('------')
for i, j in thisdict.items():
    print(i, j)

thisdict['color'] = 'black'
print(thisdict.values())