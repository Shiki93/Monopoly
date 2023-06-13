"El tablero del monopoly"

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Monopoly")
window.geometry("1280x720")

# Create a canvas to draw the game board
canvas = tk.Canvas(window, width=1280, height=720, bg="white")
canvas.pack()

# Draw the game board squares
# You can define the coordinates for each square based on your desired layout
square_width = 100
x_start = 50
y_start = 50

# Define the properties and their coordinates
properties = [
    {"name": "Mediterranean\nAvenue", "color": "brown", "x": 50, "y": 550},
    {"name": "Baltic\nAvenue", "color": "brown", "x": 50, "y": 465},
    {"name": "Oriental\nAvenue", "color": "light blue", "x": 220, "y": 550},
    {"name": "Vermont\nAvenue", "color": "light blue", "x": 305, "y": 550},
    {"name": "Connecticut\nvAvenue", "color": "light blue", "x": 390, "y": 550},
    {"name": "St. Charles\nPlace", "color": "pink", "x": 475, "y": 550},
    {"name": "States\nAvenue", "color": "pink", "x": 560, "y": 550},
    {"name": "Virginia\nAvenue", "color": "pink", "x": 645, "y": 550},
    {"name": "St. James\nPlace", "color": "orange", "x": 730, "y": 550},
    {"name": "Tennessee\nAvenue", "color": "orange", "x": 815, "y": 550},
    {"name": "New York\nAvenue", "color": "orange", "x": 900, "y": 550},
    {"name": "Kentucky\nAvenue", "color": "red", "x": 985, "y": 550},
    {"name": "Indiana\nAvenue", "color": "red", "x": 1070, "y": 550},
    # Define the other properties in a similar manner
]

# Draw the properties on the game board
square_width = 85

for prop in properties:
    x = prop["x"]
    y = prop["y"]
    color = prop["color"]

    canvas.create_rectangle(x, y, x + square_width, y + square_width, fill=color)
    canvas.create_text(x + square_width/2, y + square_width/2, text=prop["name"])

# Draw other game elements such as railroads and utilities
# You can define their coordinates and use appropriate shapes or icons

# Draw other game board elements (e.g., railroads, utilities, special spaces)

# Start the game loop
window.mainloop()