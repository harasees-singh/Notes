'''
SET TUPLE ARRAY DICTIONARY and NONE dtype
'''
# we have discussed lists
# lists is a data structure



# None
# why do we need it?
# none is a data type in python to give a notion of empty
# quantity

# tuples are collection of heterogeneous objects
# tuples are immutable

x = (1,2,3,4,5,6,6,6,'snake','holy', 4.5,True,None) # tuple initialized
# x[0] = 11 # error

# How to access any individual element of a tuple
# tuples are zero based indexed
# we can update any element of a list because it is mutable but tuples are immutable
# can we delete any element in tuple -> No as they are immutable
# operations on tuples

print(x*4)

boolean = 2 in x
print(boolean)

x = x*4
print(x)
# works fine x is now pointing to the new tuple
# you can always type cast a tupule to a list

# dictionary

# it is another data structure which stores values in <key, value> form
x = {
    "name" :"sanket",
    "job" : "None",
    (1, 2, 30) : "hey this key has to be immutable like str or tuple",
    "job" :"never explains what needs to be"
}  

print(x, type(x))

# dic stores values in random order contrary to continuous memory locations in lists

# what will happen if we give 2 same keys
# it will overwite, I want to play some SOTR

print(x["job"]) 
print(x[(1,2,30)])

# dictionarys are mutable
# How to add a new key??
x["location"] = "Bangalore"

print(x)

del x[(1, 2, 30)]   # this will remove the key 
# value pair corrres to this tuple

print(x.get("qwerty"), x.get("location"))
# get will return None if it does not find the required key
# x.clear()
# this will clear our dictionary

# what if we want to print all the keys?????

keys = x.keys()
values = x.values()
print(keys, values)


# search, insert, delete in dictionaries is theta(1) amd O(n)
# if we just want to store values instead fo key value pairs 

# we can use sets

# SETS

# sets are same as dictionaries 
s = {
    "Sanket", "Singh", 1, 2, 3, 4
}
print(s, type(s))

# sets are also unordered and randomly stored 
# in sets we can't have duplicates


s = {
    1, 2, 3, 3, 3, 3
}
print(s)

'''
SETS ARE MUTABLE
'''
s.remove(1)
s.add(10)
print(s)
# can we access any element of the set

# you will have to search for element or iterate over
# the whole set

print(2 in s)

# for loop
a = range(0, 4)
print(a, type(a))
print(4 in a)

for i in range(10):
    print("Sanket's macbook sucks")
for i in range(0, 15000, 150):
    print(i)

for i in reversed(range(15)):
    print(i)

for i in s:
    print(i)

for i in keys:
    print(i)

for i in keys:
    print(x[i])

