x_values = [1, 2, 3]  # Some iterable x
for x in x_values:
    print(x * x)

# instead of
for i in range(len(x_values)):
    print(x_values[i] * x_values[i])

# enumerate
letter_list = ['a', 'b', 'c']
for index, letter in enumerate(letter_list):
    print(f"letter_list[{index}] = '{letter}'")


# zip
def zip_example():
    countries = ('Japan', 'Korea', 'China')
    cities = ('Tokyo', 'Seoul', 'Beijing')
    for country, city in zip(countries, cities):
        print(f'The capital of {country} is {city}')


# unzip-ing
def unzip_example():
    full_name_list = [('Andrei', 'Dragan', 23),
                      ('Anton', 'Bubnyak', 24),
                      ('Flavius', 'Fischer', 25),
                      ('Iosif', 'Szabo', 26),
                      ('Matia', 'Opris', 27)]

    first_name, last_name, age = list(zip(*full_name_list))
    return first_name, last_name, age


def for_continue(limit):
    for num in range(1, limit):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)


# 'for' with break else:
def for_with_break_else(max_limit):
    for y in range(0, 3):
        print("y: {}".format(y))
        if y == max_limit:  # will be executed
            print("BREAK: y is {}\n----------".format(y))
            break
    else:  # not executed because break is hit
        print("y_loop completed without break----------\n")


# zip_example()
# unzip_example()

# for_continue(10)

# for_with_break_else(1)
# for_with_break_else(2)


