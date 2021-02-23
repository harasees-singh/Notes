def BubbleSort(l):
	
	
	for j in range(len(l)):
		swaps = False
		for i in range(len(l)-j-1):
			if l[i]>l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
				swaps = True
		if swaps == False:
			return l

	return l

# comparison based sort
# after 1 iteration the biggest element of unsorted region is at the correct position
# time coplexity: O(n**2)
# space complexity: O(1)
# inplace: Yes
# no. of comparisons: O(n**2)
# no. of swaps: O(n**2)     significant increase
# bubble sort is stable

# best case time coplexity OMEGA(n) (requires using a boolean to know if no swap occured in 1st iteration)
