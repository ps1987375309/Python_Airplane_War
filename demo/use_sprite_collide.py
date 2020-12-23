# 引入相关的包
import sys, pygame

# pygame进行初始化
pygame.init()

size = width, height = 320, 240

# 得到屏幕对象
screen = pygame.display.set_mode(size)

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height , init_pso):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        # 起始坐标点
        self.rect.topleft = init_pso


# 精灵实例
sprite_1 = Block(pygame.Color(255,0,0,),50,50,(50,50))   #颜色,大小及位置
sprite_2 = Block(pygame.Color(0,255,0,),50,50,(90,90))   #颜色,大小及位置


# 游戏主循环
while 1:

    # 处理游戏的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 绘制精灵
    screen.blit(sprite_1.image,sprite_1.rect)
    screen.blit(sprite_2.image,sprite_2.rect)

    # 矩形检测碰撞
    rest = pygame.sprite.collide_rect(sprite_1,sprite_2)
    print('rest',rest)
    # 矩形检测碰撞(更精确的碰撞，数值越大，触碰的范围(重叠区域)越大)
    rest2 = pygame.sprite.collide_rect_ratio(0.5)(sprite_1, sprite_2)
    print('rest2', rest2)
    pygame.display.flip()