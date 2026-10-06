# Music Library System

A Python `Song` class for a music streaming library. Each song stores its own
name, artist, and genre, and the class keeps library-wide statistics: the total
number of songs, the unique artists and genres, and how many songs belong to
each artist and genre.

Built for the Flatiron lab *Inheritance, Class Attributes, and Class Methods*.

## Screenshot

![All tests passing](screenshot.png)

## Installation

Requires Python 3 and [pipenv](https://pipenv.pypa.io/).

```bash
pipenv install
pipenv shell
```

## Usage

```python
from song import Song

Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Single Ladies", "Beyonce", "Pop")

Song.count         # 3
Song.genres        # ["Rap", "Pop"]
Song.artists       # ["Jay Z", "Beyonce"]
Song.genre_count   # {"Rap": 1, "Pop": 2}
Song.artist_count  # {"Jay Z": 1, "Beyonce": 2}
```

### Design

| Kind | Name | Purpose |
|------|------|---------|
| Instance attribute | `name`, `artist`, `genre` | Details of one song |
| Class attribute | `count` | Total songs created |
| Class attribute | `genres` | Unique genres (no duplicates) |
| Class attribute | `artists` | Unique artists (no duplicates) |
| Class attribute | `genre_count` | Songs per genre |
| Class attribute | `artist_count` | Songs per artist |
| Class method | `add_song_to_count` | Increments `count` |
| Class method | `add_to_genres` | Adds a new genre to `genres` |
| Class method | `add_to_artists` | Adds a new artist to `artists` |
| Class method | `add_to_genre_count` | Increments (or starts at 1) a genre's tally |
| Class method | `add_to_artists_count` | Increments (or starts at 1) an artist's tally |

All five class methods run automatically from `__init__` whenever a new `Song`
is created.

## Running Tests

```bash
pytest
```

## Project Structure

```
lib/
├── song.py            # Song class
└── testing/
    ├── conftest.py
    └── song_test.py   # pytest suite
```

## License

See [LICENSE.md](LICENSE.md).
