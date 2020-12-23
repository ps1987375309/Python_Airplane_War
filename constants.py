import os
import pygame



# 项目根目录
BASS_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件目录
ASSETS_DIR = os.path.join(BASS_DIR, 'assets')
# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMG_OVER = os.path.join(ASSETS_DIR, 'images/game_over.png')
# 游戏标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
# 游戏播放按钮图片
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')
# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.mp3')
# 游戏分数颜色
TEXT_SCORE_COLOR = pygame.Color(255,255,0)

# 我方飞机静态资源
OUR_PLANE_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero1.png'),
    os.path.join(ASSETS_DIR, 'images/hero2.png')
]

OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png')
]

# 子弹静态资源
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')

# 敌方小型飞机静态资源
SMALL_ENEMY_PLANE_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1.png')
]

SMALL_ENEMY_PLANE_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down4.png')
]
SMALL_ENEMY_PLANE_DOWN_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sounds/enemy1_down.wav')
# 击中小型飞机得分
SCORE_SHOOT_SMALL = 10

# 游戏结果存储文件地址
PLAY_RESULT_STORE_FILE = os.path.join(BASS_DIR, 'store/rest.txt')
