class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color  # "w" = white, "b" = black
        self.moves = 0  # number of moves in the game
        self.result = "-"  # "won" / "lost"
        self.time = 0  # seconds the player spent thinking

    def __str__(self):
        return f"{self.name} ({self.color}) | result: {self.result} | moves: {self.moves} | time: {self.time:.0f}s"
