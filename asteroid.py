from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        print("im dead!!")
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        dir1 = self.velocity.rotate(random_angle)
        dir2 = self.velocity.rotate(-random_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(0, 0, new_rad)
        ast1.position = self.position * 1
        ast1.velocity = dir1 * 1.2
        ast2 = Asteroid(0, 0, new_rad)
        ast2.position = self.position * 1
        ast2.velocity = dir2 * 1.2
