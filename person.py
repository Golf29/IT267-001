class Person:
    def __init__(self,name,gender,profession,hours) -> None:
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
#create object
jessa = Person('Jessa','male','Software engineer','10')
jessa.show()
jessa.work()
jessa.study()

Jon = Person('Jon','male','Doctor','15')
Jon.show()
Jon.work()
Jon.study()

lalisa = Person('lalisa','female','Korean Singer','13')
lalisa.work()
