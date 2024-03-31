from pytube import YouTube

link = input("YT link: ")
#yt = YouTube(link, on_progress_callback=progress_function)
yt = YouTube(link)

#print("Title: ", yt.title)
#print("Views: ", yt.views)

videoDownloaded = yt.streams.get_highest_resolution()
videoDownloaded.download('/Users/JULIO/Videos')