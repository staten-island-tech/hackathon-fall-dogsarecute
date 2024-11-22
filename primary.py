import urllib.parse

# Function to get Google search URL
def generate_google_link(song_name):
    # URL encode the song name to ensure it works in a URL
    query = urllib.parse.quote(song_name)
    return f"https://www.google.com/search?q={query}+song+download"

# Ask user for the song name
song_name = input("Enter the name of the song: ")

# Generate the Google search link
google_link = generate_google_link(song_name)

# Output the link
print(f"Here is a Google search link to download the song: {google_link}")
playlist = {song_name : google_link }