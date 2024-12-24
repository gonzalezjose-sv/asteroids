from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        colour_yellow = (255, 255, 145)
        pygame.draw.circle(screen, colour_yellow, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            #Data for split asteroids
            random_angle = random.uniform(20,50)
            direction_1 = self.velocity.rotate(random_angle)
            direction_2 = self.velocity.rotate(random_angle * (-1))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            #First
            split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_1.velocity = direction_1 * 1.2
            #Second
            split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_2.velocity = direction_2 * 1.2