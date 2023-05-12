import pyautogui as pg
import random
import time
while True:
    x= random.randint(100,1200)
    y=random.randint(50,1000)
    pg.moveTo(x,y,0.4)
    time.sleep(random.random()*3)