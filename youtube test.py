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






# import urllib.parse
# import webbrowser

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
#     # Open the Google link in the browser
#     webbrowser.open(google_link)
# elif search_choice == 'youtube':
#     youtube_link = generate_youtube_link(song_name)
#     print(f"Here is a YouTube search link for the song: {youtube_link}")
#     # Open the YouTube link in the browser
#     webbrowser.open(youtube_link)
# else:
#     print("Invalid choice. Please enter 'Google' or 'YouTube'.")

# # You can also add the link to a playlist dictionary if needed
# playlist = {song_name: google_link if search_choice == 'google' else youtube_link}



import urllib.parse
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Function to get Google search URL
def generate_google_link(song_name):
    query = urllib.parse.quote(song_name)
    return f"https://www.google.com/search?q={query}+song+download"

# Function to get YouTube search URL
def generate_youtube_link(song_name):
    query = urllib.parse.quote(song_name)
    return f"https://www.youtube.com/results?search_query={query}"

# Function to handle the search action
def search_song():
    song_name = song_entry.get()
    search_choice = search_choice_var.get()

    if not song_name:
        messagebox.showerror("Input Error", "Please enter a song name.")
        return
    
    if search_choice == 'Google':
        google_link = generate_google_link(song_name)
        result_label.config(text=f"Here is a Google search link to download the song: {google_link}")
        webbrowser.open(google_link)
    elif search_choice == 'YouTube':
        youtube_link = generate_youtube_link(song_name)
        result_label.config(text=f"Here is a YouTube search link for the song: {youtube_link}")
        webbrowser.open(youtube_link)
    else:
        messagebox.showerror("Choice Error", "Please choose either 'Google' or 'YouTube'.")
    
    # Close the window after the search
    root.quit()  # or root.destroy()

# Create the main window
root = tk.Tk()
root.title("Song Search")

# Create and pack widgets
song_label = tk.Label(root, text="Enter the name of the song:")
song_label.pack(pady=5)

song_entry = tk.Entry(root, width=40)
song_entry.pack(pady=5)

search_choice_var = tk.StringVar(value='Google')  # Default to Google
google_radio = tk.Radiobutton(root, text="Google", variable=search_choice_var, value='Google')
google_radio.pack(anchor='w', padx=20)

youtube_radio = tk.Radiobutton(root, text="YouTube", variable=search_choice_var, value='YouTube')
youtube_radio.pack(anchor='w', padx=20)

search_button = tk.Button(root, text="Search", command=search_song)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=5)

# Run the application
root.mainloop()
