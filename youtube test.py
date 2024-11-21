# import urllib.parse

# # Function to get Google search URL
# def generate_google_link(song_name):
#     # URL encode the song name to ensure it works in a URL
#     query = urllib.parse.quote(song_name)
#     return f"https://www.google.com/search?q={query}+song+download"

# # Function to get YouTube search URL
# def generate_youtube_link(song_name):
#     # URL encode the song name to ensure it works in a URL
#     query = urllib.parse.quote(song_name)
#     return f"https://www.youtube.com/results?search_query={query}"

# # Ask user for the song name
# song_name = input("Enter the name of the song: ")

# # Ask user if they want to search on Google or YouTube
# search_choice = input("Would you like to search on Google for song download or YouTube? (Enter 'Google' or 'YouTube'): ").strip().lower()

# # Generate the appropriate search link based on the user's choice
# if search_choice == 'google':
#     google_link = generate_google_link(song_name)
#     print(f"Here is a Google search link to download the song: {google_link}")
# elif search_choice == 'youtube':
#     youtube_link = generate_youtube_link(song_name)
#     print(f"Here is a YouTube search link for the song: {youtube_link}")
# else:
#     print("Invalid choice. Please enter 'Google' or 'YouTube'.")

# # You can also add the link to a playlist dictionary if needed
# playlist = {song_name: google_link if search_choice == 'google' else youtube_link}

import urllib.parse
import webbrowser

# Function to get Google search URL
def generate_google_link(song_name):
    # URL encode the song name to ensure it works in a URL
    query = urllib.parse.quote(song_name)
    return f"https://www.google.com/search?q={query}+song+download"

# Function to get YouTube search URL
def generate_youtube_link(song_name):
    # URL encode the song name to ensure it works in a URL
    query = urllib.parse.quote(song_name)
    return f"https://www.youtube.com/results?search_query={query}"

# Ask user for the song name
song_name = input("Enter the name of the song: ")

# Ask user if they want to search on Google or YouTube
search_choice = input("Would you like to search on Google for song download or YouTube? (Enter 'Google' or 'YouTube'): ").strip().lower()

# Generate the appropriate search link based on the user's choice
if search_choice == 'google':
    google_link = generate_google_link(song_name)
    print(f"Here is a Google search link to download the song: {google_link}")
    # Open the Google link in the browser
    webbrowser.open(google_link)
elif search_choice == 'youtube':
    youtube_link = generate_youtube_link(song_name)
    print(f"Here is a YouTube search link for the song: {youtube_link}")
    # Open the YouTube link in the browser
    webbrowser.open(youtube_link)
else:
    print("Invalid choice. Please enter 'Google' or 'YouTube'.")

# You can also add the link to a playlist dictionary if needed
playlist = {song_name: google_link if search_choice == 'google' else youtube_link}
