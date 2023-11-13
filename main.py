import pyautogui as pg
import keyboard  
import wasp_script
import threading
import time

def main():
    print('Welcome to tibia bot! choose the specified script you wanna use!.')
    print('wasp_Script_abdendriel = 1')
    script = int(input())

    if script == 1:
        print('digite a letra: h para começar!.')
        keyboard.wait('h')
        while parada:
            wasp_script.hunt_wasp()
            time.sleep(1)
        

def stop():
   global parada
   parada = True
   while True:
        if keyboard.is_pressed('p'):
            parada = not parada
            print('Parando execução do script')
            break

thread_stop = threading.Thread(target=stop)

thread_stop.start()

main()

thread_stop.join()