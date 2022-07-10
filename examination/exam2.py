class Horse:
    def __init__(self,name,age,color,max_height,weight) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.max_height = max_height
        self.weight = weight
    @property
    def name(self):
        return self.name
   
    @property
    def age(self):
        return self.age
   
    @property
    def color(self):
        return self.color
    
    @property
    def max_height(self):
        return self.max_height
    
    @property
    def weighe(self):
        return self.weight
        
        print('---Animal Information---')
    def make_sound(self):
        print('=== Animal Sound ===')
class horse(Horse):
    def info(self):
        Horse.info(self)
        print(f'My name is {self.name}.')
        print(f'my color {self.color} years old.')
        print(f'Max height {self.max_height} cm')

class Donkey(Horse):
    def info(self):
        Horse.info(self)
        print(f'I am {self.age} years old.')
        print(f'weight {self.weight} kg')
    
    def make_sound(self):
        Horse.make_sound(self)
        print(f'Donkey makes eeyore sound.')