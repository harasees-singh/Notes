def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i] # this element will be now inserted to it's correct position
		j = i - 1 # because the right place of insertion will be on left
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
		print(arr)

	return
# >> Time complexity:     O(n^2)
# >> Space complexity:    O(1)
# >> In-place:            YES
# >> No. of comparisons:  O(n^2)
# >> No. of swaps:        O(n^2)
# >> Stability:           STABLE
# 
# >> Time complexity in best case:       Omega(n)
# >> Time complexity in avg case:        Theta(n^2)
# ** Implemented in ** selection_sort.py **