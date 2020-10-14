# Joshua Prila - last updated April 28, 2020
# Downloading Youtube videos
# https://pypi.org/project/pytube/

import pytube

link = input("Enter the URL of the YouTube Video")
print("\nLink is: ",link)
#YouTube(link).streams.first().download()
#pl.download_all('/path/to/directory/')
video = pytube.YouTube(link)
youtube = video.streams.first()
youtube.download(r'E:\Thund\Downloads')
