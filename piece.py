class Piece:
    def __init__(self):
        self.name = "Bob"

    def __str__(self):
        return f"{self.name}"

def pieces_gen(size: int) -> list:
    ps = []
    for i in range(size):
        p = Piece()
        ps.append(p)
    return ps