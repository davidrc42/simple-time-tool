#!/usr/bin/env python3

import pygame
import sys
import dimenstions
import config
from mainTime import myTime
import colors
from screen import screen
from varname.helpers import Wrapper
from playsound import playsound

pygame.init()
running = True
clock = pygame.time.Clock()

pygame.display.set_caption("STT")
pygame.font.init()
timeFont = pygame.font.SysFont("monospace ", 40)
timeText = timeFont.render(myTime.returnTimeFormatted(), False, colors.GREEN)
passed_time = 0

while running:
    dt = clock.tick()
    passed_time += dt
    if passed_time > 6:
        if myTime.status == "downtime":
            if passed_time > 2000:
                playsound("/home/david/code/simple-time-tool/src/birdSound.wav")
                passed_time = 0
        elif myTime.status == "active":
            myTime.passSecond()
            passed_time = 0

    timeText = timeFont.render(myTime.returnTimeFormatted(), False, colors.WHITE)
    # clock.tick(FPS)
    screen.fill(colors.BLACK)
    screen.blit(timeText, [140, 180])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and myTime.status == "downtime":
                myTime.setStatus("active")

    pygame.display.update()
    pygame.display.flip()


pygame.quit()
