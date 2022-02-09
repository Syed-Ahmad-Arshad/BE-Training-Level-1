# ANSWERS

### Q1: What is the difference between 10 / 3 and 10 // 3?
10 / 3 gives us the answer as floating point correct upto decimals i.e, 3.33333333... However, 10//3 just gives us the integer value leaving the values after the decimal.

### Q2: What is the result of 10 ** 3?
1000. Two asterisks work as power.

### Q3: Given (x = 1), what will be the value of after we run (x += 2)?
x += 2 is similar to x = x + 2, so x will be 3.

### Q4: How can we round a number?
The round() function of python can be used for rounding a number. 

### Q5: What is the result of float(1)?
The float function converts the argument into floating point number. So 1.0 is the result.

### Q6: What is the result of bool(“False”)?
It will return True. Bool() always returns True unless the argument is empty. Bool() will return False in following cases: 
```
bool()
bool([])
bool("")
bool({})
```

### Q7: What are the falsy values in Python?
They are as follows:
```
- Zero
- None
- []
- ""
- {}
- False
```

### Q8: What is the result of 10 == “10”?
False. As the right side has a str 10. 

### Q9: What is the result of “bag” > “apple”?
True. As, when the strings are comared like this, their ASCII is being compared. So ASCII of first letter of "bag" is greater than ASCII of first letter of "apple".

### Q10: What is the result of not(True or False)?
(True or False) will return True and then the not will make it False. So, False.

### Q11: Under what circumstances does the expression 18 <= age < 65 evaluate to True?
When age is between 18 and 64. Both 18 and 64 included. 

### Q12: What does range(1, 10, 2) return?
1, 3, 5, 7, 9

### Q13: Name 3 iterable objects in Python.
An iterable is something that we can loop over. So lists, dictionaries, tuples, strings, etc.