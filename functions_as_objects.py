# 1. The function can be assigned to a variable

def get_even(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(get_even(list1))

even_list = get_even
# print(even_list(list1))


# 2. Pass the function as a parameter to another function
# ridicare la patrat sau x squared
def get_squared(func):
    result = []
    numbers = func(list1)
    for n in numbers:
        result.append(n*n)
    return result


squared_even_list = get_squared(get_even)
print(squared_even_list)


# 3. Functions can return another function
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper


speak_func = get_speak_func(0.7)
speak_func('Hello')

# def get_speak_func(text, volume):
#     def whisper():
#         return text.lower() + '...'
#     def yell():
#         return text.upper() + '!'
#     if volume > 0.5:
#         return yell
#     else:
#         return whisper
# get_speak_func('Hello, World', 0.7)()


# 4. Functions can be stores in data structures such as lists
function_list = [min, max, sum]
for func in function_list:
    print(func(list1))
# function_list[0](list1)
