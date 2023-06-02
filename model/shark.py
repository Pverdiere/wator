from fish import Fish
import random

class Shark(Fish):

    maxEnergy = 4
    symbol = "!"
    listShark = []

    def __init__(self, position) -> None:
        super().__init__(position)
        self.energy = 2
        Shark.listShark.append(self)

    def move(self,grid) -> list:
        case_disponible = self.verifMovePossible(grid)
        nextPosition = self.position if case_disponible == [] else case_disponible[random.randrange(len(case_disponible))]
        if type(nextPosition[1]) == Fish:
            self.energy += 1
        else:
            self.energy -= 1
        if self.nextReproduction == 0:
            self.gestation = True
        self.nextReproduction = Fish.timeReproduction if self.nextReproduction == 0 else self.nextReproduction -1
        return [self.position,nextPosition[0],nextPosition[1]]

    def verifMovePossible(self,grid) -> list:
        case_disponible = []
        case_a_regarder = {
            "haut": grid[(self.position[0] + 1) % len(grid)][self.position[1]],
            "bas": grid[(self.position[0] - 1) % len(grid)][self.position[1]],
            "droite": grid[self.position[0]][(self.position[1] + 1) % len(grid[0])],
            "gauche" : grid[self.position[0]][(self.position[1] - 1) % len(grid[0])]
        }

        poisson = False
        if (case_a_regarder["haut"] == type(case_a_regarder["haut"]) == Fish or
            case_a_regarder["bas"] == type(case_a_regarder["haut"]) == Fish or
            case_a_regarder["droite"] == type(case_a_regarder["haut"]) == Fish or
            case_a_regarder["gauche"] == type(case_a_regarder["haut"]) == Fish):
            poisson = True

        if (case_a_regarder["haut"] == ' ' and not(poisson)) or type(case_a_regarder["haut"]) == Fish:
            case_disponible.append([[(self.position[0] + 1) % len(grid),self.position[1]], case_a_regarder["haut"] if poisson else None])
        if (case_a_regarder["bas"] == ' ' and not(poisson)) or type(case_a_regarder["bas"]) == Fish:
            case_disponible.append([[(self.position[0] - 1) % len(grid),self.position[1]], case_a_regarder["bas"] if poisson else None])
        if (case_a_regarder["droite"] == ' ' and not(poisson)) or type(case_a_regarder["droite"]) == Fish:
            case_disponible.append([[self.position[0],(self.position[1] + 1) % len(grid[0])], case_a_regarder["droite"] if poisson else None])
        if (case_a_regarder["gauche"] == ' ' and not(poisson)) or type(case_a_regarder["gauche"]) == Fish:
            case_disponible.append([[self.position[0],(self.position[1] - 1) % len(grid[0])], case_a_regarder["gauche"] if poisson else None])
        return case_disponible
    
    def dead(self,grid):
        pass