def counting_sort_personal(arr):
    frequency = [0]*(max(arr)+1)

    
    for i in range(len(arr)):
        frequency[arr[i]] +=1
    
    # make prefix sum
    for j in range(1, len(frequency)):
        frequency[j] = frequency[j] + frequency[j-1]

    output = [0]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        output[frequency[arr[i]]-1] = arr[i]
        frequency[arr[i]] -= 1

    return output


# if range of elements is too high then it performs poorly
# not an inplace sort