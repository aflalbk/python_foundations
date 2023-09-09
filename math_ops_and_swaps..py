a = 10
b = 20
# concatenate or include non-string values within a print() function,
# you need to convert those values to strings using the str() function.
print('the values are ' + str(a) + ' and ' + str(b))

value1 = input("Enter a number")
print("user entered value is " + value1)

value1 = input('Enter 2 numbers')
value2 = input()
# the input() function always returns the user's input as a string
print('You entered values are ' + value1 + ',' + value2)

# Find the sum of 2 values
value1 = input('Enter 2 numbers for find sum')
value2 = input()
print('You entered values are ' + value1 + ',' + value2)
print('sum of the value')
# # print(value1, '+', value2, '=', (value1 + value2))  # Result like this [45 + 34 = 4534], because input as string.
print(value1, '+', value2, '=', (int(value1) + int(value2)))

# Ask 3 numbers to user to find average of numbers
num1 = int(input("Enter 3 number to find average"))
num2 = int(input())
num3 = int(input())
average = (num1 + num2 + num3 )/3
print('Average of ' + str(num1) + ',' + str(num2) + ',' + str(num3) + ' is: ' + str(average))

# Swapping values in 2 variable
a = 10
b = 20
print('Value in A: ' + str(a) + ', Value in B: ' + str(b))
# swapping.
temp = b
b = a
a = temp
print("After Swapping")
print('Value in A: ' + str(a) + ', Value in B: ' + str(b))