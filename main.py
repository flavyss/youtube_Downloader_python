import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_video():
    # Pega o link do vídeo do YouTube
    link = link_entry.get()

    # Faz o download do vídeo em formato MP4
    yt = YouTube(link)
    video = yt.streams.filter(mime_type='video/mp4').first()

    # Exibe a janela de diálogo para escolher o diretório de destino
    filepath = filedialog.askdirectory()

    # Faz o download do vídeo para o diretório escolhido
    video.download(filepath)

    # Exibe uma mensagem de sucesso
    label['text'] = "O vídeo foi baixado com sucesso!"

# Cria a janela principal
root = tk.Tk()
root.title("Baixador de vídeos do YouTube")

# Cria um campo de entrada para o link do vídeo
link_entry = tk.Entry(root, width=60)
link_entry.pack()

# Cria um botão para iniciar o download
button = tk.Button(root, text="Baixar", command=download_video)
button.pack()

# Cria uma etiqueta para exibir mensagens
label = tk.Label(root, text="")
label.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
