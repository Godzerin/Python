class character:

    def __init__(self,name,race,weapon,StartingArea,difficulty):
        
        name = input('Hello Adventurer, what is your name? ')
        print('Hello, ' + (name) + ' welcome to this typed adventurer game. I will be asking a few starting questions to get your character made!')
        raceC = input('First lets see what race you want to be, your choices are... \n' + 'HUMAN\n'+'ELF\n'+'ORC\n'+'DRAGONKIN\n').lower()
        race = raceC
        print('Perfect, you have chosen ' + (race) + '...')
        weapon = input('Alright second, lets see what weapon you want, your choices are... \n' + 'SWORD 12\n'+'DAGGER 9\n'+'GREATAXE 15\n').lower()
        print('You have chosen ' + (weapon) + '...')
        StartingArea = input('Next, lets see what weapon you want. Your choices are \n' + 'FOREST\n'+'TUNDRA\n'+'FIELD\n'+'OCEAN\n'+'DESERT\n').lower()
        print('You will be starting in the ' + (StartingArea)+'...')
        difficultyC = input('Lastly, lets see what weapon you want. Your choices are \n' + 'EASY\n'+'MEDIUM\n'+'HARD\n').lower()
        
        difficulty == difficultyC
        if difficulty == "easy":
            print("So you don't want a challenge?")
        elif difficulty == 'medium':
            print('This should be the default AT LEAST')
        elif difficulty == 'hard':
            print('As you should')


    def race
