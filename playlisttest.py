import urllib.parse
import webbrowser
import tkinter as tk
from tkinter import messagebox
import random

# Function to get Google search URL
def generate_google_link(song_name):
    query = urllib.parse.quote(song_name)
    return f"https://www.google.com/search?q={query}+song+download"

# Function to get YouTube search URL
def generate_youtube_link(song_name):
    query = urllib.parse.quote(song_name)
    return f"https://www.youtube.com/results?search_query={query}"

# Function to show search results and open the link automatically
def show_search_results():
    song_name = song_entry.get()
    search_choice = search_choice_var.get()

    if not song_name:
        messagebox.showerror("Input Error", "Please enter a song name.")
        return
    
    # Generate the search URL based on the user's choice
    if search_choice == 'Google':
        search_link = generate_google_link(song_name)
    elif search_choice == 'YouTube':
        search_link = generate_youtube_link(song_name)
    else:
        messagebox.showerror("Choice Error", "Please choose either 'Google' or 'YouTube'.")
        return

    # Display the clickable link
    result_label.config(text=f"Opening the link for: {song_name}...\n{search_link}")
    
    # Update the current link so it can be manually added later
    current_link.set(search_link)
    
    # Automatically open the link in the browser
    open_link_in_browser(search_link)

# Function to open the link in the browser
def open_link_in_browser(link):
    # Open the link in the browser
    webbrowser.open(link)

# Function to manually add the link to the playlist
def add_to_playlist():
    link = current_link.get()  # Get the current link
    song_name = song_entry.get()

    if not song_name or not link:
        messagebox.showerror("Input Error", "Please enter a song name and open the link first.")
        return
    
    # Check for duplicate songs in the playlist
    if any(song_name.lower() == existing_song[0].lower() for existing_song in playlist):
        messagebox.showerror("Duplicate Error", "This song is already in the playlist.")
        return

    # Add the song and its link to the playlist
    playlist.append((song_name, link))
    update_playlist_display()

    # Clear the song name entry field
    song_entry.delete(0, tk.END)
    
    result_label.config(text="Link added to playlist!")

# Function to update the playlist display with links
def update_playlist_display():
    playlist_text = "\n".join([f"{song[0]} - {song[1]}" for song in playlist])
    playlist_label.config(text=f"Current Playlist:\n{playlist_text}")

# Function to remove a song from the playlist
def remove_song_from_playlist():
    song_to_remove = remove_song_entry.get()
    for i, (song, _) in enumerate(playlist):
        if song_to_remove.lower() == song.lower():
            del playlist[i]
            update_playlist_display()
            messagebox.showinfo("Success", f"'{song_to_remove}' has been removed from the playlist.")
            return
    messagebox.showerror("Error", f"'{song_to_remove}' is not in the playlist.")

# Function to clear the entire playlist
def clear_playlist():
    playlist.clear()
    update_playlist_display()
    messagebox.showinfo("Success", "The playlist has been cleared.")

# Function to play (open) links in the playlist in order
def play_playlist():
    if not playlist:
        messagebox.showerror("Error", "The playlist is empty.")
        return

    def open_next_link(index=0):
        if index < len(playlist):
            song, link = playlist[index]
            result_label.config(text=f"Opening {song}...")
            webbrowser.open(link)
            # Simulate song duration (e.g., 3 minutes or 180 seconds)
            root.after(180000, open_next_link, index + 1)  # 180000ms = 3 minutes (180 seconds)
        else:
            # Once we reach the end of the playlist, restart from the beginning
            result_label.config(text="Playlist finished! Restarting playlist...")
            root.after(3000, open_next_link, 0)  # Wait 3 seconds before restarting the playlist

    open_next_link()

# Function to animate musical notes
def animate_music_notes():
    # Create 5 music notes at random starting positions
    music_notes = []
    for _ in range(5):
        x_pos = random.randint(50, 350)
        y_pos = random.randint(50, 300)
        note = canvas.create_text(x_pos, y_pos, text="♪", font=("Arial", 24), fill="black")
        music_notes.append(note)
    
    # Move each note vertically down and reset after it goes off-screen
    def move_notes():
        for note in music_notes:
            canvas.move(note, 0, 5)
            if canvas.coords(note)[1] > 400:  # If the note moves off screen
                canvas.delete(note)
                music_notes.remove(note)
                x_pos = random.randint(50, 350)
                y_pos = random.randint(50, 300)
                new_note = canvas.create_text(x_pos, y_pos, text="♪", font=("Arial", 24), fill="black")
                music_notes.append(new_note)
        canvas.after(50, move_notes)  # Keep moving the notes
    
    move_notes()

# Create the main window
root = tk.Tk()
root.title("Song Search and Playlist")

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

search_button = tk.Button(root, text="Search", command=show_search_results)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=5)

# Playlist Section
playlist = []  # List to hold the songs and their links in the playlist
playlist_label = tk.Label(root, text="Current Playlist:")
playlist_label.pack(pady=10)

# Entry and button for removing a song from the playlist
remove_song_label = tk.Label(root, text="Enter the song name to remove:")
remove_song_label.pack(pady=5)

remove_song_entry = tk.Entry(root, width=40)
remove_song_entry.pack(pady=5)

remove_button = tk.Button(root, text="Remove Song", command=remove_song_from_playlist)
remove_button.pack(pady=5)

# Entry for user to paste the link manually
link_entry_label = tk.Label(root, text="Enter song link to add to playlist:")
link_entry_label.pack(pady=5)

link_entry = tk.Entry(root, width=40)
link_entry.pack(pady=5)

# Button to manually add the link to the playlist
add_button = tk.Button(root, text="Add Link to Playlist", command=lambda: add_link_to_playlist(link_entry.get()))
add_button.pack(pady=10)

# Button to clear the entire playlist
clear_button = tk.Button(root, text="Clear Playlist", command=clear_playlist)
clear_button.pack(pady=10)

# Button to play the playlist (open links sequentially)
play_button = tk.Button(root, text="Play Playlist", command=play_playlist)
play_button.pack(pady=10)

# Create a canvas for drawing and animating musical notes
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Variable to store the current link
current_link = tk.StringVar()

# Start animating music notes
animate_music_notes()

# Function to add a manually entered link to the playlist
def add_link_to_playlist(link):
    song_name = song_entry.get()  # Get the song name from the entry field

    if not song_name or not link:
        messagebox.showerror("Input Error", "Please enter both a song name and a link.")
        return

    # Check if the song is already in the playlist
    if any(song_name.lower() == existing_song[0].lower() for existing_song in playlist):
        messagebox.showerror("Duplicate Error", "This song is already in the playlist.")
        return

    # Add the song name and link to the playlist
    playlist.append((song_name, link))
    update_playlist_display()

    # Clear the entry fields
    song_entry.delete(0, tk.END)
    link_entry.delete(0, tk.END)

    result_label.config(text="Link added to playlist!")

# Run the application
root.mainloop()
