
# Adding elements

# list.append
test_list = [1, 2, 3, 4, 5]  # use range?
test_list.append(6)  # test_list(len(test_list):) = [6]
test_list.append(['abc', 'def'])
print(test_list)

# list.extend
# test_list.extend(7)
test_list.extend([7, 8, 9, [10, 11]])
print(test_list)

# list.insert
test_list.insert(0, 0)
print(test_list)


# Removing
# list.remove
test_list.remove(5)
print(test_list)

# list.pop / list.pop(index)
test_list.pop()
print(test_list)
test_list.pop(6)
print(test_list)
test_list.pop(-1)
print(test_list)

test_list.clear()
print(test_list)


# list.sort(key=None, reverse=False)
string_list = ['This', 'is', 'a', 'string', 'list']
string_list.sort()
print(string_list)
string_list.sort(key=str.lower)
print(string_list)
string_list.sort(key=str.lower, reverse=True)
print(string_list)

mixed_list = [1, '12', 3, 4, '45']
mixed_list.reverse()
print(mixed_list)

# mixed_list.sort()
# mixed_list.sort(key=int)
print(mixed_list)
