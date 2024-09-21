import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        new_radius = self.radius-ASTEROID_MIN_RADIUS
        split_one_velocity = pygame.Vector2(self.velocity).rotate(angle)
        split_two_velocity = pygame.Vector2(self.velocity).rotate(-angle)
        
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = split_one_velocity * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = split_two_velocity * 1.2
        
