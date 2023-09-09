
class SampleClass:
    def assign_name(self, name):
        self.name = name

    def print_name(self):
        print(f"My name is : {self.name}")


akil = SampleClass()
akil.assign_name("Mr.Akil")
anil = SampleClass()
anil.assign_name("Mr.Anil kumar")

akil.print_name()
anil.print_name()

# ______________________________________________________________________________


class StudentsData:
    year = 2023

    def __init__(self, name, age, place):
        self.place = place
        self.name = name
        self.age = age

    def add_age(self, value=1):
        self.age += value

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Name : " + self.name)
        print("Age : " + str(self.age))
        print("Place : " + self.place)
        print("Year : " + str(StudentsData.year))

    @classmethod
    def add_year(cls, value=1):
        cls.year += value


rocky = StudentsData('Mr. Rocky Bhai', 34, 'KGF')
abu = StudentsData('Mr. Abu Bhai', 38, 'kerala')
professor = StudentsData('Mr. Professor', 40, 'USA')
tokyo = StudentsData('Ms. Tokyo', 28, 'Unknown')

rocky.display()
abu.display()
professor.display()
tokyo.display()

print("---------------------------")

# StudentsData.year += 10
StudentsData.add_year(10)

abu.relocate('Tamil Nadu')

students = [rocky, abu, professor, tokyo]
for student in students:
    student.add_age(10)
    student.display()

# rocky.display()
# abu.display()
# professor.display()
# tokyo.display()
