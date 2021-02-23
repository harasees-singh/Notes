'''
modules and imports in python
file I/O 
python interpreter
arrays
'''
# Python modules:
# a module can be made by a user and few are provided
# to us by python 
# 
# what to do if we need a module 
import math
result = math.factorial(6)
print(result, math.log10(6556), math.log(2.37))



from math import * # this means import all the functions from math module
print(factorial(5))


# you can import specific functions from math

from math import factorial
print(factorial(5))


# array module
# by default python does not support arrays
# python supported lists only
# array is homogeneous

''' array is a data structure which stores
homogeneous elements in contiguous memory location '''
import array
x = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
# here 'i' means integer and the list passed is the array
print(type(x), len(x))

for i in range(0, len(x)):
    print(x[i])

print()

for i in x:
    print(i)


'''
types of array are derived from C language

i -> integer
f -> float -> decimal -> 4byte
d -> double -> decimal -> 8byte

'''
x.append(7)
print(x, len(x))

# you can do slicing or use other list.functions

p = x

p.pop()
print(p, len(p))

import fibonacci_unacademy

print(fibonacci_unacademy.fib(5))

# a file in the same folder can be used as module

# how interpretaion works exactly in python???
# Python is an interpreted language
# when you write Python file.py what it does is 
# python converts your source code into an intermediate
# code then this is intermediate code is converted into machine understandable code
# intermediate code has an extension .pyc
# and is called python byte code
# and then this is converted into binary or machine understandable language
# this byte code is made via compilation
# Machine Independence/platform independence:
# python and java are these kind of langs 
# python code written in windows work just fine in any other os
# c and cpp don't support this and are os dependent
# this pyc file is executed by python virtual machine





# HIERARCHY
'''
CODE
VIRTUAL MACHINE
OS
'''


# it is the job of VM to convert python byte code to machine understandable format
# this is why python is slow

# c and cpp are directly converted to machine understandable lang
# and hence they are fast



# python -m compileall # to make __pycache__file


# why is java faster than python??
# java does pseudo interpretation 
# it reads all the functions first

# file I/O 
#

# to read or write into a file we use open()

# in open("i.txt", 'r') r means to read
# this will give a file obj

# 'r' opens in read only mode
# 'r+' opens for reading and writing both
# "w" it will be write only and will overwrite everything
# 'wt' read and write both
# 'a' is for appendmode

'''
f = open("input.txt", 'r')
# f.write("Sanket the Singh")
# read expects an argument as count -> which expects the number of bytes to be counted
s =f.read(2)
print(s)


# you can 
f = open("input.txt", "a")
f.write("this will get appended")
# s = f.read(5)
print()


f = open("input.txt", "a+")
f.write("yo what up")
s = f.read(50)
print(s)
f.seek(0)   # f is a cursor. this will reset the position of the cursor



'''
# file = open("input.txt", "r")
# text_in_the_file = file.read(5)
# print(text_in_the_file)
# text_after_sanke = file.read(5)
# print(text_after_sanke)
# file = open('input.txt', 'a')
# file.close()
# file = open("input.txt", "r")
# file.seek(10)
# text = file.read(5)
# print(text)

# open function returns a pointer 

f1 = open("input.txt", 'r')
print(f1.read(3))                          

# f1 is like a cursor 
print(f1.tell())            # to tell the current cursor position
print(f1.read(4))
print(f1.seek(0))           # seek sets the cursor position equal to the arg passed


# How to read a particular line

print(f1.readline())

for i in range(3):
    print(f1.readline())


# 'r' works only for text files

# use "rb" to read in binary mode
# for example you can read jpeg in binary mode


# write mode
# if file does not exist then it will creat one
# if it exists then all good

f2 = open("output.txt", 'w')    # new file created 
f2.write("hey man what up about to overwrite this")
print(f2.tell())


# append mode 

# if file exists then it appends new content
# if doesn't exist then makes one and writes

f2 = open("output.txt", "a")
f2.write("\nPunjab Engineering College")

# to read and append we have a+ mode
f2 = open("output.txt", "a+")
print(f2.tell())
print(f2.read(5))

# r+ is to read a file without deleting anyting
# +gives additional writing power but it won't delete anything
# r+ will write from the cursor position whereas 'a' will always append at the last
# 'wb' to write in binary mode

f3 = open("download.jpeg", 'w+b')
b_ = b"0x450x42"
f3.write(b_)

# when you write f=open() it actually opens the file and does operations
# and if below there is some other logic and you don't need your file 
f3.close()              # this will close the file
# it's always good to close the file so that it does not get affected by any other piece of code

f4 = open("sample_IO.txt", "r+")
f4.write("this is the first line\n")
f4.seek(5)
f4.write("this is the second line\n")