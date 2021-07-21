#!/usr/bin/env python3

import pygame
import dimenstions
from mainTime import myTime
import colors
from screen import screen

pygame.init()
running = True
clock = pygame.time.Clock()

# SOUND


pygame.display.set_caption("STT")
pygame.font.init()
timeFont = pygame.font.SysFont("monospace ", 40)
timeText = timeFont.render(myTime.returnTimeFormatted(), False, colors.GREEN)

passed_time = 0
while running:
    dt = clock.tick()
    passed_time += dt
    if passed_time > 1000:
        passed_time = 0
        if myTime.status == "active":
            myTime.passSecond()

    timeText = timeFont.render(myTime.returnTimeFormatted(), False, colors.GREEN)
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
