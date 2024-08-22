import math
import random
import time

def getSpeciesHealth(Race):
    if Race == 'human':
        return 100
    elif Race == 'elf':
        return 90
    elif Race == 'orc':
        return 110
    elif Race == 'dragonkin':
        return 120
    elif Race == 'test':
        return 10000000


def MainMenu(UserName,Race,money,fatigue,health):
    print(f"\n{UserName}'s Status:")
    print(f'Race: {Race}')
    print(f'Money: ${money}')
    print(f'Fatigue: {fatigue}')
    print(f'Health: {health}')


def FightMenu():
    pass

def adventure(fatigue,health,AdventureCompletion): 
    AdventureDistance = random.randint(10,20)
    AdventureCompletion -= AdventureDistance
    fatigue += random.randint(10,25)
    if fatigue > 100:
        fatigue = 100
    encounter = random.choice(['good','bad','neutral'])
    fatigue, health = encountersHandle(encounter,fatigue,health)
    if AdventureCompletion <= 0:
        print('\nYou have completed your quest!')
        return fatigue,health,AdventureCompletion
    if fatigue == 100:
        health -= random.randint(10,17)
    if health <= 0:
        print('\nYou have died...')
        return True,fatigue,health,AdventureCompletion
    return False,fatigue,health,AdventureCompletion

def encountersHandle(encounter,fatigue,health):
    if encounter == 'good':
        pass
    elif encounter == 'bad':
        pass
    elif encounter == 'neutral':
        pass
    return fatigue,health


def weaponDamage(weapon):
    if weapon == 'sword':
        return 12
    elif weapon == 'dagger':
        return 9
    elif weapon == 'greataxe':
        return 15


def rest(health):
    health += 10
    if health > 1000:
        health = 1000
    return health

def gameMode():
    pass

def Game():
    print('''In the fractured kingdom of Arlathia, ancient magic stirs as dark forces rise from forgotten depths. 
You, an adventurer drawn by fate, must navigate a world on the brink of chaos. 
Whether warrior, mage, or rogue, your choices will shape the destiny of Eldoria. Welcome to a land where legends are born, and only the bold survive.''')
    
    print('Welcome to the Adventure game! Lets start by making your character. . .')
    UserName = input('What would you like your character name to be? ')
    NameCheck = input('You want your name to be ' + (UserName) + '?' + ' Yes/No\n').lower()
    while NameCheck != 'yes':
         UserName = input('What would you like your characters name to be?')
         NameCheck = input('You want your name to be ' + (UserName) + '?' + ' Yes/No\n').lower()
         if NameCheck == 'yes':
             break    
    print('Perfect! Now ' + (UserName) + 'What weapon would you like?')
#Weapon
    WeaponChoice = input('Sword\n' + 'Dagger\n' + 'GreatAxe\n').lower()
# Use the 'and' operator to check if the choice is not any of the valid options
    while WeaponChoice != '1' and WeaponChoice != '2' and WeaponChoice != '3':
         print('Please select a valid weapon choice.')
         WeaponChoice = input('\n1. Sword\n' + '\n2. Dagger\n' + '\n3. GreatAxe\n\n')
    if WeaponChoice == "1":
        weapon = 'sword'
    elif WeaponChoice == '2':
        weapon = 'dagger'
    elif WeaponChoice == '3':
        weapon = 'greataxe'
# At this point, the user has chosen a valid weapon
    print(WeaponChoice + " that's a great choice.")
#Location
    LocationChoice = input('Where would you like to start?\n1. Forest\n2. Tundra\n3. Ocean\n4. Field\n5. Desert\n\n')
    while LocationChoice != '1' and LocationChoice != '2' and LocationChoice != '3' and LocationChoice != '4' and LocationChoice != '5':
            print('Please input a valid choice.')
            LocationChoice = input('Where would you like to start?\n1. Forest\n2. Tundra\n3. Ocean\n4. Field\n5. Desert\n\n')
    if LocationChoice == '1':
        startLocation = 'forest'
    elif LocationChoice == '2':
        startLocation = 'tundra'
    elif LocationChoice == '3':
        startLocation = 'ocean'
    elif LocationChoice == '4':
        startLocation = 'field'
    elif LocationChoice == '5':
        startLocation = 'desert'
    print('Alright, you will be starting in the ' + startLocation + '...')

    
#Race
    RaceChoice = input('What race would you like your character to be?\n1. Human\n2. Elf\n3. Orc\n4. Dragonkin\n\n')
    while RaceChoice != '1' and RaceChoice != '2' and RaceChoice != '3' and RaceChoice != '4' and RaceChoice != '5':
        print('Please select a valid race choice.')
        RaceChoice = input('What race would you like your character to be?\n1. Human\n2. Elf\n3. Orc\n4. Dragonkin\n\n')
        
    if RaceChoice == '1':
        Race = 'human'
    elif RaceChoice == '2':
        Race = 'elf'
    elif RaceChoice == '3':
        Race = 'orc'
    elif RaceChoice == '4':
        Race = 'dragonkin'
    elif RaceChoice == '5':
        Race = 'test'
    print(UserName+' you will be a ' + Race)

#Difficulty    
    DifficultyChoice = input('Alright one last thing. What would you like your difficulty to be?\n1. Easy\n2. Medium\n3. Hard\n\n')
    while DifficultyChoice != '1' and DifficultyChoice != '2' and DifficultyChoice != '3' and DifficultyChoice != '4' and DifficultyChoice != '5':
        print('Please select a valid race choice.')
        DifficultyChoice = input('Alright one last thing. What would you like your difficulty to be?\n1. Easy\n2. Medium\n3. Hard\n\n')
    if DifficultyChoice == '1':
        difficulty = 'easy'
    elif DifficultyChoice == '2':
        difficulty = 'medium'
    elif DifficultyChoice == '3':
        difficulty = 'hard'
    print('You will be starting on the ' + difficulty + ' difficulty...')

    Alive = True

    while Alive:
        GameOver = False
    
    health = getSpeciesHealth(Race)
    fatigue = 0
    money = 150
    damage = weaponDamage(weapon)
    
    #Get health from class "theCharacter"
    #theCharacter = avatar()
    while not GameOver:
        MainMenu(UserName,Race,money,fatigue,health)
        choice = input('\n Choose an action:\n1. Adventure\n2. Travel\n3. Rest\n4. Interact\n5. Search\n\nInput a choice:')
        
        if choice == "1":
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            health = rest(health)
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        else:
            print('INVALID CHOICE: Please try again')





Game()
    

    
#Kim - "I would be such a good discord kitten."