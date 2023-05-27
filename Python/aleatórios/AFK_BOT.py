import pyautogui as pg
import random
import time




tempo=int(input("Por quanto tempo ficará fora? (em segundos)"))
time.sleep(5)
while tempo>0:
    x= random.randint(100,1200)
    y=random.randint(50,1000)
    pg.moveTo(x,y,0.4)
    time.sleep(1)
    tempo-=1

