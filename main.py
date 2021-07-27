#!/usr/bin/env python3

import sys
import pygame
import os
from src.colors import myColors
import config

# from src.screen import screen
# from screen import screen
# from src.mainTime import myTime
from src.screen import screen
from src.mainTime import myTime

print(config.color)

pygame.init()
pygame.display.set_caption("STT")
clock = pygame.time.Clock()

pygame.font.init()
timeFont = pygame.font.SysFont("Helvetica", 60)
sessionLeftFont = pygame.font.SysFont("Helvetica", 30)
timeText = timeFont.render(
    myTime.returnTimeFormatted(), False, getattr(myColors, config.color)
)
sessionLeftText = sessionLeftFont.render(
    myTime.returnSessionLeftRatio(), False, getattr(myColors, config.color)
)
passed_time = 0
running = True


while running:
    # width and height of the game window
    w, h = pygame.display.get_surface().get_size()
    dt = clock.tick()
    passed_time += dt
    if passed_time > 1000:
        if myTime.status == "active":
            myTime.passSecond()
            passed_time = 0
        elif myTime.status == "downtime":
            if myTime.firstAlarmOff == True:
                myTime.playAlarm()
                myTime.firstAlarmOff = False
            elif passed_time > 3000:
                myTime.playAlarm()
                passed_time = 0

    timeText = timeFont.render(
        myTime.returnTimeFormatted(), False, getattr(myColors, config.color)
    )

    sessionLeftText = sessionLeftFont.render(
        myTime.returnSessionLeftRatio(), False, getattr(myColors, config.color)
    )

    screen.fill(getattr(myColors, config.background_color))
    screen.blit(timeText, [w / 2 - 55, h / 2 - 35])
    # screen.blit(sessionLeftText, [w / 2 - 20, h / 2 + 35])
    screen.blit(sessionLeftText, [w - 50, h - 40])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_w and myTime.status == "downtime":
                myTime.setStatus("active")
            if event.key == pygame.K_w and myTime.status == "finished":
                running = False

    pygame.display.update()
    pygame.display.flip()


pygame.quit()
