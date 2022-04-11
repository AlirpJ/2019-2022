# Joshua Prila - last updated April 10, 2022
# Downloading Youtube videos
# https://pypi.org/project/pytube/
# https://pytube.io/en/latest/

from pytube import YouTube

URL = input("enter video URL: ")
file = 'defaultDirectory'

print("\nLink is: ",link)
#YouTube(link).streams.first().download()
#pl.download_all('/path/to/directory/')
yt = YouTube(URL)
#yt.streams.first().download(file)
try:
  video = yt.streams.filter(only_audio=True).first()
  out_file = video.download(output_path = "D:downloads") # Default download path is the folder containing this file
except:
  print("error")
