import pyautogui as pg
import keyboard
import actions
import constants


#script to hunt wasps cave in ab'dendriel, using the flags described in the photos as a way to click, this script does not heal os use spells, only basic hits and uses healling spells if
# your mana is full, watch that hotkeys used during hunting are fixed as seem in the code below, since monster are weak, no other complex actions are required...
# F1 TO HEALLING SPELLS
# F6 TO ROPE
# F5 TO EAT FOOD

def hunt_wasp():
    while True:
        for i in range(1,4):
            actions.goto(f'wasp_img/foto{i}.png')
        actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
        actions.eat_food()
        actions.hole_down()
        actions.goto('wasp_img/foto5.png')
        actions.goto('wasp_img/foto6.png')
        actions.goto('wasp_img/foto7.png')
        actions.goto('wasp_img/foto8.png')
        actions.goto('wasp_img/foto9.png')
        actions.goto('wasp_img/foto10.png')
        actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
        actions.eat_food()
        actions.hole_down()
        actions.goto('wasp_img/foto11.png')
        actions.goto('wasp_img/foto12.png')
        actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
        actions.eat_food()
        actions.goto('wasp_img/foto13.png')
        actions.hole_up('imgs/anchor_floor_3.png',130,130)
        actions.goto('wasp_img/foto14.png')
        actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
        actions.eat_food()
        actions.hole_up('imgs/anchor_floor_2.png',430,0)