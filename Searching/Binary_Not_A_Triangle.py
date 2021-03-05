
# Q) not a triangle 

# you have n sticks and pick any 3 and it must not form a triangle
# we know for any 2 sides a, b if we have a third side c
# such that a + b < c then we have 1 possible answer
import bisect
n = int(input())

def bisect_right(li, target):
    n = len(li)
    low = 0
    high = n
    while(low < high):
        mid = (high+low)//2
        if target >= li[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


while True:
    li = [int(x) for x in input().split()]
    li.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            ans = ans + len(li) - bisect.bisect_right(li, li[i]+li[j])
            
    print(ans)
    n = int(input())
    if n == 0:
        break
