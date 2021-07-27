import pygame
import sys

from src.dimensions import window_height, window_width

screen = pygame.display.set_mode(
    (window_width, window_height), pygame.RESIZABLE
)
