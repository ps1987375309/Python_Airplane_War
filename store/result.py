import constants


class PlayRest(object):
    __score = 0
    __life = 3      #飞机生命数量
    __blood = 1000  #飞机血量

    @property
    def score(self):
        """ 单次游戏分数 """
        return self.__score

    @score.setter
    def score(self, value):
        """ 设置分数 """
        if value < 0:
            return None
        self.__score = value

    def set_history(self):
        """ 记录最高分 """
        if int(self.get_max_score()) < self.score:
            with open(constants.PLAY_RESULT_STORE_FILE, 'w') as f:
                f.write('{0}'.format(self.score))

    def get_max_score(self):
        """ 读取文件历史最高分 """
        rest = 0
        with open(constants.PLAY_RESULT_STORE_FILE, 'r') as f:
            r = f.read()
            if r:
                rest = r
        return rest
