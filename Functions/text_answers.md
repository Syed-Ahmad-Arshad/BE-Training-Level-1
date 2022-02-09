# ANSWERS

#### Q2: What is the difference between a parameter and an argument?
The parameters of a function are the variables a function expects while the arguments are the values that are actually passsed to it. Parameters of a function are defined while defining the function while the arguments are send while a function is actually called.

```
def my_function(parameter_1, parameter_2):
    pass

my_function(argument_1, argument_2)
```

#### Q3: All functions in Python by default return …?
All functions return None unless we explicitly return something. 

#### Q3: What are keyword arguments and when should we use them?
Keyworded arguments are useful as they avoid us from the pain of remembering the order of arguments that need to be sent to a function. We can send a keyword argument and then access it by the same name in the function.
What is important here is, we don't need to remember the order anymore.
```
def my_function(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

my_function(b=2, c=3, d=4, a=1)
Prints 1, 2, 3, 4 irrespective of the order of arguments.
```
