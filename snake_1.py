#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Product : untitled3
# @File    : snake_1.py
# @Author  : Poyeh Li
# @Time    : 2020/9/1 15:44
import pygame,random
from sys import exit
import time
pygame.init()
width = 640
high = 480

class Pic():
    row = 0
    clo = 0
    def __init__(self, row,clo):
        self.row = row
        self.clo = clo
    def copy(self):
        return Pic(row = self.row, clo = self.clo)

def shuai():
    while 1:
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 128)
        screen = pygame.display.set_mode((width, high), 0, 32)
        # pygame.draw.rect(screen,(255,255,255),(0,0,width,height))
        filename = '雪中悍刀行.png'
        p = pygame.image.load(filename)
        p = pygame.transform.scale(p, (500, 500))
        screen.blit(p, [0, 0])
        fontObject = pygame.font.Font('123.ttf', 30)
        textSurfaceObject = fontObject.render('开心吧,我没记分', True, BLUE, GREEN)
        textRectObject = textSurfaceObject.get_rect()
        textRectObject.center = (650, 200)
        screen.blit(textSurfaceObject, textRectObject)
        pygame.display.flip()
        time.sleep(5)
        break
pygame.init()
width = 800
high = 400
ROW ,CLO = 30,40

direct = 'left'
screen = pygame.display.set_mode((width,high))
pygame.display.set_caption('贪食蛇')

head = Pic(row = int(ROW/2),clo = int(CLO/2))


snake = [
    Pic(row = head.row,clo =head.clo+1),
    Pic(row = head.row,clo =head.clo+2),
    Pic(row = head.row,clo =head.clo+3)
]

def gen_food():
    while 1:
        pos = Pic(row = random.randint(0,ROW-1),clo = random.randint(0,CLO-1))
        is_call = False
        if head.row == pos.row and head.clo == pos.clo:
            is_call = True
        for body in snake:
            if body.row == pos.row and body.clo == pos.clo:
                is_call = True
                break
        if not is_call:
            break
    return pos

head_color = (0,158,128)
snakeFood = gen_food()
snakeFood_color = (255, 0, 0)
snake_color =(200, 147, 158)

def rect(pic,color):
    left = pic.clo*width/CLO
    top = pic.row*high/ROW
    pygame.draw.rect(screen,color,(left ,top, width/CLO,high/ROW))
def speed():
    time.sleep(0.1)

quit = True
clock = pygame.time.Clock()
while (quit):
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 273 or event.key == 119:
                if direct == 'left' or direct == 'right':
                    direct = 'top'
            if event.key == 274 or event.key == 115:
                if direct == 'left' or direct == 'right':
                    direct = 'bottom'
            if event.key == 276 or event.key == 97:
                if direct == 'top' or direct == 'bottom':
                    direct = 'left'
            if event.key == 275 or event.key == 100:
                if direct == 'top' or direct == 'bottom':
                    direct = 'right'

    eat = (head.row == snakeFood.row and head.clo == snakeFood.clo)

    if eat:
        snakeFood = Pic(row = random.randint(0,ROW - 1),clo = random.randint(0,CLO - 1))
    snake.insert(0,head.copy())
    if not eat:
        snake.pop()

    if direct == 'left':
        speed()
        head.clo -= 1
    if direct == 'right':
        speed()
        head.clo += 1
    if direct == 'top':
        speed()
        head.row -= 1
    if direct == 'bottom':
        speed()
        head.row += 1

    dead = False
    if head.clo <0 or head.row<0 or head.clo >=CLO or head.row >= ROW:
        dead = True
        for body in snake:
            if head.clo ==body.clo and head.row == body.row:
                dead = True
                break
        if dead:
            print("GAME OVER")
            shuai()
            quit = False


    pygame.draw.rect(screen,(255,255,255),(0,0,width,high))
    rect(head,head_color)
    rect(snakeFood,snakeFood_color)
    for body in snake:
        rect(body, snake_color)
    pygame.display.flip()