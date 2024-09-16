import random
import math
import textwrap

blood_angels_win_ascii = """
 ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄     ▄▄▄       ███▄    █   ▄████ ▓█████  ██▓      ██████     █     █░ ██▓ ███▄    █  ▐██▌ 
▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌   ▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██▒    ▒██    ▒    ▓█░ █ ░█░▓██▒ ██ ▀█   █  ▐██▌ 
▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░    ░ ▓██▄      ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒ ▐██▌ 
▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌   ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██░      ▒   ██▒   ░█░ █ ░█ ░██░▓██▒  ▐▌██▒ ▓██▒ 
░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓     ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░▒████▒░██████▒▒██████▒▒   ░░██▒██▓ ░██░▒██░   ▓██░ ▒▄▄  
░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒     ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░   ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒  ░▀▀▒ 
▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒      ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░░ ░ ▒  ░░ ░▒  ░ ░     ▒ ░ ░   ▒ ░░ ░░   ░ ▒░ ░  ░ 
 ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░      ░   ▒      ░   ░ ░ ░ ░   ░    ░     ░ ░   ░  ░  ░       ░   ░   ▒ ░   ░   ░ ░     ░ 
 ░          ░  ░    ░ ░      ░ ░     ░             ░  ░         ░       ░    ░  ░    ░  ░      ░         ░     ░           ░  ░    
      ░                            ░                                                                                              
"""

def display_victory_message():
            print(blood_angels_win_ascii)
            print("=========================")
            print("VICTORY FOR THE IMPERIUM!")
            print("=========================")
            print()
            print("The Blood Angels have triumphed over the Tyranid Swarm! The Xeno filth has been decimated!")
            print()
            print("Baal has been saved, Commander Dante has finally been allowed a moment of rest, and the legacy of Sanguinius lives on!")
            print()
            print("BURN THE HERETIC!")
            print()
            print("KILL THE MUTANT!")
            print()
            print("PURGE THE UNCLEAN!")
            print()
            print("FOR THE EMPEROR!")
            print("=" * 60)

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

def display_defeat_message():
    print(xeno_win_ascii)
    print("!!!You were overrun by the seemingly endless swarm of Xeno filth. All of Baal is lost!!!\n")
    


class Tyranids:
    def __init__(self, hive_fleet, xeno_skulls=0):
        self.hive_fleet = hive_fleet
        self.xeno_skulls = xeno_skulls
        self.regeneration_amount = 0

    def alive(self):
        return self.hive_fleet > 0

    @property
    def combined_strength(self):
        return math.ceil(self.hive_fleet * 0.75)

    def attack(self, enemy):
        if enemy.alive():
            damage = self.combined_strength
            print(f"*** The Hive Fleet {self.__class__.__name__} counter attacks the Blood Angels and kills {self.combined_strength} Space Marines! ***\n")
            
            actual_damage = enemy.take_damage(damage)

    def take_damage(self, damage):
        before_damage = self.hive_fleet
        self.hive_fleet = max(0, self.hive_fleet - damage)
        actual_damage = before_damage - self.hive_fleet
        self.calculate_regeneration()
        return actual_damage

    def calculate_regeneration(self):
        if self.__class__ != Hive_Tyrant:
            self.regeneration_amount = self.hive_fleet // 3

    def apply_regeneration(self):
        if self.regeneration_amount > 0:
            self.hive_fleet += self.regeneration_amount
            print(f"*** The {self.__class__.__name__} regenerated {self.regeneration_amount} filthy Xenos! ***")
            print()
            print()
            self.regeneration_amount = 0


class Hormagaunts(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=5):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print(f") The Hive Fleet has {self.hive_fleet} Hormagaunts left in their swarm... Their combined strength is {self.combined_strength}. Plan your next attack before they regroup!\n")


class Warriors(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=10):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print(f") The Hive Fleet have {self.hive_fleet} Warrior class Xenos left in their swarm... Their combined strength is {self.combined_strength}. Kill the filthy Xenos!\n")


class Raveners(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=15):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print(f") The Hive Fleet have {self.hive_fleet} Raveners left in their swarm... Their combined strength is {self.combined_strength}. Feel for tremors before they attack.\n")

    def take_damage(self, amount):
        if random.random() < 0.2: # 20% chance to dodge
            print("- The Raveners escaped underground! Beware what lurks below...\n")
            return 0 # Return 0 to indicate no damage was taken
        else:
            actual_damage = super().take_damage(amount)
            print(f"> The Blood Angels slaughtered {actual_damage} Raveners!\n")
            return actual_damage
        
    def apply_regeneration(self):
        super().apply_regeneration()  # Call the parent class method to apply regeneration


class Lictors(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=20):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print(f") The Hive Fleet have {self.hive_fleet} Lictors left in their swarm... Their combined strength is {self.combined_strength}. Beware of their adaptive camouflage.\n")

    def take_damage(self, amount):
        if random.random() < 0.3: # 30% chance to dodge
            print("- The Lictors activated their active camouflage! They have evaded your wrath for now...\n")
            return 0  # Return 0 to indicate no damage was taken
        else:
            actual_damage = super().take_damage(amount)
            print(f"- You slaughtered {actual_damage} Lictors!\n")
            return actual_damage
        
    def apply_regeneration(self):
        super().apply_regeneration()  # Call the parent class method to apply regeneration



class Carnifex(Tyranids):
    def __init__(self, hive_fleet, xeno_skulls=35):
        super().__init__(hive_fleet, xeno_skulls)

    def print_status(self):
        if self.alive():
            print(f") The Hive Fleet have {self.hive_fleet} Carnifices left in their swarm... Their combined strength is {self.combined_strength}. Shwo them what we think of Xenos!\n")



class Hive_Tyrant(Tyranids):
    def __init__(self, hive_fleet=1000, xeno_skulls=100):
        super().__init__(hive_fleet, xeno_skulls)
        self.max_health = 1000

    @property
    def combined_strength(self):
        return self.hive_fleet  # Combined strength is now equal to hive fleet (health)

    def print_status(self):
        if self.alive():
            print(f") The Hive Tyrant is still directing the hive mind... its health is {self.hive_fleet}/{self.max_health} and its strength is {self.combined_strength}. Sanguinius help us. \n")

    def take_damage(self, damage):
        before_damage = self.hive_fleet
        self.hive_fleet = max(0, self.hive_fleet - damage)
        actual_damage = before_damage - self.hive_fleet
        return actual_damage
    
    

# Values of Tyranid hive with Xeno Skulls rewards
hormagaunts = Hormagaunts(600, 10)
warriors = Warriors(700, 20)
raveners = Raveners(800, 30)
lictors= Lictors(900, 50)
carnifex = Carnifex(1000, 75)
hive_tyrant = Hive_Tyrant(2000, 100)



class Space_Marines:
    def __init__(self, ranks, combined_strength, xeno_skulls=0):
        self.ranks = min(ranks, 1000)  # Initialize with a maximum of 1000 ranks
        self.combined_strength = combined_strength
        self.xeno_skulls = xeno_skulls

    def alive(self):
        return self.ranks > 0

    def ranks(self, value):
        self._ranks = min(value, 1000)  # Ensure ranks never exceed 1000
    
    def attack(self, enemy):
        if enemy.alive():
            damage = self.combined_strength
            print(f"> The Blood Angels attack the {enemy.__class__.__name__} with righteous fury and deal {damage} damage!\n\n")
            
            if hasattr(enemy, 'take_damage'):
                damage_taken = enemy.take_damage(damage)
                if not damage_taken:
                    return  # If the enemy dodged, skip the rest of the logic
            else:
                enemy.hive_fleet = max(0, enemy.hive_fleet - damage)  # Prevent ranks from going negative
            
            print(f"The {enemy.__class__.__name__} are now down to {enemy.hive_fleet} filthy Xenos!\n")
            
            if not enemy.alive():
                print(f"The {enemy.__class__.__name__} has been defeated!\n")

    def take_damage(self, damage):
        before_damage = self.ranks
        self.ranks = max(0, self.ranks - damage)
        return before_damage - self.ranks

# Modify the main game loop
# First, create a list of all enemy instances
enemies = [hormagaunts, warriors, raveners, lictors, carnifex, hive_tyrant]

# Classes of Blood_Angels
class Blood_Angels(Space_Marines):
    def __init__(self, ranks, combined_strength, xeno_skulls=20):
        super().__init__(ranks, combined_strength, xeno_skulls)
        self.max_ranks = 1000  # Set maximum number of Blood Angels to 1000

    def print_status(self):
        if self.alive():
            print("==========================================================================================================================================")
            print(f"> The Blood Angels have {self.ranks} Space Marines left in their Chapter. Their combined strength is {self.combined_strength}. Hold fast!")
            print("==========================================================================================================================================")
            print()
            print(f"$ You currently have {self.xeno_skulls} Xeno Skulls $\n")
            print()
        else:
            print("> Even though they stood valiantly against the Xeno horde, The Blood Angels could not hold back the Tyranid Fleet. Baal is lost!\n")

    def check_victory(self, enemies):
        return all(not enemy.alive() for enemy in enemies)

    def attack(self, enemy):
        if random.random() < 0.2:
            damage = self.combined_strength * 2
            print(f">>> The Blood Angels give into the Black Rage and do {damage} double damage to {enemy.__class__.__name__}!\n")
        else:
            damage = self.combined_strength
            print(f">>> The Blood Angels attack the {enemy.__class__.__name__} and do {damage} damage!\n")
            print()
        
        actual_damage = enemy.take_damage(damage)
  
        if actual_damage > 0:
            # Calculate Xeno Skulls gained (1 skull per 10 Tyranids killed)
            skulls_gained = actual_damage // 10
            self.xeno_skulls += skulls_gained


        # Check if the enemy is defeated, if so it will reward the xeno_skulls
            if not enemy.alive():
               print(f"> You defeated the {enemy.__class__.__name__}! Consider visiting the Armouring Hall to recruit more units!\n")
               # Add bonus Xeno Skulls for defeating the enemy
               bonus_skulls = enemy.xeno_skulls
               self.xeno_skulls += bonus_skulls
               print(f"> You earned an additional {bonus_skulls} Xeno Skulls for defeating the {enemy.__class__.__name__}!")
               print()
               print(f"> You now have {self.xeno_skulls} Xeno Skulls.\n\n")
               print()
                
        elif actual_damage == 0:
         print(f"*** The Blood Angels' attack missed! The {enemy.__class__.__name__} remain unscathed. ***\n")
        else:  # actual_damage is False or None, indicating evasion
         print(f"*** The {enemy.__class__.__name__} managed to evade the attack! ***\n")
    
        return actual_damage

    def take_damage(self, damage):
        before_damage = self.ranks
        self.ranks = max(0, min(self.ranks - damage, self.max_ranks))
        actual_damage = before_damage - self.ranks
        return actual_damage       
    
    # Buy method to allow Blood_Angels objects to purchase items from the virtual armour_hall
    def recruit(self, item):
        self.buy(item)
    
    def buy(self, item):
        if self.xeno_skulls >= item.cost:
            if hasattr(item, 'recruit_amount'):
                if self.ranks + item.recruit_amount <= self.max_ranks:
                    self.xeno_skulls -= item.cost
                    item.apply(self)
                else:
                    remaining_slots = self.max_ranks - self.ranks
                    print()
                    print(f"Sir, we cannot recruit {item.recruit_amount} {item.name}s. We have {remaining_slots} positions available to fill.")
                    print()
                    print(f"Your chapter is at {self.ranks}/{self.max_ranks} capacity.\n\n")
            else:
                self.xeno_skulls -= item.cost
                item.apply(self)
        else:
            print(f"Not enough Xeno Skulls to recruit {item.name}. You need {item.cost}, but you only have {self.xeno_skulls}.")

# Initial Start Blood Angels Values
blood_angels = Blood_Angels(1000, 300, 25)


# Units class and its subclasses, including the recruit_amount attribute to ensure we can't recruit more than the max ranks
class Units:
    def __init__(self, name, cost, recruit_amount, combined_strength):
        self.name = name
        self.cost = cost
        self.recruit_amount = recruit_amount
        self.combined_strength = combined_strength

    def apply(self, Blood_Angels):
        pass

class Assault(Units):
    def __init__(self):
        super().__init__("Assault", 5, 100, 25)

    def apply(self, Blood_Angels):
        Blood_Angels.ranks += self.recruit_amount
        Blood_Angels.combined_strength += 10
        print(f"> The {Blood_Angels.__class__.__name__} recruit {self.recruit_amount} Assault Space Marines into their ranks and gains 10 combined strength! Combined strength is now {Blood_Angels.combined_strength}\n")
        print()

class Incursor(Units):
    def __init__(self):
        super().__init__("Incursor", 10, 75, 50)

    def apply(self, Blood_Angels):
        Blood_Angels.ranks += self.recruit_amount
        Blood_Angels.combined_strength += 25
        print(f"> The {Blood_Angels.__class__.__name__} recruit {self.recruit_amount} Incursor Space Marines into their ranks and gains 20 combined strength! Combined strength is now {Blood_Angels.combined_strength}\n")
        print()

class Chaplain(Units):
    def __init__(self):
        super().__init__("Chaplain", 25, 50, 75)

    def apply(self, Blood_Angels):
        Blood_Angels.ranks += self.recruit_amount
        Blood_Angels.combined_strength += 50
        print(f"> The {Blood_Angels.__class__.__name__} recruit {self.recruit_amount} Chaplains Space Marines into their ranks and gains 30 combined strength! Combined strength is now {Blood_Angels.combined_strength}\n")
        print()

class Dreadnaught(Units):
    def __init__(self):
        super().__init__("Dreadnaught", 50, 25, 100)

    def apply(self, Blood_Angels):
        Blood_Angels.ranks += self.recruit_amount
        Blood_Angels.combined_strength += 75
        print(f"> The {Blood_Angels.__class__.__name__} recruit {self.recruit_amount} Dreadnaughts into their ranks and gains 40 combined strength! Combined strength is now {Blood_Angels.combined_strength}\n")
        print()

class Commander(Units):
    def __init__(self):
        super().__init__("Commander", 150, 100, 500)

    def apply(self, Blood_Angels):
        Blood_Angels.ranks += self.recruit_amount
        Blood_Angels.combined_strength += 100
        print(f"> The {Blood_Angels.__class__.__name__} recruit a Commander into their ranks and gains 100 combined strength! Combined strength is now {Blood_Angels.combined_strength}\n")
        print()

# armour_hall class
class Armour_Hall:
    items = [Assault(), Incursor(), Chaplain(), Dreadnaught(), Commander()]  # armour_hall items: All unit subclasses

    def do_shopping(self, Blood_Angels):
        while True:
            print("==============================")
            print("The Magos awaits your command")
            print("==============================")
            print()
            print()
            print(f"You have {Blood_Angels.xeno_skulls} Xeno Skulls.")
            print()
            print(f"The Blood angels have {Blood_Angels.ranks}/{Blood_Angels.max_ranks} defensive positions filled.")
            print()
            print()
            print("Which Unit do we need brother?")
            print()
            print()

            for i, item in enumerate(armour_hall.items):
                print(f"{i + 1}. {item.name} Units that will fill ({item.recruit_amount}) empty defensive positions and will add ({item.combined_strength}) to your combined strength ({item.cost} Xeno Skulls)\n")
            print(f"{len(self.items) + 1}. Go back to crush more Xeno Skulls!")
            print()

            user_input = int(input("> Let's do option: "))
            print()
            print()

        
            try:
                user_input = int(user_input)
                if user_input == len(self.items) + 1:
                    print()
                    print("Hold the line brothers! Sanguinius is watching over us!\n\n")
                    break
                elif 1 <= user_input <= len(self.items):
                    item_to_buy = self.items[user_input - 1]

                    if Blood_Angels.xeno_skulls >= item_to_buy.cost:
                        Blood_Angels.buy(item_to_buy)
                    else:
                        print(f"Not enough Xeno Skulls to recruit {item_to_buy.name}. You need {item_to_buy.cost}, but you only have {Blood_Angels.xeno_skulls} Xeno Skulls.")
                        print()
                else:
                    print("Hmph, I don't recognize that option. Consulting the Codex Astartes to figure out what you require....")
                    print()
            except ValueError:
                print("Hmph, I don't recognize that option. Consulting the Codex Astartes to figure out what you require....")
                print()


armour_hall = Armour_Hall()  # Create a armour_hall object

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


def story_intro():
    story = """
The galaxy is torn asunder by the devastating events of the Cicatrix Maledictum, the great warp storm that has plunged the Imperium into a new era of darkness. Amidst the chaos, the Blood Angels, led by their indomitable Commander Dante, stand as the last line of defense for their homeworld, Baal. For centuries, the Blood Angels have guarded the sands of their irradiated world, their noble gene-seed cursed by the thirst for blood and the madness of the Black Rage.

Now, an enemy unlike any they have ever faced descends upon them. The Great Devourer, the relentless Hive Fleet Leviathan, has come to consume Baal and all that remains of its defenders. Trillions of Tyranids churn through the void, a tide of hunger that seeks to strip the planet of all life. The Blood Angels, supported by their successor chapters, brace for an apocalyptic last stand, knowing that should they fall, not only will Baal be lost, but the legacy of their Primarch, Sanguinius, may be extinguished forever.

As war breaks out, the Blood Angels prepares for the fight of their life and for their home, while far above, the enigmatic forces of the Imperium's most secretive orders stir, bearing strange tidings that may either doom Baal or grant the Blood Angels a fleeting chance at salvation. The stage is set for a battle of unimaginable scale, as ancient warriors clash against the primal hunger of the Tyranids, and Commander Dante's eternal duty to his Chapter and to the Emperor hangs in the balance...
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
print()



# MAIN GAME LOOP
# This will check if the Blood Angels are alive, and if they are, it  will print their status. If they are not, a defeat screen is displayed.
while True:
    print()
    if not blood_angels.alive() or blood_angels.ranks <= 0:
        display_defeat_message()
        break

    blood_angels.print_status()


    # Print status of each enemy or defeated message
    for enemy in [hormagaunts, warriors, raveners, lictors, carnifex, hive_tyrant]:
        if enemy.alive():
            enemy.print_status()
        else:
            if isinstance(enemy, Hormagaunts):
                print("X The endless swarm of Hormagaunts have been crushed by the Blood Angels! Rejoice in the eradication of the Xeno filth! X\n")
            elif isinstance(enemy, Warriors):
                print("X The Tyranid Warriors lay butchered across the battlefield. Xeno exoskeletons are no match for chainswords! X\n")
            elif isinstance(enemy, Raveners):
                print("X Since the Raveners were attacking from underground, you lit the crude prometheum beneath the surface. It will burn for years! X\n")
            elif isinstance(enemy, Lictors):
                print("X You listened to your bioengineered heightened senses, and saw through the Lictors' active camouflage. Threats neutralized. X\n")
            elif isinstance(enemy, Carnifex):
                print("X Through proper planning and sheer will, you have wiped out every Carnifex in the Tyranid swarm! X\n")
            elif isinstance(enemy, Hive_Tyrant):
                print("X Only by the blood of Sanguinius that flows through you were you able to defeat the Hive Tyrant! X\n")
    

    
    # Check for victory after printing status
    if blood_angels.check_victory([hormagaunts, warriors, raveners, lictors, carnifex, hive_tyrant]):
        display_victory_message()
        break

    print()

    # User Choices 
    print("=================================")
    print("Commander, what are your orders?")
    print("=================================")
    print()
    print("1. Charge into the swarm of Hormagaunts")
    print()
    print("2. Take on the Tyranid Warriors")
    print()
    print("3. Feel for vibrations from the Raveners")
    print()
    print("4. Listen to your senses to find the Lictors")
    print()
    print("5. Test your skills against the mighty Carnifices")
    print()
    print("6. Go toe to toe with the Hive Tyrant")
    print()
    print("7. Take a moment to plan your next move")
    print()
    print("8. Abandon Baal")
    print()
    print("9. Visit the Armour Hall\n\n")  # Added option to visit the armour_hall
    print("> Let's do option: ", end="")

    user_input = input()
    print()
    print()


    # Hormagaunts
    if user_input == "1":
        # Hormagaunts
        if hormagaunts.alive():
            actual_damage = blood_angels.attack(hormagaunts)
            if hormagaunts.alive():
                hormagaunts.attack(blood_angels)
                hormagaunts.apply_regeneration()
            else:
                print("X The endless swarm of Hormagaunts have been crushed by the Blood Angels! Rejoice in the eradication of the Xeno filth! X\n")
        else:
            print("* The Xeno filth has no more Hormagaunts! Worry not brother, there are plenty other skulls to crush! *\n")
    

    # Warriors        
    elif user_input == "2":
        # Warriors
        if warriors.alive():
            actual_damage = blood_angels.attack(warriors)
            if warriors.alive():
                warriors.attack(blood_angels)
                warriors.apply_regeneration()
            else:
                print("X The Tyranid Warriors lay butchered across the battlefield. Xeno exoskeletons are no match for chainswords! X\n")
        else:
            print("* The Xeno filth has no more Warriors! Worry not brother, there are plenty other skulls to crush! *\n")
    

     # Raveners
    elif user_input == "3":
        # Raveners
        if raveners.alive():
            actual_damage = blood_angels.attack(raveners)
            if raveners.alive():
                raveners.attack(blood_angels)
                if actual_damage > 0:  # Only regenerate if they took damage
                    raveners.apply_regeneration()
            else:
                print("X Since the Raveners were attacking from underground, you lit the crude prometheum beneath the surface. It will burn for years! X\n")
        else:
            print("* The Xeno filth has no more Raveners! Worry not brother, there are plenty other skulls to crush! *\n")
    

    # Lictors
    elif user_input == "4":
        # Lictors
        if lictors.alive():
            actual_damage = blood_angels.attack(lictors)
            if lictors.alive():
                lictors.attack(blood_angels)
                if actual_damage > 0:  # Only regenerate if they took damage
                    lictors.apply_regeneration()
            else:
                print("X You listened to your bioengineered heightened senses, and saw through the Lictors' active camouflage. Threats neutralized. X\n")
        else:
            print("* The Xeno filth has no more Lictors! Worry not brother, there are plenty other skulls to crush! *\n")

    # Carnifexes
    elif user_input == "5":
        print()
        if carnifex.alive():
            actual_damage = blood_angels.attack(carnifex)
            if carnifex.alive():
                carnifex.attack(blood_angels)
                carnifex.apply_regeneration()
            else:
                print("X Through proper planning and sheer will, you have wiped out every Carnifex in the Tyranid swarm! X\n")
        else:
            print("* The Xeno filth has no more Carnifexes! Worry not brother, there are plenty other skulls to crush! *\n")

    # Hive Tyrant
    elif user_input == "6":
        print()
        if hive_tyrant.alive():
            actual_damage = blood_angels.attack(hive_tyrant)
            if hive_tyrant.alive():
                hive_tyrant.attack(blood_angels)
                print()
                print(f"* The Hive Tyrant now has {hive_tyrant.hive_fleet}/{hive_tyrant.max_health} health remaining. *")
                print()
                print(f"The Hive Tyrant's strength is now {hive_tyrant.combined_strength}.")
                print()
            else:
                print("X Only by the blood of Sanguinius that flows through you were you able to defeat the Hive Tyrant! X\n")
        else:
            print("X The Tyranid's Hive Tyrant has been defeated! Now that the hive mind link is weakened, take out the remaining swarm!\n")
    

    # Plan Option
    elif user_input == "7":
        print()
        # Check the condition for Blood_Angels.alive()
        if blood_angels.alive():
            print("> There's no time for planning! The Xeno filth are relentless!\n")
            for enemy in [hormagaunts, warriors, raveners, lictors, carnifex, hive_tyrant]:
                if enemy.alive():
                    enemy.attack(blood_angels)
            if blood_angels.alive():
                print("> Somehow, by the blood of Sanguinius, you survived. Get back to the frontline Commander!\n")
            else:
                display_defeat_message()
                break

    # Abandon Baal Option
    elif user_input == "8":
        print()
        print("> All of Baal looked to you for protection! You Filthy Heretic!\n")
        display_defeat_message()
        break
    
    # Armour Hall Option
    elif user_input == "9":
            armour_hall.do_shopping(blood_angels)  # Option to visit the armour_hall
    
    # Unrecognized Selection
    else:
        print(f"> Hmph, it seems you entered {user_input} instead of a selectable option. Consulting the Codex Astartes to figure out what you require...\n\n")

    
    if not blood_angels.alive() or blood_angels.ranks <= 0:
        display_defeat_message()
        break
    
    if blood_angels.check_victory([hormagaunts, warriors, raveners, lictors, carnifex, hive_tyrant]):
        display_victory_message()
        break