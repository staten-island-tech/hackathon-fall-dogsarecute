import webbrowser
from googlesearch import search

def search_song_on_google(song_name):
    query = f"{song_name} site:youtube.com"
    
    try:
        # Searching on Google for the song's YouTube link
        results = search(query, num_results=5)  # You can adjust the number of results

        # Open the first YouTube result
        if results:
            print(f"Found YouTube links for '{song_name}':")
            for i, link in enumerate(results):
                print(f"{i+1}. {link}")
            
            # Automatically open the first link in the browser
            print(f"Opening the first result in your browser: {results[0]}")
            webbrowser.open(results[0])  # Opens the first YouTube link found

        else:
            print(f"No results found for '{song_name}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
song_name = input("Enter the song name to search: ")
search_song_on_google(song_name)
