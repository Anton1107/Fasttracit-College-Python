
#  positional args
def multiply_2_numbers(x, y):
	return x * y


# print(multiply_2_numbers(5, 4))
# print(multiply_2_numbers(5, 4, 3))

# * args
def multiply_many_numbers(*args):  # def multiply_many_numbers(*numbers):
	z = 1
	for num in args:
		z *= num
	return z


# multiply_many_numbers(4, 5)
# multiply_many_numbers(10, 9)
# multiply_many_numbers(2, 3, 4)
# multiply_many_numbers(3, 5, 10, 6)


def concatenate_kwargs(**kwargs):
	result = ""
	# Iterating over the Python kwargs dictionary
	for arg in kwargs.values():
		result += arg
	return result


# print(concatenate_kwargs(a="Python", b="Is", c="Great", d="!"))


# *args version
def concatenate_args(*args):
	result = ""
	# Iterating over args
	for arg in args:
		result += arg
	return result


# print(concatenate(a="Python", b="Is", c="Great", d="!")) ??


# Packing and unpacking examples

# Example 1:
def fun(a, b, c, d):
	print(a, b, c, d)


my_list = [1, 2, 3, 4]
# fun(my_list) # This doesn't work
# Solution: Unpacking list into four arguments:
# fun(*my_list)

# Unpacking lists example
# student = ["Matia Opris", "20", "Python Lab 4"]
# name = student[0]
# age = student[1]
# lab_number = student[2]
#
# name, age, lab_number = ["Matia Opris", "20", "Python Lab 4"]


# Example 3:
my_list2 = [1, 2, 3, 4, 5]  # my_list2 might have an unknown number of elements
# fun(*my_list2)  # fun() takes 4 positional arguments but 5 were given


def fun2(*args):
	print(args)
	print(*args)
	for arg in args:
		print(arg)


# fun2(*my_list2)
# fun2(10, 20)


# intro: a dictionary is a composite data type which consists
# of a collection of key-value pairs: { key: value }
d = {'a': 2, 'b': 4, 'c': 10, 'd': 12}
# fun(**d)


def fun_kwargs(**kwargs):
	# kwargs is a dict
	print(type(kwargs))

	# Printing dictionary items
	for key, value in kwargs.items():
		print(key, value)


# fun_kwargs(name="John", id=10100, language="Python", completed_labs=[1, 2, 3, 4])
