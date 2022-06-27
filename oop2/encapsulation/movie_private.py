class Movie:
    def __init__(self,tital,year,genre) -> None:
        self.__tital = tital
        self.__year = year
        self.__genre = genre
    def __get_movie(self):
        print(f'tital:{self.__tital}\ngenre: {self.__genre}')
    def print_detail(self):
        self.__get_movie()