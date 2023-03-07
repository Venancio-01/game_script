# -*- encoding=utf8 -*-
__author__ = "liqingshan"

from airtest.core.api import *
from utils import *

start_game_text = Template(
    r"tpl1677980228353.png", record_pos=(0.0, 0.219), resolution=(1280, 720)
)
weibo_login_icon = Template(
    r"tpl1677979851317.png", record_pos=(0.0, 0.011), resolution=(1280, 720)
)
set_name_area = Template(
    r"tpl1677981552586.png", record_pos=(0.001, -0.037), resolution=(1280, 720)
)
set_name_input = Template(
    r"tpl1677981665105.png", record_pos=(-0.054, -0.033), resolution=(1280, 720)
)
reconfirm_btn = Template(
    r"tpl1677981585460.png", record_pos=(0.126, -0.035), resolution=(1280, 720)
)
account_icon = Template(
    r"tpl1677979474528.png", record_pos=(0.002, 0.067), resolution=(1280, 720)
)
confirm_btn = Template(
    r"tpl1677983254926.png", record_pos=(0.005, 0.131), resolution=(1280, 720)
)

delete_confirm_btn = Template(
    r"tpl1677989721253.png", record_pos=(0.091, 0.166), resolution=(1280, 720)
)


def handle_login():
    if not exists(weibo_login_icon):
        return

    touch(weibo_login_icon)

    wait_appear_and_operate(
        Template(
            r"tpl1677980040843.png", record_pos=(0.001, -0.253), resolution=(720, 1280)
        )
    )
    sleep(2)

    if exists(
        Template(
            r"tpl1677992366848.png", record_pos=(-0.002, 0.147), resolution=(1280, 720)
        )
    ):
        touch(
            Template(
                r"tpl1677992366848.png",
                record_pos=(-0.002, 0.147),
                resolution=(1280, 720),
            )
        )
        sleep(0.75)
        handle_login()

    wait_appear_and_operate(start_game_text)


# 设置角色名称
def set_character_name():
    def handle_click_confirm():
        touch(confirm_btn)

    def handle_set_name():
        touch(set_name_input)
        handle_sleep()
        text("Venancio001")
        handle_sleep()
        touch(reconfirm_btn)
        handle_sleep()
        touch(reconfirm_btn)
        wait_appear_and_operate(
            Template(
                r"tpl1677992978066.png",
                record_pos=(-0.004, 0.067),
                resolution=(1280, 720),
            ),
            handle_click_confirm,
        )

    wait_appear_and_operate(set_name_area, handle_set_name)


# 删除角色
def delete_character():
    def handle_delete_character():
        touch(account_icon)
        handle_sleep()
        touch(
            Template(
                r"tpl1677978481930.png",
                record_pos=(0.149, 0.177),
                resolution=(1280, 720),
            )
        )
        handle_sleep()
        touch(
            Template(
                r"tpl1677978506150.png",
                record_pos=(0.089, -0.016),
                resolution=(1280, 720),
            )
        )
        handle_sleep()
        if exists(
            Template(
                r"tpl1677978704216.png",
                record_pos=(0.001, 0.07),
                resolution=(1280, 720),
            )
        ):
            touch(
                Template(
                    r"tpl1677978704216.png",
                    record_pos=(0.001, 0.07),
                    resolution=(1280, 720),
                )
            )
            handle_sleep()
            if exists(
                Template(
                    r"tpl1677978752969.png",
                    record_pos=(-0.001, 0.071),
                    resolution=(1280, 720),
                )
            ):
                touch(delete_confirm_btn)
                handle_sleep()
                touch(delete_confirm_btn)

    wait_appear_and_operate(account_icon, handle_delete_character)
