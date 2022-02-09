# ANSWERS

### Q2: What is the difference between a parameter and an argument?
The parameters of a function are the variables a function expects while the arguments are the values that are actually passsed to it. Parameters of a function are defined while defining the function while the arguments are send while a function is actually called.

```
def my_function(parameter_1, parameter_2):
    pass

my_function(argument_1, argument_2)
```

### Q3: All functions in Python by default return …?
All functions return None unless we explicitly return something. 

### Q4: What are keyword arguments and when should we use them?
Keyword arguments are useful as they avoid us from the pain of remembering the order of arguments that need to be sent to a function. We can send a keyword argument and then access it by the same name in the function.
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

### Q5: How can we make a parameter of a function optional?
By giving a default value to the parameter, we can make a parameter optional.
```
def my_func(parameter=99):
    print(parameter)

my_func()
Prints 99 even when no argument is provided. 
```

### Q6: What happens when we prefix a parameter with an asterisk?
At times, we might need to send an arbitrary number of positional arguments to a function according to the need. For that, an asterisk helps us. When we put it with the parameter in a function, it then expects random number of arguments.
```
def my_func(*args):
    for arg in args:
        print(arg)
my_func(1, 2, 3, 4, 5)
my_function() may accept as many arguments as one wants to send. 
```

### Q7: What about two asterisks?
Similarly, if someone wants to send different number of keyword arguments to a function in different situations, two asterisks in the parameters may help.
Now with two asterisks, the number of arguments and their order, both don't matter for a function. 
```
def my_func(**kwargs):
    print(kwargs["a"])

my_func(b=2, a=1, c=3)
my_function() may accept as many keyword arguments as one wants to send. 
```
