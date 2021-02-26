# given a perfect square value S between 1 and 10**9
# find it's square root
n = 16
li = [i for i in range(n)]

def BinarySearch(li, left, right):
    if left == right:
        return left
    mid = (left+right)//2
    if mid*mid < n:
        left = mid+1
    else:
        right = mid
    ans = BinarySearch(li, left, right)
    return ans
    
print(BinarySearch(li, 0, len(li)-1))


# discrete binary search can be carried out on monotonic sequences
# there are n rectangles of same size (w*h) it is required to find a square of the smallest size
# into which these rectangles can be packed we can't rotate the rectangles
# find the side of the smallest square

# biggest square possible will be max(w,h)*n
# min (not possible) = 0

# if mid//w * mid//h >= n to inculcate all rectangles
# then reject the right half

# do binary search

def good(mid, n, w, h):     # it will tell whether mid is good or not
    return (mid//w)*(mid//h) >= n

def adjust_rectangle(w, h, n):
    low = 0
    high = max(w, h)*n
    ans = -1
    while low < high:
        mid = low + (high-low)//2
        if good(mid, n, w, h):
            high = mid
            ans = mid
        else:
            low = mid + 1
    return ans

print(adjust_rectangle(2, 3, 3))

# Time complexity is O(max(w,h)*n)

# you have a practical and you do 'n' copies of a page 
# There are 2 machines at the shop
# first one copies that a sheet in x seconds 
# and the second one copies in y seconds
# you can run both machines parallely and can create photocopy
# of both original and copied page find the minimum time required to make n copies

# if mid is 'good' eleminate right half
# mid is 'good' if mid//p + mid//q >= n - 1

# i will reuse the already written good()

def printing_copies(n, x, y):
    if n == 1:
        return min(x,y)
    
    low = 0
    high = max(x,y)*n
    ans = -1
    while low < high:
        mid = low = (high-low)//2
        if good(mid, n-1, x, y):
            ans = mid
            high = mid-1
        else:
            low = mid + 1

    return ans + min(x,y)

print(printing_copies(5, 1, 2))
