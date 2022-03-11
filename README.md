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

## Function with return values
A function can return data as a result \
```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"
user_input = input("enter value here:\n")
print(user_input)


def days_to_units(no_of_days):
    return f"{no_of_days} days are  {no_of_days * calculate_to_second }  {name_of_units}"  ------> # Function is excuted


my_var = days_to_units(user_input) -----> # return value is assigned to variable
print(my_var) -----> # variable value is print to standerd output
```
![image](https://user-images.githubusercontent.com/99127429/157707050-01990d48-8676-41cc-a31e-adfb22ea5ac0.png)

it does give exact value so use casting for that 

<img width="914" alt="image" src="https://user-images.githubusercontent.com/99127429/157707865-2366b280-bccc-486b-af19-ce70387779fd.png">

## Conditions(if else) & boolean data type

```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"
user_input = input("enter value here:\n")
user_input_number = int(user_input)
print(user_input)


def days_to_units(no_of_days):
    print(no_of_days > 0)  ---------> # it display weather condition is true or false (operates boolean datatype)
    if no_of_days > 0:
        return f"{no_of_days} days are  {no_of_days * calculate_to_second }  {name_of_units}"
    elif no_of_days == 0:
        return "you have entered zero value"    
    else:
        return "return also give same result"


my_var = days_to_units(user_input_number)
print(my_var)
```
<img width="628" alt="image" src="https://user-images.githubusercontent.com/99127429/157712820-4e5c8330-0230-41f0-ab44-7eea3ac1bcd1.png">

it display type of class (ex: int, string, boolean)

<img width="426" alt="image" src="https://user-images.githubusercontent.com/99127429/157713829-a3b03f7d-acfe-45bc-8c18-886b27814814.png">

## More user_input validation
```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(no_of_days):
    condition_check = no_of_days > 0
    print(type(condition_check))
    if no_of_days > 0:
        return f"{no_of_days} days are  {no_of_days * calculate_to_second }  {name_of_units}"
    elif no_of_days == 0:
        return "you have entered zero value"
    else:
        return "return also give same result"


user_input = input("enter value here:\n")


if user_input.isdigit():
    user_input_number = int(user_input)
    print(user_input)
    my_var = days_to_units(user_input_number)
    print(my_var)
else:
    print("its not ant integer number")

```
## clean up our code
```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(no_of_days):
    condition_check = no_of_days > 0
    print(type(condition_check))
    if no_of_days > 0:
        return f"{no_of_days} days are  {no_of_days * calculate_to_second }  {name_of_units}"
    elif no_of_days == 0:
        return "you have entered zero value"
    else:
        return "return also give same result"


user_input = input("enter value here:\n")


def validate_excute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        print(user_input)
        my_var = days_to_units(user_input_number)
        print(my_var)
    else:
        print("its not ant integer number")


validate_excute()
```
## Nested if...else
```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(no_of_days):
    return f"{no_of_days} days are  {no_of_days * calculate_to_second }  {name_of_units}"


user_input = input("enter value here:\n")


def validate_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            my_var = days_to_units(user_input_number)
            print(my_var)
        elif user_input_number == 0:
            print("you have entered zero value")
    else:
        print("its not ant integer number")


validate_execute()
```

## Error handling with try and expect/catch
converting if else statements into try cache 


## while loops
To execute logic multiple times \

while loop execute set of statement as long as condition is true







































