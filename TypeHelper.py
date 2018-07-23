import pyautogui, time, random, sys

def typeMonkeyAhAhAh(targetWPM=75,posX=0,posY=0):
    pyautogui.click(posX,posY)

    text_file = open("TypeHelper.txt", "r")
    text = text_file.read()
    charList=list(text)

    charsPerWord= len(charList)/len(text.split())
    charsPerSecond=targetWPM*charsPerWord/60
    delayPerChar=1/charsPerSecond
    pyautogui.typewrite(charList,delayPerChar*(random.random()/10*4+.8))

def targetWPMFunc():
    targetWPM = pyautogui.prompt('What is your target WPM? \nLeave blank for default of 75wpm')
    if targetWPM==None:
        return None
    try:
        return int(targetWPM)
    except:
        targetWPM = 75
        return targetWPM

def targetPosFunc():
    while True:
        try:
            targetPos = pyautogui.prompt('What is your target X and Y position?\nFormat:     100 700')
            if targetPos == None:
                return None,None
            pos=targetPos.split()
            x=int(pos[0])
            y=int(pos[1])
            return x,y
        except: pass

def wheretoClick():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            time.sleep(.01)
            sys.stdout.write('\r' + positionStr)
    except KeyboardInterrupt:
        print('\n')

def instructions():
    pyautogui.alert(text='\n\nTo use, create a file'
                         'named "TypeHelper.txt" in the same directory as this executable.'
                         ' Open, put in your text, and save the text file.\n\nTo find mouse position, '
                         'use "Find mouse position" on the menu, watch output for coordinates.'
                         '\n\nThe rest should be self explanatory. :) ', title='Instructions', button="Let's go!")

def choosePath():
    restartOptions=True
    while(restartOptions):
        restartOptions = False
        options=['Write text', 'Find mouse position', 'Instructions', 'Cancel']
        choice= pyautogui.confirm(text='This program is used to type text at a specific WPM.\n\nYou choose the location on screen and the WPM rate.', title='Main Menu', buttons=[*options])
        print (choice)
        if choice == options[0]:
            targetWPM=targetWPMFunc()
            if not targetWPM==None:
                x,y = targetPosFunc()
                print (x,y, targetWPM )
                if not x == None or not y==None:
                    typeMonkeyAhAhAh(targetWPM,x,y)
        if choice == options[1]:
            wheretoClick()
        if choice == options[2]:
            instructions()
            restartOptions=True
        if choice == options[3]: exit()


choosePath()




