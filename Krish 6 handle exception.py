### 15th Sept

##### one exception

x = 1 / 0

# Traceback (most recent call last):
#   File "/Users/indrani.sarkar/Python_Functional/Lists/krish 5 remove duplicates from a list.py", line 24, in <module>
#     x = 1 / 0
# ZeroDivisionError: division by zero


try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")



a = 'okay'
b = 'ok'

print(a*b)

# Traceback (most recent call last):
#   File "/Users/indrani.sarkar/Python_Functional/Basics/Krish 6 handle exception.py", line 21, in <module>
#     print(a*b)
# TypeError: can't multiply sequence by non-int of type 'str'


try:
    a = 'okay'
    b = 'ok'
    print(a*b)

except TypeError:
    print("Wrong type")

# Wrong type


##### multiple exceptions
    
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("A value error occurred!")
except (TypeError, KeyError):
    print("Either a TypeError or a KeyError occurred!")
