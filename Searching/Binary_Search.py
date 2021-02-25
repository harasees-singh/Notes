# 2)Binary search
# time complexity O(logn)
# space complexity O(1)
# can be applied on all those search conditions where we can divide the search space into 2 parts such that 
# 2 parts are distinguishable based on some property

def BinarySearch(arr, target):
    # define the search space
    n = len(arr)
    left, right = 0, n-1
    while left <= right:
        mid = (left +right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1