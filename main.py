# -*- encoding=utf8 -*-
__author__ = "liqingshan"

# import threading

from airtest.core.api import *

from utils import handle_skip,open_menu,handle_fllow

from account import handle_login,set_character_name,delete_character

from fight import handle_fight,use_goddess_skills,handle_levelup,handle_back_town

from record import on_enter_game,fight,team,grow_up,learn_skills,store,task,account,get_hero,after_set_name

auto_setup(__file__)


pkg_name = 'com.nhnet.SKQUEST'


# set_character_name()


def delete():
    open_menu()
    delete_character()
    

# handle_login()
# on_enter_game()
# set_character_name()
# after_set_name()
# team()
# fight()
# grow_up()
# learn_skills()
store()
task()
account()
get_hero()
# delete()

