class Student:
    def __init__(self,name:str,id:str,major:str = "IT",) -> None:
        self.id = id
        self.name = name
        self.major = major
    def display_detail(self):
        print(f'id:{self.id}')
        print(f'name:{self.name}')
        print(f'major:{self.major}')
def __del__(self):
    print(f'Object was destroyed')
if __name__ == '__main__':
    jessica = Student('111','Jesica','IT')
    John = Student('112','John','MKT',)
    amy = Student('113','Amy')
    
    jessica.display_detail()
    John.display_detail()
    amy.display_detail()
