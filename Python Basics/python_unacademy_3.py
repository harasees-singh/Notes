'''formatting strings in python'''
s = "hello"
w = "world"

name = "Sanket"
year = 2021
greeting = "hello, %s to %d" %(name, year)
print(greeting)

# %s %d are called format specifiers
'''
%s for string
%d for integer
%f for fload
%b for binary
%r for boolean
'''
# welcome, ______ to the yea _______
# we will pass variables in these fillups
# you don't want any type of variable to come here
# you always want a string in the first blank and 
# am omteger in the second fillup
binary = 0b101 #this works stores binary as integer base 10

greeting = "hello, {x}".format(x = name)
print(greeting)
greeting = "hello, {x} to {y}".format(x = name, y = year)
print(greeting)
greeting = "hello, {} to {}".format(name, year)
print(greeting)
greeting = f"hello, {name}, binary is {~binary:0b} to {year}" # 'F' can also be used # "~" means complement -> gives binary of -5 which is -6(-110)
print(greeting)


print(format(12, "b"))  # prints binary

'''slicing in python''' # same for lists

s = "codechef"
print(s[:2]) # from start to first 2 elements
l = [1, 1, 2, 3 ,4 ,54 ,4 ,1 ,1 ,15]
print(l[2:4])

# l[start index : end index + 1 : jump]
# by default jump = 1
print(l[0:5:2])
print(l[1:]) # start from 1 till end
print(l[:5]) # start from 0 till 5-1 index
print(l[-2:]) # last two elements
print(l[::2]) # index selected: 1 3 5 7 9 so on

# concept of mutability in strings

li = [1,2, 3,4 , 5, 6]
li[2] = 22 # this works 
# this works for lists because lists are mutable
st = "codechef"
'''st[2] = "r"''' # this won't work
# because strings are not mutable

# we can also assign a list by slicing
li[1:5] = [1, 2, 4, 5] 

'''
functions
'''
# how python reads your code
# we will later discuss this indepth
# python is an interpreted language
# by default programming languages are of 3 types 
# compiled , interpreted ,  hybrid(compiled+interpreted)
# c, cpp     ruby, python   java
# compiled languages are those languages that use a
# compiler to convert code to machine readable language
# compiler is a program that reads your code and if ther
# are no errors then it will execute

# interpreted languages use an interpreter which 
# reads code line by line and the first line where it seees
# an error it stops there

# python's interpreter reads our code line by line..



# functions
x1 = 10
y1 = 20
x2 = 31
y2 = 19
# we are supposed to calculate distance between 2 points

c = ((x1-x2)**2 + (y1-y2)**2)**0.5


# DRY : don't repeat yourself

# function is a block of organised, reusable code that is uded to perform single, 
# related action to improve code modularity
# we have based on implementation 2 types of function
# 1) inbuilt
# 2) user-defined
# In math alos we have functions like f(x) like function is a 
# black box which will take some input and return 
# some output
# f(x, y)
# In python also a function can or cannot take an 
# input (argument) , to do some computation
# we will create some functions now in python we
# can create a function like this
'''
def functionname(arguments):
    this will create a new block where you will write logic
    return value 
'''
def euclidean_distance(x1, y1, x2, y2):
    '''this function will calculate euclidean distance\nx1(int): x coordinate of first point\ny1(int): y coordinate of first point\nx2(int): x coordinate of second point\ny2(int): y coordinate of second point'''
    value = ((x1-x2)**2 + (y1-y2)**2)**0.5
    '''
    comment
    '''
    return value

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2)+ abs(y1-y2)

retval = euclidean_distance(12, 1, 0, 3)
print(retval)

print(manhattan_distance(1, 2, 4, 5))

print(euclidean_distance.__doc__) # damn
print(len.__doc__)


# docstrings 
# docstrings are custom documentation that you can
# give for a function. We can wrtie the name of the function
# and get it's docstring

# need for return if we have print()
# let's assume if we want to use the output of our
# function somewhere else
# a function without input and return also works

# you can have required arguments 
# keyword arguments
# default arguments
# variable-length arguments

# required arguments-> these are arguments passed to a fucntion
# in correct functional order
# no. of arguments passed should be equal to 
# required arguments


# keyword arguments are used when calling a fucntion
# you pass the parameter name with the value you want to use

def fun(a,b):
    print(a+b)

fun(b=10, a=3)

# default argument 
# by using a default argument, we put a dafault value to 
# a parameter while defining a function.
# while a making a fucntion call, if we don't pass
# an argument then it's default value is uded

def foo(a, b, c=0):
    return a+b+c
print(foo(1, 2)) # 3

'''def bar(a, b=4, z=3,c)
    return a+b+z+c
print(bar(1, 2, 3, 4)) # error'''

# if you want to pass default arguments then you should not have 
# any required argu to the right side of them.
def foobar(a=1,b=2,c=3):
    return a*b*c
print(foobar(5))

# variable length argument
# we may want to process many inputs but we don't 
# know how many

# then we use variable length args

def sumofnums(x, *nums):
    i = 0
    result = 0
    while i < len(nums):
        result+=nums[i]
        i+=1
    
    print(type(nums))
    print(len(nums))
    return result

s = sumofnums(10, 1, 2, 3, 4, 5, 6)
print(s)


# scope defines visibility of a var

# visibility means where you can use a var
x=100 # this x will be global

def foobar2():
    x = 10
    print(x)

foobar2()
print(x) #100 will be printed

# if local x is not found then global x will be used


'''
SUMMARY
1) required args 
2) keyword args                     to kill the positional importance of args
3) default args                     to be used in case user does not pass one
4) variable length args             to accept unknown number of args from user
'''
p = [1,2,3,4,5,6,7,8]
*nums ,= p
for i in range(8):
    print(f"hey the number is {i}")
print(nums is p)
print(nums == p)


