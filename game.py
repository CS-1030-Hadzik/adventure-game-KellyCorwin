# Welcome message and introduction to the game
print("Welcom to this CS 1030 Adventure Game!")
print("If you aren't a filthy milk-drinker and are stout of hear, please proceed...", '\n')

# Ask for the player's name
player_name = input("What is your name, adventurer? ").strip() # Remove any leading or trailing whitespace from the player's input

# Use an f-string to display the same message in a more readable format
print(f"Welcome, {player_name}! You look lactose intolerant. Your journey beings now.")

# Describe the starting area of the game
starting_area = """
You find yourself in a small village, ...like really small, surrounded by dense, dark forests.
The sound of rustling leaves fills the air, and a faint tinge of putrifaction compells you to think "...I must away...".
Ahead lies a path trampled by little, dainty feet. Where it leads you know not, but forward you tread nonetheless...
"""
print(starting_area)

# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): ").lower().strip() # Convert the player's input to lowercase and remove whitespace

# Respond based on the player's decision
if decision == "yes":
    print(f"A brave choice, {player_name}! You are stalwart as ever. You step onto the path and venture into the unkown.")
elif decision == "no":
    print("""You think to yourself, "Perhaps the town harlots are missing me after all...". You turn and head back pondering your life choices.""")
elif decision != "yes" and decision != "no":
    print("Easily distracted by your undiagnosed medieval ADHD you stand there, unsure what to do next.")

    continue_decision = input("You look back to the path, are you ready do go now? (yes or no): ").lower().strip()

    if continue_decision == "yes":
        print(f"A brave choice, {player_name}! You are stalwart as ever. You step onto the path and venture into the unkown.")
    elif continue_decision == "no":
        print("""You think to yourself, "Perhaps the town harlots are missing me after all...". You turn and head back pondering your life choices.""")
    else:
        print("Unable to make a decision you stand there forever, your name forgotten by time.")

