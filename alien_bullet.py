import pygame
from pygame.sprite import Sprite

class AlienBullets(Sprite):
	""" create alien bullets"""
	def __init__(self, ai_game, alien):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.bullet_speed = ai_game.settings.bullet_speed
		self.color = (155, 0, 0)
		#create bullet rect
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = alien.rect.midbottom

		self.y = float(self.rect.y)

	def update(self):
		"""move the bullet torwards the player"""
		self.y += self.bullet_speed
		self.rect.y = self.y

	def draw_alien_bullet(self):
		"""draw alien bullet to screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)






