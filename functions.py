
def message():
	"""
	this is a print function without parameters
	"""
	print("Welcome to Lab4")


message()


def course_func(name, course_name):
	"""
	This is a function with 2 positional parameters
	:param name:
	:param course_name:
	"""
	print(f"Hello {name} Welcome to Lab4")
	print(f"Your class is about {course_name}")


course_func('Andrei', 'Python functions')
# course_func(name='Andrei', 'Python functions')
# course_func(name='Andrei', course_name='Python functions')
# course_func('Andrei', course_name='Python functions')


def course_func_default(name, course_name='Python Functions'):
	"""
	This is a function with 2 parameters
	:param name: positional parameter
	:param course_name: default parameter
	"""
	print(f"Hello {name} Welcome to Lab4")
	print(f"Your class is about {course_name}")


course_func_default("Octavian")
# course_func_default(name='Andrei', 'Python functions')
# course_func_default(name='Andrei', course_name='Python functions')
# course_func_default('Andrei', course_name='Python functions')
