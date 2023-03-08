from strings.strings_definitions import message

print(message)

# upper() /lower() Turns all chars in UPPERCASE/lowercase
print(message.upper())
# message.count(): Return the number of non-overlapping
# occurrences of substring sub
print(message.count('in'))
# message.index(): Return the lowest index in the string
# where substring sub is found
print(message.index('in'))
print(message.index('in', -10))
# message.isalpha(): Return True if all characters in
# the string are alphabetic
print(f"Has the string only alphabetic chars? No")
print('1234'.isnumeric())
print('1234'.isdigit())

# Split a string by a given separator, the result is a list
# could any character,the most used ones are: ".", " ", ", "
immutable_types_string = " a, b, c"
print(immutable_types_string.split(','))
mutable_types_list = ["x", "y", "z"]
print(', '.join(mutable_types_list))

# replace(old, new): Return a copy of the string with all
# occurrences of substring old replaced by new
