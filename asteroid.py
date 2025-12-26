import pygame
import random
from circleshape import *
from constants import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, ):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("this was a small asteroid and we're done")
            return 

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_movement = self.velocity.rotate(angle)
        new_movement2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first = Asteroid(self.position.x, self.position.y, new_radius)
        second = Asteroid(self.position.x, self.position.y, new_radius)
        first.velocity = new_movement * 1.2
        second.velocity = new_movement2 * 1.2
            
        