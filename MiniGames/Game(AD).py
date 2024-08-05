import math
import random



def begginning():
    Start1 = input('Hello Adventurer, what is your name? ')
    print('Hello, ' + (Start1) + (' welcome to this typed adventurer game. I will be asking a few starting questions to get your character made!'))
    
    wChoice = input('First lets see what weapon you want. Your choices are \n' + 'SWORD 12\n'+'DAGGER 9\n'+'GREATAXE 15\n').lower()

    
    Weapon = wChoice

    if Weapon == 'sword':
        print('You have chosen the sword as your first weapon')
    elif Weapon == 'dagger':
        print('You have chosen the dagger as your first weapon')
    elif Weapon == 'greataxe':
        print('You have chosen the greataxe as your first weapon')
    
    # Get the loop working so that it'll keep asking till getting a correct answer!
    
    #Get sidearms working

    """else:
        while Weapon != 'sword' or 'dagger' or 'greataxe':
            wChoice = input("I'm sorry that's not an option, please pick one. Sword, Dagger, Greataxe").lower()
            Weapon = wChoice
    """    
    '''offHand = input=("Would you like a sidearm?").lower
    if offHand == 'yes':
        SideArm = input('what would you like your off hand to be?:\n'+'Flintlock\n'+'Shield\n'+'Torch\n')
    elif offHand == 'no':
        print('Alright you will be continuing without a offhand.')
    '''
 
class Forest():



 

begginning()
