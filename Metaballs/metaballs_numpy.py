""" Pygame application which calculate metaballs with numpy
"""

import sys
import random
import pygame
import numpy as np

from pygame.locals import HWSURFACE, DOUBLEBUF
from pygame.math import Vector2

from ball import Ball

# config window Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 5000
N_BALLS = 6


def euclid_dist(vector_p1, vector_p2):
    """ calculated the euclidean distance between 2 points """
    distances = vector_p1 - vector_p2
    return np.hypot(distances[:, :, 0], distances[:, :, 1])


def gray(image, mode="saturate"):
    """ create r,g,b layers to create grayscale image from 2d array """

    if mode == "saturate":
        image[image >= 255] = 255
    else:
        # Mode normalize
        image = 255 * (image / image.max())

    width, height = image.shape
    ret = np.empty((width, height, 3), dtype=np.uint8)
    ret[:, :, 2] = ret[:, :, 1] = ret[:, :, 0] = image
    return ret


class MetaBalls:
    """ Metaball game """

    def __init__(self) -> None:
        """Init pygame and related game objects"""
        pygame.init()
        self._screen = pygame.display.set_mode(
            [SCREEN_WIDTH, SCREEN_HEIGHT], HWSURFACE | DOUBLEBUF
        )
        self._screen.fill(pygame.Color("black"))
        pygame.display.set_caption("MetaBalls")
        self._clock = pygame.time.Clock()
        self._index_pixel = Vector2(0, 0)

        # Init metaballs in random positions
        self._balls = []
        for _ in range(N_BALLS):
            ball = Ball(
                self._screen,
                Vector2(
                    random.random() * (SCREEN_WIDTH - 1),
                    random.random() * (SCREEN_HEIGHT - 1),
                ),
                radius=BALL_RADIUS,
            )
            self._balls.append(ball)

        self._dt_seconds = None

        self._grid_xy = np.zeros((SCREEN_WIDTH * SCREEN_HEIGHT * 2)).reshape(
            SCREEN_WIDTH, SCREEN_HEIGHT, 2
        )

        self._img = np.zeros(SCREEN_WIDTH * SCREEN_HEIGHT).reshape(
            SCREEN_WIDTH, SCREEN_HEIGHT
        )

        for pos_x in range(SCREEN_WIDTH):
            for pos_y in range(SCREEN_HEIGHT):
                self._grid_xy[pos_x][pos_y] = pos_x, pos_y

    def show_fps(self) -> None:
        """ Show framerate in upper left corner """
        font = pygame.font.SysFont("Arial", 18)
        fps = str(f"{1/self._dt_seconds:.3f}")

        fps_text = font.render(fps, 1, pygame.Color("coral"))
        self._screen.blit(fps_text, (10, 0))

    def check_events(self) -> None:
        """ Check pygame events """
        # loop through all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def draw(self) -> None:
        """ Draw metaballs to screen """
        self._img.fill(0)

        for ball in self._balls:
            distances = euclid_dist(self._grid_xy, ball.pos_np)
            self._img += ball.radius / distances

        pygame.surfarray.blit_array(self._screen, gray(self._img))

    def update(self) -> None:
        """ Update objects """
        # Listcomprehension to be fast as possible
        [ball.update(self._dt_seconds) for ball in self._balls]

    def run(self) -> None:
        """ Main game loop to update and draw objects """
        # control the draw update speed
        self._dt_seconds = self._clock.tick(120) / 1000

        # check events
        self.check_events()

        self.update()
        self.draw()

        # update the screen with what we've drawn
        self.show_fps()
        pygame.display.flip()


if __name__ == "__main__":
    # initialize MetaBalls pygame
    meta_balls = MetaBalls()

    while True:
        # Run until user exits pygame window
        meta_balls.run()
