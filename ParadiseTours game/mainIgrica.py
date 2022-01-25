#  Copyright (c) Filip Gogic 2022.

import pygame
import player
import enemy
import random

# Initialize game
pygame.init()

# Set main screen to 800x600 resolution,caption and icon
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paradise Tours', 'PT')
icon = pygame.image.load('palm.png')
pygame.display.set_icon(icon)

background = pygame.image.load('empty-sea-beach-background.jpg')

# Initializing New Player
new_player = player.player()

# Initializing Enemies
# first_enemy = enemy.enemy(1)
# first_enemy.set_x(168)
# second_enemy = enemy.enemy(2)
# second_enemy.set_x(368)
# third_enemy = enemy.enemy(3)
# third_enemy.set_x(600)
# boss_enemy = enemy.enemy(4)
# boss_enemy.set_y(25)
# boss_enemy.set_x(336)
list_of_enemies = []

for i in range(3):
    level = random.randint(1, 4)
    x = random.randint(0, 672)
    y = random.randint(0, 300)
    new_enemy = enemy.enemy(level)
    new_enemy.set_new_coordinates(x, y)
    list_of_enemies.append(new_enemy)
    print(level)

running = False
while not running:
    # Screen backgroud color
    screen.fill((255, 150, 150))
    screen.blit(background, (0, 0))
    # Movement controls
    x, y = new_player.get_coordinates()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x > 0:
            new_player.go_left()
    if keys[pygame.K_RIGHT]:
        if x < width - 64:
            new_player.go_right()
    if keys[pygame.K_UP]:
        if y > 0:
            new_player.go_up()
    if keys[pygame.K_DOWN]:
        if y < height - 64:
            new_player.go_down()

    # Closing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass

    new_player.put_on_screen(screen)
    for enemies in list_of_enemies:
        enemies.put_on_screen(screen)
        if enemies.get_x() > 0 and enemies.switch_direction == 0:
            enemies.go_left()
        if enemies.get_x() < width and enemies.switch_direction == 1:
            enemies.go_right()
        if width - 65 < enemies.get_x():
            enemies.change_direction()
            enemies.set_speed(enemies.get_speed() + 0.01)
            enemies.set_y(enemies.get_y() + 3)
        if enemies.get_x() < 1:
            enemies.change_direction()
            enemies.set_speed(enemies.get_speed() + 0.01)
            enemies.set_y(enemies.get_y() + 3)

    # first_enemy.put_on_screen(screen)
    # second_enemy.put_on_screen(screen)
    # third_enemy.put_on_screen(screen)
    # boss_enemy.put_on_screen(screen)
    pygame.display.update()
