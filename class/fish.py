import random

class Fish:

    nextId = 0
    symbol = "§"

    def __init__(self,position) -> None:
        Fish.nextId += 1
        self.id = Fish.nextId.copy()
        self.nextReproduction = 5
        self.position = position

    def move(self,grid) -> list:
        case_disponible = self.verifMovePossible(grid)
        nextPosition = self.position if case_disponible == [] else case_disponible[random.randrange(4)]
        

    def verifMovePossible(self,grid) -> list:
        case_disponible = []
        case_a_regarder = {
            "haut": grid[(self.position[0] + 1) % grid.len()][self.position[1]],
            "bas": grid[(self.position[0] - 1) % grid.len()][self.position[1]],
            "droite": grid[self.position[0]][(self.position[1] + 1) % grid[0].len()],
            "gauche" : grid[self.position[0]][(self.position[1] - 1) % grid[0].len()]
        }

        if case_a_regarder["haut"] == '':
            case_disponible.append(case_a_regarder["haut"])
        if case_a_regarder["bas"] == '':
            case_disponible.append(case_a_regarder["bas"])
        if case_a_regarder["droite"] == '':
            case_disponible.append(case_a_regarder["droite"])
        if case_a_regarder["gauche"] == '':
            case_disponible.append(case_a_regarder["gauche"])
        
        return case_disponible
        
