import random
import pygame
import numpy as np
import cupy as cp

from pygame.math import Vector2
from pygame import draw


class Ball:
    """ Ball object with position and velocity """

    def __init__(
        self,
        screen,
        pos,
        radius: int = 1,
    ) -> None:
        self._pos = pos
        self._speed = Vector2(0, 0)
        # self._speed[:] = (random.random() * 50), (random.random() * 50)
        self._speed.x = random.random() * 50
        self._speed.y = random.random() * 50
        self._radius = radius
        self._screen = screen
        self._color = pygame.Color(0, 0, 0)
        self._pos_np = np.array([0, 0], dtype="int32")
        self._pos_cp = cp.array([0, 0])

        self._max_screen_width = self._screen.get_width()
        self._max_screen_height = self._screen.get_height()

    @property
    def radius(self):
        """ return radius"""
        return self._radius

    def update(self, dt) -> None:
        """Update position and check screen boundaries"""

        self._pos.x += self._speed.x * dt
        self._pos.y += self._speed.y * dt

        if self._pos.x > self._max_screen_width:
            self._speed.x *= -1

        if self._pos.x <= 0:
            self._speed.x *= -1

        if self._pos.y > self._max_screen_height:
            self._speed.y *= -1

        if self._pos.y <= 0:
            self._speed.y *= -1

    @property
    def pos(self):
        return self._pos

    @property
    def pos_np(self):
        self._pos_np[0] = self._pos.x
        self._pos_np[1] = self._pos.y
        return self._pos_np

    @property
    def pos_cp(self):
        self._pos_cp[0] = self._pos.x
        self._pos_cp[1] = self._pos.y
        return self._pos_cp
