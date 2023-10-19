# To download a YouTube video type in the commandline: python youtube_downloader.py <"YouTube link">
#
from pytube import YouTube
from sys import argv

link = argv[1] # First command line argument that we give

yt = YouTube(link) # YouTube object with our argument (link)

# For printing the video's title and author
print("Title: ", yt.title)

print("Author: ", yt.author)

yd = yt.streams.get_highest_resolution() # downloads highest resolation of video

yd.download('/Users/kirra/OneDrive/YouTube_Downloads') # The folder you want the downloads to go to
