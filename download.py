import os
from musicscript.album import Album
from musicscript.program_runner import ProgramRunner
from musicscript.runner import Runner

print("👾 Hello, Music Script")

### ENTER Metadata
artist = input("Enter Artist Name: ")
title = input("Enter Album Name: ")
url = input("Enter Yotube Playlist / Soundcloud Album: ")

### Detault EXAMPLE
if not artist: 
    artist = "LUCKI"

if not title: 
    title = "GEMINI!"
    
if not url: 
    url = "https://www.youtube.com/watch?v=-_CXWQQIOnQ&list=OLAK5uy_nOYJu0d8SCcr6K9n_0cJFEwG9WwjtyJQk"

album = Album()
album.artist = artist
album.title = title
album.url = url
album.path = "music/" + album.artist + " - " + album.title
album._download_path = album.path + '/download'

print("📦 Album Directory: ", album.path)

def download(album: Album, log=False):
    """Download songs using yt-dlp"""

    os.makedirs(album._download_path, exist_ok=True)

    args = [
        'yt-dlp',
        '-x',
        '--audio-format',
        'mp3',
        '-P',
        f'{album._download_path}',
        '-vU', 
        '-R', 
        'inf',
        '--file-access-retries', 
        'inf',
        '--fragment-retries',
        'inf',
        '-o',
        '%(title)s.%(ext)s',
        '--parse-metadata',
        "title:%(title)s",
        '--parse-metadata',
        "artist:%(artists)",
        '--parse-metadata',
        "album:%(album)",
        '--parse-metadata',
        "album_artist:%(album_artist)",
        '--parse-metadata',
        "genre:%(genre)",
        '--parse-metadata',
        "date:%(upload_date)",
        '--parse-metadata',
        "composer:%(composer)",
        album.url
    ]
    p = ProgramRunner(program=args)
    res = p.run()
    if log:
        print("📦 Finished Running download", res[1])
        if res[0].stdout:
            print("🪵 Log: ", res[0].stdout)
    print("🗂️ Download Results: ", res[1])

download(album, log=True)

def rename_songs(album: Album, log=False):
    """Rename songs by removing yt-dlpd download tags"""
    files = os.listdir(album._download_path)
    for file in files:
        new_name = file.replace(" (Official Video)", "")
        new_name = new_name.replace(" (Official Visualizer)", "")
        new_name = new_name.replace(f"{album.artist} - ", "")
        # TODO: santize song titles
        new_path = album._download_path + "/" + new_name
        old_path = album._download_path + "/" + file
        os.rename(old_path, new_path)
    if log:
        print("📦 Renamed Songs Complete")

rename_songs(album, log=True)

def add_metadata(album: Album, log=False):
    """Add song metadata, ex. Artist Name, Album Name"""
    
    files = os.listdir(album._download_path)

    for file in files:
        # new paths
        file_path = album._download_path + "/" + file
        new_path = album.path + "/" + file

        # song metadata
        album_name = 'album=' + f'{album.title}'
        artist_name = 'artist=' + f'{album.artist}'
        args =  [
            'ffmpeg', 
            '-i', 
            file_path, 
            '-y', 
            '-metadata', 
            album_name, 
            '-metadata', 
            artist_name, 
            f"{new_path}"
        ]

        # run ffmpeg
        p = ProgramRunner(program=args)
        res = p.run()
        if log:
            print("📦 Adding Song metadata:", res[1], file)
            if res[0].stderr:
                print("🪵 Log:", res[0].stderr)
            if res[1] == Runner().PASS:
                args = ["rm", f"{file_path}"]
                p = ProgramRunner(program=args)
                p.run()

    # Clean download directory
    if len(os.listdir(album._download_path)) == 0:
        args = ["rm", "-rf", f"{album._download_path}"]
        p = ProgramRunner(program=args)
        p.run()
        print("🧹 Cleaned download directory")
    else:
        print("⚠️ Download directory has aritfacts")

add_metadata(album, log=True)

print("🗂️ Job Completed", album.path, "from:", album.url)