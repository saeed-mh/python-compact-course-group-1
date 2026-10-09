import time


class Game:
    def __init__(self, board, p1, p2):
        self.board = board
        self.players = [p1, p2]
        self.moves = 0
        self.start = time.time()

    def play(self):
        turn, chain = 0, None  # chain = checker that must continue jumping
        while True:
            me, other = self.players[turn], self.players[1 - turn]
            options = self.board.legal_moves(me.color)
            if chain:
                options = [(chain, t) for t in chain.moves(self.board)[1]]
            if not options:  # no legal move -> me loses
                break

            # status of the player and of the board
            self.board.show()
            w, b = len(self.board.checkers("w")), len(self.board.checkers("b"))
            print(
                f"Move #{self.moves + 1} | {me.name} ({me.color}) | his moves: {me.moves} | checkers: w={w}, b={b}"
            )

            t0 = time.time()
            ans = (
                input("Enter move 'row,col,row,col' or 'f' to finish the game: ")
                .strip()
                .lower()
                .strip()
                .lower()
            )
            me.time += time.time() - t0
            if ans == "f":  # player finishes the game -> gives up
                break
            try:
                r1, c1, r2, c2 = map(int, ans.replace(",", " ").split())
            except ValueError:
                print("Wrong input!")
                continue
            move = [
                (ch, t) for ch, t in options if (ch.row, ch.col, *t) == (r1, c1, r2, c2)
            ]
            if not move:
                print("Illegal move! (a capture is mandatory if possible)")
                continue

            ch = move[0][0]
            was_king = ch.king
            captured = self.board.move(ch, r2, c2)
            me.moves += 1
            self.moves += 1
            print(f"{me.name} moved ({r1},{c1}) -> ({r2},{c2})")
            # same player continues if he can jump again (and was not just crowned)
            chain = (
                ch
                if captured and ch.king == was_king and ch.moves(self.board)[1]
                else None
            )
            if not chain:
                turn = 1 - turn
        self.finish(me, other)

    def finish(self, loser, winner):
        loser.result, winner.result = "lost", "won"
        self.board.show()
        print("\n===== GAME SUMMARY =====")
        print(
            f"Board: {self.board.size}x{self.board.size} | total moves: {self.moves} | game time: {time.time() - self.start:.0f}s"
        )
        for p in self.players:
            print(p, "| checkers left:", len(self.board.checkers(p.color)))
