import os

class Node:
    def __init__(self) -> None:
        pass

class Piece:
    def __init__(self, _color):
        self.color = _color
    def __str__(self):
        return ("r" if self.color == "red" else "b")

class Tile:
    def __init__(self, _p=None) -> None:
        if _p: self.val = _p
        else: self.val = None
        pass

    def __str__(self):
        if self.val: return str(self.val)
        return '-'

class Board:
    b = [[], [], [], [], [], [], [], []]
    def __init__(self):
        self.gen_board()

    def __self__(self):
        return self.b

    def gen_board(self):
        for i in self.b:
            for j in range(8):
                i.append(Tile())

        def gen_black():
            for i in range(3):
                for j in range(8):
                    if (i + j) % 2 == 1:
                        self.b[i][j] = Tile(Piece("black"))

        def gen_red():
            for i in range(5, 8, 1):
                for j in range(8):
                    if (i + j) % 2 == 1:
                        self.b[i][j] = Tile(Piece("red"))

        gen_black()
        gen_red()
            
    def print_board(self):
        for i in range(8):
            for j in range(8):
                x = self.b[i][j]
                print(f"{x}{i}{j}", end=" ")
            print()

    def move(self, x):
        start = x[0]
        end = x[1]
        if self.b[start[0]][start[1]]:
            if str(self.b[end[0]][end[1]]) == '-':
                return "Valid move."
            print(self.b[end[0]][end[1]])
        return "Invalid Move."

class Game:
    def __init__(self) -> None:
        self.start()

    def start(self):
        self.board = Board()
        self.game_loop()
        return

    def game_loop(self):
        print("Type \'q\' to quit.")
        msg = None
        while(True):
            # self.clear()
            self.board.print_board()
            if msg: print(msg)
            msg = None
            print("Input [s:xy] [d:xy]: ", end="")
            x = input()
            if x == 'q':
                break
            else:
                try:
                    x = (int(x[0]), int(x[1])), (int(x[3]), int(x[4]))
                    # msg = f"{self.board.b[x[0][0]][x[0][1]]}, {x}"
                    msg = self.board.move(x)
                except:
                    msg = "Invalid Input. Try again."

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

def main():
    game = Game()

if __name__ == '__main__':
    main()