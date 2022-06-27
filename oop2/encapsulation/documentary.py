from movie_proticted import Movie

class Documentary(Movie):
    def __init__(self) -> None:
        super().__init__()  
        self.channel = None
    def add_channel(self,channel:str):
        self.channel = channel
        