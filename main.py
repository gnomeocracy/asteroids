# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import Player

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updateable, drawable)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)    
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()