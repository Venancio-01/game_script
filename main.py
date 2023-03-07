# -*- encoding=utf8 -*-
__author__ = "liqingshan"

# import threading

from airtest.core.api import *
from utils import *
from account import *
from record import *

auto_setup(__file__)

# 应用包名
pkg_name = "com.nhnet.SKQUEST"


# 打开菜单，删除角色
def handle_delete_character():
    open_menu()
    delete_character()


def main():
    handle_login()
    on_enter_game()
    set_character_name()
    after_set_name()
    handle_set_team()
    handle_first_battle()
    handle_grow_up()
    handle_learn_skills()
    handle_view_store()
    handle_view_task()
    handle_view_account()
    handle_get_hero()
    # handle_delete_character()


main()

