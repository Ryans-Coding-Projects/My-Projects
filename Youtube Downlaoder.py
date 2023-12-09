#Use this program to download youtube videos

from pytube import Youtube

def Download(link):
    youtubeObject = Youtube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.downlaod()
    except:
        print("An error has occurred")
    print("Download completed")

link = input("Enter Youtube Video URL: ")
Download(link)
