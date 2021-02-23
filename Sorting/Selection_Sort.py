
def find_min_element(arr, start):
    min_index = start
    start+=1

    while start< len(arr):
        if arr[start]< arr[min_index]:
            min_index = start
        
        start += 1
    
    return min_index


def selection_sort(arr):
    i = 0
    while i<len(arr):
        min_index = find_min_element(arr, i)
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

        i+=1
    return

# it is a comparison based sorting algorithm
# let's say you have 2 parts of your list one sorted and the other unsorted
# time: O(n**2)
# space: O(1)
# swaps: O(n)
# comparisons: O(n**2)
