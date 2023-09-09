"""
using while loop print like this in 10 rows
                  *
                 * *
                * * *
               * * * *
              * * * * *
              like this
"""

n = 10
i = 1
while i <= n:
    # print space
    j = 1
    while j <= (n - i):
        print(' ', end='')
        j += 1

    # print asterisks
    k = 0
    while k < i:
        print('* ', end='')
        k += 1

    # move to the next line
    print("")
    i += 1


"""
Question:
You are tasked with creating a program that calculates the factorial
of a given positive integer.
The factorial of a number is the product of all positive
integers from 1 to that number.

Write a Python program that takes a positive integer as input
and calculates its factorial using a for loop.
Then, print the result.
"""

text = ''
factorial = 1
value = int(input("Enter a value to find factorial"))

# Write a for loop to calculate the factorial
if value < 0:
    print('Factorial is not defined for negative numbers')
elif value == 1 or value == 0:
    print(f"The factorial of {value} is 1")
else:
    expression_parts = []
    for num in range(1, (value+1)):
        expression_parts.append(str(num))
        factorial = factorial * num
    # Output: Print the factorial
    expression = ' x '.join(expression_parts)
    print(expression + '= ' + str(factorial))
