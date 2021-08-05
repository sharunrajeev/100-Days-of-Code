# Type checking

message = "Hello World"
print(type(message))
# outputs -> <class 'str'>

integer = 123
print(type(integer))
# outputs -> <class 'int'>

# ----------------------------------------

# Type conversion
number = "123" 
print(type(number)) # string

number = int(number) # converts to integer
print(type(number)) # integer

number = float(number) # converts to float
print(type(number)) # float

# ----------------------------------------

# Type Error
number = 123
print(number + " is a number")  
# This returns type error
# because the number is not a string

# To solve the error 
print(int(number) + " is a number")