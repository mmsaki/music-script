# Music Script

Add metadata to downloaded songs from Youtube Playlist or Soundcloud.

<img width="508" alt="Screenshot 2024-12-20 at 2 50 56 PM" src="https://github.com/user-attachments/assets/99b7c16f-2318-408e-ae74-ae1615b40fe8" />


## Dependencies

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - used to download songs from youtube / soundcloud / spotify
- [ffmpeg](https://ffmpeg.org/download.html) - using for adding metadata to music files

## How to Install

Install from pypi:

```sh
pip install musicscript
```

Run `musicscript` in terminal:

```sh
# run in terminal
musicscript

# 👾 Hello, Music Script
# Enter Artist Name:
# Enter Album Name:
# Enter Yotube Playlist / Soundcloud Album:
```

<img width="722" alt="Screenshot 2024-12-18 at 9 51 21 AM" src="https://github.com/user-attachments/assets/3022e351-de04-4c17-9261-ac8ab02145f3" />

## Local Setup

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
cd music-script;

uv sync;

uv run musicscript;

# Answer input prompts
#
# 👾 Hello, Music Script
# Enter Artist Name:
# Enter Album Name:
# Enter Yotube Playlist / Soundcloud Album:
```

## Test

TODO!

Enjoy offline streaming!
