import urllib.parse
import webbrowser
import requests
from bs4 import BeautifulSoup
import random

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

# Function to get a random User-Agent to avoid scraping blocks
def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    ]
    return random.choice(user_agents)

# Function to get the first Google search result link
def get_first_google_link(song_name):
    url = generate_google_link(song_name)
    headers = {'User-Agent': get_random_user_agent()}  # Random User-Agent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Google search results are typically inside <a> tags with class "BVG0Nb"
        first_result = soup.find('a', href=True, class_='BVG0Nb')
        if first_result:
            return first_result['href']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Google search results: {e}")
    return None

# Function to get the first YouTube video link
def get_first_youtube_link(song_name):
    url = generate_youtube_link(song_name)
    headers = {'User-Agent': get_random_user_agent()}  # Random User-Agent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # YouTube video links are typically in <a> tags with id="video-title"
        first_video = soup.find('a', {'id': 'video-title'})
        if first_video:
            return f"https://www.youtube.com{first_video['href']}"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching YouTube search results: {e}")
    return None

# Ask user for the song name
song_name = input("Enter the name of the song: ")

# Ask user if they want to search on Google or YouTube
search_choice = input("Would you like to search on Google for song download or YouTube? (Enter 'Google' or 'YouTube'): ").strip().lower()

# Generate the appropriate search link and open the first result based on user's choice
if search_choice == 'google':
    google_link = get_first_google_link(song_name)
    if google_link:
        print(f"Opening the first Google result: {google_link}")
        webbrowser.open(google_link)
    else:
        print("No results found on Google.")
elif search_choice == 'youtube':
    youtube_link = get_first_youtube_link(song_name)
    if youtube_link:
        print(f"Opening the first YouTube video: {youtube_link}")
        webbrowser.open(youtube_link)
    else:
        print("No videos found on YouTube.")
else:
    print("Invalid choice. Please enter 'Google' or 'YouTube'.")
