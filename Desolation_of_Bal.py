import random

# Base class for Items
class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def apply(self, dante):
        pass

# Tonic class that adds 2 to the dante's health when applied
class Tonic(Item):
    def __init__(self):
        super().__init__("Tonic", 10)

    def apply(self, dante):
        dante.health += 2
        print(f"The {dante.__class__.__name__} uses the Tonic and gains 2 health! Health is now {dante.health}\n")

# Sword class that adds 2 to the dante's power when applied
class Sword(Item):
    def __init__(self):
        super().__init__("Sword", 20)

    def apply(self, dante):
        dante.power += 2
        print(f"The {dante.__class__.__name__} wields the Sword and gains 2 power! Power is now {dante.power}\n")


# Store class
class Store:
    items = [Tonic(), Sword()]  # Store items: Tonic and Sword

    def do_shopping(self, dante):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f"You have {dante.coins} coins.")
            print("What do you want to buy?")

            for i, item in enumerate(Store.items):
                print(f"{i + 1}. {item.name} ({item.cost} coins)")
            print("9. Leave the store")

            user_input = int(input("> "))

            if user_input == 9:
                print("Thanks for visiting the store!")
                break
            elif 1 <= user_input <= len(Store.items):
                item_to_buy = Store.items[user_input - 1]

                if dante.coins >= item_to_buy.cost:
                    dante.buy(item_to_buy)
                else:
                    print("Sorry, you don't have enough coins to buy that item.")
            else:
                print("Invalid input, please try again.")


# Create class Character that the classes of dante and Goblin will pull from
class Character:
    def __init__(self, health, power, bounty=0):
        self.health = health
        self.power = power
        self.bounty = bounty

# If the character's health is greater than 0, it will return True to being alive.
    def alive(self):
        return self.health > 0
    
# Whenever a character (which is assigned to dante and Goblin) attacks an enemy, it will print who attacked who and then give back a value of the enemies health
    def attack(self, enemy):
        if enemy.alive():
         damage = self.power
         enemy.health = max(0, enemy.health - damage)  # Prevent health from going negative
         print(f"The {self.__class__.__name__} attacks the {enemy.__class__.__name__}!")
         print(f"The {enemy.__class__.__name__}'s health is now {enemy.health}")
         if not enemy.alive():
            print(f"The {enemy.__class__.__name__} has been defeated!\n")
        else:
            print(f"The {enemy.__class__.__name__} has already been defeated\n")

    def take_damage(self, damage):
        self.health -= damage


# Add a coins attribute to the Character class. Have it default to a value of 20
    def coins(self, coins = 20):
        self.coins = 20


# Classes of dante
class Dante(Character):
    def __init__(self, health, power, coins =20):
        super().__init__(health, power, bounty =0)
        self.coins = coins ## Initialize dante with some starting coins
    def print_status(self):
        if self.alive():
         print (f"Dante has {self.health} health and {self.power} power.\n")
        else:
         print ("GAME OVER\n")

# Make the dante generate double damage points during an attack with a probability of 20%. If random number is less than .2, it will do a default attack.   
    def attack(self, enemy):
        if random.random() < 0.2:
            double_damage = self.power * 2
            enemy.health -= double_damage
            print(f"The {self.__class__.__name__} musters all of his strength and strikes with double damage!")
            print(f"The {enemy.__class__.__name__} takes {double_damage} damage!")
        else:
            super().attack(enemy)

        # Check if enemy is defeated, if so it will reward the bounty
        if not enemy.alive():
            print(f"You defeated the {enemy.__class__.__name__} and earned {enemy.bounty} coins! Visit the Store to spend.\n")
            self.coins += enemy.bounty  # Add bounty to dante's coins
            print(f"You now have {self.coins} coins.\n")


# Add a buy method to the dante class so that dante objects can purchase items from a  virtual store
# Give the method an item parameter. The item being purchased will be passed as an arguement into the method.
# It should subtract an items cost from the dante object's avaiable coins
    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)
        

# Class of Goblin
class Goblin(Character):
    def __init__(self, health, power, bounty =5):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
            print (f"The Goblin has {self.health} health and {self.power} power\n")
        

# Class of Shadow 
class Shadow(Character):
    def __init__(self, health, power, bounty =6):
        super().__init__(health, power, bounty)

    def print_status(self):
        print (f"The Shadow has {self.health} health and {self.power} power\n")

# Only 1 starting health but will only take damage about once out of every ten etimes he is attacked.
    def take_damage(self, amount):
        if random.random() < 0.5:
            self.health -= amount
            print(f"The Shadow takes {amount} of damage!\n")
        else:
         print("The Shadow dodged your attack!\n")


# Class of Zombie
class Zombie(Character):
    def __init__(self, health, power, bounty =20):
        super().__init__(health, power, bounty)

    def print_status(self):
        print (f"The Zombie has {self.health} health and {self.power} power\n")

# Make the Zombie class not die if it's health reaches zero
    def alive(self):
        return True


# Class of Archer
class Archer(Character):
    def __init__(self, health, power, bounty =10):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
         print (f"The Archer has {self.health} health and {self.power} power\n")


# Class of Wizard
class Wizard(Character):
    def __init__(self, health, power, bounty =15):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
         print (f"The Wizard has {self.health} health and {self.power} power\n")

# values Characters Health and Power
dante = Dante(100, 10)
goblin = Goblin(55, 8, 5)
shadow = Shadow(15, 5, 6)
zombie= Zombie(10, 7, 20)
archer = Archer(25, 6, 10)
wizard = Wizard(35, 15, 15)

store = Store()  # Create a Store object


def display_opening_screen():
    print("\n\n\n▓█████▄ ▓█████   ██████  ▒█████   ██▓    ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █     ▒█████    █████▒    ▄▄▄▄    ▄▄▄       ██▓    ")
    print("▒██▀ ██▌▓█   ▀ ▒██    ▒ ▒██▒  ██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █    ▒██▒  ██▒▓██   ▒    ▓█████▄ ▒████▄    ▓██▒    ")
    print("░██   █▌▒███   ░ ▓██▄   ▒██░  ██▒▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒   ▒██░  ██▒▒████ ░    ▒██▒ ▄██▒██  ▀█▄  ▒██░    ")
    print("░▓█▄   ▌▒▓█  ▄   ▒   ██▒▒██   ██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒   ▒██   ██░░▓█▒  ░    ▒██░█▀  ░██▄▄▄▄██ ▒██░    ")
    print("░▒████▓ ░▒████▒▒██████▒▒░ ████▓▒░░██████▒▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░   ░ ████▓▒░░▒█░       ░▓█  ▀█▓ ▓█   ▓██▒░██████▒")
    print(" ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ▒░▒░▒░  ▒ ░       ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░")
    print(" ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░     ░ ▒ ▒░  ░         ▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░")
    print(" ░ ░  ░    ░   ░  ░  ░  ░ ░ ░ ▒    ░ ░    ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░    ░ ░ ░ ▒   ░ ░        ░    ░   ░   ▒     ░ ░   ")
    print("   ░       ░  ░      ░      ░ ░      ░  ░     ░  ░         ░      ░ ░           ░        ░ ░              ░            ░  ░    ░  ░")
    print(" ░                                                                                                             ░                    \n\n\n")

# Call the function to display the opening screen before game starts
display_opening_screen()

import textwrap

def game_story_intro():
    story = """
The galaxy is torn asunder by the devastating events of the Cicatrix Maledictum, the great warp storm that has plunged the Imperium into a new era of darkness. Amidst the chaos, the Blood Angels, led by their indomitable Chapter Master, Commander Dante, stand as the last line of defense for their homeworld, Baal. For centuries, the Blood Angels have guarded the sands of their irradiated world, their noble gene-seed cursed by the thirst for blood and the madness of the Black Rage.

Now, an enemy unlike any they have ever faced descends upon them. The Great Devourer, the relentless Hive Fleet Leviathan, has come to consume Baal and all that remains of its defenders. Millions of bioforms churn through the void, a tide of hunger that seeks to strip the planet of all life. The Blood Angels, supported by their successor chapters, brace for an apocalyptic last stand, knowing that should they fall, not only will Baal be lost, but the legacy of their Primarch, Sanguinius, may be extinguished forever.

As war breaks out, Dante prepares for the fight of his long and storied life, while far above, the enigmatic forces of the Imperium's most secretive orders stir, bearing strange tidings that may either doom Baal or grant the Blood Angels a fleeting chance at salvation. The stage is set for a battle of unimaginable scale, as ancient warriors clash against the primal hunger of the Tyranids, and Dante's eternal duty to his chapter and to the Emperor hangs in the balance...
    """

    # Split the story into paragraphs based on the double newlines
    paragraphs = story.strip().split("\n\n")
    
    # Use textwrap.fill to wrap each paragraph individually, adding extra newline between each
    wrapped_paragraphs = [textwrap.fill(paragraph, width=100) for paragraph in paragraphs]
    
    # Join paragraphs with an additional newline (for spacing between them)
    formatted_story = "\n\n".join(wrapped_paragraphs)
    
    # Print the formatted story with spacing between paragraphs
    print(formatted_story)


# Call the function to display the story
game_story_intro()

# This will check if the characters are alive, and if they are, it  will print their status
while dante.alive():
    print()
    dante.print_status()
    if goblin.alive():
        goblin.print_status()
    else:
        print("The puny Goblin was no match for you\n")
    if shadow.alive():
        shadow.print_status()
    else:
        print("The Shadow could not escape your fury\n")
    if zombie.alive():
        zombie.print_status()
    else:
        print("You just broke the game! WOO HOO!\n")
    if archer.alive():
        archer.print_status()
    else:
        print("You hit the archer from HOW FAR?!\n")
    if wizard.alive():
        wizard.print_status()
    else:
        print("Cordless Hole Punchers don't care about no spells son!\n")
    print()

 # User Choices 
    print("What do you want to do?\n")
    print("1. Fight Goblin")
    print("2. Fight the Shadow")
    print("3. Fight the Zombie")
    print("4. Fight the Archer")
    print("5. Fight the Wizard")
    print("6. Do Nothing")
    print("7. Flee")
    print("8. Visit the Store")  # Added option to visit the store
    print("> ", end="")
     
     
    user_input = input()
    print()
    if user_input == "1":
        if goblin.alive():
            dante.attack(goblin)
            if goblin.alive():
                goblin.attack(dante)
        else:
            print(f"The {goblin.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "2":
        if shadow.alive():
            dante.attack(shadow)
            if shadow.alive():
                shadow.attack(dante)
        else:
            print(f"The {shadow.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "3":
        if zombie.alive():
            dante.attack(zombie)
            if zombie.alive():
                zombie.attack(dante)
        else:
            print(f"The {zombie.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "4":
        if archer.alive():
            dante.attack(archer)
            if archer.alive():
                archer.attack(dante)
        else:
            print(f"The {archer.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "5":
        if wizard.alive():
            dante.attack(wizard)
            if wizard.alive():
                wizard.attack(dante)
        else:
            print(f"The {wizard.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "6":
        print("He's just standing there... MENACINGLY!\n")
        if goblin.alive(): goblin.attack(dante)
        if shadow.alive(): shadow.attack(dante)
        if zombie.alive(): zombie.attack(dante)
        if archer.alive(): archer.attack(dante)
        if wizard.alive(): wizard.attack(dante)
        if not dante.alive(): print("Oh no, The dante has died! Better luck next time! GAME OVER\n")
        break
    elif user_input == "7":
        print("Throwing in the towel huh? I knew you couldn't handle it!\n")
        break
    elif user_input == "8":
        store.do_shopping(dante)  # Option to visit the store
    else:
        print(f"Uh Oh! Looks like you entered {user_input} instead of a selectable option. Try again!\n")
     
    # Check if the dante has died
    if not dante.alive():
        print("Oh no, The dante has died! Better luck next time! GAME OVER\n")
        break