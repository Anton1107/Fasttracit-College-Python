
def is_even(number):  # docstring
	if number % 2 == 0:
		return True
	else:  # is 'else' really necessary?
		return False


n = 17
print(f"Number {n} is {'even' if is_even(n) else 'odd'}")
# print(f"Number {n} is {'even' if is_even(number=n) else 'odd'}")


def arithmetic(num1, num2):
	addition = num1 + num2
	subtraction = num1 - num2
	multiply = num1 * num2
	division = num1 / num2
	return addition, subtraction, multiply, division


add, sub, multiply, division = arithmetic(10, 2)
result = arithmetic(10, 2)
print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", multiply)
print("Division: ", division)



