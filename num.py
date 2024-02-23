#print every 3 nums:
def every_three_nums(start):
  return list(range(start, 101, 3))
print(every_three_nums(91))
#returns [91, 94, 97, 100]

#remove middle nums:
def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
#returns [4, 23, 42] because elements at indices 1, 2, and 3 have been removed


#double index
def double_index(my_list, index):
  # Checks to see if index is too big
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list 
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list
print(double_index([3, 8, -10, 12], 2))
