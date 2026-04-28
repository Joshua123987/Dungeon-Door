print("=== THE DUNGEON OF DOOM ===")


# Ask the player for their name
player_name = input("What is your name, brave soul?")


# Ask the player to choose a number
print(f"\nWelcome, {player_name}!")
print("You stand before two doors.")
print("Door 1 is made of iron. Door 2 is made of wood.")


# Ask player to choose a door
choice = input("Which door do you choose? (1 or 2):")
# Check which door was chosen
if choice == "1":
    print("\nYou push open the heavy iron door...")
    print("Inside you find a treasure chest!")
    print("You gain 50 gold.")
elif choice == "2":
    print("\nYou push open the creaky wooden door...")
    print("A goblin jumps out and attacks you!")
    print("You lose 20 health.")
else:
    print("\nYou stand there doing nothing")
    print("The dungeon collapses around you!.")
