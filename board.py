from piece import *

R = 0
B = 1

class Board:
    def __init__(self):
        DIM = [10,10]
        pieces_r = pieces_gen(DIM[R])
        peices_b = pieces_gen(DIM[B])

        # for p in pieces_r:
        #     print(p)

    