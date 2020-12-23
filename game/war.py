import pygame
import sys

import constants
from game.plane import OurPlane, SmallEnemyPlane
from store.result import PlayRest


class PlaneWar(object):
    """ 飞机大战 """
    READY = 0    # 准备中
    PLAYING = 1  # 游戏中
    OVER = 2     # 游戏结束

    # 游戏状态
    status = READY

    our_plane = None
    frame = 0  # 播放帧数

    # 一架飞机可以属于多个精灵组
    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # 游戏结果
    rest = PlayRest()

    def __init__(self):
        pygame.init()
        # 获取屏幕对象
        self.width, self.height = 480, 852
        self.screen = pygame.display.set_mode((self.width, self.height))

        # 设置标题
        pygame.display.set_caption('飞机大战')

        # 加载背景图片
        self.bg = pygame.image.load(constants.BG_IMG)
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)
        # 游戏标题
        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()
        # 游戏标题图片的宽度和高度
        t_width, t_height = self.img_game_title.get_size()
        # 标题位置
        self.img_game_title_rect.topleft = (int((self.width - t_width) / 2), int(self.height / 2 - t_height))

        # 开始按钮
        self.btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
        self.btn_start_rect = self.btn_start.get_rect()
        btn_width, btn_height = self.btn_start.get_size()
        self.btn_start_rect.topleft = (int((self.width - btn_width) / 2), int(self.height / 2 + btn_height))

        # 游戏文字字体
        self.score_font = pygame.font.SysFont('fangsong', 32)

        # 加载背景音乐播放及设置音量
        # pygame.mixer.music.load(constants.BG_MUSIC)
        # pygame.mixer.music.play(-1)
        # pygame.mixer.music.set_volume(0.2)

        # 我方飞机对象
        self.our_plane = OurPlane(self.screen, speed=5)

        self.clock = pygame.time.Clock()

        # 记录上次按键，用于控制飞机
        self.key_down = None

    def bind_event(self):
        """ 绑定事件"""
        # 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 退出游戏
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标点击进入游戏
                if self.status == self.READY:
                    self.status = self.PLAYING
                    self.rest.score = 0
                elif self.status == self.OVER:
                    self.status = self.READY
                    self.add_small_enemies(6)
            elif event.type == pygame.KEYDOWN:
                # 键盘事件 ASWD
                self.key_down = event.key
                if self.status == self.PLAYING:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.our_plane.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.our_plane.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.our_plane.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.our_plane.move_right()
                    elif event.key == pygame.K_SPACE:
                        # 发射子弹
                        self.our_plane.shoot()

    def add_small_enemies(self, num):
        # 随机添加N架小型飞机
        for i in range(num):
            plane = SmallEnemyPlane(self.screen, 3)
            plane.add(self.small_enemies, self.enemies)

    def run_game(self):
        """ 游戏主循环部分 """
        while True:
            # 设置帧速率
            self.clock.tick(60)
            self.frame += 1
            if self.frame >= 60:  # 防止一直往上加很大占用内存
                frame = 0
            # 绑定事件
            self.bind_event()

            # 更新游戏状态
            if self.status == self.READY:  # 游戏准备中
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 标题
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                # 开始按钮
                self.screen.blit(self.btn_start, self.btn_start_rect)
                # 重置移动按键
                self.key_down = None
            elif self.status == self.PLAYING:  # 游戏进行中
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 绘制飞机
                self.our_plane.update(self)
                # 绘制子弹
                self.our_plane.bullets.update(self)
                # 绘制敌方飞机
                self.small_enemies.update()
                # 游戏分数
                score_text = self.score_font.render('得分：{0}'.format(self.rest.score),
                                                    False, constants.TEXT_SCORE_COLOR)
                self.screen.blit(score_text, score_text.get_rect())
            elif self.status == self.OVER:  # 游戏结束
                # 游戏背景
                self.screen.blit(self.bg_over, self.bg_over.get_rect())
                # 本局分数统计
                score_text = self.score_font.render('{0}'.format(self.rest.score),
                                                    False, constants.TEXT_SCORE_COLOR)
                score_text_rect = score_text.get_rect()
                text_w, text_h = score_text.get_size()
                score_text_rect.topleft = (
                    int((self.width - text_w) / 2),
                    int(self.height / 2)
                )
                self.screen.blit(score_text, score_text_rect)
                # 历史最高分数
                score_his = self.score_font.render(
                    '{0}'.format(self.rest.get_max_score()), False, constants.TEXT_SCORE_COLOR
                )
                self.screen.blit(score_his, (150, 40))
            pygame.display.flip()
