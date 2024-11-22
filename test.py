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

# Create a canvas for drawing and animating musical notes
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Start animating music notes
animate_music_notes()

# Run the application
root.mainloop()
