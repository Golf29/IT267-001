class Animal:
    def __init__(self,name,age) -> None:
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @name.setter    
    def info(self,value):
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age = value

    def info(self):
        print('---Animal Information---')
    def make_sound(self):
        print('=== Animal Sound ===')