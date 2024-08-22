import random
import time
import sqlite3

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

#Menus

#Pops up when the game in in the main menu
def StatusMenu(UserName,Race,money,fatigue,health):
    print(f"\n{UserName}'s Status:")
    print(f'Race: {Race}')
    print(f'Money: ${money}')
    print(f'Fatigue: {fatigue}')
    print(f'Health: {health}')

#Runs when the player is in a fight EX: Goblin
def FightMenu(AdventureCompletion):
    print('-----------------------')
    print(f'Adventure Length: {AdventureCompletion}')
    print('-----------------------')
    print('1. Attack')
    print('2. Block')
    print('3. Skill List') #Skilllist
    print('4. Rest')
    print('5. Run')

def TravelMenu():
    print('1. Artoria')
    print('2. Stoneheart Fort')
    print('3. Hunius Castle')
    print('4. Trinket Village')

def TownMenu():
    print('1. Shop')
    print('2. Quest Board')
    print('3. Bank')
    print('4. Chat')
    print('5. leave')



def TownInteractions(money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance):
    TownMenu()
    inTown = True
    while inTown is True: 
        
        TownInput = input('What would you like to do here? ')
        if TownInput == '1':
            print(f'Welcome to the {TownLocation} shop.')
            print('----------------------------')
            print('1. Steel Sword - DMG: 17 Cost: 160')
            print('2. Knight Armor - +50 Health Cost: 300')
            print('3. Exit Shop')
            ShopInput = input('What would you like to buy? ')
            
            if ShopInput == '1':
                if money >= 160:
                    weapon = 'Steel Sword'  # Use assignment here
                    print('You bought a Steel Sword')
                    money -= 160
                    damage = 17
                else:
                    print("You don't have enough money.")
                    
            elif ShopInput == '2':
                if money >= 300:
                    health += 50
                    print('You bought Knight Armor') 
                    money -= 300
                else:
                    print("You don't have enough money.")
            else:
                print('Please input a valid choice')
            
            return money, damage, UserName, health, TownSelect, TownLocation, weapon,BankBalance
        elif TownInput == '2':
            pass
        elif TownInput == '3':
            print(f'\nHello, welcome to {TownLocation} bank, your current balance is {BankBalance}.\n What would you like to do?\n 1. Deposit\n 2. Withdrawl\n3. View Account\n')
            BankInput = input('Please input an option')
            if BankInput == '1':
                BankAmount = int(input('How much would you like to deposit? '))
                if BankAmount >= money:
                    print("You don't have that much money, please try again or leave")
                elif BankAmount < 0:
                    print('Please give a valid amount')
                else:
                    BankBalance = BankBalance + BankAmount
                    print(f'You have put in {BankAmount} into your account, you now have {BankBalance} in your account.')
            elif BankInput == '2':
                BankAmount = int(input('How much would you like to withdrawl? '))
                if BankAmount >= BankBalance:
                    print(f"You don't have enough to take out. You have {BankBalance} in your account.")
                elif BankAmount <= 0: 
                    print(f'Please input a valid input')
                elif BankInput == '3':
                    BankBalance = BankBalance - BankAmount
                    print(f'You have withdrawed {BankAmount} from your account, you now have {BankBalance}')
            return money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance

        elif TownInput == '4':
            print('1. Kim')
            print('2. Caedmon')
            print('3. Alaina')
            print('4. Daniil')
            NpcChat = input('Who would you like to talk to?')
            if NpcChat == '1':
                CurrentNPC = 'Kim'
                print(f'You bumped into something while walking in the plaza of {TownLocation}. You look around and see nothing new...this was until you gazed down at this short statured women who had her gaze in a book. She was short, with brown bangs and squinted eyes.')
                print('\n???: Erm, I was walking this way. Please move out the way...\n')
                time.sleep(.5)
                print('1. Who are you? / 2. Ignore Her')
                KimChat = input('Please select a dialogue choice...')
                if KimChat == '1':
                    print(f'\n{UserName}: Who are you?\n')
                    print("Why, I'm the red queen of course, now please move\n")
                elif KimChat == '2':
                    print(f'{UserName} has ignored the random girl, she clearly did not take a liking to that...')
                    print('???: HEY YOU! You think you can bump into someone and walk away? You will never guess that I am the RED QUEEN')
                    health -= 10
                    print(f'The "red queen" kicked {UserName} dealing 10 damage.')
                    print('')

        elif TownInput == '5':
            print('You left the town.')
            inTown = False
            break


        
        return money, damage, UserName, health, TownSelect, TownLocation, weapon,BankBalance

def enounters():
    pass

#Skills
Fireball = [25]
WaterBall = [25]
IceShard = [25]
WindBlade = [25]
LightningBolt = [25]
Heal = [35]
Siphon = [27]
DaggerThrow = [25]
VerticalSlash = [35]
CrushingBlow = [40]
ManaMissile = [25]
Crush = [30]
DragonBreath = [30]
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



def skillList(skills,Race):
    if Race == 'elf':
        pass
    elif Race == 'orc':
        pass
    elif Race == 'dragonkin':
        pass
    elif Race == 'test':
        pass

    pass


#The code handling the adventure players go on and pickin random encounters
def adventure(fatigue, health, AdventureCompletion,money,damage,): 
    
    AdventureCompletion = int(AdventureCompletion)
    AdventureDistance = random.randint(10,20)
    AdventureCompletion -= AdventureDistance
    
    fatigue += random.randint(10,25)
    if fatigue > 100:
        fatigue = 100

    encounter = random.choice(['goblin2'])


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
#'boar':[40,15],'skeleton':[50,20],'goblin':[]'

EncounterList = {'troll':[random.randint(40,70),15],'boar':[random.randint(25,37),7],'skeleton':[random.randint(50,90),12],'goblin':[random.randint(37,50),10],
                 'Giant Spider':[random.randint(60,100),18],'Angry Plant':[random.randint(25,37),11],'Stone Golem':[random.randint(100,120),40],'Bandit':[random.randint(100,130),9],
                 'Giant Lizard':[random.randint(40,90),15],'Orb Boss':[random.randint(80,130), 30],'Poison Snake':[random.randint(50,90),22],'Evil Rabbit':[random.randint(20,35),7]}

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
        
    elif encounter == 'goblin2':
            
            if encounter == 'goblin2':
                rEncounterKey = random.choice(list(EncounterList.keys()))
            else:
                rEncounterKey = encounter

            rEncounterKey = random.choice(list(EncounterList.keys()))
            rEncounter = EncounterList[rEncounterKey]
            print(f'You encountered an, {rEncounterKey}...')

            eHealth = rEncounter[0]
            eDamage = rEncounter[1]
            
            while eHealth > 0:
                health -= eDamage
                time.sleep(2)
                if eDamage == 'blocked':
                    eDamage = 0
                    print(f'You blocked the {rEncounterKey} attack your health is now {health}\n')
                else:
                    print(f'\nThe {rEncounterKey} did {eDamage} your health is now {health}\n')
                
                if health <= 0: #Checking if player has died
                    print('You have died...respawning')
                    Alive = False
                    time.sleep(1)
                    break
                
                FightMenu(AdventureCompletion)
                FightPrompt = input('What would you like to do?')
                if FightPrompt == '1': # Attack
                    eHealth -= damage
                    if eHealth <0:
                        eHealth = 0
                    print(f'You did {damage} to the {rEncounterKey}, it has {eHealth} health left...')
                elif FightPrompt == '2': # Block
                    blockReduction = random.randint(7, 15)
                    eDamage = max(eDamage - blockReduction, 0)  # Ensure that gDamage does not go below 0
                    print(f'You blocked {blockReduction}')
                elif FightPrompt == '3': #skill list
                    print('Skill list coming soon...')
                elif FightPrompt == '4': # Rest
                    rest(health)
                    print('You rested and gained health')
                elif FightPrompt == '5': #Run
                    print('You ran away')
                    break
                if eHealth <= 0: #Goblin death
                    time.sleep(1)
                    print(f"\nYou have defeated the {rEncounterKey}\n")
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
    global BankBalance 
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

            if choice == '2':
                TravelMenu()
                TownSelect = input('Input a town to go to...')
                if TownSelect == '1':
                    TownLocation = 'artoria'
                    money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance = TownInteractions(money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance)
                elif TownSelect == '2':
                    TownLocation = 'stoneheart fort'
                    money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance = TownInteractions(money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance)
                elif TownSelect == '3':
                    TownLocation = 'hunius castle'
                    money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance = TownInteractions(money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance)
                elif TownSelect == '4':
                    TownLocation = 'Trinket Village'
                    money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance = TownInteractions(money, damage, UserName, health, TownSelect, TownLocation, weapon, BankBalance)
                else:
                    print('\nPlease select a valid choice.\n')

                
            elif choice == '3':
                health = rest(health)
            
            if choice == '.':
                GameOver = True
                break
            else:
                print('INVALID CHOICE: Please try again')
                
BankBalance = 0
Game()
    

    
#Kim - "I would be such a good discord kitten."
#Kim - "I do tricks on something else"
#Kim - "Red queen type shit."
