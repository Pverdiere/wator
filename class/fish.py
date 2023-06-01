class Fish:

    nextId = 0

    def __init__(self,position) -> None:
        Fish.nextId += 1
        self.id = Fish.nextId.copy()
        self.nextReproduction = 5
        self.position = position