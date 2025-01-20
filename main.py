import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        screen.fill("black")

        for updatables in updatable:
            updatables.update(dt)
        
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.kill()
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()

        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
