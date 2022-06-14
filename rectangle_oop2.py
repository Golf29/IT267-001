class Rectangle:
    def __init__(self) -> None:
        self.width = 0
        self.length = 0
        self.area = 0
    def get_data(self):
        self.width = float(input('Enter width: '))
        self.length = float(input('Enter length: '))
    def comput_area(self):
        self.area = self.width * self.length

    def print_area(self):
        print(f'Ractangle Area: {self.area}')

# create object
rec_obj = Rectangle()
rec_obj.get_data()
rec_obj.comput_area()
rec_obj.print_area()