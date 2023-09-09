# Create a file and write something in it.
f = open("created_using_python.py", "w")
f.write("print('This is a Python file; I created it using Python code')")
f.close()

# read that file
with open("created_using_python.py","r") as cup:
    file = cup.read()

print(file)

