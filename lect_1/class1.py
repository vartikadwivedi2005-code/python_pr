#python
#interpreter and compiler
#python is an interpreted language, which means that it is executed line by line. The interpreter reads the code and executes it directly, without the need for a separate compilation step. This allows for faster development and easier debugging, as you can see the results of your code immediately.

#Python is dynamically typed language. This means that you do not need to declare the type of a variable when you create it. The interpreter will determine the type of the variable based on the value assigned to it. For example, if you assign a string value to a variable, it will be treated as a string, and if you assign a number, it will be treated as a number. This flexibility allows for more dynamic and flexible programming, but it also means that you need to be careful

#Keywords 
#Keywords are reserved words in Python that have a specific meaning and cannot be used as variable names or identifiers. Some examples of keywords in Python include:
# if, else, elif, for, while, break, continue, def, return, class, import, from, as, pass, and, or, not, is, in, lambda, with, yield, try, except, finally, raise, global, nonlocal.

#Identifiers
#Identifiers are names used to identify variables, functions, classes, and other objects in Python. They must follow certain rules:
#1. An identifier must start with a letter (a-z, A-Z) or an underscore (_).
#2. The rest of the identifier can contain letters, digits (0-9), and underscores.
#3. Identifiers are case-sensitive, meaning that "myVariable" and "myvariable" are considered different identifiers.
#4. Identifiers cannot be the same as keywords.
#Examples of valid identifiers:
# my_variable
# _private_variable
# MyClass


#variables
#Variables are used to store data in Python. They can hold different types of data, such as numbers, strings, lists, and more. To create a variable, you simply assign a value to it using the equals sign (=). For example:
x = 10
name = "Alice"
#In this example, we have created a variable named "x" and assigned it the value of 10, and a variable named "name" with the value "Alice". You can use these variables later in your code to perform operations or display their values.
#properties of variables
#1. Variables can be reassigned to different values.
#2. Variables can hold different types of data.
#3. Variables can be used in expressions and calculations.
#4. Variables can be printed or displayed to the user.
#5. Two or more variables can refer to the same value in memory (aliasing).

print(x)
print(name)

#heap and stack
#In Python, memory management is handled through a combination of the heap and stack. The stack is used for storing local variables and function call information, while the heap is used for dynamic memory allocation, such as when creating objects or data structures. When a variable is created, it is stored in the stack, and if it references an object or data structure, that object is stored in the heap. The Python interpreter manages memory automatically, so you don't need to worry about manual memory management in most cases.
