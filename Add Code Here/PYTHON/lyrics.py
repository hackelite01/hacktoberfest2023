# pip install lyricsgenius

import lyricsgenius

api_key = "YOUR_API_KEY"

genius = lyricsgenius.Genius(api_key)
artist = genius.search_artist("Pop Smoke", max_songs=5,sort="title")
song = artist.song("100k On a Coupe")

print(song.lyrics)
