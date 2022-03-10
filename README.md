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

```
calculate_to_second = 24 * 60 * 60  ------> define variables
name_of_units = "seconds"

def days_to_units():  ----------> # defind the funtion
    print(f"20 days are  {20 * calculate_to_second }  {name_of_units}")
    print("hello")

days_to_units() -----> #calling the function
```
information can passed into a function as parameters \
parameters are also called arguments \
```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(no_of_days, custom_message):
    print(f"{no_of_days} days are  {20 * calculate_to_second }  {name_of_units}")
    print(custom_message)


days_to_units(20, "good")
days_to_units(30, "wow!")
```

## scope
A variable is avilable only inside the region it is created \
Global scope = variable avilable with in any scope \
Local scope = variable created inside the function \

ex: \
no_of_units -----> global scope \
no_of_days -----> local scope 

## user input

To ask user for input \
python stops excuting when it comes to the input() \

input() is a built-in function provided by python itself \
```
user_input = input("enter value here:\n")
print(user_input)
```

