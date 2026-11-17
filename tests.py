import pygame
import powerup as powerup_module

from powerup import PowerUp
from alien_bullet import AlienBullets


# Simple objects to simulate the game, settings, and alien.
class FakeSettings:
    bullet_speed = 2
    bullet_width = 5
    bullet_height = 10
    powerup_speed = 3
    powerup_lifetime = 5


class FakeGame:
    def __init__(self):
        self.settings = FakeSettings()
        self.screen = pygame.Surface((800, 600))
        self.powerup = None


class FakeAlien:
    def __init__(self):
        self.rect = pygame.Rect(100, 50, 40, 40)


# Create a PowerUp without loading its image.
def make_powerup(game):
    item = PowerUp.__new__(PowerUp)
    pygame.sprite.Sprite.__init__(item)

    item.ai_game = game
    item.settings = game.settings
    item.y = 100.0
    item.rect = pygame.Rect(100, 100, 20, 20)

    return item


# Test 1: Activating a power-up doubles bullet speed.
def test_powerup_activation():
    game = FakeGame()
    item = make_powerup(game)

    item.activate()

    assert game.settings.bullet_speed == 4
    assert game.powerup is item


# Test 2: Deactivating a power-up restores bullet speed.
def test_powerup_deactivation():
    game = FakeGame()
    item = make_powerup(game)

    game.settings.bullet_speed = 4
    item.deactivate()

    assert game.settings.bullet_speed == 2


# Test 3: A power-up moves downward.
def test_powerup_update():
    game = FakeGame()
    item = make_powerup(game)

    item.update()

    assert item.y == 103.0
    assert item.rect.y == 103


# Test 4: An alien bullet moves downward.
def test_alien_bullet_update():
    game = FakeGame()
    alien = FakeAlien()

    bullet = AlienBullets(game, alien)
    starting_y = bullet.rect.y

    bullet.update()

    assert bullet.rect.y == starting_y + 2
    assert bullet.y == float(bullet.rect.y)


# Run all tests.
if __name__ == "__main__":
    pygame.init()

    test_powerup_activation()
    test_powerup_deactivation()
    test_powerup_update()
    test_alien_bullet_update()

    print("All tests passed!")

    pygame.quit()
