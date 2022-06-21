class Animal:
    animal = 'CAT'

    def new_animal(self,name:str,breed:str,colour:str,age:int):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age


    def print_detail(self):
        print(f'-----------------------------------')
        print(f'name:{self.name}')
        print(f'animal:{self.animal}')
        print(f'breed:{self.breed}')
        print(f'colour:{self.colour}')
        print(f'age:{self.age}')
        
    def __del__(self):
        print(f'Object was destroyed')

if __name__ == '__main__':
    Animal.animal = 'FISH'
    ula = Animal()
    ula.animal = 'DOG'
    ula.new_animal('ula','Scottish','white',1)
    ula.print_detail()

    drac = Animal()
    drac.new_animal('Drac','Scottich','white',1)
    drac.print_detail()
    drac.breed = 'Carfish'
    drac.print_detail()
    
    Animal.print_detail(ula)
    Animal.print_detail(drac)
    
    print(f'{Animal.__dict__}')
    print(f'{ula.__dict__}')

    peter = Animal()
    peter.new_animal('Peter','Rarrot','green yellow red',2)
    peter.legs = 2
    print(f'{peter.__dict__}')