def binary_search_on_rotated(arr, target):
    n = len(arr)
    start, end = 0, n-1

    while start<=end:
        mid = start + (end-start)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= arr[start]:
            if target >= arr[start] and target < arr[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if target <= arr[end] and target > arr[mid]:
                start = mid+1
            else:
                end = mid-1
            
    return -1