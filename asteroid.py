from circleshape import *
from constants import *
from math import pi
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.mass = pi*pow(radius,2)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_mass = pi*pow(child_radius,2)
        child_total_velocity = self.velocity / ((child_mass*2) / (self.mass))

        break_angle = random.uniform(20,50)

        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child1.velocity = child_total_velocity.rotate(break_angle)
        child2 = Asteroid(self.position.x, self.position.y, child_radius)
        child2.velocity = child_total_velocity.rotate(-break_angle)

        
        