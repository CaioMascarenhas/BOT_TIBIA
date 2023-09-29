import pyautogui as pg
import keyboard  
import wasp_script

def main():
    print('Welcome to tibia bot! choose the specified script you wanna use!.')
    print('wasp_Script_abdendriel = 1')
    script = int(input())

    if script == 1:
        print('digite a letra: h para começar!.')
        keyboard.wait('h')
        wasp_script.hunt_wasp()
        
        



main()