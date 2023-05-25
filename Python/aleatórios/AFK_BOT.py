import pyautogui as pg
import random
import time
<<<<<<< HEAD

tempo=0
contador=int(input("Quanto tempo vai rodar o bot em segundos: "))
while tempo< contador:
=======
tempo=int(input("Por quanto tempo ficará fora? (em segundos)"))
while tempo >0:
>>>>>>> 6e38728e5c53f3ce13a0084df544bcd15064ff8f
    x= random.randint(100,1200)
    y=random.randint(50,1000)
    pg.moveTo(x,y,0.4)
    time.sleep(1)
<<<<<<< HEAD
    tempo+=1
=======
    tempo-=1
>>>>>>> 6e38728e5c53f3ce13a0084df544bcd15064ff8f
