from typing import Union
from dataclasses import dataclass


@dataclass
class Song:
    title: str = ""
    artist: str = ""
    track: Union[int, str] = ""
    lyrics: str = ""
    genius_url: str = ""
    performer: str = ""
    comment: str = ""
    composer: str = ""
    grouping: str = ""
    copyright: str = ""
    description: str = ""
    synopsis: str = ""
    path: str = ""
