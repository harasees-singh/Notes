import bisect

# time complexities of bisect left and right are O(logn)

li = [8, 10, 45, 46, 47, 45, 42, 12]

index_where_x_should_be_inserted_is = bisect.bisect_right(li, 13)   # 2 returned 
index_where_x_should_be_inserted_is = bisect.bisect_left(li, 46)   # 4 returned 
print(index_where_x_should_be_inserted_is)


print(bisect.bisect_right([2,6,3,8,4,7,9,4,6,1], 5))        # it returns 5 or in other words 5 should be inserted between 4 and 7
                                                            # seems like it starts checking from the center


# note if list is not sorted then it will still work 



sorted_list = [1, 2, 2, 3, 4, 5, 6]
print(bisect.bisect_right(sorted_list, 2), bisect.bisect_left(sorted_list, 2))
# note: you can get the count of 2 from the above info provided by the right and left bisect 
# since right bisect returns 3 and left one returns 1 it means there are 3-1 = 2 number of 2s present already in the list
