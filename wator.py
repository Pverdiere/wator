import math
import random
import time
from model.fish import Fish
from model.shark import Shark

grid = {}
largeur = 50
longueur = 180
listPoisson = []

for i in range(largeur):
    grid[i] = []
    for j in range(longueur):
        grid[i].append(" ")

def initFish(largeur,longueur,grid) -> list:
    nbPoisson = math.floor((longueur/3) * largeur)
    listPoisson = []
    for i in range(nbPoisson):
        ok = False
        while not(ok):
            largRandom = random.randrange(largeur)
            longRandom = random.randrange(longueur)
            caseSelect = grid[largRandom][longRandom]
            if caseSelect == " ":
                grid[largRandom][longRandom] = Fish([largRandom,longRandom])
                listPoisson.append(grid[largRandom][longRandom])
                ok = True
    return listPoisson

def initShark(listPoisson,largeur,longueur,grid):
    nbShark = math.floor(len(listPoisson)/3)
    for i in range(nbShark):
        ok = False
        while not(ok):
            largRandom = random.randrange(largeur)
            longRandom = random.randrange(longueur)
            caseSelect = grid[largRandom][longRandom]
            if caseSelect == " ":
                grid[largRandom][longRandom] = Shark([largRandom,longRandom])
                ok = True

listPoisson = initFish(largeur,longueur,grid)
initShark(listPoisson,largeur,longueur,grid)

while True:
    print("nb Fish :",len(listPoisson))
    for poisson in listPoisson:
        positions = poisson.move(grid)
        poisson.setPosition(positions[1])
        if poisson.gestation:
            poisson.setGestation(False)
            newFish = Fish([positions[0][0],positions[0][1]])
            listPoisson.append(newFish)
            grid[positions[0][0]][positions[0][1]] = newFish
        else:
            grid[positions[0][0]][positions[0][1]] = " "
        grid[positions[1][0]][positions[1][1]] = poisson
    print("nb Shark :",len(Shark.listShark))
    for shark in Shark.listShark:
        positions = shark.move(grid)
        if(positions):
            shark.setPosition(positions[1])
            if isinstance(positions[2],Fish) and not(isinstance(positions[2],Shark)):
                grid[positions[2].position[0]][positions[2].position[1]] = ' '
                listPoisson.remove(positions[2])
            if shark.gestation:
                shark.setGestation(False)
                newShark = Shark([positions[0][0],positions[0][1]])
                Shark.listShark.append(newShark)
                grid[positions[0][0]][positions[0][1]] = newShark
            else:
                grid[positions[0][0]][positions[0][1]] = ' '
            grid[positions[1][0]][positions[1][1]] = shark

    print("_" * (len(grid[0]) + 2))
    for key, ligne in grid.items():
        textLigne = ""
        for col in ligne:
            textLigne += col if type(col) == str else col.symbol
        print(f"|{textLigne}|")
    time.sleep(1.5)