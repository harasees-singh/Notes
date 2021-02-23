def merge(a, b):
    n = len(a)
    m = len(b)

    ouput = [0]*(n+m)

    i, j, k = 0, 0, 0
    while i<n and j<m:

        if a[i]<b[j]:
            ouput[k] = a[i]
            i+=1
            k+=1
        
        else:
            ouput[k] = b[j]
            j+=1
            k+=1

    while(j<m):         # if i was exhausted
        ouput[k] = b[j]
        j+=1
        k+=1
    
    while(i<n):         # if j was exhausted
        ouput[k] = a[i]
        i+=1
        k+=1
    
    return ouput


# space complexity: O(n+m)
# time complexity: O(n+m)


# merge sort says if you have an unsorted list 
# divide your list into 2 equal halves 
# sort the left half recursively 
# sort the right half recursively



def merge_sort(arr, left, right):

    if left == right:
        # base case
        return [arr[left]] # or return [arr[right]]

    mid = (left+right)//2

    left_half = merge_sort(arr, left, mid)
    right_half = merge_sort(arr, mid+1, right)
    ouput = merge(left_half, right_half)
    return ouput


# time complexity: 
# let T(n) be a function which calculates no. of operations to apply
# merge sort on a list of size n

# T(n) = T(n/2) + T(n/2) + O(n) where O(n) is the time complexity for merge()
# T(n) = 2*T(n/2) + O(n)        this is the recurrence relateion
# T(n/2) = 2*T(n/4) + O(n/2)
# T(n/4) = 2*T(n/8) + O(n/4)

# T(n) = O(n) + 2*O(n/2) + 4*O(n/4) +....
# T(n) = O(nlog2(n))

# space complexity:
# python/java have a garbage collector
# O(n + logn) = O(n)
# this is not inplace
# it is stable
# no swaps involved

# Q) what are the number of comparisons needed for merge sort 
# O(nlogn)