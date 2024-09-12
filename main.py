import pygame
from constants import *
from player import Player

def main() -> int:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        player.update(dt)
        player.draw(screen)
        
        # This line is what *actuallY* draws the screen; so needs to go after all draw calls.
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()