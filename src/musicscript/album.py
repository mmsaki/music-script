from dataclasses import dataclass
from typing import List
from musicscript.song import Song


@dataclass
class Album:
    """Class that describes an Album"""

    album_artist: str = ""
    album_name: str = ""
    year: str = ""
    genre: str = ""
    cover: str = ""
    path: str = ""
    url: str = ""
    copyright: str = ""
    download_path: str = ""

    def __init__(self):
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)
