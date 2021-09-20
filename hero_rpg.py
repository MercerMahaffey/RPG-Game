# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
# import keyboard
import random

def main():

    # class Items:
    #     def __init__ (self, name, method)
    # store_items = ["Health Tonic - 10", "Armor Plate - 20", "Evasion Potion - 15", "Steel Sword - 25", "Regenerating Potion - 25"]
    heart_symbol = u'\u2764'

    class StoreItems:
        def __init__(self, name, health, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical

    health = StoreItems("Health Tonic", 10, 0, 0, 0, 0, 10, 0, 0)
    armor = StoreItems("Armor Plate", 0, 0, 0, 0, 0, 20, 2, 0)
    evasion = StoreItems("Evasion Potion", 0, 0, 2, 0, 0, 15, 0, 0)
    sword = StoreItems("Steel Sword", 0, 2, 0, 0, 0, 25, 0, 0)
    recup = StoreItems("Regenerating", 0, 0, 0, 2, 0, 0, 0, 0)

    item_list = [health, armor, evasion, sword, recup]



    class Character:
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical
        def alive(self):
            if self.health >0:
                return True
            else:
                return False
        def print_status(self):
            if self.name == "You":
                print(f"{self.name} have {self.health} health and {self.power} power.")
            else:
                print(f"{self.name} has {self.health} health and {self.power} power.")
        def attack(self, enemy):
            roll = random.randrange(11)          
            if roll > enemy.evade:
                if roll < self.critical:
                    double_damage = 2 *self.power
                    enemy.health -= (double_damage - enemy.armor)
                    if enemy.armor > 0:
                        print(f"{enemy.name} has {enemy.armor} armor, which blocks some damage.")
                    print(f"Critical hit! {self.name} did {double_damage - enemy.armor} damage to {enemy.name}.")
                else:
                    enemy.health -= (self.power - enemy.armor)
                    if enemy.armor > 0:
                        print(f"{enemy.name} has {enemy.armor} armor, which blocks some damage.")
                    print(f"{self.name} did {self.power - enemy.armor} damage to {enemy.name}.")
            else:
                print(f"{enemy.name} evaded the attack!")
            if enemy.resur == 1:
                if enemy.health <=0:
                    enemy.health = 10
                    if enemy.name == "You":
                        print(f"{enemy.name} are dead! ... But you have been resurrected, You cannot be defeated!")
                    else:
                        print(print(f"The {enemy.name} is dead... Wait! No! The {enemy.name} resurrected! It cannot be defeated!"))
            elif enemy.recup >0:
                enemy.recuperate()

            if enemy.health <=0:
                if enemy.name == "You":
                    print(f"{enemy.name} are dead!")
                else:
                    print(f"The {enemy.name} is dead.")
                    print(f"You gain {enemy.bounty} coins for defeating the {enemy.name}.")
                    character_choice.bounty += enemy.bounty
                    defeated_enemy()

        def fighting(self, opponent):           # fighting state
            print(f"You come accross a {opponent.name} looking for a fight.")
            while character_choice.alive() and opponent.alive():
                exiting = "no"
                character_choice.print_status()
                opponent.print_status()
                print("What do you want to do?")
                print(f"1. attack {opponent.name}")
                print("2. do nothing")
                print("3. flee")
                print("> ", end=' ')
                fight_input = input()
                if fight_input == "1":
                    character_choice.attack(opponent)
                    exiting = "yes"
                elif fight_input == "2":
                    exiting = "yes"
                    pass
                elif fight_input == "3":
                    print(f"You fled from the {opponent.name}.")
                    exiting = "yes"
                    break
                if opponent.health > 0:
                    opponent.attack(character_choice)
                elif exiting == "no":
                    print("Invalid input {}".format(fight_input))
            opponent.reset_health()
        def store(self):        # visiting store
            while True:
                print(f"You have {self.bounty} coins and entered the store which has the following Items:")
                count = 1
                for item in item_list:
                    print(f"{count}. {item.name} - {item.bounty} coins")
                    count +=1
                print("q. exit store")
                print("> ", end=' ')
                buy_num = input()
                if buy_num == "1":
                    if self.bounty >= health.bounty:
                        self.bounty -= health.bounty
                        #check for coins if enough or insufficient
                        self.health = health.health
                        print(f"You purchased a {health.name} restoring your health to {self.health}.")
                    else:
                        print("Not enough coins.")
                if buy_num == "2":
                    if self.bounty >= armor.bounty:
                        self.bounty -= armor.bounty
                        self.armor += armor.armor
                        print(f"You purchased {armor.name} increasing your armor to {self.armor}.")
                    else:
                        print("Not enough coins.")
                if buy_num == "3":
                    if self.bounty >= evasion.bounty:
                        self.bounty -= evasion.bounty
                        self.evade += evasion.evade
                        print(f"You purchased {evasion.name} increasing your evade to {self.evade}.")
                    else:
                        print("Not enough coins.")
                if buy_num == "4":
                    if self.bounty >= sword.bounty:
                        self.bounty -= sword.bounty
                        self.power += sword.power
                        print(f"You purchased {sword.name} increasing your damage to {self.power}.")
                    else:
                        print("Not enough coins.")
                if buy_num == "5":
                    if self.bounty >= recup.bounty:
                        self.bounty -= recup.bounty
                        self.recup += recup.recup
                        print(f"You purchased {recup.name} increasing your health regeneration to {self.recup}.")
                    else:
                        print("Not enough coins.")
                if buy_num == "q":
                    break
        def recuperate(self):
            roll = random.randrange(11)
            if roll < self.recup + 1:
                self.health += 2
                if self.name == "You":
                    print("You restored some health")
                else:
                    print(f"The {self.name} restored some health")
        def reset_health(self):
            self.health = self.health2


    class Goblin(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical

    class Hero(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical
    
    class Zombie(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical

    class Treeman(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical

    class Shadow(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical

    class Bandit(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical
    
    class Wizard(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical

    class Orc(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical

    class Highwayman(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical
    
    class Dragon(Character):
        def __init__(self, name, health, health2, power, evade, recup, resur, bounty, armor, critical):
            self.name = name
            self.health = health
            self.health2 = health2
            self.power = power
            self.evade = evade
            self.recup = recup
            self.resur = resur
            self.bounty = bounty
            self.armor = armor
            self.critical = critical

    # def character_choose():
    #     character_choice = input("Welcome! \n ")

    #        name, health, damage, evade chance, recup chance, resurrect ability, bounty, armor, critical
    
        
    goblin = Goblin("Goblin", 6, 6, 2, 0, 0, 0, 5, 0, 0)
    hero = Hero("Hero", 10, 10, 5, 1, 0, 0, 20, 0, 2)
    zombie = Zombie("Zombie", 4, 4, 1, 0, 3, 0, 5, 0, 0)
    treeman = Treeman("Treeman", 8, 8, 3, 0, 2, 0, 10, 0, 0)
    shadow = Shadow("Shadow", 1, 1, 2, 9, 0, 0, 15, 0, 0)
    orc = Orc("Orc", 12, 12, 3, 0, 0, 0, 15, 1, 0)
    bandit = Bandit("Bandit", 7, 7, 3, 1, 0, 0, 10, 0, 0)
    highwayman = Highwayman("Highwayman", 6, 6, 3, 0, 0, 0, 10, 1, 0)
    dragon = Dragon("Dragon", 20, 20, 9, 1, 0, 0, 100, 2, 1)
    wizard = Wizard("Wizard", 10, 10, 15, 0, 0, 0, 75, 0, 0)

    playable_characters = [goblin, hero, treeman, shadow, orc, bandit, zombie, highwayman]
    bosses = [dragon, wizard]

    char_num = 1
    for char in playable_characters:
        print(char_num, char.name)
        char_num +=1

    character_num = int(input("Choose the character you want to play as: \n"))
    character_choice = playable_characters[character_num - 1]
    character_choice.name = "You"
    character_choice.bounty = 0
    
    enemies = [goblin, treeman, shadow, orc, zombie, bandit, highwayman]
    del enemies[character_num-1]
    
    size = 11
    half = 5
    map = []
    coordinate = [0, 0]

    def create_map():
        for y in range(0,size):
            map.append([])
            for z in range(0,size):
                map[y].append(" ")
    
    def print_board(map, coordinate):
        co_x = coordinate[0]
        co_y = coordinate[1]
        for y in range(0, size):
            print(" ")
            for x in range(0, size):
                if x == half and y == half:
                    print("Y", end = " ")
                else:
                    print(map[y + co_y][x + co_x], end = " ")
        print(" ")
    
    def generate_map_horizontal(map, vert):
        temp_list = []
        roll1 = random.randrange(22)
        roll2 = random.randrange(22)
        if vert == "up":
            for x in range(len(map[0])):
                if x == roll1 or x == roll2:
                    temp_list += random.choice(space_list)
                else:
                    temp_list += " "
            map.insert(0, temp_list)
            coordinate[1] +=1
        if vert == "down":
            for x in range (len(map[-1])):
                if x == roll1 or x == roll2:
                    temp_list += random.choice(space_list)
                else:
                    temp_list += " "
            map.insert(len(map), temp_list)
            
    def generate_map_vertical(map, hor):
        roll1 = random.randrange(22)
        roll2 = random.randrange(22)
        if hor == "left":
            count = 0
            for item in map:
                if count == roll1 or count == roll2:
                    item.insert(0, random.choice(space_list))
                    
                else:
                    item.insert(0, " ")
                count +=1
            coordinate[0] +=1
        if hor == "right":
            count = 0
            for item in map:
                if count == roll1 or count == roll2:
                    item.append(random.choice(space_list))
                else:
                    item.append(" ")
                count +=1
    space_list = ["$", "$", "!", "?", "?", "?", "?", "?", "?"]
        
    def check_position():
        co_x = coordinate[0] + half
        co_y = coordinate[1] + half

        if map[co_y][co_x] == "$":
            character_choice.store()
        if map[co_y][co_x] == "G":
            character_choice.fighting(goblin)
        if map[co_y][co_x] == "O":
            character_choice.fighting(orc)
        if map[co_y][co_x] == "W":
            character_choice.fighting(wizard)
        if map[co_y][co_x] == "D":
            character_choice.fighting(dragon)
        if map[co_y][co_x] == "S":
            character_choice.fighting(shadow)
        if map[co_y][co_x] == "Z":
            character_choice.fighting(zombie)
        if map[co_y][co_x] == "T":
            character_choice.fighting(treeman)
        if map[co_y][co_x] == "B":
            character_choice.fighting(bandit)
        if map[co_y][co_x] == "H":
            character_choice.fighting(highwayman)
        if map[co_y][co_x] == "!":
            opponent = random.choice(bosses)
            map[co_y][co_x] = opponent.name[0]
            character_choice.fighting(opponent)
        if map[co_y][co_x] == "?":
            opponent = random.choice(enemies)
            map[co_y][co_x] = opponent.name[0]
            character_choice.fighting(opponent)
        
    def defeated_enemy():
        co_x = coordinate[0] + half
        co_y = coordinate[1] + half
        map[co_y][co_x] = " "
    
    def travelling():
        go = "yes"
        create_map()
        while character_choice.alive() and go == "yes":
            print_board(map, coordinate)
            print(f"{character_choice.health * heart_symbol} -- {character_choice.bounty} coins.")
            direction = input("Use WASD to move. 'q' to quit. \n")
            if len(direction) == 1:
                if direction == "w":
                    if coordinate[1] == 0:
                        generate_map_horizontal(map, "up")
                    coordinate[1] -= 1
                    go = "no"
                if direction == "s":
                    if coordinate[1] == len(map) - size:
                        generate_map_horizontal(map, "down")
                    coordinate[1] += 1
                    go = "no"
                if direction == "a":
                    if coordinate[0] == 0:
                        generate_map_vertical(map, "left")
                    coordinate[0] -= 1
                    go = "no"
                if direction == "d":
                    if coordinate[0] == len(map[0]) - size:
                        generate_map_vertical(map, "right")
                    coordinate[0] += 1
                if direction == "q":
                    print("Goodbye")
                    exit()
                check_position()
            else:
                print("Invalid input. Use WASD keys to move.")
    



    

    while character_choice.alive():
        # exiting = "no"
        # opponent = random.choice(enemies)
        character_choice.print_status()
        travelling()
        # print(f"You have {character_choice.bounty} coins.")
        # print("What do you want to do?")
        # print("1. fight an enemy")
        # print("2. go to store")
        # print("q. quit game.")
        # print("> ", end=' ')
        # raw_input = input()
        # if raw_input == "1":
        #     character_choice.fighting(opponent)
        #     exiting = "yes"
        # elif raw_input == "2":
        #     character_choice.store()
        #     exiting = "yes"
        # elif raw_input == "q":
        #     exit()
        # elif exiting == "no":
        #     print("Invalid input {}".format(raw_input))



main()