## Variable names in flask
Variable names can be handy when we need to use the route data dynamically.
To use it set the route inside <> this will make the route a variable

Example

```python
@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"
```

## Debug mode
* Debug mode is a handy tool that could help developer to debug the code with ease.
To turn on the debug mode, use the following code,

```python
if __name__ == "__main__":
    app.run(debug=True)
```

* Another helpful thing in debug mode is the debug view \
This view will help us to get more of the error and its details to resolve them.

## Converter of variables
This is to change or declare the type of data that is in the route.
```python
@app.route("/<string:name>")
def greet(name):
    return f"Hello {name}!"
```
This above code mentions name as a string.
We can have different types like string, int, path etc.


## Python Decorators
* This is a very important and useful topic of Python
* Due to its versatility it can be a powerful weapon once we master it.
* Let me explain it in simple words.
* First consider a function which returns another function, this is technically called nested function
```python
def function1(function3):
    def function2():
        return f"{function3} World"
    return function2
```
* Here we have three function one being the main function (function1), second being the parameter of function 1 (function3) and lastly the wrapper function (function 2)
* This function can help to execute a special function called wrapper here with the function being passed to it.
* For example, let the passed function returns "Hello" which is passed to function3, function3 has a wrapper function which adds " World" at the end of the data passed to it.
* So when the function2 is returned by function1, we get "Hello World"

We can use @ symbol to call decorator function, here @function1 calls the decorator function
Example,
```python
@function1
def hello():
    return "Hello"
```
So here calling hello will trigger function1 passing hello() function to it.
Then the wrapper function is returned by adding " World" at the end of the function being passed that is hello()

## Advance Decorator topic
We can pass data to the decorators using args and kwargs
```python
def decorator(function):
    def wrapper(*args, **kwargs):
        # your logic with args passed
        return function
    return wrapper
```
This is called as
```python
@decorators
def new_function(argument):
    return argument
```
The argument is passed as args to the wrapper function