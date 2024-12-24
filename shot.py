from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        colour_red = (250, 82, 110)
        pygame.draw.circle(screen, colour_red, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)