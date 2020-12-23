# 引入相关的包
import sys, pygame

# pygame进行初始化
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

# 得到屏幕对象
screen = pygame.display.set_mode(size)

ball = pygame.image.load("./static/intro_ball.gif")
ballrect = ball.get_rect()

# 游戏主循环
while 1:

    # 处理游戏的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # 更新游戏的状态
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # 在屏幕上面进行绘制
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()