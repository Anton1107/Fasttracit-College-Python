

# Strings format:
# format() method
from strings.strings_definitions import m

string_var = "This article is written in {}"
print(string_var.format("Python"))
string_var2 = "Format example #{} for {} {}"
print(string_var2.format(2, "Python", "strings"))
# F-strings aka formatted string literals
print(f"First string var is: '{m}' of length {len(m)} ")
print(f"First string var is: '{string_var}' of length {len(string_var)} ")
