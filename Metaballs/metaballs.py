# PyGame Skeleton
""" Pygame application which calculate metaballs in python/pygame
"""
import sys
import random
import pygame

from pygame import draw
from pygame.locals import HWSURFACE, DOUBLEBUF
from pygame.math import Vector2

from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 5000
N_BALLS = 6


def color_grey(value: int) -> pygame.Color:
    """ Calculate rgb grayscale value """
    value = int(value)
    if value >= 255:
        value = 255
    return pygame.Color(*((value,) * 3))


class MetaBalls:
    """Metaball game"""

    def __init__(self) -> None:
        """Init pygame and related game objects"""
        pygame.init()
        self._screen = pygame.display.set_mode(
            [SCREEN_WIDTH, SCREEN_HEIGHT], HWSURFACE | DOUBLEBUF
        )

        pygame.display.set_caption("MetaBalls")
        self._clock = pygame.time.Clock()
        self._index_pixel = Vector2(0, 0)
        self._balls = Ball(self._screen, Vector2(50, 50), radius=BALL_RADIUS)
        self._dt_seconds = None
        self._color = pygame.Color(0, 0, 0)
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

    def draw(self):
        """ Draw metaballs to screen """
        for pos_x in range(SCREEN_WIDTH):
            for pos_y in range(SCREEN_HEIGHT):
                pixel_value = 0
                # calculate pixel value and draw each pixel
                for ball in self._balls:
                    self._index_pixel[:] = pos_x, pos_y
                    distance = self._index_pixel.distance_to(ball.pos)
                    pixel_value += ball._radius / distance

                self._screen.set_at((pos_x, pos_y), color_grey(pixel_value))

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
    # initialise MetaBalls pygame
    mb = MetaBalls()
    while True:
        mb.run()
