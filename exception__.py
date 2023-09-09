b = 0

try:
    a = 10/b
    print(a)
    print("try completed")
except ZeroDivisionError:
    print("cant be divided by zero")

print("program completed.")
