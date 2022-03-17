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

```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(no_of_days):
    return f"{no_of_days} days are  {no_of_days * calculate_to_second }  {name_of_units}"


user_input = input("enter value here:\n")


def validate_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            my_var = days_to_units(user_input_number)
            print(my_var)
        elif user_input_number == 0:
            print("you have entered zero value")
    except ValueError:
        print("its not ant integer number")


validate_execute()
```


## while loops
To execute logic multiple times \

while loop execute set of statement as long as condition is true

## Let user execute the program
<img width="541" alt="image" src="https://user-images.githubusercontent.com/99127429/157870075-82867cd9-baf3-421d-ba61-bf6dc69ba53a.png">

we can mention like below also
![image](https://user-images.githubusercontent.com/99127429/157870851-b3c76d18-0cbe-48cb-a114-e936b6d8f5c6.png)

## list and for loops
List is used to store multiple datatypes in a single variable \
A list can contain several data types

<img width="525" alt="image" src="https://user-images.githubusercontent.com/99127429/158111120-1b4b9dbb-1d76-4fa3-8cd4-1b8b3316cc40.png">

```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(no_of_days):
    return f"{no_of_days} days are  {no_of_days * calculate_to_second }  {name_of_units}"


def validate_execute():
    try:
        user_input_number = int(no_of_days_element)
        if user_input_number > 0:
            my_var = days_to_units(user_input_number)
            print(my_var)
        elif user_input_number == 0:
            print("you have entered zero value")
    except ValueError:
        print("its not ant integer number")


user_input = ""
while user_input != "exit":
    user_input = input("enter value here: \n")
    for no_of_days_element in user_input.split(", "):
        validate_execute()
        
```

## syntax of list ------->(list is one of data type)

```
my_list = ["jan", "feb", "march"]
print(my_list[2])
my_list.append("April")
print(my_list)
print(my_list[3])

```

## Set ----> another data type
 set is nothing but a list data type but not allowed duplicate values

<img width="428" alt="image" src="https://user-images.githubusercontent.com/99127429/158377918-dfe49e8a-6b7c-4cb6-8738-d62e65ba10f9.png">

```
calculate_to_second = 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(no_of_days):
    return f"{no_of_days} days are  {no_of_days * calculate_to_second}  {name_of_units}"


def validate_execute():
    try:
        user_input_number = int(no_of_days_element)
        if user_input_number > 0:
            my_var = days_to_units(user_input_number)
            print(my_var)
        elif user_input_number == 0:
            print("you have entered zero value")
    except ValueError:
        print("its not ant integer number")


user_input = ""
while user_input != "exit":
    user_input = input("enter value here: \n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))
    for no_of_days_element in set(list_of_days):
        validate_execute()
        
 ```       

## Basic set operations and syntax
set is unorderd and unchangeble \

1) items in the set don't have specific order
2) items can't refered by an index
3) items can't be changed only added/removed

<img width="367" alt="image" src="https://user-images.githubusercontent.com/99127429/158382206-08a6c452-cdb7-428b-8741-120fe12fdd01.png">

## Built in fnctions

each datatype has its own built in function whcih are useful or make sense only for this datatype \

standalone built in function \
print() ---> print to standered output device \
input() ---> ask user for input \
set() ----> return a new set ---> convert list into set \
int() ----> convert value into integer number \

"2","3".split() ----> is also a built in function \

## Dictionary datatype

- are used to store values in key:value pair, \
- is a collection which doesn't allow dupicate values \

![image](https://user-images.githubusercontent.com/99127429/158404010-a7dfc888-a8e4-48b3-9c8e-850a4d79b386.png)

```
user_input = input("enter values here:\n")
days_and_units = user_input.split(":")
print(days_and_units)
days_to_units_dictionary = {"days": days_and_units[0], "hours": days_and_units[1]}
print(days_to_units_dictionary["days"]) # --------> if we enter key it will dispaly value in the output
print(days_to_units_dictionary["hours"])
print(days_to_units_dictionary)

```

## Modules

- logically organised your python code and \
- Module should contain related code \
- A module is just a .py file \
- using module we can refer one .py file in another .py file \

## Create a module and import statement
- create another file called helper.py in that we mention all functions \
- import functions in helper.py in main function
ex:
- import helper
- from helper import *
- import helper as h ----> rename module with h here

## sample excercise for count_down days

```
import datetime

user_input = input("enter goal with date:\n")
days_and_goal = user_input.split(':')
goal = days_and_goal[0]
date = days_and_goal[1]

goal_date = datetime.datetime.strptime(date, '%d-%m-%Y')
today_date = datetime.datetime.today()


print(user_input.split(':'))
print(goal)
countdown_days = today_date - goal_date
print(f"you have only  {countdown_days} to complete you goal")
```
    


    
    
    
    
    

    












