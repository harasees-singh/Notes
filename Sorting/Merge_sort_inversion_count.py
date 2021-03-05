li = [2, 1, 3, 1]
# if you make all the possible paris then the pair with a[i]>a[j] with i < j counts as 1 inversion pair


count = 0

def merge(a, b):
    global count
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
            count += (n - i)    # icrement count by the number of possible inversion pairs 
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

inv_count = merge_sort(li, 0, len(li) - 1)
print(inv_count, count)

