import pytube

# Введіть посилання на відео
video_url = input("Введіть посилання на відео з YouTube: ")

# Створюємо об'єкт YouTube
youtube = pytube.YouTube(video_url)

# Виберіть роздільну здатність відео
video = youtube.streams.get_highest_resolution()

# Виберіть шлях для збереження відео
save_path = input("Введіть шлях для збереження відео: ")

# Завантажуємо відео
video.download(save_path)

print("Відео успішно завантажено!")