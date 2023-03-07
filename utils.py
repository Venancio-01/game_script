# -*- encoding=utf8 -*-
__author__ = "liqingshan"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import random

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

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
point_icon_1 = Template(
    r"tpl1677984279265.png", record_pos=(0.272, 0.201), resolution=(1280, 720)
)
point_icon_2 = Template(
    r"tpl1677983974150.png", record_pos=(0.289, 0.202), resolution=(1280, 720)
)


def wait_appear_and_click(img, fn=lambda image: touch(image)):
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
    if not exists(menu_icon):
        while not exists(menu_icon):
            keyevent("BACK")
            sleep(0.5)
    touch(menu_icon)
    sleep(0.5)


def handle_skip():
    if exists(skip_icon):
        print("exists skip_icon")
        touch(skip_icon)
        sleep(0.5)

    if exists(continue_icon):
        print("exists continue_icon")
        touch(continue_icon)
        sleep(0.5)
