class Movie:
    def __init__(self) -> None:
        self._tital = ''
        self._year = 0
        self._genre = ''
        self._rating = 6
    def _add_movie(self,tital,year,genre,rating=6):
        self._tital = tital
        self._year = year
        self._genre = genre
        self._rating = rating
        
    def _get_movie(self):
        print(f'tital: {self._tital}\nyear:{self._year}\nrating: {self._rating}')