import os

ROWS = 8
COLS = 8

board = [[' ' for i in range(COLS)] for j in range(ROWS)]
pieces = []

red = []
black = []

class Piece():
    row = None
    col = None
    color = None

    def __init__(self, _row, _col, _color):
        self.row = _row
        self.col = _col
        self.color = _color


def print_board():
    for x in board:
        print(*x)

def gen_pieces():
    i = 0
    for y in range(3):
        if i == 1: i = 0
        else: i = 1
        for x in range(i, 8, 2):
            p = Piece(x,y, 'red')
            pieces.append(p)
    i = 1
    for y in range(5, 8):
        if i == 1: i = 0
        else: i = 1
        for x in range(i, 8, 2):
            p = Piece(x,y, 'black')
            pieces.append(p)
    return

def gen_board():
    gen_pieces()
    for x in pieces:
        board[x.col][x.row] = 'o' if x.color == 'red' else 'x'

def main():
    gen_board()
    print_board()
    return

if __name__ == "__main__":
    main()