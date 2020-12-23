import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    """ 子弹类 """

    # 子弹状态
    active = True

    def __init__(self, screen, plane, speed = None):
        super().__init__()
        self.screen = screen
        # 子弹速度
        self.speed = speed or 10
        # 飞机对象，判断子弹来自于哪架飞机
        self.plane = plane
        # 加载子弹图片
        self.image = pygame.image.load(constants.BULLET_IMG)

        # 改变子弹位置
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx     # 水平居中
        self.rect.top = plane.rect.top     # 射出去的位置就是飞机顶部

        # 发射的音乐效果
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, war):
        """ 更新子弹位置 """
        self.rect.top -= self.speed   # 子弹向上移动，每次自动，距离顶部的距离减少对应的速度值
        # 超过范围销毁
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        # 绘制子弹
        self.screen.blit(self.image, self.rect)
        # 碰撞检测，检测子弹是否已经碰撞到了敌机
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        # print(rest, 666)
        for r in rest:
            # 子弹消失
            self.kill()
            # 飞机爆炸，坠毁效果
            r.broken_down()
            # 成绩统计
            war.rest.score += constants.SCORE_SHOOT_SMALL
            # 保存历史记录
            war.rest.set_history()
