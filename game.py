# Welcome message and introduction to the game
print("Welcom to the Adventure Game!")
print("Your journey begins here...", '\n')

# Ask for the player's name
player_name = input("What is your name, adventurer? ")

# Concatenate string to create a personalized welcome message
print("Welcome, " + player_name + "! Your journey beings now.", '\n')

# Use an f-string to display the same message in a more readable format
print(f"Welcome, {player_name}! Your journey beings now.", '\n')

# Describe the starting area of the game
starting_area = """
You find yourself in a small village surrounded by dense forests.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

