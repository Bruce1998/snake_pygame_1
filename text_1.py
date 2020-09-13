import pygame, sys
from pygame.locals import *
> # 初始化pygame
> pygame.init()
> # 窗口
> screen = pygame.display.set_mode((500,400))
> pygame.display.set_caption('Font')
> # 设定颜色
> WHITE = (255,255,255)
> GREEN = (0,255,0)
> BLUE = (0,0,128)
> # 字体
> fontObject = pygame.font.Font('resources/ARBERKLEY.ttf',50)
> textSurfaceObject = fontObject.render('PyGame',True,BLUE,GREEN)
> textRectObject = textSurfaceObject.get_rect()
> textRectObject.center = (250,200)
> # 背景
> screen.fill(WHITE)
> # 绘制字体
> screen.blit(textSurfaceObject, textRectObject)
> while True:
>     for event in pygame.event.get():
>         if event.type == QUIT:
>             pygame.quit()
>             sys.exit()
>     pygame.display.update()