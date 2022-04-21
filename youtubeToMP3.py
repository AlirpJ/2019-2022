# Joshua Prila - last updated April 21, 2022
# Downloading Youtube videos
# https://pypi.org/project/pytube/
# https://pytube.io/en/latest/

from pytube import YouTube

print("YouTube to Mp3")

URL = input("enter video URL: ")
yt = YouTube(URL)

try:
    print("Downloading...")
    video = yt.streams.filter().first()
    out_file = video.download() # Default download path is the folder containing this file
    #output_path = "D:downloads"
except:
    print("error")
