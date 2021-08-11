# Positional and Keyowrd arguments

# Positional arguments
def greet(name,msg):
    print(msg+" "+name)

greet("Sharun","Good morning") # the position is important. The will be assiged on order
# Output -> Good morning Sharun
greet("Good morning", "Sharun") # here the position of the argument changes the ouptut changes.
# Output -> Sharun Good morning // which is not the desired output

# Keyword arguments
greet(name="Sharun",msg="Good morning") # here the position is not important. The will be assiged based on the name of the parameter
# Output -> Good morning Sharun
greet(msg="Good morning",name="Sharun") # here the position of the argument changes the ouptut doesnot change.
# Output -> Sharun Good morning // which is  the desired output