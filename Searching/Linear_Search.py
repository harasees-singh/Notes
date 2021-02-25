# 1) linear search
# O(n) TC
# O(1) SC

def LinearSearch(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return 1
    return -1