import sys, pygame
import board

C_BLACK = (155,0,0)
C_RED = (255,0,0)

WINDOW = (400,400)
SCREEN = pygame.display.set_mode(WINDOW)
BACKGROUND = pygame.Surface(WINDOW)

def draw_screen(board: board.Board) -> None:
    for i in range(8):
        for j in range(8):
            c = C_BLACK
            if (j % 2 != 0): c = C_RED
            pygame.draw.rect(BACKGROUND, c, 
                            (i*50,j*50,40,40))
    SCREEN.blit(BACKGROUND,(0,0))
    pygame.display.flip()

def main():
    pygame.init()
    b = board.Board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        draw_screen(b)

if __name__ == "__main__":
    main()