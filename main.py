import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main() -> int:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if player.collides(item):
                print ("Game Over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()
        
        # This line is what *actuallY* draws the screen; so needs to go after all draw calls.
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()