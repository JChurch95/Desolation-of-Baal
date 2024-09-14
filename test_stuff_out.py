import random

# Base class for Items
class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def apply(self, Blood_Angels):
        pass

# Tonic class that adds 2 to the Blood_Angels's ranks when applied
class Tonic(Item):
    def __init__(self):
        super().__init__("Tonic", 10)

    def apply(self, Blood_Angels):
        Blood_Angels.ranks += 2
        print(f") The {Blood_Angels.__class__.__name__} uses the Tonic and gains 2 ranks! ranks is now {Blood_Angels.ranks}\n")

# Sword class that adds 2 to the Blood_Angels's power when applied
class Sword(Item):
    def __init__(self):
        super().__init__("Sword", 20)

    def apply(self, Blood_Angels):
        Blood_Angels.power += 2
        print(f") The {Blood_Angels.__class__.__name__} wields the Sword and gains 2 power! power is now {Blood_Angels.power}\n")


# armour_hall class
class Armour_hall:
    items = [Tonic(), Sword()]  # armour_hall items: Tonic and Sword

    def do_shopping(self, Blood_Angels):
        while True:
            print("=====================")
            print("The Magos awaits your command")
            print("=====================")
            print(f"You have {Blood_Angels.coins} Xeno Skulls.")
            print("Which unit best suits your plans brother?")

            for i, item in enumerate(armour_hall.items):
                print(f"{i + 1}. {item.name} ({item.cost} skulls)")
            print("9. Go back to crush more Xeno Skulls")

            user_input = int(input("> "))

            if user_input == 3:
                print("Hold the line brothers! Sanguinius is watching over us!")
                break
            elif 1 <= user_input <= len(armour_hall.items):
                item_to_buy = armour_hall.items[user_input - 1]

                if Blood_Angels.coins >= item_to_buy.cost:
                    Blood_Angels.buy(item_to_buy)
                else:
                    print("I'm sorry Brother, you don't have enough Xeno Skulls to buy that item.")
            else:
                print("Consulting the Codex Astartes to figure out what you require...")


class Space_Marines:
    def __init__(self, ranks, power, xeno_skulls=0):
        self.ranks = ranks
        self.power = power
        self.xeno_skulls = xeno_skulls
        self.coins = 20  # Default coins value

    def alive(self):
        return self.ranks > 0

    def attack(self, enemy):
        if enemy.alive():
            damage = self.power
            print(f") The {self.__class__.__name__} attack the {enemy.__class__.__name__} with righteous fury!\n")
            
            if hasattr(enemy, 'take_damage'):
                damage_taken = enemy.take_damage(damage)
                if not damage_taken:
                    return  # If the enemy dodged, skip the rest of the logic
            else:
                enemy.ranks = max(0, enemy.ranks - damage)  # Prevent ranks from going negative
            
            print(f"The {enemy.__class__.__name__}'s ranks is now {enemy.ranks}")
            
            if not enemy.alive():
                print(f"The {enemy.__class__.__name__} has been defeated!\n")
        else:
            print(f"The {enemy.__class__.__name__} has already been defeated\n")

    def take_damage(self, damage):
        self.ranks -= damage

# Classes of Blood_Angels
class Blood_Angels(Space_Marines):
    def __init__(self, ranks, power, coins =20):
        super().__init__(ranks, power, xeno_skulls =0)
        self.coins = coins ## Initialize Blood_Angels with some starting coins
        

    def print_status(self):
        if self.alive():
         print (f"The Blood_Angels have {self.ranks} Space Marines left in their Chapter. Hold fast!\n")
        else:
         print ("Even though they stood valiantly against the Xeno horde, The Blood Angels could not hold back the Tyranid Fleet. Baal is lost!\n")

# Make the Blood_Angels generate double damage points during an attack with a probability of 20%.
    def attack(self, enemy):
        if random.random() < 0.2:
            double_damage = self.power * 2
            enemy.hive_fleet -= double_damage
            print(f") The {self.__class__.__name__} give into the Black Rage...\n")
            print(f") They slaughter {double_damage} of the {enemy.__class__.__name__}!\n\n")
        else:
            super().attack(enemy)

        # Check if the enemy is defeated, if so it will reward the xeno_skulls
        if not enemy.alive():
            print(f"You defeated the {enemy.__class__.__name__} and earned {enemy.xeno_skulls} Xeno Skulls! Visit the Armouring Hall to recruit more units.\n")
            self.coins += enemy.xeno_skulls  # Add xeno_skulls to Blood_Angels's coins
            print(f"You now have {self.coins} Xeno Skulls.\n")
        
        # After attacking, print Blood_Angels's status
        self.print_status()

    # Buy method to allow Blood_Angels objects to purchase items from the virtual armour_hall
    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

        
class Tyranids:
    def __init__(self, hive_fleet, xeno_skulls=0):
        self.hive_fleet = hive_fleet
        self.xeno_skulls = xeno_skulls

    def alive(self):
        return self.hive_fleet > 0

    def attack(self, enemy):
        if enemy.alive():
            damage = self.hive_fleet
            print(f") The {self.__class__.__name__} charges the {enemy.__class__.__name__}!")
            
            if hasattr(enemy, 'take_damage'):
                damage_taken = enemy.take_damage(damage)
                if not damage_taken:
                    return  # If the enemy dodged, skip the rest of the logic
            else:
                enemy.ranks = max(0, enemy.ranks - damage)  # Prevent ranks from going negative
            
            print(f"The {enemy.__class__.__name__} power numbers are down to{enemy.ranks}")

    def take_damage(self, damage):
        self.hive_fleet -= damage


# Class of Gaunts
class Gaunts(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=5):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print (f"The Gaunts have {self.hive_fleet} bioforms left in their swarm... Plan your next step before they regroup!\n")

# Class of Warriors
class Warriors(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=6):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print (f"The Xeno filth have {self.hive_fleet} Warrior class Xenos left in their swarm... Wait for an opening when they swing their sword\n")
        
 
# Class of Ravener
class Ravener(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=10):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print (f"The Hive Fleet have {self.hive_fleet} Raveners left in their swarm... Feel for tremors before they attack.\n")

# Class of Lictor
class Lictor(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=20):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print (f"The Xeno filth have {self.hive_fleet} Lictors left in their swarm... Beware their adaptive camoflouge\n")
# Only take damage 20% of the time
    def take_damage(self, amount):
        if random.random() < 0.2:
            self.ranks -= amount
            print(f") You killed {amount} Lictors!\n")
            return True  # Return True if damage was taken
        else:
            print(") The Lictor activated their active camoflouge! They have escaped for now...\n")
            return False  # Return False if the attack was dodged
        
# Class of Carnifex
class Carnifex(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=10):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print (f"The Tyranid swarm have {self.hive_fleet} Carnifex left in their swarm... You will need sound planning to make it out alive.\n")

# Class of Hive Tyrant
class Hive_Tyrant(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=15):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print (f"The  have {self.hive_fleet} Carnifex left in their swarm... You will need sound planning to make it out alive.\n")


armour_hall = Armour_hall()  # Create a armour_hall object


def title_screen():
    print("\n\n\n▓█████▄ ▓█████   ██████  ▒█████   ██▓    ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █     ▒█████    █████▒    ▄▄▄▄    ▄▄▄      ▄▄▄       ██▓    ")
    print("▒██▀ ██▌▓█   ▀ ▒██    ▒ ▒██▒  ██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █    ▒██▒  ██▒▓██   ▒    ▓█████▄ ▒████▄   ▒████▄    ▓██▒    ")
    print("░██   █▌▒███   ░ ▓██▄   ▒██░  ██▒▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒   ▒██░  ██▒▒████ ░    ▒██▒ ▄██▒██  ▀█▄ ▒██  ▀█▄  ▒██░    ")
    print("░▓█▄   ▌▒▓█  ▄   ▒   ██▒▒██   ██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒   ▒██   ██░░▓█▒  ░    ▒██░█▀  ░██▄▄▄▄██░██▄▄▄▄██ ▒██░    ")
    print("░▒████▓ ░▒████▒▒██████▒▒░ ████▓▒░░██████▒▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░   ░ ████▓▒░░▒█░       ░▓█  ▀█▓ ▓█   ▓██▒▓█   ▓██▒░██████▒")
    print(" ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ▒░▒░▒░  ▒ ░       ░▒▓███▀▒ ▒▒   ▓▒█░▒▒   ▓▒█░░ ▒░▓  ░")
    print(" ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░     ░ ▒ ▒░  ░         ▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░")
    print(" ░ ░  ░    ░   ░  ░  ░  ░ ░ ░ ▒    ░ ░    ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░    ░ ░ ░ ▒   ░ ░        ░    ░   ░   ▒    ░   ▒     ░ ░   ")
    print("   ░       ░  ░      ░      ░ ░      ░  ░     ░  ░         ░      ░ ░           ░        ░ ░              ░            ░  ░     ░  ░    ░  ░")
    print(" ░                                                                                                             ░                             ")


# Call the function to display the opening screen before game starts
title_screen()

def pad_ascii_art(art, padding=10):
    lines = art.split('\n')
    padded_lines = [' ' * padding + line + ' ' * padding for line in lines]
    return '\n'.join(padded_lines)

ascii_art = """
                             Q                           Q   
                             QQ                         QQ   
                             QQ                         QQ   
                             QQQ                       QQQ   
                             QQQ                       QQQ   
                             QQQQ                     QQQQ   
                           Q  QQQQ                   QQQQ  Q 
                           QQ QQQQQ                 QQQQQ QQ 
                           QQQQQQQQQQ             QQQQQQQQQQ 
                           QQQQQQQQQQQQ         QQQQQQQQQQQQ 
                            QQQQQQQQQQQQQ     QQQQQQQQQQQQQ  
                          Q  QQQQQQQQQQQQ  Q  QQQQQQQQQQQQ  Q
                          QQQQQQQQQQQQQQ   Q  QQQQQQQQQQQQQQQ
                           QQQQQQQQQQQQQ  QQQ  QQQQQQQQQQQQQ 
                            QQQQQQQQQQQ   QQQ   QQQQQQQQQQQ  
                             QQQQQQQQQ    QQQ    QQQQQQQQQ   
                           QQQQQQQQQQQQ  QQQQQ  QQQQQQQQQQQQ 
                           QQQQQQQQQQQQQ QQQQQ QQQQQQQQQQQQQ 
                            QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ  
                              QQQQQQQQQQ QQQQQQQQQQQQQQQQ    
                            Q QQQQQQQQQQQQQQQQQQQQQQQQQQQ Q   
                             QQQQQQQ    QQQQQQQ    QQQQQQQ   
                              QQQQQ     QQQQQQQ     QQQQQ    
                                       QQQQQQQQQ             
                                       QQQQQQQQQ             
                                       QQQQQQQQQ             
                                       QQQQQQQQQ             
                                        QQQQQQQ              
                                         QQQQQ               
\n"""

# Pad the ASCII art with 20 spaces on each side
padded_art = pad_ascii_art(ascii_art, padding=20)

print(padded_art)


import textwrap

def story_intro():
    story = """
The galaxy is torn asunder by the devastating events of the Cicatrix Maledictum, the great warp storm that has plunged the Imperium into a new era of darkness. Amidst the chaos, the Blood Angels, led by their indomitable power Master, Commander Dante, stand as the last line of defense for their homeworld, Baal. For centuries, the Blood Angels have guarded the sands of their irradiated world, their noble gene-seed cursed by the thirst for blood and the madness of the Black Rage.

Now, an enemy unlike any they have ever faced descends upon them. The Great Devourer, the relentless Hive Fleet Leviathan, has come to consume Baal and all that remains of its defenders. Trillions of Tyranids churn through the void, a tide of hunger that seeks to strip the planet of all life. The Blood Angels, supported by their successor chapters, brace for an apocalyptic last stand, knowing that should they fall, not only will Baal be lost, but the legacy of their Primarch, Sanguinius, may be extinguished forever.

As war breaks out, the Blood Angels prepares for the fight of their life and for their home, while far above, the enigmatic forces of the Imperium's most secretive orders stir, bearing strange tidings that may either doom Baal or grant the Blood Angels a fleeting chance at salvation. The stage is set for a battle of unimaginable scale, as ancient warriors clash against the primal hunger of the Tyranids, and Commander Dante's eternal duty to his power and to the Emperor hangs in the balance...
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
story_intro()
print()

# Values of Tyranid hive with Xeno Skulls rewards
blood_angels = Blood_Angels(1000, 250)
gaunts = Gaunts(600, 20)
warriors = Warriors(200, 30)
ravener = Ravener(100,40)
lictor= Lictor(50, 50)
carnifex = Carnifex(10, 75)
hive_tyrant = Hive_Tyrant(1, 1000)

# This will check if the characters are alive, and if they are, it  will print their status
while blood_angels.alive():
    print()
    blood_angels.print_status()
    if gaunts.alive():
        gaunts.print_status()
    else:
        print("The seemingly endless swarm of gaunts have been crushed beneath the feet of the mighty Blood Angels. Rejoice in the eradication of the Zeno filth!\n")
    if warriors.alive():
        warriors.print_status()
    else:
        print("The Tyranid Warriors lay butchered across the battfield. Xeno exoskeletons are no match for chainswords!\n")
    if ravener.alive():
        ravener.print_status()
    else:
        print("Since the Raveners were attacking from underground, you lit the crude prometheum beneath the surface. It will burn for years before ever letting up!\n")
    if lictor.alive():
        lictor.print_status()
    else:
        print("You listened to your bioengineered heightened senses, and saw through the Lictors' active camoflouge. Threats neutralized.\n")
    if carnifex.alive():
        carnifex.print_status()
    else:
        print("Through proper planning and sheer will, you have wiped out every Carnifex in the Tyranid swarm!\n")
    if hive_tyrant.alive():
        hive_tyrant.print_status()
    else:
        print("Only by the blood of Sanguinius that flows through you were you able to defeat the Hive Tyrant!\n")
    print()

 # User Choices 
    print("What orders do you wish to give Commander?\n")
    print("1. Rush into the swarm of Gaunts")
    print("2. Take on Tyranid Warriors")
    print("3. Feel for vibrations from the Ravener")
    print("4. Listen to your senses to find the Lictor")
    print("5. Test your skills against the Carnifex")
    print("6. Go toe to toe with the Hive Tyrant")
    print("7. Call for Retreat")
    print("8. Abandon Baal")
    print("9. Visit the Armour_Hall\n")  # Added option to visit the armour_hall
    print("> ", end="")
     
     
    user_input = input()
    print()
    if user_input == "1":
        if gaunts.alive():
            blood_angels.attack(gaunts)
            if gaunts.alive():
                gaunts.attack(blood_angels)
        else:
            print(f"The Xeno filth has no more {enemy.__class__.__name__}! Worry not brother, there are plenty other skulls to crush!\n")
    if user_input == "2":
        if warriors.alive():
            blood_angels.attack(warriors)
            if warriors.alive():
                warriors.attack(blood_angels)
        else:
            print(f"The Xeno filth has no more {enemy.__class__.__name__}! Worry not brother, there are plenty other skulls to crush!\n")
    if user_input == "3":
        if ravener.alive():
            blood_angels.attack(ravener)
            if ravener.alive():
                ravener.attack(blood_angels)
        else:
            print(f"The Xeno filth has no more {enemy.__class__.__name__}! Worry not brother, there are plenty other skulls to crush!\n")
    if user_input == "4":    
        if lictor.alive():
            blood_angels.attack(lictor)
            if lictor.alive():
                lictor.attack(blood_angels)
        else:
            print(f"The Xeno filth has no more {enemy.__class__.__name__}! Worry not brother, there are plenty other skulls to crush!\n")
    if user_input == "5":
        if carnifex.alive():
            blood_angels.attack(carnifex)
            if carnifex.alive():
                carnifex.attack(blood_angels)
            if not carnifex.alive():
             print(f"The Xeno filth has no more {enemy.__class__.__name__}! Worry not brother, there are plenty other skulls to crush!\n")
    if user_input == "6":
        if hive_tyrant.alive():
            blood_angels.attack(hive_tyrant)
            if hive_tyrant.alive():
                hive_tyrant.attack(blood_angels)
            if not hive_tyrant.alive():
             print(f"The Xeno filth has no more {enemy.__class__.__name__}! Worry not brother, there are plenty other skulls to crush!\n")
    if user_input == "7":
    # Check the condition for Blood_Angels.alive()
     if blood_angels.alive():
        print("Heretic! Your Duty is to fight and die for The Emperor!\n")
        # Enemy attacks
        for enemy in [Gaunts, Warriors, Ravener, Lictor, Carnifex, Hive_Tyrant]:
            if enemy.alive():
                enemy.attack(blood_angels)
        print()
        
        if blood_angels.alive():
            print("Somehow, by the blood of Sanguinius, you survived. Get back to the frontline Commander!\n")
        else:
            print("You were overrun by the seemingly endless swarm of Xeno filth. Baal is lost!\n")
            
            xeno_win_ascii = """
            ▒██   ██▒▓█████  ███▄    █  ▒█████    ██████     █     █░ ██▓ ███▄    █ 
            ▒▒ █ █ ▒░▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▒██    ▒    ▓█░ █ ░█░▓██▒ ██ ▀█   █ 
            ░░  █   ░▒███   ▓██  ▀█ ██▒▒██░  ██▒░ ▓██▄      ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒
             ░ █ █ ▒ ▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░  ▒   ██▒   ░█░ █ ░█ ░██░▓██▒  ▐▌██▒
            ▒██▒ ▒██▒░▒████▒▒██░   ▓██░░ ████▓▒░▒██████▒▒   ░░██▒██▓ ░██░▒██░   ▓██░
            ▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░   ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ 
            ░░   ░▒ ░ ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░     ▒ ░ ░   ▒ ░░ ░░   ░ ▒░
             ░    ░     ░      ░   ░ ░ ░ ░ ░ ▒  ░  ░  ░       ░   ░   ▒ ░   ░   ░ ░ 
             ░    ░     ░  ░         ░     ░ ░        ░         ░     ░           ░ 
            """
            print(xeno_win_ascii)
            break  # Exit the loop when this condition is met
    if user_input == "8":
        print("Throwing in the towel huh? I knew you couldn't handle it!\n")
        break
    if user_input == "9":
        armour_hall.do_shopping(Blood_Angels)  # Option to visit the armour_hall
    elif user_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print(f"Uh Oh! Looks like you entered {user_input} instead of a selectable option. Try again!\n")
     
