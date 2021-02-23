# you are given a number n check if the no. is prie or not
import math

n = 4


def prime(n):
    if n==2 or n==3 :
        return True
    if n%6 == 1 or n%6==5:
        if n % 2 == 0:
            return False

        for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    else:
        return False


print(prime(n))

# calculating a**b without ** operator

# isinstance(3.5, float) will return true

def powerIteratrive(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        print("please enter valid inputs")
        return None
    
    temp = 1
    for i in range(0, b):
        temp = temp*a 

    return temp

a = 2
b = 2
result = powerIteratrive(a, b)
print(result)

# recusion

# base case
# self work
# recursive part



def powerRecursive(a, b):
    if b==0:
        return 1
    if b==1:
        return a
    
    # recursive task
    return a*powerRecursive(a, b-1)

# this code has time complexity O(n)
# and space complexity O(n) as well
# call stack is the only part that takes the maximum space
# O(n) corres to n stack frames 
# it is corres to the maximum space that you used during the execution of the program


# can we optimize a**b calculation?


'''
you can write f(a,b) = f(a,b/2)*f(a*b/2)

'''

def powerRecursiveOptimized(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    
    recursive_task = powerRecursiveOptimized(a, b//2)
    if b%2 == 0:
        return recursive_task*recursive_task
    else:
        return recursive_task*recursive_task*a

# T(b) = T(b/2) + 1
# this means no of operations for b will be equal to no of operations for b/2 +1 
# 1 comparison per operation

# time and space complexity = O(log2n)


# T(b/2) + 1
# and so on

# at last T(2) = T(1) + 1

# at last T(b) = T(1) + K where k is total actual comparisons
# k = log2(b)


# think of another series b, b/3, b/9 and so on
# here the time complexity will turn out to be more than the previous case and similarly for every n>2
# the reason is purely mathematical. therefore halving 2 each time is the most efficient way in this kind of recursive algorithm 

''' 
in case of recursive code of fibonacci as well the space complexity turns out to be O(n)

istead of O(2**n) (which is the time complexity)
the reason being the maximum memory occupied by the program at any given time t does not exceed a particular limit which is proportional to n
think of f(5) calling f(4) and f(3). f(3) is not called until f(4) returns something. similarly f(4) calls f(3) which calls f(2) which calls f(1) which returns 1.
the number of stack frames added in the call stack will be 5 at this point and then these will be destroyed subsequently, and the height of call stack will never
exceed n 

and hence the space complexity in the worst case will be O(n)
'''

# given a number n print all natural numbers till n
# code the solution recursively

# me trying

def NumsTillGivenNumber(n):
    if n == 1:
        print(1)
    
    else:
        NumsTillGivenNumber(n-1)
        print(n)




NumsTillGivenNumber(996)            # limit of recursion depth is 996, error for n=997

# f(n) is a function and let's assume this works perfectly and prints natural numbers till n
# this implies f(n) also works perfectly 
# we are assuming f(n-1) will eventually print all the numbers from 1 to n-1 and we just need to print n after that

# given a number all natural numbers till n in decreasing order

def NumbersTillOne(n):
    if n==1:
        print(1)
    else:
        print(n)
        NumbersTillOne(n-1)

NumbersTillOne(4)

# time and space complexity of both these codes is O(n)

# given a list of integers write a function, write a function to check if the list is arranged in increasing order solve it recursively

def ListSortChecker(array):
    if len(array)==1:
        print("yes")
    else:
        if array[-1] >= array[-2]:
            array.pop()
            ListSortChecker(array)
        else:
            print("no")


a = [1, 2, 3, 5, 8, 9]
# edit to fix pass by reference problem
b = a[:]        # b is a copy of a so we can do our stuff on b without affecting a
ListSortChecker(b)
print(a)        # mutable objs are passed by reference therefore our list eventually changes during the recursive calls

# the base case is that we know if we have a list of 1 length then it will be in increasing order obviously

# time complexity O(n)
# space complexity O(n)

# Q) let's say you have an nXn board
# you have n queens
# you have to place these n queens such that no queen attacks the other


# stairs question
# now from any step, you can either jump by 1 step or 2 steps 
# in how many different ways you can reach the last step?

'''
if you have number of ways for n==3
we can prepend 1 at the back

Base case:       
Self work:      
recursion:      
'''    

def ways(n, i, path):     # i represents where you are currently at
    # path is a string that stores the path
    if (i>n):
        return
        
    if i==n:
        # this base case shows that you are at the destination
        # jsut print the path and go back
        print(path)
        return

    ways(n, i+1, path + " 1")                     # self work and recursive call in the same step
    ways(n, i+2, path + " 2")     

ways(3, 0, "")

# you are given a list of size n, where all the elements of 
# the list are integers . every elemeent in the list is present twice except for 1 special element find the special element


# [1, 2, 1, 3, 2]
# 2 should be the answer here

li = [1, 2, 1, 3, 2]

# all elements are present in pair except one 
# can we any how eliminate the elements present in pair 
# if we xor a number by itself then it becomes 0
# what we can do is we can iterate over the list and bring out the xor of all the elements.
# the final value will be our answer

x = 0
for i in range(len(li)):
    x^=li[i]

print(x)

# usage of dictionary
# dict {
# <key>:value,
# <key>:value,
# }

# avg case insertion, deletion, search is THETA(1)

# worst case, THETA(n) but this rarely happens

# you are given a string of length n.
# find all the characters which are non-repeating

# example "unacademy"

# ans will be uncdemy

def getUniqueCharacters(string):
    freq_map = {}
    for i in range(0, len(string)):
        if freq_map.get(string[i]) == None:
            freq_map[string[i]] = 1
        else:
            freq_map[string[i]]+=1
    
    result = []

    for k in freq_map.keys():
        if freq_map[k] == 1:
            result.append(k)
    
    return tuple(result)


string = "codechef"
print(getUniqueCharacters(string))

# new stuff

# like 1 dimensional list we can have n dimensional list as well


'''
like a list of lists is a 2-D list
'''
# you are given an integer list of size n. now after taking input of the list you will get another integer Q
# q represents no. of queries that means you will get q queries and inside each query you will get 2 numbers denoting index of array lof list L and R.
# you have to print sum of elements from L to R for each query

li = [1, 2, 7, 1, 3, 2]


def calculate_prefix_sum(li):
    result = []
    sum = 0
    for i in range(0, len(li)):
        sum+=li[i]
        result.append(sum)
    return result

def process_query(prefix, li, l, r):
    return prefix[r] - prefix[l] + li[l]



for i in range(0, n):
    #x = int(input())
    x = 45
    li.append(x)

prefix_sum = calculate_prefix_sum(li)
q = 0

while(q > 0):
    # l, r = map(int, input().split())
    l, r = 1, 5
    print(process_query(prefix_sum, li, l, r))
    q-=1

# given a list of integers of size n, print all the subsets of the given list.

'''
for the input [1, 2, 3]

answer should be
[]
[1]
[2]
[3]
[1, 2]
[2, 3]
[1, 3]
[1, 2, 3]

total 8 because each element has 2 choices 

'''


def subset(li, idx, output):
    """
    li -> input list
    idx -> is used to point to current element
    output -> output string

    """
    if idx == len(li):
        print(output)
        return
    
    subset(li, idx+1, output+str(li[idx]))
    subset(li, idx+1, output)
    return

li = list(map(int, input().split()))
subset(li, 0, "")

# use bitwise operators to solve this iteratively

# similar to break there are 2 more statements 
# continue and paas

# continue: goes back for next iteration of the nearest loop
# pass: pass is used to indicate some missing code. it is simply ignored by the interpreter

def SubsetsIteratively(l):
    base = []   
    lists = [base] 
    for i in range(len(l)): 
        orig = lists[:] 
        new = l[i] 
        for j in range(len(lists)): 
            lists[j] = lists[j] + [new] 
        lists = orig + lists 
          
    print(lists) 


SubsetsIteratively(li)


