# The traditional FizzBuzz program, but using a for loop.

for i in range(1, 101):
    # if i is divisible by both 3 and 5, print "fizzbuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # if i is divisible by 3, print "fizz"
    elif i % 3 == 0:
        print("Fizz")
    # if i is divisible by 5, print "buzz"
    elif i % 5 == 0:
        print("Buzz")
    # otherwise, just print i
    else:
        print(i)