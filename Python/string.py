# String is data that stores a sequence of characters.
# basic operations on strings include concatenation, slicing, and formatting.
# "hello" + "world"  -> "helloworld" # Concatenation
# "hello world"[0:5] -> "hello" # Slicing
# length of a string can be found using the len() function
# len("hello") -> 5

from ast import operator


str1 = "This is a string"
str2 = 'Another string'
str3 = """This is a multi-line string"""
print(str1)
print(str2)
print(str3)

# Escape sequence characters are used to represent special characters in a string. For example, \n represents a new line, \t represents a tab, and \\ represents a backslash.
str4 ="This is a string .\nit can span multiple lines."
print(str4)
str5 = "This is a string with a tab character.\tIt is used to create space."
print(str5)


# Concatenation: Joining two strings together using the + operator (e.g., "Hello" + "World" becomes "HelloWorld").
str6 = "Hello"
str7 = "World"
finalstr  = str6 + str7
print(finalstr)

# Length: The len() function counts the total number of characters in a string, including spaces and punctuation.
str8 = "Hello, World!"
length = len(str8)
print(length)

string = "Python"
string1 ="Diaries"
final_string = string + " " + string1
print(final_string)
print(len(final_string))


# Indexing: Every character in a string has a specific position number called an index, starting from 0.
# Example: In "Python", index 0 is 'P', index 1 is 'y', and so on.
# Note: You can access characters via index but cannot modify them directly (Strings are immutable).
# Example: str[0] gives the first character of the string, str[1] gives the second character, and so on. Negative indexing allows you to access characters from the end of the string (e.g., str[-1] gives the last character).
# Spaces and punctuation are also counted as characters in a string. For example, in the string "Hello, World!", the space and the comma are included in the character count.
# String object does not support item assignment, which means you cannot change a character in a string directly by assigning a new value to an index. For example, if you have a string str = "Hello", you cannot do str[0] = 'h' to change the first character to lowercase. Instead, you would need to create a new string with the desired changes.
str9 = "Python"
print(str9[0])  # Output: 'P'
print(str9[1])  # Output: 'y'
print(str9[2])  # Output: 't'
print(str9[3])  # Output: 'h'
print(str9[4])  # Output: 'o'
print(str9[5])  # Output: 'n'


# Slicing: Extracting a portion of a string using the syntax str[start:end], where start is the index of the first character to include and end is the index of the first character to exclude.
# Example: str[0:5] gives the substring from index 0 to index 4 (inclusive), which is "Hello" in the string "Hello, World!".
str10 = "Hello, World!"
print(str10[1:4])  # Output: 'ell'
print(str10[0:5])  # Output: 'Hello'
print(str10[7:])   # Output: 'World!'
print(str10[:5])   # Output: 'Hello'
print(str10[5:len(str10)])  # Output: ', World!'
# Missing start index defaults to 0, and missing end index defaults to the length of the string. For example, str[:5] is equivalent to str[0:5], and str[5:] is equivalent to str[5:len(str)].
# Negative indices can also be used in slicing to count from the end of the string. For example, str[-5:] gives the last 5 characters of the string, and str[:-5] gives all characters except the last 5.
str11 = "Hello, World!"
print(str11[-5:])  # Output: 'World!'
print(str11[:-5])  # Output: 'Hello, '










