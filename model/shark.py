from model.fish import Fish
import random

class Shark(Fish):

    maxEnergy = 10
    symbol = "\033[91m§\033[0m"
    listShark = []
    timeReproduction = 5

    def __init__(self, position) -> None:
        super().__init__(position)
        self.energy = 4
        Shark.listShark.append(self)

    def move(self,grid) -> list:
        case_disponible = self.verifMovePossible(grid)
        nextPosition = self.position if case_disponible == [] else case_disponible[random.randrange(len(case_disponible))]
        if isinstance(nextPosition[1],Fish) and not(isinstance(nextPosition[1],Shark)) and self.energy < Shark.maxEnergy:
            self.energy += 1
        else:
            self.energy -= 1
            if self.energy <= 0:
                self.dead(grid)
                return False
        if case_disponible != []:    
            if self.nextReproduction == 0:
                self.gestation = True
            self.nextReproduction = Fish.timeReproduction if self.nextReproduction == 0 else self.nextReproduction -1
        return [self.position,nextPosition if case_disponible == [] else nextPosition[0],None if case_disponible == [] else nextPosition[1]]

    def verifMovePossible(self,grid) -> list:
        case_disponible = []
        case_a_regarder = {
            "haut": grid[(self.position[0] + 1) % len(grid)][self.position[1]],
            "bas": grid[(self.position[0] - 1) % len(grid)][self.position[1]],
            "droite": grid[self.position[0]][(self.position[1] + 1) % len(grid[0])],
            "gauche" : grid[self.position[0]][(self.position[1] - 1) % len(grid[0])]
        }

        poisson = False

        if ((isinstance(case_a_regarder["haut"],Fish) and not(isinstance(case_a_regarder["haut"],Shark))) or
            (isinstance(case_a_regarder["bas"],Fish) and not(isinstance(case_a_regarder["bas"],Shark))) or
            (isinstance(case_a_regarder["droite"],Fish) and not(isinstance(case_a_regarder["droite"],Shark))) or
            (isinstance(case_a_regarder["gauche"],Fish) and not(isinstance(case_a_regarder["gauche"],Shark)))):
            poisson = True

        if (case_a_regarder["haut"] == ' ' and not(poisson)) or (isinstance(case_a_regarder["haut"],Fish) and not(isinstance(case_a_regarder["haut"],Shark))):
            case_disponible.append([[(self.position[0] + 1) % len(grid),self.position[1]], case_a_regarder["haut"] if poisson else None])
        if (case_a_regarder["bas"] == ' ' and not(poisson)) or (isinstance(case_a_regarder["bas"],Fish) and not(isinstance(case_a_regarder["bas"],Shark))):
            case_disponible.append([[(self.position[0] - 1) % len(grid),self.position[1]], case_a_regarder["bas"] if poisson else None])
        if (case_a_regarder["droite"] == ' ' and not(poisson)) or (isinstance(case_a_regarder["droite"],Fish) and not(isinstance(case_a_regarder["droite"],Shark))):
            case_disponible.append([[self.position[0],(self.position[1] + 1) % len(grid[0])], case_a_regarder["droite"] if poisson else None])
        if (case_a_regarder["gauche"] == ' ' and not(poisson)) or (isinstance(case_a_regarder["gauche"],Fish) and not(isinstance(case_a_regarder["gauche"],Shark))):
            case_disponible.append([[self.position[0],(self.position[1] - 1) % len(grid[0])], case_a_regarder["gauche"] if poisson else None])
        return case_disponible
    
    def dead(self,grid):
        grid[self.position[0]][self.position[1]] = ' '
        Shark.listShark.remove(self)