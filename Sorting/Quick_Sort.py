# QUICK SORT
    
# given a list of size n and any one element from the list called the pivot element
# you need to segregate all the elements lesser than pivot on the left side and greater than pivot on the right side in any order


# let's say you have a list like [10, 7, 8, 9, 1, 5]
# we can iterate over the entire list and compare with the pivot

# partition algorithm 👀

# TC: THETA(nlogn), OMEGA(nlogn), O(n**2)
# SC: O(logn)
# in place: yes
# stable: no

import random

def partition(arr, left, right):
    m = left
    pivot_index = random.randrange(left, right)
    pivot = arr[pivot_index]
    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
    for i in range(left, right):
        if arr[i]<pivot:
            arr[i], arr[m] = arr[m], arr[i]
            m += 1
        
    arr[m], arr[pivot_index] = arr[pivot_index], arr[m]
    return m


def quicksort(arr, left, right):
    if left >= right:
        return

    pivot_index = partition(arr, left, right)
    quicksort(arr, left, pivot_index-1)
    quicksort(arr, pivot_index+1, right)

    return    
    