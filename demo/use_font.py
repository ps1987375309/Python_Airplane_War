import sys,pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

# 定义颜色
red = pygame.Color(255,0,0)

# 查看系统字体
# fonts = pygame.font.get_fonts()
# print(fonts)

# 使用字体 方式一 使用系统字体
# font = pygame.font.SysFont('fangsong',40,True,True)
# 方式二  使用自定义字体
font = pygame.font.Font('simkai.ttf',40)

# 文字对象
text = font.render('得分',True,red)

# 加载背景音乐
bg_music = pygame.mixer.music.load('./static/bg_music.mp3')

# 设置音量取值范围0-1
pygame.mixer.music.set_volume(0.5)

# 播放音乐
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 绘制
    screen.blit(text,(20,20))
    # 渲染输出
    pygame.display.flip()