import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            roid_angle = random.uniform(20, 50)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, split_radius)
            split1.velocity = self.velocity.rotate(roid_angle) * 1.2
            split2 = Asteroid(self.position.x, self.position.y, split_radius)
            split2.velocity = self.velocity.rotate(-roid_angle) * 1.2
            

            


