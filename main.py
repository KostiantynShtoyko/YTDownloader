import tkinter as tk
from pytube import YouTube

def download_video():
    video_url = entry_url.get()
    save_path = entry_path.get()
    try:
        youtube = YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video.download(save_path)
        label_status.config(text="Відео успішно завантажено!")
    except:
        label_status.config(text="Помилка при завантаженні відео.")

root = tk.Tk()
root.title("Завантажувач відео з YouTube")

# Url
label_url = tk.Label(root, text="Введіть посилання на відео:")
label_url.pack()
entry_url = tk.Entry(root)
entry_url.pack()

# Шлях
label_path = tk.Label(root, text="Введіть шлях для збереження відео:")
label_path.pack()
entry_path = tk.Entry(root)
entry_path.pack()

# Кнопка завантаження
button_download = tk.Button(root, text="Завантажити", command=download_video)
button_download.pack()

# Статус
label_status = tk.Label(root, text="")
label_status.pack()

root.mainloop()