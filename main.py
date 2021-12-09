from pytube import YouTube

url = 'https://www.youtube.com/watch?v=XfvQWnRgxG0&ab_channel=MindMaster'
video = YouTube(url)

print("\nTítulo do vídeo: ", video.title)
print("\nTumbnail do vídeo: ", video.thumbnail_url)

video = video.streams.get_highest_resolution()
video.download()