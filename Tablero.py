"El tablero del monopoly"

import tkinter as tk

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
    {"name": "Electric\nCompany", "color": "grey", "x": 180, "y": 50},
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
    {"name": "Atlantic\nAvenue", "color": "yellow", "x": 700, "y": 375},
    {"name": "Ventnor\nAvenue", "color": "yellow", "x": 700, "y": 505},
    {"name": "Water\nWorks", "color": "grey", "x": 700, "y": 570},
    {"name": "Marvin\nGardens", "color": "yellow", "x": 700, "y": 635},
    {"name": "Go to Jail", "color": "grey", "x": 700, "y": 700},
    {"name": "Pacific\nAvenue", "color": "green", "x": 500, "y": 765},
    {"name": "North Carolina\nAvenue", "color": "green", "x": 450, "y": 700},
    {"name": "Community\nChess", "color": "magenta", "x": 400, "y": 700},
    {"name": "Pennsylvania\nAvenue", "color": "green", "x": 350, "y": 700},
    {"name": "Chance", "color": "magenta", "x": 250, "y": 700},
    {"name": "Park\nPlace", "color": "dark blue", "x": 200, "y": 700},
    {"name": "Tax Over\nLuxury", "color": "grey", "x": 150, "y": 700},
    {"name": "Boardwalk", "color": "dark blue", "x": 100, "y": 700},
]

# Define the railroads and their coordinates
railroads = [
    {"name": "Reading\nRailroad", "color": "black", "x": 50, "y": 375},
    {"name": "Pennsylvania\nRailroad", "color": "black", "x": 375, "y": 50},
    {"name": "B. & O.\nRailroad", "color": "black", "x": 700, "y": 440},
    {"name": "Short\nLine", "color": "black", "x": 300, "y": 700},
]

# Draw the properties on the game board
square_width = 65

for prop in properties:
    x = prop["x"]
    y = prop["y"]
    color = prop["color"]

    canvas.create_rectangle(x, y, x + square_width, y + square_width, fill=color)

for rr in railroads:
    x = rr["x"]
    y = rr["y"]
    color = rr["color"]

    canvas.create_rectangle(x, y, x + square_width, y + square_width, fill=color)

# Draw other game elements such as railroads and utilities
# You can define their coordinates and use appropriate shapes or icons

# Draw other game board elements (e.g., railroads, utilities, special spaces)

# Start the game loop
window.mainloop()