from fish import Fish

class Shark(Fish):

    energy = 2
    maxEnergy = 4

    def __init__(self, position) -> None:
        super().__init__(position)
