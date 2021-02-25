# finding a solution with a time complexity of logn depends on the fact 
# whether we are able to divide our search space into 2 parts 
# based on some property or not.

# find an element that is bigger than it's neighbours

# Peak element

# case 1 is positive slope or when a[i] < a[i+1]
# case 2 is negative slope or when a[i] > a[i+1]

def find_peak(arr):
    low, high = 0, len(arr) - 1
    
    while low < high:
        mid = low + (high-low)//2
        # print(low, high)

        if arr[mid] > arr[mid+1]:
            # case 2
            high = mid
        else:
            # case 1
            low = mid + 1       # in case we are left with only 2 elements then mid will be equal to low or the left element. on a positive slope doing low = mid+1 will ensure the fact that we keep moving towards the peak
                                # if you don't do low = mid+1 this it will get stuck in the loop because mid value of low will always be set to mid and
                                # high will not change anyway
    return low

li = [1, 2, 3, 4, 5, 7, 5, 2, 3]

print(find_peak(li))