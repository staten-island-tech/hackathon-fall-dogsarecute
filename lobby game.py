# import urllib.parse
# import webbrowser
# import tkinter as tk
# from tkinter import messagebox
# import random

# # Function to get Google search URL
# def generate_google_link(song_name):
#     query = urllib.parse.quote(song_name)
#     return f"https://www.google.com/search?q={query}+song+download"

# # Function to get YouTube search URL
# def generate_youtube_link(song_name):
#     query = urllib.parse.quote(song_name)
#     return f"https://www.youtube.com/results?search_query={query}"

# # Function to handle the search action
# def search_song():
#     song_name = song_entry.get()
#     search_choice = search_choice_var.get()

#     if not song_name:
#         messagebox.showerror("Input Error", "Please enter a song name.")
#         return
    
#     if search_choice == 'Google':
#         google_link = generate_google_link(song_name)
#         result_label.config(text=f"Here is a Google search link to download the song: {google_link}")
#         webbrowser.open(google_link)
#     elif search_choice == 'YouTube':
#         youtube_link = generate_youtube_link(song_name)
#         result_label.config(text=f"Here is a YouTube search link for the song: {youtube_link}")
#         webbrowser.open(youtube_link)
#     else:
#         messagebox.showerror("Choice Error", "Please choose either 'Google' or 'YouTube'.")
    
#     # Close the window after the search
#     root.quit()  # or root.destroy()

# # Function to animate musical notes
# def animate_music_notes():
#     # Create 5 music notes at random starting positions
#     music_notes = []
#     for _ in range(5):
#         x_pos = random.randint(50, 350)
#         y_pos = random.randint(50, 300)
#         note = canvas.create_text(x_pos, y_pos, text="♪", font=("Arial", 24), fill="black")
#         music_notes.append(note)
    
#     # Move each note vertically down and reset after it goes off-screen
#     def move_notes():
#         for note in music_notes:
#             canvas.move(note, 0, 5)
#             if canvas.coords(note)[1] > 400:  # If the note moves off screen
#                 canvas.delete(note)
#                 music_notes.remove(note)
#                 x_pos = random.randint(50, 350)
#                 y_pos = random.randint(50, 300)
#                 new_note = canvas.create_text(x_pos, y_pos, text="♪", font=("Arial", 24), fill="black")
#                 music_notes.append(new_note)
#         canvas.after(50, move_notes)  # Keep moving the notes
    
#     move_notes()

# # Create the main window
# root = tk.Tk()
# root.title("Song Search")

# # Create and pack widgets
# song_label = tk.Label(root, text="Enter the name of the song:")
# song_label.pack(pady=5)

# song_entry = tk.Entry(root, width=40)
# song_entry.pack(pady=5)

# search_choice_var = tk.StringVar(value='Google')  # Default to Google
# google_radio = tk.Radiobutton(root, text="Google", variable=search_choice_var, value='Google')
# google_radio.pack(anchor='w', padx=20)

# youtube_radio = tk.Radiobutton(root, text="YouTube", variable=search_choice_var, value='YouTube')
# youtube_radio.pack(anchor='w', padx=20)

# search_button = tk.Button(root, text="Search", command=search_song)
# search_button.pack(pady=10)

# result_label = tk.Label(root, text="", wraplength=400)
# result_label.pack(pady=5)

# # Create a canvas for drawing and animating musical notes
# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()

# # Start animating music notes
# animate_music_notes()

# # Run the application
# root.mainloop()

import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width = 600
height = 400
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up clock
clock = pygame.time.Clock()

# Define snake block size
block_size = 10
snake_speed = 15

# Set font for score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    game_display.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Starting position of snake
    x1 = width / 2
    y1 = height / 2

    # Movement direction
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Generate food for snake
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Game over if snake goes out of bounds
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(blue)

        # Draw food
        pygame.draw.rect(game_display, red, [foodx, foody, block_size, block_size])

        # Update snake body
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Remove snake tail to keep snake moving
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for collisions with the snake's own body
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw snake
        draw_snake(block_size, snake_List)
        display_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake ate food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        # Control the snake's speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()

