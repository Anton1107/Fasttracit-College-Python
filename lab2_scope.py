

my_variable = 'Outer scope: at module level'


def scope_function():
	my_variable = 'Inner Scope: inside the function'
	print(my_variable)


scope_function()
# print(my_variable)
