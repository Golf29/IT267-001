from animal import Animal
class Dog(Animal):
    def info(self):
        Animal.info(self)
        print(f'I am a dog.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old.')
    def make_sound(self):
        #super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Woof!! Woof!! sound.')

class Cat(Animal):
    def info(self):
        Animal.info(self)
        print(f'I am a cat.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old.')
    def make_sound(self):
        #super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Meaw!! Meaw!! sound.')

class Cow(Animal):
    def info(self):
        Animal.info(self)
        print(f'I am a cow.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old.')
    def make_sound(self):
        #super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Moo!! Moo!! sound.')
