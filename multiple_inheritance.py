# multi level inheritance

class First:
    def display_1(self):
        print("this is first class")


class Second(First):
    def display_2(self):
        print("this is second class")


class Third(Second):
    def display_3(self):
        print("this is third class")


c = Third()
c.display_1()
c.display_2()
c.display_3()

print()
# -------------------------------------------------------
# multiple inheritance

class First:
    def display_1(self):
        print("this is first class")


class Second():
    def display_2(self):
        print("this is second class")


class BothInThis(First, Second):
    def display_3(self):
        print("both in this class")


fs = BothInThis()
fs.display_1()
fs.display_2()
fs.display_3()

# -----------------------------------------------
print()


class FirstOne:
    def display(self):
        print("this is first class")


class SecondOne:
    def display(self):
        print("this is second class")


class BothInThisOne(FirstOne, SecondOne):
    def display_3(self):
        print("both in this class")


fso = BothInThisOne()
fso.display_3()
fso.display()

print(BothInThisOne.mro())

print()
# -------------------------------------------
# Diamond Problem
class Aaa:
    def display(self):
        print("this is Aaa class")


class Bbb(Aaa):
    def display1(self):
        print("this is Bbb class")


class Ccc(Aaa):
    def display(self):
        print("this is Ccc class")


class Ddd(Bbb, Ccc):
    def display_3(self):
        print("Ddd class")


diamond = Ddd()
diamond.display()
# result is : "this is Ccc class"
# because mro
print(Ddd.mro())

print()
# -----------------------------------------------------
# Method overloading

class MainClass:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        name = self.name + " " + other.name
        return name


first_name = MainClass("Harry")
last_name = MainClass("Potter")

# using method overloading
full_name = first_name + last_name
print(full_name)
