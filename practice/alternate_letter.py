class Student:
    """Developed by balaji for python demo"""
# constructor will be executed automatically at the time of object creation
# The main purpose of constructor is to declare and initialize instance variables
# per object constructor will be executed once
# Constructor can take atleast one argument(self)
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def talk(self):
        print("My name is: ", self.name)
        print("My age is:", self.age)
        print("My marks are:", self.marks)


# here "nale" is the reference variable
nale = Student("Balaji", 28, 80)
nale.talk()
