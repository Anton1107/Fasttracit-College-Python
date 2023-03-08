# 3. List slicing
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = numbers_list[::2]
print(even_list)
# print(numbers_list[::-1])
print(numbers_list[1:5:3])
print(numbers_list[::-2])
# print(numbers_list[7:4:-2])


# 4. Lists can be nested
# index:      0            1                           2       3          4
test_list = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

print(test_list[0], test_list[2], test_list[4])
print(test_list[1], test_list[3])
print(test_list[1][0])
print(test_list[1][1][1])
print(test_list[3][::-1])


# 4. Lists are mutable
list2 = test_list
test_list[0] = 1
print(id(test_list), test_list)
print(id(list2), list2)
string1 = 'This is a string'
string2 = string1
string2 = string2 + '!'
print(id(string1), string1)
print(id(string2), string2)
# string1[0] = 3

# 6. Lists are dynamic
test_list[0] = [1, 2, 3, 4]
print(test_list)

test_list[1:3] = [string1]
print(test_list)

test_list[1:3] = [string1, string2]
print(test_list)

del test_list[0]
print(test_list)


new_list = ['some', 'other', 2.4, 76]
test_list = test_list + new_list
print(test_list)
# print(new_list) ?

new_list = test_list + new_list
print(new_list)
print(test_list)

new_list += 'string'
# new_list += ['string']
# print(new_list) ?

# Use "in"/"not in" operator to check if an item is present in the list or not
print('some' in new_list)
print('non-existent' in new_list)
