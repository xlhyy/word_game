# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, render_template, request

app = Flask(__name__)

from gconfig import game_config


@app.route("/", methods=["GET"])
def index():
    """
    首页
    :return:
    """
    cur_num = int(request.args.get("cur_num", 0))
    cur_choose = request.args.get("cur_choose", "A")
    data = init_map()
    if cur_num+1 > len(data):
        cur_num = 0
        cur_choose = ""

    return render_template("index.html", cur_num=cur_num, cur_choose=cur_choose, data=data)


def init_map():
    """
    初始化地图
    :return:
    """
    result = {}
    point_config = game_config.map["point"]
    choose_config = game_config.map["choose"]

    num = 0
    for point_id in point_config.keys():
        config = point_config[point_id]
        result[num] = {
            "des": config["des"],
            "img": config["img"],
            "A": choose_config[config["A"]],
            "B": choose_config[config["B"]],
        }
        num += 1
    return result


if __name__ == "__main__":
    app.run(debug=True)
