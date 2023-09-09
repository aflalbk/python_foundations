my_list = [2, 3, 4, 5, 6, 7, 8]

# Ordered:
# Lists in Python are ordered collections.
# The order of elements is maintained, and you can access them by their index.
print(my_list[2])
print(my_list[3])

# Mutable:
# Lists are mutable, meaning you can change their content. You can add, remove, or modify elements.
my_list_1 = [2, 3, 4, 5, 6, 7, 8]
print(my_list_1)
my_list_1[2] = 9
print(my_list_1)

# Heterogeneous:
# Lists can hold elements of different data types in the same list.
my_list_2 = [2, 'hi', 'free', 3.4, 6, True, False]
print(my_list_2)

# Dynamic:
# Lists can change in size dynamically by adding or removing elements.
print(my_list)
my_list.append(9)  # add 9 in the end of list
print(my_list)
my_list.remove(3)  # remove 3 from the list
print(my_list)
my_list.remove(my_list[3])  # remove 3rd index value form the list
print(my_list)

# Iterable:
# Lists can be iterated using loops to process each element sequentially.
for values in my_list:
    print(values)

# Slicing:
# You can use slicing to extract sublists from a list based on indices.
print(my_list[2:5])

# Nesting:
# Lists can be nested within other lists, creating multi-dimensional structures.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(nested_list[2][2])
print(nested_list[1][1])
index = nested_list.index([4, 5, 6])
print(index)

# In-Place Sorting:
# Lists can be sorted in-place using the sort() method, rearranging elements in ascending order.
my_list_3 = [4, 9, 2, 9, 5, 0, -1, -6, 3, 4]
print('Before sorting ' + str(my_list_3))
my_list_3.sort()
print('After sorting ' + str(my_list_3))

# concatenate list with list
list_1 = ['hi', 'data', 'image.png', 23]
list_2 = list_1 + [2, 'free', 'download', 34, 'user']
print(list_1)
print(list_2)

# Ask a value to user and append that given value into the list
list_1 = ['hi', 'data', 'image.png', 23]
list_1.append(input('enter a value'))
print(list_1)