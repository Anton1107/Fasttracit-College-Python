m = 'This is a string in Python'
me = "This is also a string"
mes = "It's a string"
mess = '"Beautiful is better than ugly.". Said Tim Peters'
messa = 'It\'s also a valid string'
messag = r'C:\python\bin'
message = """This is a string in triple quotes"""
message1 = '''This is a string in triple quotes'''


# strings are iterable: you can loop through
for c in message1:
    print(c)

# TODO: change the above code to use 'while' structure

# TODO what does >>> message[2] = 'd' do ?

# string slicing
print(message[0:4])
print(message[-6:-1])
if message[0:] == message[:] == message:
    print(message)
print(message[25:])
print(message[:3])

# check if a phrase or character is present in a string: use keyword "in"
print('string' in message)
if 'string' in message:
    message = 'Bind variable "message" to a new string object'
print(message)
