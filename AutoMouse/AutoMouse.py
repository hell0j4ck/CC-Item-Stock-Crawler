import pyautogui
import time
import random


print("\n__Developer__: Jack Jabra\n")
print("__Copyright__: Copyright © 2022 Jack Jabra\n")
print("__License__: Public\n")
print("__Version: 1.0\n")
print("DISCLAIMER: I will not be held responsible for the illegitimate use of this tool.\n")

print('ATTENTION: In order to terminate this script, please use CTRL+C while the console is visible. \nOtherwise move your mouse to the top left corner of your screen to terminate.\n \n')

input('Press ENTER to continue...\n \n \n \n \n')

def moveclick():
    
    counter=0
    
    while True:

        randomNumberX = random.randint(0,500)
        randomNumberY = random.randint(0,500)

        pyautogui.moveTo(randomNumberX, randomNumberY, duration=1)
        pyautogui.click()
        counter=counter+1
        time.sleep(movedelay)
        continue
        
        
def movenoclick():
    
    counter=0
    
    while True:

        randomNumberX = random.randint(0,500)
        randomNumberY = random.randint(0,500)

        pyautogui.moveTo(randomNumberX, randomNumberY, duration=0.5)
        counter=counter+1
        time.sleep(movedelay)
        continue
        
        
while True:
    
    movedelay = input('How many seconds would you like between mouse moves? ')
    
    try:
        movedelay = float(movedelay)
        
    except:
        
        print('\nNot a valid number\n')
        continue
        
    if movedelay < 2:
        
        print('\nPlease choose a delay over 2 seconds.\n')
        continue
    
        
    else:
        
        pass
    
    
    while True:
        
        click = input('\nDo you want mouse clicks along with movement? Y/N ')
        
        
        if click == 'y' or click == 'Y':

            moveclick()
            break

        elif click == 'n' or click == 'N':

            movenoclick()
            break


        else:

            print('\nPlease choose Y or N\n')
            continue

    break



    
