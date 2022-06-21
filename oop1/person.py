from time import perf_counter


class Person:
    country = 'Thailand' #class variable
    def __init__(self,name,gender,profession,hours) -> None:
        #instance
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hours = hours
    def work(self):
        print(f'{self.name}is working as a {self.profession}')
    def study(self):
        print(f'{self.name} studies for {self.hours}hour(s)')
    def show(self):
        print(f'name:{self.name} Gender: {self.gender} Profession: {self.profession} study: {self.hours}')
    def __del__(self):
        print(f'Object destroyed')
#create object
jessa = Person('Jessa','male','Software engineer','10')
jessa.show()
jessa.work()
jessa.study()
print('----------------------------')
Jon = Person('Jon','male','Doctor','15')
Jon.show()
Jon.work()
Jon.study()
print('----------------------------')
lalisa = Person('lalisa','female','Korean Singer','13')
lalisa.work()
Person.country
print(f'Class Variable: {Person.country}')
print(f'Instance Variable: {lalisa.country}')
#assign value
lalisa.country = 'Korea'
print('----------------------------')
print(f'Class Variable: {Person.country}')
print(f'Instance Variable: {lalisa.country}')
print(f'Instance Variable: {Jon.country}')

Person.country = 'England'
print('----------------------------')
print(f'Class Variable: {Person.country}')
print(f'Instance Variable: {lalisa.country}')
print(f'Instance Variable: {Jon.country}')