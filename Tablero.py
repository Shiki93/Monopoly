"El tablero del monopoly"

import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Monopoly")
window.geometry("1920x1080")


# Create a canvas to draw the game board
canvas = tk.Canvas(window, width=1920, height=1080, bg="light green")
canvas.pack()

# Define the properties and their coordinates
properties = [
    {"name": "GO", "color": "grey", "x": 50, "y": 700},
    {"name": "Mediterranean\nAvenue", "color": "brown", "x": 50, "y": 635},
    {"name": "Community\nChess", "color": "magenta", "x": 50, "y": 570},
    {"name": "Baltic\nAvenue", "color": "brown", "x": 50, "y": 505},
    {"name": "Tax Over\nIncome", "color": "grey", "x": 50, "y": 440},
    {"name": "Oriental\nAvenue", "color": "light blue", "x": 50, "y": 310},
    {"name": "Chance", "color": "magenta", "x": 50, "y": 245},
    {"name": "Vermont\nAvenue", "color": "light blue", "x": 50, "y": 180},
    {"name": "Connecticut\nAvenue", "color": "light blue", "x": 50, "y": 115},
    {"name": "Jail", "color": "grey", "x": 50, "y": 50},
    {"name": "St. Charles\nPlace", "color": "pink", "x": 115, "y": 50},
    {"name": "Electric\nCompany", "color": "purple", "x": 180, "y": 50},
    {"name": "States\nAvenue", "color": "pink", "x": 245, "y": 50},
    {"name": "Virginia\nAvenue", "color": "pink", "x": 310, "y": 50},
    {"name": "St. James\nPlace", "color": "orange", "x": 440, "y": 50},
    {"name": "Community\nChess", "color": "magenta", "x": 505, "y": 50},
    {"name": "Tennessee\nAvenue", "color": "orange", "x": 570, "y": 50},
    {"name": "New York\nAvenue", "color": "orange", "x": 635, "y": 50},
    {"name": "Parking", "color": "grey", "x": 700, "y": 50},
    {"name": "Kentucky\nAvenue", "color": "red", "x": 700, "y": 115},
    {"name": "Chance", "color": "magenta", "x": 700, "y": 180},
    {"name": "Indiana\nAvenue", "color": "red", "x": 700, "y": 245},
    {"name": "Illinois\nAvenue", "color": "red", "x": 700, "y": 310},
    {"name": "Atlantic\nAvenue", "color": "yellow", "x": 700, "y": 440},
    {"name": "Ventnor\nAvenue", "color": "yellow", "x": 700, "y": 505},
    {"name": "Water\nWorks", "color": "purple", "x": 700, "y": 570},
    {"name": "Marvin\nGardens", "color": "yellow", "x": 700, "y": 635},
    {"name": "Go to Jail", "color": "grey", "x": 700, "y": 700},
    {"name": "Pacific\nAvenue", "color": "green", "x": 635, "y": 700},
    {"name": "North Carolina\nAvenue", "color": "green", "x": 570, "y": 700},
    {"name": "Community\nChess", "color": "magenta", "x": 505, "y": 700},
    {"name": "Pennsylvania\nAvenue", "color": "green", "x": 440, "y": 700},
    {"name": "Chance", "color": "magenta", "x": 310, "y": 700},
    {"name": "Park\nPlace", "color": "dark blue", "x": 245, "y": 700},
    {"name": "Tax Over\nLuxury", "color": "grey", "x": 180, "y": 700},
    {"name": "Boardwalk", "color": "dark blue", "x": 115, "y": 700},
]

# Define the railroads and their coordinates
railroads = [
    {"name": "Reading\nRailroad", "color": "light grey", "x": 50, "y": 375},
    {"name": "Pennsylvania\nRailroad", "color": "light grey", "x": 375, "y": 50},
    {"name": "B. & O.\nRailroad", "color": "light grey", "x": 700, "y": 375},
    {"name": "Short\nLine", "color": "light grey", "x": 375, "y": 700},
]

# Load dice images
dice_images = [
    tk.PhotoImage(file="Imagenes\dice1.png"),
    tk.PhotoImage(file="Imagenes\dice2.png"),
    tk.PhotoImage(file="Imagenes\dice3.png"),
    tk.PhotoImage(file="Imagenes\dice4.png"),
    tk.PhotoImage(file="Imagenes\dice5.png"),
    tk.PhotoImage(file="Imagenes\dice6.png"),
]

player_token_image = tk.PhotoImage(file="Imagenes/token1.png")

# Draw the properties on the game board
square_width = 65
text_font = ("Arial", 8)

for prop in properties:
    x = prop["x"]
    y = prop["y"]
    color = prop["color"]
    canvas.create_rectangle(x, y, x + square_width, y + square_width, fill=color)
    canvas.create_text(x + square_width / 2, y + square_width / 2, text=prop["name"], font=text_font, anchor="center")

for rr in railroads:
    x = rr["x"]
    y = rr["y"]
    color = rr["color"]
    canvas.create_rectangle(x, y, x + square_width, y + square_width, fill=color)
    canvas.create_text(x + square_width / 2, y + square_width / 2, text=rr["name"], font=text_font, anchor="center")

# Function to roll the dice and show the result
def roll_dice():
    # Simulate rolling the dice and getting the results
    dice_result1 = random.randint(1, 6)
    dice_result2 = random.randint(1, 6)
    canvas.delete("dice")
    canvas.create_image(820, 150, image=dice_images[dice_result1 - 1], tags="dice")
    canvas.create_image(880, 150, image=dice_images[dice_result2 - 1], tags="dice")
    move_player_token(dice_result1 + dice_result2)

# Function to move the player token
def move_player_token(steps):
    # Get the current position of the player token
    x, y = canvas.coords(player_token)

    # Calculate the new position after moving the given number of steps
    new_x = x + steps * square_width

    # Check if the new position is beyond the board boundaries
    if new_x >= 1920:
        # Player token reached or passed the end of the board, move it back to the start
        new_x = player_start_x
        y = player_start_y
    elif new_x >= 700 and y == player_start_y:
        # Player token reached the end row, move it to the next row
        new_x = 700
        y -= square_width

    # Move the player token to the new position
    canvas.coords(player_token, new_x, y)

roll_button = tk.Button(canvas, text="Roll Dice", command=roll_dice)
canvas.create_window(820, 100, window=roll_button)

# Create the player token on the board
player_start_x = 80  # Initial X position of the player token
player_start_y = 730  # Initial Y position of the player token
player_token = canvas.create_image(player_start_x, player_start_y, image=player_token_image)


# Start the game loop
window.mainloop()