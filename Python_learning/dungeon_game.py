import random


def combat(enemy_name, enemy_min_damage, enemy_max_damage,player_min_damage, player_max_damage):
    """Runs a combat encounter. Returns remaining health."""
    global player_health
    enemy_alive = True


    print(f"\nA wild {enemy_name} attacks!")


    while enemy_alive:
        print(f"\nYour health: {player_health}")
        print(f"What do you do against the {enemy_name}")
        print("1. Fight")
        print("2. Run away")


        action = input("Choose 1 or 2: ")


        if action == "1":
            player_damage = random.randint(player_min_damage, player_max_damage)
            enemy_damage = random.randint(enemy_min_damage, enemy_max_damage)


            print(f"\nYou strike the {enemy_name} for {player_damage} damage!")
            print(f"The {enemy_name} hits you back for {enemy_damage} damage.")


            player_health = player_health - enemy_damage
            enemy_alive = False


        elif action == "2":
            escape_damage = random.randint(enemy_min_damage, enemy_max_damage)


            print(f"\nYou turn and run! The {enemy_name} hits you for {escape_damage} damage!")
            player_health = player_health - escape_damage
            enemy_alive = False


        else:
            hesitate_damage = random.randint(enemy_min_damage + 5, enemy_max_damage + 5)


            print(f"\nYou hesitate! The {enemy_name} strikes for {hesitate_damage} damage!")
            player_health = player_health - hesitate_damage


        return player_health




# Dungeon Adventure Game
# Lesson 2 - Health, Inventory, and Multiple Rooms

# Player_name, player_health, inventory variables
player_name = input("What is your name, adventurer? ")
player_health = 100
inventory = []


print(f"\nWelcome, {player_name}!")
print(f"Health: {player_health}")
print(f"Inventory: {inventory}")

# --- Room 1: The Entrance ---
print("\n=== THE ENTRANCE HALL ===")
print("Torches flicker on the stone walls.")
print("On the floor, you see a rusty sword and a bread roll.")


# add items to inventory using .append()
inventory.append("rusty sword")
inventory.append("bread roll")

# Random bonus loot! 40% chance of finding gold.
loot_chance = random.randint(1,100)


if loot_chance <= 40:
    gold_amount = random.randint(1,20)
    inventory.append(f"{gold_amount} gold coins")
    print(f"\nLucky! You also spot {gold_amount} gold coins under a loose stone.")
else:
    print("\nYou searched around but find nothing else.")


print(f"\nYou pick up the items!")
print(f"Inventory: {inventory}")
print(f"You have {len(inventory)} items.")

# --- Room 1.5: The Healing Fountain ---
print("\n=== THE FOUNTAIN CHAMBER ===")
print("A glowing fountain sparkles in the center of the room.")
print("The water looks magical.")


print("\nDo you drink from the fountain?")
print("1. Drink deeply")
print("2. Just a sip")
print("3. Skip it - could be poisoned")


fountain_choice = input("Choose 1,2, or 3")

if fountain_choice == "1":
    heal_amount = random.randint(20,40)
    player_health= player_health + heal_amount
    print(f"\nYou drink deeply. The magic water restores {heal_amount} health!")
    print(f"Your health is now {player_health}.")

elif fountain_choice == "2":
    heal_amount = random.randint(5, 15)
    player_health = player_health + heal_amount
    print(f"\nYou take a cautious sip. You recover {heal_amount} health.")
    print(f"Your health is now {player_health}.")

elif fountain_choice == "3":
    print("\nYou ignore the fountain and move on.")
    print("Probably wise — this is a dungeon after all.")

else:
    print("\nYou stare at the fountain, confused.")
    print("A random splash hits your face. Nothing happens.")

# --- STATUS UPDATE ---
print("\n--- Current Status ---")
print(f"Health: {player_health}")
print(f"Inventory: {inventory}")
print("-" * 25) # Prints 25 dashes as a divider

# ---ROOM 2: The Guard Post ---
print("\n=== THE GUARD POST ===")
print("A sleepy goblin guard block the path.")
print("He wakes up and attacks")


combat("goblin", 5, 15, 15, 30)
inventory.append("goblin ear")
print("The goblin falls! You collect a goblin ear.")


# --- Room 3: The Dragon's Lair ---
print("\n=== THE DRAGON'S LAIR ===")
print("The tunnel opens into a massive cavern.")
print("Gold coins litter the floor.")
print("A dragon sleeps on a mountain of treasure.")
print("\nThe dragon wakes up.")


combat("dragon", 15, 35, 20, 40)


if player_health <= 0:
    print("\nThe dragon's fire consumes you.")
else:
    print("\nYou defeated the dragon!")
    print("You grab as much treasure as you can carry!")
    dragon_gold = random.randint(50, 100)
    inventory.append(f"{dragon_gold} gold coins")
    print(f"You collect {dragon_gold} gold coins.")


# --- AFTER THE FIGHT ---
print("\n" + "=" * 40)
print("===  ADVENTURE COMPLETE ===")
print("=" * 40)


if player_health <= 0:
    print("You have fallen in the dungeon...")
    print("GAME OVER!")
else:
    # Count total items
    total_items = len(inventory)


    # Count gold from inventory
    total_gold = 0
    for item in inventory:
        if "gold" in item:
            # Extract the number from strings like "50 gold coins"
            gold_amount = item.split()[0]
            total_gold = total_gold + int(gold_amount)

    print(f"You surived, {player_health}!")
    print(f"Health remaining: {player_health}")
    print(f"Items collected: {total_items}")
    print(f"Total gold: {total_gold}")
    print(f"Full Inventory: {inventory}")
    print("\nVICTORY! Your name will be remembered!")

