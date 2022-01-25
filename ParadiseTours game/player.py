#  Copyright (c) Filip Gogic 2022.
import pygame


class player:
    # Starting coordinates
    x_coord = 368
    y_coord = 450
    speed = 0.3

    def __init__(self):
        self.image = pygame.image.load('tomato.png')

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

    def get_x(self):
        return self.x_coord

    def get_y(self):
        return self.y_coord

    def get_coordinates(self):
        return self.x_coord, self.y_coord

