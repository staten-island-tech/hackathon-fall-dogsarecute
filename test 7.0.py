import webbrowser
from youtubesearchpython import VideosSearch

def get_youtube_url(song_name):
    """Searches for the song on YouTube and returns the URL."""
    video_search = VideosSearch(song_name, limit = 1)  # limit is set to 1 to get the first result
    results = video_search.result()
    video_url = results['videos'][0]['link']  # Get the URL of the first result
    return video_url

def create_playlist():
    """Create a playlist based on user input."""
    num_songs = int(input("How many songs do you want in your playlist? "))
    songs = []

    for i in range(num_songs):
        song = input(f"Enter song #{i + 1}: ")
        songs.append(song)

    # Play the songs in order
    for song in songs:
        print(f"Playing: {song}")
        song_url = get_youtube_url(song)
        webbrowser.open(song_url)  # Opens the song in the browser

if __name__ == "__main__":
    create_playlist()
