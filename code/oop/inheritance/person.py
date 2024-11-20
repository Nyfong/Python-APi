class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname =lname
    
    def Name(self):
        printString = f'first name:{self.fname}, last name:{self.lname}'
        return printString

#inheritance  -> student inherited from Person (Student:Child , Person:Parent)
class Student(Person):
    pass
    # Use the pass keyword when 
    # you do not want to add any other properties or methods to the class.

    

object = Student('kdet toch', ' Saouy')
print(object.Name())
