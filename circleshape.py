import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.expired = False
        self.wrap_count = 0

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
    
    def wrap_around_move(self):
        if self.position.x > SCREEN_WIDTH + self.radius*2:
            if self.expired: self.kill()
            self.position.x = 0
            self.wrap_count += 1
        elif self.position.x < 0 - self.radius*2:
            if self.expired: self.kill()
            self.position.x = SCREEN_WIDTH
            self.wrap_count += 1
            
        if self.position.y > SCREEN_HEIGHT + self.radius*2:
            if self.expired: self.kill()
            self.position.y = 0
            self.wrap_count += 1
        elif self.position.y < 0 - self.radius*2:
            if self.expired: self.kill()
            self.position.y = SCREEN_HEIGHT
            self.wrap_count += 1