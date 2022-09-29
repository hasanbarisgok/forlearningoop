#https://www.techgeekbuzz.com/blog/python-object-oriented-programming-exercise/
#Python OOPs Exercise 1: Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.

from traceback import print_tb


class studentsforExercise1:                                                                                                    # ->  The class had been created
    name:str = ''
    age:int = 0
    grade:str = 0
    def __init__(self,name,age,grade):                                                                                         # -> Constructor 
                                                                                                                               # -> Attributes have been initalized
        self.name = name
        self.age = age
        self.grade = grade

stdnt1 = studentsforExercise1('Baris',21,'2025')                                                                                # -> The object had been created
print(f"{stdnt1.name} {stdnt1.age} {stdnt1.grade}")


#Python OOPs Exercise 2: Write a Program to create a valid empty class by name Students, with no properties
class studentsforExercise2:
    pass
stdnt2 = studentsforExercise2()

#Python OOPs Exercise 3: Write a program to create a child class Teacher that will inherit the properties of Parent class Staff
class Staff():
    def __init__(self,role,dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}") 
        print(f"role : {self.role}") 
        print(f"salary : {self.salary}")

    #inherit from the Staff Class

class Teacher(Staff):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Teacher", "Science", 25000)   # -> for initializing the Parent Class

teacher = Teacher("A name", 25)
teacher.show_details() # to show teacher details. The intherit class is personal, and this can be changeable. 
                       #But mom class (class Staff) is general, so same for every teachers. (salaries, job, etc.). We don't need to change these informations.

