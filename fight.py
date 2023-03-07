# -*- encoding=utf8 -*-
__author__ = "liqingshan"

from airtest.core.api import *

leader_eliminate_3 = Template(r"tpl1677984928248.png", record_pos=(0.299, 0.231), resolution=(1280, 720))
leader_eliminate_1 = Template(r"tpl1677985221033.png", record_pos=(0.402, 0.232), resolution=(1280, 720))
level_up_icon = Template(r"tpl1677985315974.png", record_pos=(0.003, -0.173), resolution=(1280, 720))
reach_highest_level = Template(r"tpl1677985458032.png", record_pos=(-0.005, -0.18), resolution=(1280, 720))
back_town_icon = Template(r"tpl1677985521565.png", record_pos=(0.276, 0.212), resolution=(1280, 720))
confirm_btn = Template(r"tpl1677985332308.png", record_pos=(-0.001, 0.184), resolution=(1280, 720))
goddess_skills = Template(r"tpl1677985094706.png", record_pos=(0.409, 0.156), resolution=(1280, 720))


def handle_fight():
    if exists(leader_eliminate_3):
        touch(leader_eliminate_3);
    
    elif exists(leader_eliminate_1):
        touch(leader_eliminate_1);
        
        
def handle_levelup():
    if exists(level_up_icon):
        touch(confirm_btn);
        sleep(0.5)
        
    if exists(reach_highest_level):
        touch(confirm_btn);
        sleep(0.5)
    

def handle_back_town():
    if exists(back_town_icon):
        touch(back_town_icon);
        sleep(0.5)
    


def use_goddess_skills():
    if exists(goddess_skills):
        touch(goddess_skills);
        sleep(0.5)
    