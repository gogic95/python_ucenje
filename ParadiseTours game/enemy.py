#  Copyright (c) Filip Gogic 2022.
import random

import pygame


class enemy:
    # Starting coordinates
    x_coord = 368
    y_coord = 185
    speed = 0.1
    switch_direction = 0

    def __init__(self, level):
        if level == 1:
            self.image = pygame.image.load('virus.png')
        if level == 2:
            self.image = pygame.image.load('virus2.png')
        if level == 3:
            self.image = pygame.image.load('virus3.png')
        if level == 4:
            self.image = pygame.image.load('virusBoss.png')

    def put_on_screen(self, screen):
        screen.blit(self.image, (self.x_coord, self.y_coord))

    def set_new_coordinates(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def go_left(self):
        self.x_coord -= self.speed

    def go_right(self):
        self.x_coord += self.speed

    def go_up(self):
        self.y_coord -= self.speed

    def go_down(self):
        self.y_coord += self.speed

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_speed(self):
        return self.speed

    def get_x(self):
        return self.x_coord

    def set_x(self, x):
        self.x_coord = x

    def get_y(self):
        return self.y_coord

    def set_y(self, y):
        self.y_coord = y

    def get_coordinates(self):
        return self.x_coord, self.y_coord

    def random_movement(self):
        direction = random.randint(1, 4)
        if direction == 1:
            self.go_left()
        if direction == 2:
            self.go_right()
        if direction == 3:
            self.go_up()
        if direction == 4:
            self.go_down()

    def get_switch(self):
        return self.switch_direction

    def change_direction(self):
        if self.switch_direction == 0:
            self.switch_direction = 1
        else:
            self.switch_direction = 0
