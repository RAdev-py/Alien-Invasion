import pygame

from pygame.sprite import Sprite
from time import time


class PowerUp(Sprite):
    """A class to represent a powerup dropped by aliens."""

    def __init__(self, ai_game, alien):
        """Initialize the powerup and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.settings = ai_game.settings

        # Load the powerup image and set its rect attribute.
        original_image =  pygame.image.load('images/lightning.png').convert_alpha()
        self.image = pygame.transform.scale_by(original_image, 0.1)

        self.rect = self.image.get_rect()

        # Start each new powerup at the position where an alien was just killed.
        self.rect.x = alien.rect.x
        self.rect.y = alien.rect.y

        # Store the powerup's exact position.
        self.y = float(self.rect.y)


    # def check_edges(self):
    #     """Return True if powerup is at edge of screen."""
    #     screen_rect = self.screen.get_rect()
    #     return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def activate(self):
        self.activation_time = time()
        self.ai_game.powerup = self
        self.settings.bullet_speed *= 2
        print("Power Activated")

    def deactivate(self):
        self.settings.bullet_speed /= 2

    def update(self):
        """Move the powerup down."""
        self.y += self.settings.powerup_speed
        self.rect.y = self.y

    def expire(self):
        return time() - self.activation_time > self.settings.powerup_lifetime

    def blitme(self):
        """Draw the powerup at its current location."""
        self.screen.blit(self.image, self.rect)