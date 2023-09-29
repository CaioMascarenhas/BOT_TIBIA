import pyautogui as pg
import time
import constants


def check_battle():
    return pg.locateOnScreen('imgs/region_battle.png', region=constants.REGION_BATTLE)

def kill_monster():
    while True:
        if pg.locateOnScreen('imgs/region_battle.png',region=constants.REGION_BATTLE):
            break
        is_battle = check_battle()
        if is_battle == None:
            pg.press('space')
            while pg.locateOnScreen('imgs/battle_red.png',confidence=0.8, region=constants.REGION_BATTLE) !=None or pg.locateOnScreen('imgs/battle_red2.png', confidence=0.7, region=constants.REGION_BATTLE) !=None:
                if pg.locateOnScreen('imgs/region_battle.png'):
                    pg.scroll(1)
                    pg.sleep(1)
                    break
                print('esperando o monstro morrer') 
            time.sleep(2)
            print('procurando outro monstro')
        print(is_battle)



def check_status(name,delay,x,y,rgb,button_name):
    print(f'checkando {name}...')
    pg.sleep(delay)
    if pg.pixelMatchesColor(x,y, rgb):
        pg.press(button_name)


def eat_food():
    pg.press('F5')
    print('comendo comida...')



def hole_down():
    box = pg.locateOnScreen('imgs/hole_down.png', confidence=0.8)
    if box:
        x,y = pg.center(box)
        pg.moveTo(x,y)
        pg.click()
        pg.sleep(5)
        kill_monster()



def hole_up(img_anchor, plus_X,plus_Y):
    box = pg.locateOnScreen(img_anchor, confidence=0.8)
    if box:
        x,y = pg.center(box)
        pg.moveTo(x + plus_X, y + plus_Y)
        pg.press('F6')
        pg.click()
        time.sleep(5)
        kill_monster()
        



def goto(img):
    if img:
        imagem = img
        vai = pg.locateOnScreen(img, confidence=0.8,region=constants.REGION_MINIMAP)
        if vai is not None:
            x, y = pg.center(vai)
            pg.moveTo(x, y)
            pg.click()
            pg.moveTo(100,100)
            pg.sleep(15)
            kill_monster()
            if pg.locateOnScreen('imgs/fotobase.png',confidence=0.9, region=constants.REGION_MINIMAP) != None or pg.locateOnScreen('imgs/fotobaseh.png',confidence=0.9, region=constants.REGION_MINIMAP):
                print('nao chegou ainda no local!!')
                kill_monster()
                print('indo ao local!')
                goto(imagem)

            



