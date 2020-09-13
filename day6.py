#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Product : untitled3
# @File    : day6.py
# @Author  : Poyeh Li
# @Time    : 2020/8/31 9:04
import pygame ,sys
pygame.init()
screen = pygame.display.set_mode(500,400)
pygame.display.set_caption('Font')
WHITE = (255,255,255)
GREEN = (0,255.0)
BLUE = (0,0,128)

fontObject = pygame.font.Font('123.ttf',50)
textSuefaceObject = fontObject.render('pygame',Ture,BLUE,GREEN)
textRectObject = textSuefaceObject.get_reet()
textRectObject.conter = (250,250)

screen.fill(WHITE)