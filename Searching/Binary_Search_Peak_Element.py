# whether we are able to divide our search space into 2 parts 
# based on some property or not.

# find an element that is bigger than it's neighbours

# Peak element

def find_peak(arr):
    low, high = 0, len(arr) - 1
    
    while low < high:
        mid = low + (high-low)//2
        # print( low, high)

        if arr[mid] > arr[mid+1]:
            # case 2
            high = mid
        else:
            # case 1
            low = mid + 1

    return low

li = [1, 2, 3, 4, 5, 7, 5, 2, 3]

print(find_peak(li))