# python

print()
## Data Type
strings

print("print any string")----string

numbers

print(2) --->number

print(2.5)  ---> float

boolen

print()

### string concatenation(mixing strings)

print(f"20 days are  {20 * 24 * 60}  minutes")

here f stand for format

## variable

calculate_to_second = 24 * 60 * 60

calculate_to_second is a variable name and numbers are values

print(f"20 days are  {20 * calculate_to_second }  seconds")
```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"
print(f"20 days are  {20 * calculate_to_second }  {name_of_units}")
```
## Functions
functions are mainly used to avoid repeating the same logic \
a function is defind using def key word \
Block of code (code inside def function) only run when its called \
information can passed into a function as parameters \
parameters are also called arguments \
```
calculate_to_second = 24 * 60 * 60  ------> define variables
name_of_units = "seconds"

def days_to_units():  ----------> # defind the funtion
    print(f"20 days are  {20 * calculate_to_second }  {name_of_units}")
    print("hello")

days_to_units() -----> #calling the function
```



