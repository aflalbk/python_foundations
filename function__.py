# This function simply prints 'hello' when called.
def call_hello():
    print('hello')


# Calling the function to display 'hello' in the console.
call_hello()


# This function takes a 'name' parameter and prints a formatted string.
def my_name(name):
    print(f'my name is {name}')


# Calling the function with the argument "Python" to print "my name is Python".
my_name("Python")

# Assigning the string "Akhil" to the variable 'data' and calling the 'my_name' function with 'data' as an argument.
data = "Akhil"
my_name(data)


# This function takes two parameters, 'name' and 'age', and prints them in a formatted string.
def my_name_age(name, age):
    print(f'my name is {name} and age is {age}')


# Creating a list 'data' with name and age, then calling 'my_name_age' with elements from the list.
data = ['Aflal', 23]
my_name_age(data[0], data[1])


# This function takes two numbers, adds them, and returns the result.
def find_sum(num1, num2):
    sum_num = num1 + num2
    return sum_num


# Calling 'find_sum' with 12 and 23 as arguments and storing the result in 'total'.
total = find_sum(12, 23)
# Printing the result, which should be 35.
print(total)


# This function takes any number of arguments and calculates their sum.
def many_number_sum(*numbers):
    num_sum = 0
    for num in numbers:
        num_sum += num
    return num_sum


# Calling 'many_number_sum' with multiple numbers and storing the result in 'value_sum'.
value_sum = many_number_sum(23, 45, 56, 34, 56, 34, 56, 56)
# Printing the sum of all the numbers provided, in this case, it should be 360.
print(value_sum)

# Assigning the value 10 to the global variable 'num1'.
num1 = 10


# This function defines a local variable 'num1' with a value of 5 and prints it.
def check():
    num1 = 5
    print("this is a local num1 " + str(num1))


# Calling the 'check' function, which prints the local 'num1'.
check()

# Printing the global 'num1' variable, which is 10.
print("this is a global num1 " + str(num1))

# Calling a function 'my_name_age' with keyword arguments 'age' and 'name'.
my_name_age(age=23, name='no name')


# This function 'my_name_age_20' takes 'name' as a required argument and 'age' as an optional defaulting to 20.
def my_name_age_20(name, age=20):
    print(f'my name is {name} and age is {age}')


# Calling 'my_name_age_20' with 'name' as 'batman', age will default to 20.
my_name_age_20('batman')

# Calling 'my_name_age_20' with 'name' as 'old batman' and explicitly setting 'age' to 34.
my_name_age_20('old batman', 34)

# The following function definition is incorrect due to the default argument position.
# Python requires non-default arguments to be defined before default arguments.
# def my_name_batman_age(name = 'batman', age):
#     print(f'my name is {name} and age is {age}')
# Uncommenting this will result in a SyntaxError.

# Attempting to call 'my_name_batman_age' with only 'age' specified will also result in an error.
# my_name_batman_age(23)

'''
Problem: Calculate the Average

Write a Python function called calculate_average that takes a list of numbers as input and returns the average (mean)
of those numbers. Your function should do the following:

Accept a list of numbers as its parameter.
Calculate the sum of all the numbers in the list.
Divide the sum by the total number of elements in the list to find the average.
Return the average as a floating-point number (rounded to two decimal places).
'''


def calculate_average(numbers):
    average = sum(numbers) / len(numbers)
    average = round(average, 2)
    return average


numbers = []
print("Enter values to find average and press enter again to finish")
while True:
    num = input()
    if not num:
        break
    num = int(num)
    numbers.append(num)

average_value = calculate_average(numbers)
print(f'average value of numbers is :{average_value}')
