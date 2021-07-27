#!/usr/bin/env python3

import sys
import collections
import pygame
import os
from src.matchColors import returnMatchedColors
from src.colors import myColors
from src.screen import screen
from src.mainTime import myTime
import config

color, background_color = returnMatchedColors()

pygame.init()
pygame.display.set_caption("STT")
clock = pygame.time.Clock()

pygame.font.init()
timeFont = pygame.font.SysFont("Helvetica", 60)
sessionLeftFont = pygame.font.SysFont("Helvetica", 30)
timeText = timeFont.render(myTime.returnTimeFormatted(), False, color)

sessionLeftText = sessionLeftFont.render(myTime.returnSessionLeftRatio(), False, color)

passed_time = 0
running = True


while running:
    # width and height of the game window
    w, h = pygame.display.get_surface().get_size()
    dt = clock.tick()
    passed_time += dt
    if passed_time > 100:
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

    timeText = timeFont.render(myTime.returnTimeFormatted(), False, color)

    sessionLeftText = sessionLeftFont.render(
        myTime.returnSessionLeftRatio(), False, color
    )

    screen.fill(background_color)
    screen.blit(timeText, timeText.get_rect(center=screen.get_rect().center))
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
