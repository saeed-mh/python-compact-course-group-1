from checker import Checker


class Board8:  # type 1: 8x8
    def __init__(self, size=8, rows=3):
        self.size = size
        self.grid = [[None] * size for _ in range(size)]  # array of checkers
        for r in range(size):
            for c in range(size):
                if (r + c) % 2 == 1:
                    if r < rows:
                        self.grid[r][c] = Checker("b", r, c)
                    elif r >= size - rows:
                        self.grid[r][c] = Checker("w", r, c)

    def inside(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size

    def checkers(self, color):
        return [x for row in self.grid for x in row if x and x.color == color]

    def legal_moves(self, color):
        """List of (checker, target). If a capture exists it is mandatory."""
        simple, jumps = [], []
        for ch in self.checkers(color):
            s, j = ch.moves(self)
            simple += [(ch, t) for t in s]
            jumps += [(ch, t) for t in j]
        return jumps or simple

    def move(self, ch, r, c):
        """Moves the checker. Returns True if it captured something."""
        captured = abs(r - ch.row) == 2
        if captured:
            self.grid[(r + ch.row) // 2][(c + ch.col) // 2] = None
        self.grid[ch.row][ch.col] = None
        self.grid[r][c] = ch
        ch.row, ch.col = r, c
        if (ch.color == "w" and r == 0) or (ch.color == "b" and r == self.size - 1):
            ch.king = True
        return captured

    def show(self):
        print("\n   " + " ".join(str(c) for c in range(self.size)))
        for r in range(self.size):
            print(f"{r:<2} " + " ".join(str(x) if x else "." for x in self.grid[r]))


class Board10(Board8):  # type 2: 10x10 (inheritance)
    def __init__(self):
        super().__init__(10, 4)
