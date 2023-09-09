my_string = "Hi, my name is python"

# Strings in Python are immutable
print(my_string[15])
# we are trying to change 'P' instead of 'p'
# my_string[15] = 'P'  # "Error message : 'str' object does not support item assignment".
# which means Strings are immutable

# Immutable, but Can Be Reassigned:
my_string_1 = "Hi, my name is python"
my_string_1 = "Hi, This is me"
print(my_string)

# Strings are ordered sequences of characters
print(my_string[0])
print(my_string[15])

# You can access characters or substrings of a string using indexing and slicing
substring = my_string[0:15]
print(substring)

# Concatenation:
# You can combine strings using the + operator. For example:
name = substring + "Aflal"
print(name)
# or
my_Name = 'Aflal'
name = substring + my_Name
print(name)

# Length:
# You can find the length (number of characters) of a string
print(len(my_string))

# Escape Characters:
# Strings can contain escape characters like \n for newline or \t for tab.
my_string_2_0 = "Hi, my\nname is\npython"
my_string_3_0 = "Hi, my\tname is\tpython"
print(my_string_2_0)
print(my_string_3_0)

# String Interpolation:
# using the .format() method
name = 'aflal'
age = 21
my_string_data = 'My name is {} and my age is {}'.format(name,age)
print(my_string_data)
# Using f-strings (Formatted String Literals)
my_string_data = f'My name is {name} and my age is {age}'
print(my_string_data)

# String Literals:
# You can define strings using single quotes ('), double quotes ("),
# or triple-quoted strings (''' or """) for multi-line strings:
my_string_1_0 = 'this is a string'
my_string_2 = "this is also a string"
my_string_3 = '''this is a multi line string, 
we can add one line,
or two line, 
we can add as many line we need. '''

# Python provides a variety of built-in string methods
# that allow you to manipulate and work with strings efficiently.
# Here are some commonly used string methods:

# .capitalize(): Converts the first character of the string to uppercase and the rest to lowercase.
my_str = "happy new year"
cap_my_str = my_str.capitalize()
print(cap_my_str)

# .upper(): Converts all characters in the string to uppercase.
upp_my_str = my_str.upper()
print(upp_my_str)

# .lower(): Converts all characters in the string to lowercase.
low_my_srt = my_str.lower()
print(low_my_srt)

# .strip(): Removes leading and trailing whitespace characters from the string.
text = "  Happy New Year    "
nospace_text = text.strip()
print(nospace_text)

# .replace(old, new): Replaces all occurrences of the specified old substring with the new substring.
new_my_str = my_str.replace('happy', 'happy happy')
print(new_my_str)

# .split(separator): Splits the string into a list of substrings
# based on the specified separator (default is whitespace).
text = "apple,banana,cherry"
split_text = text.split(',')
print(split_text)

# .find(substring): Returns the lowest index where the specified
# substring is found in the string, or -1 if it's not found.
text = "Hello, World!"
result = text.find("World")
print(result)