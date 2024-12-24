# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

#Groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock to set fps
    clockie = pygame.time.Clock()
    dt = 0

    #Player and shots
    Player.containers = (updatable, drawable)
    main_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Shot.containers = (shots, updatable, drawable)

    #Asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    new_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Painting the screen black
        colour_black = (0,0,0)
        screen.fill(colour_black)

        #Updating and drawing
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()

        #Checking for collisions
        for i in asteroids:
            if i.check_collision(main_player):
                print("GAME OVER")
                return
            for j in shots:
                if j.check_collision(i):
                    j.kill()
                    i.split()

        #ticking to set fps
        dt = clockie.tick(60) / 1000
if __name__ == "__main__":
    main()