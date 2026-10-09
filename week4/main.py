from board import Board8, Board10
from player import Player
from game import Game


if __name__ == "__main__":
    board = Board10() if input("Board type (8 or 10): ").strip() == "10" else Board8()
    p1 = Player(input("Name of player 1 (white, moves first): "), "w")
    p2 = Player(input("Name of player 2 (black): "), "b")
    Game(board, p1, p2).play()
