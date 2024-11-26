import urllib.parse

def generate_google_link(song_name):
  
    query = urllib.parse.quote(song_name)
    return f"https://www.google.com/search?q={query}+song+download"

song_name = input("Enter the name of the song: ")


google_link = generate_google_link(song_name)

print(f"Here is a Google search link to download the song: {google_link}")
playlist = {song_name : google_link }