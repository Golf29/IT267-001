class Movie:
    def __init__(self) -> None:
        self.tital = ''
        self.year = 0 
        self.genre = ''

    def add_movie(self,tital:str,year:int,genre:str):
        self.tital = tital
        self.year = year
        self.genre = genre
    def get_movie(self):
        return self.tital
        
if __name__ == '__main__':
    m = Movie()
    m.add_movie('Mulan',2020,'action')
    print(f'tital: {m.get_movie()}')
    
    print(f'Tital:{m.tital}')
    print(f'Year: {m.year}')
    print(f'Genre: {m.genre}')