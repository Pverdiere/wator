import math
import random
import time
import os
import pygame
from model.fish import Fish
from model.shark import Shark



def main():
    pygame.init()

    pygame.display.set_caption("minimal program")

    grid = {}
    longueur = 240
    largeur = 180

    screen = pygame.display.set_mode((longueur,largeur))

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
    i=0
    running = True
    while running:
        i += 1
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

        for key, ligne in grid.items():
            print(key)

        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        running = False


        #os.system("clear")
        #
        #print("itération :",i)
        #print("nb Fish :",len(listPoisson))
        #print("nb Shark :",len(Shark.listShark))
        #
        #print("_" * (len(grid[0]) + 2))
        #for key, ligne in grid.items():
        #    textLigne = ""
        #    for col in ligne:
        #        textLigne += col if type(col) == str else col.symbol
        #    print(f"|{textLigne}|")
        time.sleep(0.5)

main()