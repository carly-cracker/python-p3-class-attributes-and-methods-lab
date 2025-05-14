class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.__class__.add_song_to_count(self)
        self.__class__.add_to_genres(self)
        self.__class__.add_to_artist(self)
        self.__class__.add_to_genre_count(self.genre)
        self.__class__.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls, self):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, song):
        cls.genres.append(song.genre)

    @classmethod
    def add_to_artist(cls, song):
        cls.artists.append(song.artist)

    @classmethod
    def add_to_genre_count(cls, genre ):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    @classmethod
    def show_genre_hitogram(cls):
        return cls.genre_count
    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count [artist] += 1
        else :
            cls.artist_count[artist] = 1
    @classmethod
    def show_artist_hitogram(cls):
        return cls.artist_count



last = Song("lasty","buurna", "afrobeat")
the_older = Song("the older", "dolly parton", "country")
print(Song.count)
print(Song.genres)
print(Song.artists)