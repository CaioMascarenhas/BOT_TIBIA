import pyautogui as pg
import time

REGION_PARTY = (1570,135,171,147)
REGION_LIFE = (1599,200)
REGION_GRANSIO= (1447,140,144,139)


def Sio ():

    while True:
        if pg.pixelMatchesColor(1597, 171, (96, 191, 96)):  #cor verde
            pg.press('F7')
            time.sleep(0.05)
            pg.press('F7')
            print('Usando Sio... vida no verde')
            pg.sleep(1)

        if pg.pixelMatchesColor(1597, 171, (191, 191, 0)):   #cor amarela
            if pg.pixelMatchesColor(1652,171,(75,75,75)) and pg.locateOnScreen('imgs/region_gransio.png', confidence=0.9, region=REGION_GRANSIO):
                pg.press('F8')
                time.sleep(0.05)
                pg.press('F8')
                print('Usando GRANSIO... vida no amarelo')
                pg.sleep(1)
            else:
                pg.press('F7')
                time.sleep(0.05)
                pg.press('F7')
                print('Usando sio... vida no amarelo')
                pg.sleep(1)

        if pg.pixelMatchesColor(1597,171,(191,48,48)) or pg.pixelMatchesColor(1597,171,(95,0,0)):  #cor vemelha ou preta
            if pg.locateOnScreen('imgs/region_gransio.png', confidence=0.9, region= REGION_GRANSIO):
                pg.press('F8')
                time.sleep(0.05)
                pg.press('F8')
                print('Usando GRANSIO... vida no vermelho ou preto ')
                pg.sleep(1)
            else:
                pg.press('F7')
                time.sleep(0.05)
                pg.press('F7')
                pg.sleep(1)
                print('Usando Sio... vida no vermelho ou preto ')
                
print('Começando...')
#pg.displayMousePosition()
Sio()