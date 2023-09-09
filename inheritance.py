# Create a subclass
print(1)  # \n

class BaseClass:
    def display(self):
        print("hello")


class SubOfBaseClass(BaseClass):
    def display1(self):
        print('Welcome')


# calling base class
print("calling base class")
a = BaseClass()
a.display()

# calling subclass
print("\ncalling sub class of base class")
b = SubOfBaseClass()
b.display1()
# we can also call baseclass method
b.display()

# _____________________________________________________________
# Accessing Base Class method from subclass
print(2)  # \n

class BaseClass:
    def set_name(self, name):
        self.name = name


class SubOfBaseClass(BaseClass):
    def display1(self):
        print('Welcome')

    def display_name(self):
        print("name : " + self.name)


# this is not going to work because both are entirely different classes
"""
rob = BaseClass()
rob.set_name("Robert")

sub_rob = SubOfBaseClass()
sub_rob.display_name()
"""

# but we can use like this
sub_rob = SubOfBaseClass()

# Actually the set_name method is in the base class,
# but we can call it in the subclass as well.
sub_rob.set_name("Robert")
sub_rob.display_name()

# _____________________________________________________________
# constructor over-ride
print(3)  # \n

class BaseClass:
    def __init__(self):
        print("base class constructor")

class SubClass(BaseClass):
    def __init__(self):
        print("Subclass constructor")
# if the subclass has no constructor, the base class constructor will work
# if the subclass has subclass constructor, it will override the base class constructor.
hi = SubClass()

# _____________________________________________________________
# function over-ride
print(4)  # \n

class BaseClass:
    def name_display(self):
        print("MR. King")

class SubClass(BaseClass):
    def name_display(self):
        print("MR. King Killer")

k = SubClass()
k.name_display()

# _____________________________________________________________
# Accessing Base Class constructor
print(5)  # \n

class BaseClass:
    def __init__(self):
        print("base class constructor")

class SubClass(BaseClass):
    def __init__(self):
        super().__init__()  # now first work base class init and continue to rest of the code in this constructor
        print("Subclass constructor")


hi = SubClass()

# _____________________________________________________________
# Accessing base class function
print(6)  # \n

class BaseClass:
    def name_display(self):
        print("MR. King")

class SubClass(BaseClass):
    def name_display(self):
        super().name_display()
        print("MR. King Killer")

k = SubClass()
k.name_display()