empty_tuple = ()

tuple1 = (3, 4)
print(type(tuple1))
tuple2 = (3, 3, 'x', [1, 2])
print(type(tuple2))
tuple3 = 3, 4, 'c', [1, 2]
print(type(tuple3))

students = [
    ("George", ["CompSci", "Physics"]),
    ("Marc", ["Maths", "CompSci", "Stats"]),
    ("Ana", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Diana", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Robert", ["Sociology", "Economics", "Law", "Stats", "Music"])]
print(students[0][0])
print(students[0][1])
print(students[0][1][0])

# tuples are immutable
tuple4 = ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# tuple4[0] = 88888 # does not support item assignment

# tuples can contain mutable objects, such as lists:
tuple5 = ([1, 2, 3], [3, 2, 1])
tuple5[0][0] = 10
print(tuple5)


# tuple functions:
# index(elem, start, end) - start/end are optional
# count(elem)

# tuple2 = (3, 3, 'x', [1, 2])
# dir(tuple2)

print(f"Index of 'x' is {tuple2.index('x', 1, 3)}")
# print(f"Index of 'x' is {tuple2.index('x', 1, 2)}")
print('x' in tuple2)

print(f"Number of occurrences of 3 is: {tuple2.count(3)}")
print(f"Number of occurrences of 3 is: {tuple2.count([1, 2])}")
print(f"Number of occurrences of 3 is: {tuple2.count(7)}")


# reversing a tuple
tuple1 = (3, 4)
tuple1 = tuple1[::-1]
print(tuple1)

# adding tuples together
# tuple2 = (3, 3, 'x', [1, 2])
add_tuple = tuple1 + tuple2
print(add_tuple)

print(id(tuple1))
tuple1 = tuple1 + tuple2
print(tuple1)
print(id(tuple1))

l1 = [1, 2]
print(id(l1))
l1.append([3, 4])
print(id(l1))

# sorting tuples
# sorted() https://realpython.com/python-sort/

tuple6 = (23, 5, 56, 100, 2, 0)
print(sorted(tuple6))

tuple7 = ('a', 'f', 'h', 'b', 'C')
print(sorted(tuple7, key=str.lower))


amount = 1000  # original
# year 1
new_amount = amount + amount * 0.035

# year 2
new_amount2 = new_amount + new_amount * 0.035