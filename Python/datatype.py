# DATA TYPES - data types are the classification of data items. It represents the kind of value that tells what operations can be performed on a particular data.
# Python has several built-in data types, including:
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range
# 3. Text Type: str
# 4. Mapping Type: dict
# 5. Set Types: set, frozenset
# 6. Boolean Type: bool
# 7. None Type: NoneType

# name1 = "sky"
# name2 = 'blue'
# name3 = """hello world"""

# print(name1)
# print(name2)
# print(name3)

# age = 20
# old = False
# a = None
# print(type(old))
# print(type(a))

#arithmetic operators
# a = 5
# b = 2
# sum = a+b
# print(sum)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)   # remainder
# print(a**b)  # exponentiation
# print(a//b)  # floor division 


# #relational operators
# a =50
# b =20
# print(a == b) #equal to
# print(a != b) #not equal to
# print(a>b)  #greater than
# print(a<b)  #less than
# print(a>=b) #greater than or equal to
# print(a<=b) #less than or equal to

#assignment operators
# num =10
# num +=5
# print(num)
# num -=4
# print("num:", num)
# num *= 5
# print("num:", num)
# num /= 5
# print("num:", num)
# num %= 3
# print("num:", num)
# num **= 2
# print("num:", num)


#logical operators
print(not True)
print(not False)
a = 40
b = 20
print(not (a>b)) #False

val1 = True
val2 = True
print("AND operator:",val1 and val2) 

val1 = True
val2 = False
print("AND operator:",val1 and val2) 

val1 = True
val2 = False
print("OR operator:",val1 or val2)


val1 = False
val2 = False
print("OR operator:",val1 or val2) 

print("OR operator:" , (a == b) or (a > b)) #True
