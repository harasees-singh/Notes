'''recursion'''
# to recurse is divine
x = 1
y = 20

# given two numbers write a program to swap them

def swap(x,y):
    t = x
    x = y
    y = t
    return x, y

print(swap(x,y))
print(x, y)         # x and y are not changed.. interesting

def swap_pythonic(a,b):
    a, b = b, a
    return (a, b)

print(swap_pythonic(x,y))
print(x, y)   

# let's see if lists are are updated or not

def update_list(li):
    li.append(10)
    print(f"inside function after update li = {li}")

li = [1, 2, 3, 4, 5, 6]
update_list(li)
print(li)       # this updated the list.. interesting

# this won't work for strings because strings are immutable

# when we pass a list inside a function then it is
# passed by reference(actual original list is passed)
# so whatever is change is made to that will persist
# But in case of int, strings, bool, float they are 
# passed by value( meaning a copy of them is passed )
# so the changes won't persist outside the function

def update(x):
    x+=1
y = 10
print(y)
update(y)
print(y)

# pass by value-> int, str, pool, float
# pass by reference->lists

# recursion
# a story to understand recursion
# a child couldn't sleep so her mother told her a story aobut a little frog,

# Mathematically recursion is the process where we 
# have special composite functiionsm, where the composite
# is made such that function calls itself inside it only 



'''recursion is defined as a tool where a function
solving a bigger problem, calls itself inside it to solve 
another problem, till the time we reach to a stage
where we have the smallest already solved problem
with an extra memory buffer'''

# factorial

# let us say f(n) is a function that returns n!
# f(0) = 1 this is your base csae
# assume f(n) works for n=k then we have value for n=k+1
# f(k+1)=(k+1)*f(k)


# fibonacci series: 0,1,1,2,3,5,8,13...
# any ith term is the sum of previous 2 terms
# base case-> f(0) = 0, f(1) = 1
# for n = k, f(k) correctly calculates kth fibonacci
# for n=k-1 f(k-1) correctly calcs k-1 th fib
# f(n) = f(n-1) + f(n-2)

def fibonacci_recursion(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        answer =fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
    
    return answer

print(fibonacci_recursion(7))

def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n

print(factorial(4))

# your 32GB ram has to store a lot of things
# some amount is allocated to run your python code


# call stack    
# heap(pool)    everything is random

# call stack is a linear memory storage
# you will always add on the top and remove from the top
# Call stack->whenever you call a function we add an entry
# to the top of call stack. this entry is called as stack frame
# these are frames of function calls 
# what is there in a frame? all the local variables of a 
# function are there in the frame
# local variable will die after stack frame is removed



# return-> removes the entry of the frame from call stack
# and returns a value

'''
loops are space optimized 
recursion is not
but some algorithms are really easy to implement via recursion

'''
# the purpose of print function is to pass the values to the outp


'''
COMPLEXITY ANALYSIS OF ALGORITHMS

'''
# processes consume some memory
# to execute a task process takes some time
# we want the algo to be memory and time efficient


# how can we calculate how much time an algorithm takes to execute


# the point at which the code starts to execute and the point
# where the code ends we can put time stamps there and 
# then obtain the execution time
# this is called experimental analysis but this is not the
# best way
# 
# 
# because your computer system does not actually execute everything
# parallely
# 
# 
# multitasking is a myth but not entirely
# 
# 
# cores are like individual units that exist in computer system
# 
# 
# multiprocessing and multitasking are 2 different terms
# multiprocessing exists multitasking is a myth
# at any instant t you can have any only n parallel processes
# in an n core machine
# 
# 
# in a single core you have a list of processes and at some time t
# your cpu will pick 1 process and then put the rest on hold 
# in waiting state
# your cpu will execute that process for some definite time t
# and then pick some other process and so on
# 
# time consumed vs input size graph
# 10**8 cycles in 1sec for a microprocessor
# 
# the change in execution time based on change in input is a better
# metric to measure
# this is called rate of growth of algorithm execution time
# and the algo having lesser rate of growth will be better
# for example something like ax**n + bx**(n-1) + ... + const is a polynomial
# if we compare 2 polynomials with same degree will have similar
# rate of growths for large value of x
# 
# let us say if we compare a linear expression and a quadratic cureve
# then the linear will be better
# 
# if we can approximately visualize the rate of growth in terms of the 
# highest degree polynomial,we can compare algorithms
# 
# this type of analysis is called asymptotic analysis   
# 1) what is the best case
# 2) avg case
# 3) worst case
# 
# avg case represents on an average what polynomial the algo
# follows and the worst case is when you don't do any optimization
# 


# consider prime number code where we check till sqrt(n) 


# best case is represented by "omega(1)" when n = 2
# avg case is represented by "theta(sqrt(n))" when n = 10**8
# worst case is represented by "O(sqrt(n))" when n = 10**16

# consider the algo 

# implement your own insertion algorithm that inserts at the last
# of the list where you can only create list of constant size
# you cannot use append instead write your own function called
# add at last, that adds element at last


# 1 2 3 4 5 6 7 8 9
# [1]
# [1, 2]
# [1, 2, 3]
# 
# 
# instead we can use this algo
# 
# [1]
# [1, 2]
# [1, 2, 3, ]
# [1, 2, 3, 4] # by doubling the size of array we did not have to make a new array altogether
# [1, 2, 3, 4, , , , ]
# 
# 
# 
# here 
# Omega(1) best case
# O(n) worst case
# theta()
