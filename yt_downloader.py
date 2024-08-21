import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import json

def is_json_format(filepath):
    """Check if the file is in JSON format."""
    print('Im here')
    try:
        print('Im here2')
        with open(filepath, 'r') as file:
            print('Im here3')
            json.load(file)
            print('Im here4')
        return True
    except ValueError:
        print('Im here5')
        return False

import time

def convert_json_to_netscape(json_file, netscape_file):
    """Convert JSON cookies to Netscape format, fixing invalid expiration dates."""
    try:
        with open(json_file, 'r') as file:
            cookies = json.load(file)

        with open(netscape_file, 'w') as file:
            file.write("# Netscape HTTP Cookie File\n")
            for cookie in cookies:
                # Fix expiration date if necessary
                expiration_date = cookie.get('expirationDate', 0)
                if expiration_date > time.time() + 10*365*24*60*60:  # More than 10 years in the future
                    expiration_date = time.time() + 365*24*60*60  # Set to 1 year from now

                file.write(f"{cookie['domain']}\t{'TRUE' if cookie['domain'][0] == '.' else 'FALSE'}\t"
                           f"{cookie['path']}\t{'TRUE' if cookie['secure'] else 'FALSE'}\t"
                           f"{int(expiration_date)}\t"  # Ensure it's an integer
                           f"{cookie['name']}\t{cookie['value']}\n")
    except Exception as e:
        print(f"Failed to convert cookies: {e}")
        raise

def download_youtube_content(url, download_path, quality, audio_only, is_playlist):
    try:
        # Print the current working directory
        current_directory = os.getcwd()
        print(f"Current working directory: {current_directory}")

        # Check and convert cookies if necessary
        cookies_file = './cookies.json'
        print('hi------')
        if is_json_format(cookies_file):
            print('hi2')
            print("Cookies file is in JSON format. Converting to Netscape format...")
            convert_json_to_netscape(cookies_file, cookies_file)

        # Determine the path to yt-dlp binary
        yt_dlp_path = os.path.join(os.path.dirname(__file__), 'yt-dlp')  # For Linux/macOS
        # yt_dlp_path = os.path.join(os.path.dirname(__file__), 'yt-dlp.exe')  # For Windows
        print(f"Path to yt-dlp: {yt_dlp_path}")

        # Set the format string based on user choice
        format_str = 'bestaudio' if audio_only else f'bestvideo[height<={quality}]+bestaudio/best'
        print(format_str)
        # Define the command to download content
        command = [
            yt_dlp_path,
            '-f', format_str,
            '--merge-output-format', 'mp4',
            '-o', f'{download_path}/%(title)s.%(ext)s',
            '--cookies', cookies_file,
            url
        ]

        # If the quality doesn't exist, fallback to the best quality
        command.extend(['--format-sort', 'quality,res'])

        # Add playlist options if needed
        if not is_playlist:
            command.append('--no-playlist')

        # Execute the command and print progress in real-time
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Print each line of output as it's received
        for line in process.stdout:
            print(line, end="")  # 'end=""' prevents adding extra new lines

        # Wait for the process to complete and get the exit code
        process.wait()

        if process.returncode == 0:
            print("Download completed successfully.")
        else:
            print(f"Download failed with return code {process.returncode}.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def on_download():
    url = entry_url.get()
    download_path = entry_path.get()
    quality = quality_var.get()
    audio_only = var_audio_only.get()
    is_playlist = var_playlist.get()

    if not url or not download_path:
        messagebox.showerror("Input Error", "Please provide the URL and download path.")
        return

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    try:
        download_youtube_content(url, download_path, quality, audio_only, is_playlist)
        messagebox.showinfo("Success", "Download completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the Tkinter application window
root = tk.Tk()
root.title("YouTube Downloader")

# Create and place the widgets
tk.Label(root, text="URL:").grid(row=0, column=0, padx=10, pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Download Path:").grid(row=1, column=0, padx=10, pady=10)
entry_path = tk.Entry(root, width=50)
entry_path.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Quality:").grid(row=2, column=0, padx=10, pady=10)
quality_var = tk.StringVar(value="1080")  # Default value
quality_options = ["144", "240", "360", "480", "720", "1080", "1440", "2160"]
quality_menu = tk.OptionMenu(root, quality_var, *quality_options)
quality_menu.grid(row=2, column=1, padx=10, pady=10)

var_audio_only = tk.BooleanVar()
chk_audio_only = tk.Checkbutton(root, text="Audio Only", variable=var_audio_only)
chk_audio_only.grid(row=3, column=1, padx=10, pady=10, sticky="w")

var_playlist = tk.BooleanVar(value=True)
chk_playlist = tk.Checkbutton(root, text="Download as Playlist", variable=var_playlist)
chk_playlist.grid(row=4, column=1, padx=10, pady=10, sticky="w")

button_download = tk.Button(root, text="Download", command=on_download)
button_download.grid(row=5, column=1, padx=10, pady=20, sticky="e")

# Run the Tkinter event loop
root.mainloop()
