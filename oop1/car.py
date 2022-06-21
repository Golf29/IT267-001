from cgitb import text


class Car:
    def __init__(self,model,colour,year,price) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    def print_detail(self):
        print(f"Modul: {self.model}")
        print(f"Colourl: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")

    @staticmethod
    def get_static_method(text):
            print(f"String:{text}")
    @classmethod
    def get_class_method(cls):
        print(f"this is class method with {text}")
if __name__ == "__main__":
    my_car = Car("Cross","white",2022,1500000)
    my_car.print_detail()

    Car.get_static_method('hello Classs')
    my_car.get_static_method("Good Car Object")
    Car.get_class_method("Go home")