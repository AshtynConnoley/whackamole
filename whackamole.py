import pygame
import random


def main():
    try:
        def Draw_Grid():
            for i in range(0, 16):
                pygame.draw.line(screen, (100, 100, 100), (0, i * 32), (720, i * 32))
            for i in range(0, 20):
                pygame.draw.line(screen, (100, 100, 100), (i * 32, 0), (i * 32, 640))

        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_row = 0
        mole_col = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y =event.pos
                    row = y//32
                    col = x//32
                    if mole_row == row and mole_col == col:
                        mole_row = random.randrange(0, 16)
                        mole_col = random.randrange(0, 20)
            screen.fill("light green")
            #added an extra 2 pixels to row and 3 to column to make mole appear more centered
            screen.blit(mole_image, mole_image.get_rect(topleft=(3+(mole_col*32), 2+ (mole_row*32))))
            Draw_Grid()
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
