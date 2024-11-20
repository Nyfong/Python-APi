class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

#creating instance
p1 = Person("kdet Thom", 36)
print(f'Name:{p1.name}, age:{p1.age}')