#global variable
from distutils.log import error
from turtle import color


bird_type = "parrot"

class Bird:
    #class variable
    bird_name = "Peter"


    def __init__(self,color) -> None:
        #instance variable
        self.color = color

        #local variable
        country = "Thailand"
        print(country)

    def show(self):
        return f'{bird_type}{Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    print(f'*****{bird_type}*****')
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())

    #เรียก class variable
    #print(bird_name) error
    #เรียก class variable ชื่อคลาส.class_variable
    print(Bird.bird_name)
    #ชื่อวัตถุ
    print(my_bird.bird_name)
    #เรียก instance
    #print(Bird.color)#error
    print(my_bird.color)