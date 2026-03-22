class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, ' says bark, bark, bark!')

class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name, ' says meow meow!')

class Bird():
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name, ' says tweet')


od1 = Dog('Ousmane')
od2 = Dog('Anchita')
od3 = Cat('Mario')
od4 = Cat('Mara')
od5 = Bird('Marlo')

petList = [od1, od2, od3, od4, od5]
for pet in petList:
    pet.speak()
