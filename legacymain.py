import pyautogui as pg
import keyboard
import time

#code that used to be main in the beggining of the bot, used to tests

REGION_BATTLE = (1749,486,156,51)
REGION_MINIMAP = (1752,26,110,109)

POSITION_MANA_FULL = (966,34)
COLOR_MANA_FULL = (0,54,119)

POSITION_LIFE =(368,31)



def check_battle():
    return pg.locateOnScreen('imgs/region_battle.png', region=REGION_BATTLE)

def kill_monster():
    while True:
        if pg.locateOnScreen('imgs/region_battle.png',region=REGION_BATTLE):
            break
        is_battle = check_battle()
        if is_battle == None:
            pg.press('space')
            while pg.locateOnScreen('imgs/battle_red.png',confidence=0.8, region=REGION_BATTLE) !=None or pg.locateOnScreen('imgs/battle_red2.png', confidence=0.7, region=REGION_BATTLE) !=None:
                if pg.locateOnScreen('imgs/region_battle.png'):
                    pg.scroll(1)
                    pg.sleep(1)
                    break
                print('esperando o monstro morrer') 
            time.sleep(2)
            print('procurando outro monstro')
        print(is_battle)

#kill_monster()




def check_status(name,delay,x,y,rgb,button_name):
    print(f'checkando {name}...')
    pg.sleep(delay)
    if pg.pixelMatchesColor(x,y, rgb):
        pg.press(button_name)


def eat_food():
    pg.press('F5')
    print('comendo comida...')

#keyboard.wait('h')
#check_status('mana',5,*POSITION_MANA_FULL,(0,54,119),'F1')
#eat_food()

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
        


#keyboard.wait('h')
#hole_up('imgs/anchor_floor_3.png', 130, 130)
#hole_up('imgs/anchor_floor_2.png', 430, 0)



#def goto(img):
#    if img:
#        vai = pg.locateOnScreen(img,confidence=0.8)
#        x,y = pg.center(vai)
#        pg.moveTo(x,y)
#        pg.click()
 #       if pg.locateOnScreen('fotobase.png') !=None:
  #          check_battle()
   #         goto(img)


def goto(img):
    if img:
        imagem = img
        vai = pg.locateOnScreen(img, confidence=0.8,region=REGION_MINIMAP)
        if vai is not None:
            x, y = pg.center(vai)
            pg.moveTo(x, y)
            pg.click()
            pg.moveTo(100,100)
            pg.sleep(15)
            kill_monster()
            if pg.locateOnScreen('fotobase.png',confidence=0.9, region=REGION_MINIMAP) != None or pg.locateOnScreen('fotobaseh.png',confidence=0.9, region=REGION_MINIMAP):
                print('não chegou ainda no local!!')
                kill_monster()
                print('indo ao local!')
                goto(imagem)

            



while True:
    goto('wasp_img/foto.png')
    goto('wasp_img/foto2.png') 
    goto('wasp_img/foto3.png')
    check_status('mana',1,*POSITION_MANA_FULL,(0,54,119),'F1')
    eat_food()
    hole_down()
    # goto('wasp_img/foto4.png')
    goto('wasp_img/foto5.png')
    goto('wasp_img/foto6.png')
    goto('wasp_img/foto7.png')
    goto('wasp_img/foto8.png')
    goto('wasp_img/foto9.png')
    goto('wasp_img/foto10.png')
    check_status('mana',1,*POSITION_MANA_FULL,(0,54,119),'F1')
    eat_food()
    hole_down()
    goto('wasp_img/foto11.png')
    goto('wasp_img/foto12.png')
    check_status('mana',1,*POSITION_MANA_FULL,(0,54,119),'F1')
    eat_food()
    goto('wasp_img/foto13.png')
    hole_up('imgs/anchor_floor_3.png',130,130)
    goto('wasp_img/foto14.png')
    check_status('mana',1,*POSITION_MANA_FULL,(0,54,119),'F1')
    eat_food()
    hole_up('imgs/anchor_floor_2.png',430,0)


#pg.moveTo(1804,78)