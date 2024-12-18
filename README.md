# Music Script

Download songs from youtube playlist into an Album:

## Dependencies

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - used to download songs from youtube / soundcloud / spotify
- [ffmpeg](https://ffmpeg.org/download.html) - using for adding metadata to music files

## Run Project

> [!NOTE]
>
> ### Installing UV
>
> Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) python package manager written in rust
>
> ```sh
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```
>
> After install uv you can clone this project with:
>
> ```sh
> git clone https://github.com/mmsaki/music-script.git
> ```

Run inside project

```sh
uv run download.py

# Answer input prompts
#
# 👾 Hello, Music Script
# Enter Artist Name:
# Enter Album Name:
# Enter Yotube Playlist / Soundcloud Album:
```

## Test

Add songs to your apple music and enjoy offline streaming!
