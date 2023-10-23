import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import moviepy.editor as mp

def download_video():
    link = link_entry.get()
    yt = YouTube(link)

    file_type = file_type_var.get()

    if file_type == "mp4":
        video = yt.streams.filter(mime_type='video/mp4').first()
        filepath = filedialog.askdirectory()
        video.download(filepath)
        label['text'] = "O vídeo foi baixado"
    elif file_type == "mp3":
        audio = yt.streams.filter(only_audio=True).first()
        filepath = filedialog.askdirectory()
        audio.download(filepath)

        video_title = yt.title
        video_filename = audio.default_filename
        mp4_filepath = filepath + "/" + video_filename
        mp3_filepath = filepath + "/" + video_title + ".mp3"
        os.rename(mp4_filepath, mp3_filepath)

        label['text'] = "O áudio foi baixado"

root = tk.Tk()
root.title("KripTube - o Brabo")

banner_label = tk.Label(root, text="F.L.A.V.Y.T.U.B.E", font=("Arial", 30, "bold"))
banner_label.pack()
made_by_label = tk.Label(root, text="Feito por Flavyson Felipe", font=("Arial", 12))
made_by_label.pack()

link_entry = tk.Entry(root, width=60)
link_entry.pack()

file_type_var = tk.StringVar()
mp4_radio = tk.Radiobutton(root, text="MP4", variable=file_type_var, value="mp4")
mp4_radio.pack()
mp3_radio = tk.Radiobutton(root, text="MP3", variable=file_type_var, value="mp3")
mp3_radio.pack()

button = tk.Button(root, text="Baixar", command=download_video)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()
