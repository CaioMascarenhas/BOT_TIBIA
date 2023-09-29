import pyautogui as pg
import keyboard

#script to take printscreen of the selecteds spots of your cursor in the window, especially the marks on minimap

class Rec:
    def __init__(self):
        print('oi')
    
    def photo(self):
        x,y = pg.position()
        photo = pg.screenshot(region=(x-3,y-3,6,6))
        photo.save('foto14.png')


record = Rec()
keyboard.wait('h')
record.photo()