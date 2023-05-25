import pyautogui as pg
import random
import time

tempo=0
contador=int(input("Quanto tempo vai rodar o bot em segundos: "))
while tempo< contador:
    x= random.randint(100,1200)
    y=random.randint(50,1000)
    pg.moveTo(x,y,0.4)
    time.sleep(1)
    tempo+=1