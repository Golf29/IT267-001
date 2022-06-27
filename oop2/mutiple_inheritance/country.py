from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        self.name = name
        self.area = area
        self.population = pop

    def getpopulationdensity(self):
        return self.population / self.area
    
    def showdetail(self):
        print(f'Countre: {self.name}')
        print(f'Location: {self.getcordinate()}')
        print(f'Population: {self.population:,d}')
        print(f'Area {self.area:,.2f}')
        print(f'Density: {self.getpopulationdensity():,.2f}')
        print(f'Time zone: {self.gettimezone()}')
        print(f'Climat: {self.getclimate()}')
        print(f'Temperture(C): {self.getcelcius()}')
        print(f'Temperature(F): {self.getfahrenheit()}')
        print(f'Weather: {self.getweather()}')
        print('******************************************')