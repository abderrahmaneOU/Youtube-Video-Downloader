from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try: 
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print('video downloaded successfully')
    except Exception as e:
        print(e)    
        
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f'selected folder: {folder}')
        
    return folder


root = tk.Tk()
root.withdraw()

video_url = input('please entre a youtube url: ')
save_dir = open_file_dialog()

if save_dir:
    print('started downloading')
    download_video(video_url, save_dir) 
else:
    print('invalid save location')