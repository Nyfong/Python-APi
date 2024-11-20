#hierarchical inheritance

class Animal:
    def __init__(self, sound, name):
        self.sound = sound
        self.name = name
    def animalSound(self):
        print(f'{self.name} sound: {self.sound}')

#DOG  class  (Dog and Cat -> inherited from Animal)
class Dog(Animal):
    def __init__(self, sound, name):
        #add construter for parent
        super().__init__(sound, name) 
        #By using the super() function,
        # you do not have to use the name of the parent element, 
        # it will automatically inherit the methods and properties from its parent.

#cat class
class Cat(Animal):
    def __init__(self, sound, name):
        #add construter for parent
        super().__init__(sound, name)
    
#creating instances

meow = Cat('meow','Cat')    
dog = Dog('Wuzzz','Golden')
meow.animalSound()
dog.animalSound()