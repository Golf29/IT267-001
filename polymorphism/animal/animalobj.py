#from animalsubclass import Dog,Cat,Cow
from animalsubclass import *
dogobj = Dog("Fluffy",4)
catobj = Cat("Milo",2.5)
cowobj = Cow("phil",5)
for animal in (dogobj,catobj,cowobj):
    print('**********')
    animal.info()
    animal.make_sound()