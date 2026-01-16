# Welcome message and introduction to the game
print("Welcom to the Adventure Game!")
print("Your journey begins here...", '\n')

# Ask for the player's name
player_name = input("What is your name, adventurer? ").strip()

# Concatenate string to create a personalized welcome message
# print("Welcome, " + player_name + "! Your journey beings now.")

# Use an f-string to display the same message in a more readable format
print(f"Welcome, {player_name}! Your journey beings now.")

# Describe the starting area of the game
starting_area = """
You find yourself in a small village surrounded by dense forests.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): "). lower() .strip()

# Respond based on the player's decision
if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.")
elif decision != "yes" and decision != "no":
    print("Confused, you stand still, unsure of what to do.")
    continue_decision = input("Do you want to take the path now? (yes or no): ").lower().strip()
    if continue_decision == "yes":
        print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
    elif continue_decision == "no":
        print(player_name + ", you decide to wait. Perhaps courage will find you later.")
    else:
        print("You stay in the forest and are forgotten by time.")

