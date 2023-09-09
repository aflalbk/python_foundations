"""
Given an integer,n
 , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
"""


n = int(input('Enter a positive integer number'))
if n % 2 == 1 or 6 <= n <= 20:
    print('Weird')
else:
    print('Not Weird')


'''
Question:
You are writing a program that determines if a given year is a leap year or not. A leap year is either:

1. Divisible by 4 but not divisible by 100, or
2. Divisible by 400.
Write a Python program that takes a year as input from the user and prints whether it's a leap year or not.
'''


year = int(input('Please enter a year (AD) to determine whether it is a leap year or not.\n'))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")


'''
Question:
You are writing a program that determines the season based on the month entered by the user. 
The program should take an integer representing the month (1 for January, 2 for February, and so on) as input and 
print the corresponding season.

Spring: March to May (months 3, 4, and 5)
Summer: June to August (months 6, 7, and 8)
Autumn: September to November (months 9, 10, and 11)
Winter: December to February (months 12, 1, and 2)
Write a Python program that takes the month as input from the user and prints the season.
'''

month = int(input('Please input a month (in 1-12) to determine its corresponding season.\n'))
month_name = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
if not(1 <= month <= 12):
    print("Please enter a correct value")
elif 3 <= month <= 5:
    print(f'{month_name[month]} corresponds to the spring season.')
elif 6 <= month <= 8:
    print(f'{month_name[month]} corresponds to the summer season.')
elif 9 <= month <= 11:
    print(f'{month_name[month]} corresponds to the autumn season.')
else:
    print(f'{month_name[month]} corresponds to the winter season.')
