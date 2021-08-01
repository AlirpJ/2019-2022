# Joshua Prila - last updated August 1, 2021
# Downloading Youtube videos
# https://pypi.org/project/pytube/

from pytube3 import YouTube

link = input("Enter the URL of the YouTube Video: \n")
file = 'defaultDirectory'

print("\nLink is: ",link)
#YouTube(link).streams.first().download()
#pl.download_all('/path/to/directory/')
video = YouTube(link)
video.streams.first().download(file)
