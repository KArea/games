import pygame
import sys

#初始化pygame
pygame.init()

#定义窗口尺寸；移动速度；背景颜色
size = width,height = 600,400
speed = [-2,1]
bg = (255,255,255)

#创建指定尺寸窗口；设置窗口标题；加载图片并用变量turtle指向图片
screen = pygame.display.set_mode(size)
pygame.display.set_caption('初次见面，请大家多多关照！')
turtle = pygame.image.load('turtle.png')

#获取图片的位置矩形
position = turtle.get_rect()
#用transform.flip方法定义图像的左右转向动作
l_head = turtle
r_head = pygame.transform.flip(turtle,True,False)

while True:
    #设定退出条件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            turtle = l_head
            speed = [-1,0]
        if event.key == pygame.K_RIGHT:
            turtle = r_head
            speed = [1,0]
        if event.key == pygame.K_UP:
            speed = [0,-1]
        if event.key == pygame.K_DOWN:
            speed = [0,1]
    
    #移动图像
    position = position.move(speed)

    #用transform.flip方法翻转图像，参数为：图片变量；x轴翻转；y轴翻转
    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle,True,False)
        #x方向速度取反
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)                     #填充背景色
    screen.blit(turtle,position)        #在背景上绘制图片
    pygame.display.flip()               #刷新屏幕
    pygame.time.delay(10)               #挂起程序
