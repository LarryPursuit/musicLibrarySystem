class Song:
    """A song in the music library.

    Each instance stores its own name, artist, and genre. The class itself
    keeps library-wide statistics that update every time a Song is created.
    """

    # Class attributes: shared by every Song, not owned by any one instance.
    count = 0           # total number of songs created
    genres = []         # unique genres across all songs
    artists = []        # unique artists across all songs
    genre_count = {}    # genre -> number of songs, e.g. {"Rap": 5}
    artist_count = {}   # artist -> number of songs, e.g. {"Beyonce": 17}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Record this new song in the class-level statistics.
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add the genre to the genres list if it isn't already there."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add the artist to the artists list if it isn't already there."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the genre's tally, starting it at 1 if it's new."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increment the artist's tally, starting it at 1 if they're new."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
