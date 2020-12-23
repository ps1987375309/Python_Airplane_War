import sys, pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
# 加载图片
image = pygame.image.load('./static/hero1.png')
image2 = pygame.image.load('./static/hero2.png')

# 定义控制帧速率对象
clock = pygame.time.Clock()

#控制图片切换
counter = 0

while True:
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 控制帧速率
    clock.tick(60)

    # 绘制白色背景
    screen.fill(pygame.Color(255,255,255))
    # 绘制图片
    if (counter % 5 == 0):
        screen.blit(image,(20,20))
    else:
        screen.blit(image2,(20, 20))

    # 渲染
    pygame.display.flip()