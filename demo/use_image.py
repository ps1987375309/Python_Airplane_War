import sys, pygame

# 初始化
pygame.init()

# 创建屏幕对象
screen =pygame.display.set_mode((500,500))

# 加载图片
ball = pygame.image.load('./static/intro_ball.gif')

# 创建颜色
red = pygame.Color(255,0,0)

# 游戏主循环
while True:
    # 处理事件--点击关闭
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 画线
    pygame.draw.line(screen,red,(1,1),(200,200),8)
    # 绘制
    screen.blit(ball,(100,100))
    pygame.display.flip()