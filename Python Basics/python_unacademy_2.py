# mambership operators
arr = [1, 2, 4, 5]
print(1 in arr) # returns True

print(3 not in arr) # returns True

# Identity operator
print(3 is 4)
print(4 is True) # False
# it will check if both have same values and the same type
print(7 is not 7)

# order of precedence
# how does python evaluate BODMAS type problems? order of precedence is as follows
'''
for cascading it will read from right to left for eg. 2**3**4 
will be resolved as 2**81

**
~, +, - (+,- for sign purposes like -1)
*, /, %, //
+, -
<<, >>
&
|, ^
<=, >=, <, >
==, != 
=, %=, /= and so on (assignments)
is, is not
in, not in
and, or, not

'''
a = 3
a = 4
# what happens here
'''there will be a memory space containing 3 and a will point to 3
when you assign 4 in a it will make a new space containing 4 and make a to point at it'''
a = [1, 2, 3]
b = [1, 2, 3]
print(a, b)
b[0] = 22
print(a, b)
# print the following pattern for the value of n
'''
    *
   ***
  *****
 *******
*********
'''
n = 5
for j in range(n):
    print(" "*(n-j+1) + "*"*(2*j+1))
    
# you can concatenate strings
# you can concatenate lists
li = [1, 2, 3]
print(li + [4, 5, 6]) # gives a new list without changing original li
li = li + [4, 5, 6] # makes a new list and makes li point to the new list

# indexing starts from 0 in lists (from left direction)
# we have another indexing starting from -1 on the far right
'''try:
    a = 2 + "sanket" # error
except:
    exit(1)'''

a = "sanket"
# pattern 
n= 4
row = 1
while row<=n:
    print(" "*(n-row), end = "\t") # for each row we have n-row spaces
    i=1
    while i<= row:
        print(i, end = "\t")
        i+=1
    
    i-=2
    while i>0:
        print(i, end="\t")
        i-=1
    print()
    row+=1

# armstrong number-> it is a number which is equal to the sum of cubes of it's digit 
# number <= 999
# given a number N check if this is a n-narcissistic number
# for example 1634
# 1**4 + 6**4 + 3**4 + 4**4
n = str(1634)
length = len(n)
sum = 0
i = 0
while i<length:
    sum+=int(n[i])**length
    i+=1

if sum == int(n):
    print(True)
else:
    print(False)

# we keep one bit as sign bit
'''
if the most significant bit is 1 it is negative
if the most significant bit is 0 it is positive 

there is an issue with 0 having both positive and negative values for
ex 1000 and 0000 will both represent zero

this is a counting problem: how binary stores negative numbers

they do that using 2's complement of a number

let's say we have 5 = 101
1's complement is :invert_all_the_bits: 010
add binary 1 to it: 011 this is the 2's complement
this is the value of -5 in binary 


all positive numbers will have most signi bit 0
all negative numbers will have most signi bit 1
0 will be 0000 (in a 4 bit machine)


in an n bit machine range of numbers is from 
-2^(n-1) to 2^(n-1)-1

'''
# strings 

# slicing in strings and lists

# operators for strings and inbuilt functions in strings

# formatting of strings and mutability of strings

# in python strings are indexed just like lists
# first char is zero index 
# 'codechef'
string = '''
='codechef'
s[0] = 'c'
s[1] = 'o'
s[-1] = 'f'

if you have a multiline string like this then on the 0th index 
will have new line character and similarly the last char will be new line char
'''  
print(string[1], string[2], string[-1])

print('\nyo what up')

# strings can be compared on dictionary or lexicographic method

print("aa" < "aab")

# membership operator
first = "sanket"

print("a" in first)
print("aa" in "sanket")

# formatting strings in python
# you can add a variable inside a string on runtime 
# without using concatenation
