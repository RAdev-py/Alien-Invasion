import pygame
from pygame.sprite import Sprite
class Explosion(Sprite):
    """class to create explosion particles"""
    def __init__(self, ai_game, center):
        """creates an explosion at the center given"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.images = []
        for img in range(1,17):
            self.images.append(pygame.image.load(f"images/ExplosionSprites/ex{img}.png").convert_alpha())
        self.index = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=center)

    def update(self):
        """update the explosion animation"""
        self.index += 1
        if self.index >= 15:
            self.kill()
        self.image = self.images[self.index]



