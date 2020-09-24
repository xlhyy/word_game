# coding: utf-8

from gconfig.map_config import map_name, map_point, map_choose


class GameConfig(object):
    """
    游戏配置
    """
    @property
    def map(self):
        return {
            "point": map_point,
            "choose": map_choose,
        }


game_config = GameConfig()