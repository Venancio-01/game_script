# -*- encoding=utf8 -*-
__author__ = "liqingshan"

from airtest.core.api import *

import random

start_game_text = Template(
    r"tpl1677980228353.png", record_pos=(0.0, 0.219), resolution=(1280, 720)
)
weibo_login_icon = Template(
    r"tpl1677979851317.png", record_pos=(0.0, 0.011), resolution=(1280, 720)
)
menu_icon = Template(
    r"tpl1677978989963.png", record_pos=(0.459, -0.249), resolution=(1280, 720)
)
skip_icon = Template(
    r"tpl1677983392537.png", record_pos=(0.305, -0.251), resolution=(1280, 720)
)
continue_icon = Template(
    r"tpl1677988160158.png", record_pos=(0.354, 0.198), resolution=(1280, 720)
)
account_icon = Template(
    r"tpl1677979474528.png", record_pos=(0.002, 0.067), resolution=(1280, 720)
)
confirm_btn = Template(
    r"tpl1677979425371.png", record_pos=(0.091, 0.147), resolution=(1280, 720)
)

# 随机等待
def handle_sleep(type="short"):
    map = {
        "short": [0.3, 0.8],
        "middle": [0.8, 1.5],
        "long": [1.5, 2.5],
    }
    sleep(random.uniform(*map[type]))


# 等待图片出现并执行操作
def wait_appear_and_operate(img, fn=lambda image: touch(image)):
    while True:
        if exists(img):
            fn()
            break


# 点击屏幕右侧区域
def handle_click():
    x_range = [782, 1024]
    y_range = [184, 390]
    point = [
        random.randint(x_range[0], x_range[1]),
        random.randint(y_range[0], y_range[1]),
    ]

    touch(point)


# 打开菜单
def open_menu():
    while True:
        if exists(menu_icon):
            touch(menu_icon)
            break
        else:
            keyevent("BACK")
            sleep(0.3)


def handle_skip():
    if exists(skip_icon):
        print("exists skip_icon")
        touch(skip_icon)
        sleep(0.5)

    if exists(continue_icon):
        print("exists continue_icon")
        touch(continue_icon)
        sleep(0.5)
