class Checker:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.king = False

    def directions(self):
        if self.king:
            return [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        d = -1 if self.color == "w" else 1  # white goes up, black goes down
        return [(d, -1), (d, 1)]

    def moves(self, board):
        """Returns (simple_moves, jumps) as lists of target squares (row, col)."""
        simple, jumps = [], []
        for dr, dc in self.directions():
            r, c = self.row + dr, self.col + dc
            if not board.inside(r, c):
                continue
            other = board.grid[r][c]
            if other is None:
                simple.append((r, c))
            elif other.color != self.color:
                r2, c2 = r + dr, c + dc
                if board.inside(r2, c2) and board.grid[r2][c2] is None:
                    jumps.append((r2, c2))
        return simple, jumps

    def __str__(self):
        return self.color.upper() if self.king else self.color
