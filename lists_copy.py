# list.copy Shallow Copy

list1 = [1, 'element']
list2 = list1[:]  # Copy using "[:]" equivalent with list2 = list1.copy()
list2[0] = 2  # Only affects list2, not list1
print(list1[0])  # Displays 1

# By contrast on assigning
list1 = [1, 'element']
list2 = list1
list2[0] = 2  # Modifies the original list as well
print(list1[0])  # Displays 2

list1 = [1, [2, 3]]  # Notice the second item being a nested list
list2 = list1[:]  # A shallow copy
list2[1][0] = 4  # Modifies the 2nd item of list1 as well
print(list1[1][0])  # Displays 4 rather than 2

import copy
list1 = [1, [2, 3]]  # Notice the second item being a nested list
list2 = copy.deepcopy(list1)  # A deep copy
list2[1][0] = 4  # Leaves the 2nd item of list1 unmodified
print(list1[1][0])  # Displays 2
