# python is an open source language
# zen of python is the vision around which python is built
# cpp is used in frequency trading 
# python and java are industry leading

# syntax refers to the set of rules that govern the structure of statements in programming languages 
# python is very verbose

# terminal or cmd prompt is cli command line interface and gui is graphic user interface.
# in command line yuo write code line by line

# cli is command line interface
# there is no graphics involved. you can't use interactive gestures to do things
# every action you do is a command.
# in cloud computing. cloud is analogy derived from servers in data centres.
# cli relies on cli because gui is not available
# python console is also called REPL console
# R- read
# E- evaluate
# P- print
# L- loop

print("hello world")
print("harasees", "singh", end = " ")
print("op", end = " ")
print("hey yo what up", end = "\n")
# when you take input from user it always takes input as text
# variable name can't start with a number . it must start with a letter or underscore
# no space is allowed in variable name and only underscore is added. variable naming is case sensitive.
# what kind of data we can store in a variable 
# there are a lot more data types in python than one realises
# integer lists arrays decimal boolean character
x_int = 10
y_int = 20
# in python decimals are called float

# x_float is the most stupid variable name I have ever heard 
sanket = "my name is sanket"
print(sanket)
t= True
print(t)
# "for text always wrap it in double quotes"
# text is called string in python and some other languages
# type(x) function returns the class of x
# boolean are of two types True and False
x = True
y = False
print(type(x))
# 'class<bool>' is printed
# single quotes are also used to represent string in python
# writing string in multiple lines
a = '''use triple 
quotes'''
print(a)
# only triple quotes support multi line string
# quadruple = '''' hey yo what up''''
# print(quadruple)
# syntax error
'sample'
# how is a character created in python?
# string is a collection of multiple characters arranged in a formation
# to create a character in python we just make a string of length 1
# eg.
char = 'y'
# there is no data type like char in python, it's just a string of length 1
# do you think to understand a code snippet we need some documentation?
# documentation is provided in the form of comments
# comments are some part of your code that is never executed when we run the code
# there sole purpose is readability
# to write comments in python use '#'
# drop a yes or no in the poll 
# my laptop battery is draining quick af
'''
1. Integer ()
2. float (used to represent decimal in python)
3. boolean (this is just used to store either true or false)
4. string (this is used to store text) you can make a string with single or double quotes and a multiline string with triple quotes
5. character (in python character doesn't exist separately we can make just a string of length 1)
6. complex number (stores complex number)
'''
comp = 2 + 3j
print(comp, type(comp))
# j here is math.sqrt(-1) :)


# a keyword is a set of special words that have a special
# meaning in a language. each keyword has different usage. 
# never use a keyword as a name of user defined variable or object if you want to get specific


# python will take them in some other sense 
# True = 1 :error:
# what are keywords ?
# some sexy keywords : nonlocal, is, in, for, True, break, except, continue, del, elif, raise
# print is a function, stay tuned...
# :sir_flexing_hard:
# how to print ' " '
# enter is '\n'
# delete is :idk:
# some characters have symbol some don't have it, these are called special characters
# these are also called special characters
# there exist multiple escape characters 

# single quotes
x = "\'"
print(x)
# can also write like x = '\"' to print double quotes
y = "\''"
print(y)
v = ' " '
print(v)
# these are called escape characters becuase they are preceded with backslash


# new line given by "\n"
p = 'sanket \n singh'
print(p)


# tab space '\t'
t = 'sanket \t singh'
print(t)

# how to print '\'
print('hey this is backslash: \\')

'''
welcome operators
'''

# arithmetic + - * ** % / //

x = 34
y = 17
print(x+y, x-y, x*y, x//y, x**y)
# this beats retarded this instrus mental

# comparison and relational operators == != < > 

print(2 != 3) # returns boolean

# logical operators

print("use of and", (x !=y) and (x >= y))
print(x and y) # if true y is returned if x happens to be false x or zero is returned
print(not x) # boolean is returned
# 0 is false all other numbers are true
print(5 and 0)

# empty string is False and non empty is True
print(5 or 6)
print(0 or 4)

# statement is a syntactic unit of a language that expresses some action
# to be carried out.
# in python generally one line of code represents one statement
# print("hello world"); 
# this works but not recommended
# in python any piece of code which is in one single line is 
# executed as a statement
# Q. Can we have two print statements in one line???
print("hey yo what up"); print("this is executed")
# this is to be avoided
print("hello world"), print("hello world again")
# this also works 

# Blocks:
# some set of statements define one block of code

# Q. what are blocks
# set of multiple statements 
# Indentation: a part of space given before a statement is called 
# indentation
# say we want a separate block, we need to give another indentation

# Conditionals :
# if condition is true you execute something
# else do something
# if condition:
#     'do something'
# else:
#     'do something'

if 10 > 5:
    print("10 is greater than 5") # this is the start of the new block
    print("random sh*t")

# for conditions to be executed they need to be in separate block
# when we want to execute something specific use else


# giving repeated command
# in python we write loops using while
# while to denote a loop 
while True:
    print("infinity ain't a thing")
    break
    
# press 'crtl C' to stop infinite loop


'''new class arrays and lists'''
# this will be a basic calculator app
# we will make a calculator that will prompt the menu again and again
'''print("welcome to calculator")
menu = """Please choose one operation from the list
a) for addition press           +
b) for subtraction press        -
c) for multiplication press     *
d) for division press           /
e) for exponent press           ^
f) for remainder press          %
"""
while True:
    print(menu)
    operator = input()
    print("please enter two valid inputs to perform", operator)
    a = int(input())
    b = int(input())
    if operator == '+':
        print("output is ", a+b)
    elif operator == '*':
        print("output is ", a*b)
    elif operator == "/":
        print("output is ", a/b)
    elif operator == '^':
        print("output is ", a**b)
    elif operator is '%':
        print("ouput is ", a%b)
    else:
        print("Invalid operator")

    print("do you feel like calculating more?")
    again = input()
    if not (again == 'Y' or again == 'yes' or again == 'y'):
        print("thanks for using the calci, see you again:)")
        break # breaks the nearest loop''' 

# when we write break it breaks the nearest loop always
# for taking multiple inputs in the same line either use lists 
# or you can take the whole input in a string and use split() funciton


# taking multiple inputs in the same line 



'''x, y, z = input().split(",")
print(type(x))
x = int(x)
y = int(y)
z = int(z)
print(type(x))
print(x, y, z)'''

# by default it will split the string wherever it sees the space character
# 
p = input().split()
print(type(p)) # list
p = map(int, p)
print(type(p)) # map

# lists in python
'''lists are an alterante to arrays in python'''
# by default the word array means homogenous collection of elements
# but lists give you all the features of arrays and lists are heterogenous
# [1, "sanket, True, 47.5"]
# lists are superset of arrays
# we have both arrays and lists both in python

# initialization of list in python

# lists can be misused so you can use array

a = []
b = [1, 2, 3]
c = [1, "a", "string", 6+9j]
print(a)
print(b)
print(c)

# How to add elements in the list 

b.append(33)
c.append(29)
# adds an element at the end of the list
# how is indexing done in lists of python ??
# -> same like flowcharts i.e. 0 based indexing

print(c[0], c[1], c[2])

# Are lists mutable ??
# YES

# remove the last element
c.pop()
c.extend([23, 'true', True, 45]) # appending multiple items
print(c)

# remove from specific index
c.pop(3)

# can we remove any specific element ??
c.remove(45) # first occurence of 45
print(c)

# can we remmove all the elements at once?
c.clear()
print(c)

c.reverse()


# taking multiple inputs

a = input().split(", ")
# your computer can execute 10**8 instructions per sec.
# this time is generally referred for C and C++
# for python expect about thrice the time


'''assignment operator'''
# 1. = -> it will assign the value on rhs to the variable on left
# 2. a = a+1
a = 10
a += 1 # instead of writing a = a+1 also works
# in general a += b

# similarly you can do a-=1 and a*=1 or a%=2 and so on
# a++ does not exist in python

a=-1 # htis will assign negative 1 to a 

# What will happen if we write a-= -1
# this will increase a by 1

# bitwise operator 1. & -> a&b -> will do bitwise and on th
# binary of a, b
z = 5 &4 # 5-> 101 & 4->100 this will give 100 or 4
print(z)

'''similarly we have | or , ^ XOR, ~ bitwise not'''
print(5|4) # 5
print(5^4) # 1
print(~5)  # -6
'''theroy behind -6 negative numbers are stored in the form of 
2's complement, explore'''

''' << left shift operator
'''
print(z = 1 << 3) # appends 3 zeroes to the right of 1
print(z = 5 >> 2) # prepend 2 zeores on the left and remove
# last two zeroes,here z will become 001 in binary

# (101) >> 2 # 001
'''right shift ny two spots'''
 

'''6 in binary is (110) so 6 << 3 will be 110000'''


'''membership operators'''
