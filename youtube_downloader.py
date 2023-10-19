from pytube import YouTube
from sys import argv

link = argv[1] # First command line argument that we give

yt = YouTube(link) # YouTube object with our argument (link)

print("Title: ", yt.title)

print("Views: ", yt.views)


