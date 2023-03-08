# Comparisons

places_list = ["Berlin", "Paris", "Cluj-Napoca"]
current_city = "Cluj-Napoca"
# current_city = "cluj-Napoca" // lower

for place in places_list:
	if place < current_city:
		print(f"{place} comes before {current_city}")
	elif place > current_city:
		print(f"{place} comes after {current_city}")
	else:
		print(f"{place} is identical to {current_city}")

# 'is' vs '=='
# example 2
list1 = [1, 2, 3]
list2 = [1, 2, 3]
# print('Lists values are equal' if list1 == list2 else 'List are not equal')
# print('Objects are identical' if list1 is list2 else 'Objects are not identical')
