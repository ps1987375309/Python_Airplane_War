import random
import pygame
import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """
        飞机基类
    """
    # 飞机图片列表
    plane_images = []
    # 飞机爆炸图片列表
    destroy_images = []
    # 坠毁音乐地址
    down_sound_src =None
    # 飞机状态 True 活的 False 死的
    active = True
    # 飞机发射子弹精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self.screen = screen
        # 加载静态资源
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()
        # 飞机飞行速度
        self.speed = speed or 10    # 不传值默认为10
        # 获取飞机位置
        self.rect = self.img_list[0].get_rect()
        # 获取飞机宽度和高度
        self.plane_w, self.plane_h = self.img_list[0].get_size()
        # 获取屏幕宽度和高度
        self.width, self.height = self.screen.get_size()
        # 改变飞机初始位置
        self.rect.left = int((self.width - self.plane_w) / 2)
        self.rect.top = int(self.height / 2 + 150)

    def load_src(self):
        """
        加载静态资源
        """
        # 飞机图像
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))
        # 飞机坠毁图像
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))
        # 坠毁音乐
        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        """ 飞机向上移动 """
        self.rect.top -= self.speed

    def move_down(self):
        """ 飞机向下移动 """
        self.rect.top += self.speed

    def move_left(self):
        """ 飞机向左移动 """
        self.rect.left -= self.speed

    def move_right(self):
        """ 飞机向右移动 """
        self.rect.left += self.speed

    def broken_down(self):
        """ 飞机坠毁效果 """
        # 播放坠毁音乐
        if self.down_sound:
            self.down_sound.play()
        # 播放坠毁动画
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
        # 坠毁后
        self.active = False

    def shoot(self):
        """ 飞机发射子弹 """
        bullet = Bullet(self.screen, self, 10)
        self.bullets.add(bullet)   # 将子弹对象加入子弹精灵组里面


class OurPlane(Plane):
    """
        我方飞机类
    """
    # 飞机图片列表
    plane_images = constants.OUR_PLANE_IMG_LIST
    # 飞机爆炸图片列表
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    # 坠毁音乐地址
    down_sound_src = None

    def update(self, war):
        """ 更新飞机动画效果 """
        self.move(war.key_down)
        # 飞机喷气式效果
        if war.frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)

        # 飞机碰撞检测
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        if rest:
            # 游戏结束
            war.status = war.OVER
            # 敌方飞机清除
            war.enemies.empty()
            war.small_enemies.empty()
            # 我方飞机坠毁效果
            self.broken_down()
            # 记录游戏战绩

    def move(self, key):
        """  """
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        # 向上移动，超出范围重置
        super().move_up()   # 继承父类方法
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        # 向下移动，超出范围重置
        super().move_down()  # 继承父类方法
        if self.rect.top >= self.height-self.plane_h:
            self.rect.top = self.height-self.plane_h

    def move_left(self):
        # 向上移动，超出范围重置
        super().move_left()  # 继承父类方法
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        # 向上移动，超出范围重置
        super().move_right()  # 继承父类方法
        if self.rect.left >= self.width - self.plane_w:
            self.rect.left = self.width - self.plane_w


class SmallEnemyPlane(Plane):
    """ 敌方小型飞机类 """
    # 飞机图片列表
    plane_images = constants.SMALL_ENEMY_PLANE_IMG_LIST
    # 飞机爆炸图片列表
    destroy_images = constants.SMALL_ENEMY_PLANE_DESTROY_IMG_LIST
    # 坠毁音乐地址
    down_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SHOOT_SOUND

    def __init__(self, screen, speed):
        super().__init__(screen, speed)
        self.init_pos()

    def init_pos(self):
        # 随机位置生成敌机
        self.rect.left = random.randint(0, self.width - self.plane_w)
        # 屏幕之外随机高度
        self.rect.top = random.randint(-5 * self.plane_h, -self.plane_h)

    def update(self, *args):
        super().move_down()
        self.blit_me()
        # 向下超出屏幕之外，重置飞机
        if self.rect.top >= self.height:
            self.active = False
            self.reset()

    def reset(self):
        """ 重置飞机状态，达到复用效果 """
        self.active = True
        self.init_pos()

    def broken_down(self):
        # 飞机爆炸
        super().broken_down()
        # 重复利用
        self.reset()