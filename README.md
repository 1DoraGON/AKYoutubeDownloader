# YouTube Downloader

A simple, open-source tool for downloading YouTube videos, playlists, and audio files in various quality options, bypassing YouTube's restrictions.

## Features

- **Download Videos and Playlists:** Supports downloading both individual videos and entire playlists.
- **Quality Selection:** Choose the desired video quality (from 144p to 2160p).
- **Audio-Only Option:** Option to download audio only in the best available quality.
- **Cookie Support:** Bypasses YouTube's restrictions by using cookies.
- **Simple GUI:** A user-friendly interface built with Tkinter.

## Requirements

- Python 3.x
- `yt-dlp` binary (included with the app)
- `Tkinter` library (usually included with Python)
-  `PyInstaller` library (for building the app run pyinstaller filename.py)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

2. **Download `yt-dlp`:**

   - Linux/macOS:
     ```bash
     curl -L https://yt-dlp.org/downloads/latest/yt-dlp -o yt-dlp
     chmod a+rx yt-dlp
     ```
   - Windows:
     Download the `yt-dlp.exe` from the official [yt-dlp website](https://github.com/yt-dlp/yt-dlp/releases) and place it in the project directory.

3. **Install Python dependencies:**

   ```bash
   pip install tkinter
   ```

## Usage

1. **Run the Application:**

   ```bash
   python yt_downloader.py
   ```

2. **Enter the following details:**

   - **URL:** The URL of the YouTube video or playlist.
   - **Download Path:** The directory where the downloaded files will be saved.
   - **Quality:** Select the desired video quality.
   - **Audio Only:** Check this option if you want to download only the audio.
   - **Download as Playlist:** Check this option if you are downloading a playlist.

3. **Click "Download":** The tool will start downloading the content based on your selections.

## Contributing

Feel free to fork this repository, make improvements, and submit a pull request. All contributions are welcome!

*(PS: You might encounter some debugging `print()` statements xD)*
