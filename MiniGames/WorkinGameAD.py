import random
import time

#Health for the character depending on choice
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

#Pops up when the game in in the main menu
def StatusMenu(UserName,Race,money,fatigue,health):
    print(f"\n{UserName}'s Status:")
    print(f'Race: {Race}')
    print(f'Money: ${money}')
    print(f'Fatigue: {fatigue}')
    print(f'Health: {health}')

def enounters():
    pass

#Skills
Fireball = [14]
WaterBall = [14]
IceShard = [14]
WindBlade = [14]
LightningBolt = [14]
Heal = [25]
Siphon = [17]
DaggerThrow = [15]
VerticalSlash = [17]
CrushingBlow = [22]
ManaMissile = [19]
Crush = [23]
DragonBreath = [25]
TestKill = [100000]



#Skill categories
def skills(FireSkills, WaterSkills,IceSkills,WindSkills,LightningSkills,HolySkills,DarkSkills,LightWeaponSkills,MediumWeaponSkills,HeavyWeaponSkills,MiscSkills,RaceSkills):
    FireSkills = [Fireball]
    WaterSkills = [WaterBall]
    IceSkills = [IceShard]
    WindSkills = [WindBlade]
    LightningSkills = [LightningBolt]
    HolySkills = [Heal]
    DarkSkills = [Siphon]
    LightWeaponSkills = [DaggerThrow]
    MediumWeaponSkills = [VerticalSlash]
    HeavyWeaponSkills = [CrushingBlow]
    MiscSkills = []
    RaceSkills = [ManaMissile,Crush,DragonBreath,TestKill]



def skillList():
    pass

#Runs when the player is in a fight EX: Goblin
def FightMenu(AdventureCompletion):
    print('-----------------------')
    print(f'Adventure Length: {AdventureCompletion}')
    print('-----------------------')
    print('1. Attack')
    print('2. Block')
    print('3. Skill List')#Skilllist
    print('4. Rest')
    print('5. Run')

#The code handling the adventure players go on and pickin random encounters
def adventure(fatigue, health, AdventureCompletion,money,damage,): 
    
    AdventureCompletion = int(AdventureCompletion)
    AdventureDistance = random.randint(10,20)
    AdventureCompletion -= AdventureDistance
    
    fatigue += random.randint(10,25)
    if fatigue > 100:
        fatigue = 100

    encounter = random.choice(['goblin'])


    Alive, encounter, fatigue, health, money, damage,AdventureCompletion = encountersHandle(encounter, fatigue, health, money, damage, AdventureCompletion)
    
    if not Alive or health <= 0:
        return True, fatigue, health, money, damage, AdventureCompletion

    if AdventureCompletion <= 0:
        print('\nYou have completed your quest!')
        return True, fatigue, health, money, damage, AdventureCompletion
    
    if fatigue == 100:
        health -= random.randint(10,17)
    
    if health <= 0:
        print('\nYou have died...Restarting')
        return True, fatigue, health, money, damage, AdventureCompletion
  
  
    return False, fatigue, health, money, damage, AdventureCompletion


# Mob holding
goblin = [random.randint(37,50),7]
evilRabbit = [random.randint(20,35),5]
orcBoss = [random.randint(80,130),15]


#Putting out every encounter a player can have happen
def encountersHandle(encounter, fatigue, health, money, damage,AdventureCompletion):
    Alive = True
    
    if encounter == 'good':
        print('You found a pouch of money.')
        money += 25
    
    elif encounter == 'bad':
        print('You tripped in front of another group of adventurers. -1000 Aura')
    
    elif encounter == 'neutral':
        print('Nothing happened.')
    
    elif encounter == 'goblin':
        print('A goblin jumped out in front of you\n')
        gHealth = goblin[0]
        while gHealth > 0:
            gDamage = goblin[1]
            health -= gDamage
            time.sleep(2)
            if gDamage == 'blocked':
                gDamage = 0
                print(f'You blocked the goblins attack your health is now {health}\n')
            else:
                print(f'\nThe goblin did {gDamage} your health is now {health}\n')
            
            if health <= 0: #Checking if player has died
                print('You have died.')
                Alive = False
                break
            
            FightMenu(AdventureCompletion)
            FightPrompt = input('What would you like to do?')
            if FightPrompt == '1': # Attack
                gHealth -= damage
                if gHealth <0:
                    gHealth = 0
                print(f'You did {damage} to the goblin, it has {gHealth} health left...')
            elif FightPrompt == '2': # Block
                blockReduction = random.randint(7, 15)
                gDamage = max(gDamage - blockReduction, 0)  # Ensure that gDamage does not go below 0
                
                print(f'You blocked {blockReduction}')

            elif FightPrompt == '3': #skill list
                print('Skill list coming soon...')
            elif FightPrompt == '4': # Rest
                rest(health)
                print('You rested and gained health')
            elif FightPrompt == '5': #Run
                print('You ran away')
                break
            
            if gHealth <= 0: #Goblin death
                time.sleep(1)
                print("\nYou have defeated the goblin\n")
                money_drop = random.randint(25,50)
                money += money_drop
                print(f'\nYou found {money_drop} money. You now have {money}.\n')
                break
        
    return True, encounter, fatigue, health, money, damage, AdventureCompletion


#Base damages for the starter weapons
def weaponDamage(weapon):
    if weapon == 'sword':
        return 12
    elif weapon == 'dagger':
        return 9
    elif weapon == 'greataxe':
        return 15

#A healing function for in the main menu (Needs to be added to the fight menu)
def rest(health):
    health += 10
    if health > 1000:
        health = 1000
    return health


#Will handle the difficulties
def gameMode():
    pass


#The start up code that will send and take data from outside of this function
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
    WeaponChoice = input('1. Sword\n' + '2. Dagger\n' + '3. GreatAxe\n')
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
    GameOver = False
    print('gaming')
    while not GameOver:
        print('gaming2')
        adventure_ongoing, fatigue, health, money, damage, AdventureCompletion = adventure(fatigue, health, AdventureCompletion, money, damage)
        if adventure_ongoing:
            GameOver = True
        else:
            print("The adventure continues...")  # Continue with the adventure
            
    while not GameOver:
            StatusMenu(UserName, Race, money, fatigue, health)
            choice = input('\nChoose an action:\n1. Adventure\n2. Travel\n3. Rest\n4. Interact\n5. Search\n\nInput a choice:')
            if choice == "1":
                AdventureSelect = input('What adventure difficulty would you like?\n1. Easy\n2. Medium\n3. Hard\n')
                if AdventureSelect == '1':
                    AdventureCompletion = random.randint(100, 170)
                if AdventureSelect == '2':
                    AdventureCompletion = random.randint(150, 250)
                if AdventureSelect == '3':
                    AdventureCompletion = random.randint(200, 400)
                
                GameOver, fatigue, health, money, damage, AdventureCompletion = adventure(fatigue, health, AdventureCompletion, money, damage)
            elif choice == '3':
                health = rest(health)
            
            if choice == '.':
                GameOver = True
                break
            else:
                print('INVALID CHOICE: Please try again')
                

Game()
    

    
#Kim - "I would be such a good discord kitten."