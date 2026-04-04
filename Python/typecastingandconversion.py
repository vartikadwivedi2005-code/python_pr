#type conversion - the process of converting one data type to another is called type conversion. It can be done using built-in functions like int(), float(), str(), etc. Type conversion can be implicit or explicit. Implicit type conversion is done automatically by Python when it encounters an operation between different data types, while explicit type conversion is done manually by the programmer using the built-in functions.

a = 5
b = 2.5
print(type(a))
print(type(b))

#type casting - the process of converting one data type to another is called type casting. It is done using built-in functions like int(), float(), str(), etc. Type casting can be implicit or explicit. Implicit type casting is done automatically by Python when it encounters an operation between different data types, while explicit type casting is done manually by the programmer using the built-in functions.

a = 5
b = 2.5
print(float(a)) #converting int to float
print(int(b))   #converting float to int
print(str(a))   #converting int to string
print(str(b))   #converting float to string

a =3.14
a = str(a)  #converting float to string

print(type(a))

