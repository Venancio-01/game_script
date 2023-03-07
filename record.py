# -*- encoding=utf8 -*-
__author__ = "liqingshan"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from utils import handle_click
import random


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

skip_icon = Template(r"tpl1677990215475.png", record_pos=(0.303, -0.251), resolution=(1280, 720))
continue_icon = Template(r"tpl1677992654596.png", record_pos=(0.405, 0.23), resolution=(1280, 720))

set_name_area = Template(r"tpl1677981552586.png", record_pos=(0.001, -0.037), resolution=(1280, 720))


def on_enter_game():
    while True:
        if exists(set_name_area):
            break
            
        if exists(skip_icon):
            touch(skip_icon)
            continue
        
        touch([10,10])
        sleep(0.5)
        

            
def after_set_name():
    while True:
        if exists(Template(r"tpl1677990696427.png", record_pos=(0.311, -0.25), resolution=(1280, 720))):
            touch(Template(r"tpl1677990696427.png", record_pos=(0.311, -0.25), resolution=(1280, 720)));
            sleep(0.75)
        
        elif exists(Template(r"tpl1677997732476.png", record_pos=(0.302, -0.251), resolution=(1280, 720))):
            touch(Template(r"tpl1677997732476.png", record_pos=(0.302, -0.251), resolution=(1280, 720)));
            sleep(0.75)
        
        elif exists(Template(r"tpl1677990659137.png", record_pos=(0.406, 0.232), resolution=(1280, 720))):
            touch(Template(r"tpl1677990659137.png", record_pos=(0.406, 0.232), resolution=(1280, 720)))
            sleep(0.75)
            
        else: touch([10.10])
        
        if exists(Template(r"tpl1677990761162.png", record_pos=(0.398, 0.185), resolution=(1280, 720))):
            break
                    

# 设置队伍
def handle_set_team():
    touch(Template(r"tpl1677990761162.png", record_pos=(0.398, 0.185), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677990765335.png", record_pos=(-0.362, 0.034), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677990769360.png", record_pos=(-0.325, 0.0), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677990773101.png", record_pos=(0.312, 0.209), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677990776995.png", record_pos=(0.31, 0.194), resolution=(1280, 720)))
    sleep(0.75)

    while True:
        if exists(Template(r"tpl1677990790296.png", record_pos=(-0.254, 0.016), resolution=(1280, 720))):break
        
        touch([10,10])
        sleep(0.5)
    touch(Template(r"tpl1677990790296.png", record_pos=(-0.254, 0.016), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677990794079.png", record_pos=(-0.171, 0.018), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677990799260.png", record_pos=(0.405, 0.23), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677990803735.png", record_pos=(0.33, 0.231), resolution=(1280, 720)))


# 处理第一场战斗
def handle_first_battle():
    while True:
        if not exists(Template(r"tpl1677998079948.png", record_pos=(-0.222, -0.032), resolution=(1280, 720))):
            touch([15,15])
            continue
            
        touch(Template(r"tpl1677988307456.png", record_pos=(0.406, 0.229), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988311163.png", record_pos=(-0.028, 0.205), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988331687.png", record_pos=(0.406, 0.229), resolution=(1280, 720)))
        sleep(2.5)
        touch(Template(r"tpl1677988344619.png", record_pos=(0.405, 0.228), resolution=(1280, 720)))
        touch(Template(r"tpl1677988347728.png", record_pos=(-0.027, 0.218), resolution=(1280, 720)))

        sleep(1.25)
        touch(Template(r"tpl1677995541723.png", record_pos=(0.304, 0.244), resolution=(1280, 720)))

        sleep(1.25)
        touch(Template(r"tpl1677988384132.png", record_pos=(0.403, 0.231), resolution=(1280, 720)))

        max_cont = 3
        current_count = 0
        while True:
            if exists(Template(r"tpl1677988387808.png", record_pos=(0.398, 0.158), resolution=(1280, 720))):
                touch(Template(r"tpl1677988387808.png", record_pos=(0.398, 0.158), resolution=(1280, 720)));
                current_count += 1
                if current_count == max_cont: break
                sleep(0.5)

            else:
                touch([10,10])
                sleep(0.5)

        while a < 4:
            touch([10,10])
            a += 1
            sleep(0.75)


        while True:
            if exists(Template(r"tpl1677988443202.png", record_pos=(0.005, 0.187), resolution=(1280, 720))):
                touch(Template(r"tpl1677988443202.png", record_pos=(0.005, 0.187), resolution=(1280, 720)));
                break

            touch([1112,621])
            sleep(0.5)

        sleep(0.75)
        touch(Template(r"tpl1677988445517.png", record_pos=(0.005, 0.195), resolution=(1280, 720)))

        sleep(0.75)
        touch(Template(r"tpl1677988447086.png", record_pos=(0.005, 0.195), resolution=(1280, 720)))

        sleep(0.75)
        touch(Template(r"tpl1677988449078.png", record_pos=(0.005, 0.195), resolution=(1280, 720)))

        sleep(0.75)
        touch(Template(r"tpl1677988451926.png", record_pos=(0.28, 0.214), resolution=(1280, 720)))

        sleep(0.75)
        touch(Template(r"tpl1677991230753.png", record_pos=(0.294, -0.25), resolution=(1280, 720)))
    

        
# 处理训练（吃面包）
def handle_grow_up():
    while True:
        if not exists(Template(r"tpl1677998792138.png", record_pos=(-0.218, -0.034), resolution=(1280, 720))):
            touch([10,10])
            continue
        touch(Template(r"tpl1677988834673.png", record_pos=(0.407, 0.232), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988838003.png", record_pos=(0.407, 0.232), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988852879.png", record_pos=(0.391, 0.217), resolution=(1280, 720)))
        sleep(0.75)
        touch([10,10])
        sleep(0.75)
        touch([10,10])
        sleep(0.75)
        touch(Template(r"tpl1677988876734.png", record_pos=(0.03, -0.102), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988883307.png", record_pos=(0.409, 0.219), resolution=(1280, 720)))
        sleep(1.5)
        touch([10,10])
        sleep(0.75)
        touch(Template(r"tpl1677988898396.png", record_pos=(0.001, 0.212), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988949133.png", record_pos=(0.467, -0.245), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1677988956686.png", record_pos=(0.402, 0.23), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1677991304434.png", record_pos=(0.294, -0.245), resolution=(1280, 720)))

        sleep(0.75)
        touch(Template(r"tpl1677988967364.png", record_pos=(0.406, 0.231), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988972664.png", record_pos=(0.002, 0.188), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988978323.png", record_pos=(0.405, 0.229), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988983017.png", record_pos=(0.255, 0.214), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988988034.png", record_pos=(0.095, 0.212), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1677988992827.png", record_pos=(0.004, 0.064), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677988996188.png", record_pos=(0.395, 0.226), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677989009676.png", record_pos=(0.409, 0.224), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677989014127.png", record_pos=(0.405, 0.228), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677989018799.png", record_pos=(0.467, -0.246), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677989024943.png", record_pos=(0.47, -0.249), resolution=(1280, 720)))
        sleep(0.75)
        
        break
        
    
# 处理学习技能
def handle_learn_skills():
    touch([10,10])
    sleep(0.75)
    touch(Template(r"tpl1677989057067.png", record_pos=(-0.346, 0.208), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989066735.png", record_pos=(-0.277, 0.123), resolution=(1280, 720)))
    sleep(0.75)
    touch([10,10])
    sleep(0.75)
    touch([10,10])
    sleep(0.75)
    touch(Template(r"tpl1677989082544.png", record_pos=(-0.238, -0.145), resolution=(1280, 720)))
    sleep(0.75)
    touch([10,10])
    sleep(1)
    touch(Template(r"tpl1677995991913.png", record_pos=(-0.105, -0.062), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989099096.png", record_pos=(0.262, 0.112), resolution=(1280, 720)))
    sleep(1)
    touch(Template(r"tpl1677989102741.png", record_pos=(0.043, -0.058), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989104302.png", record_pos=(0.357, 0.23), resolution=(1280, 720)))
    sleep(0.75)
    touch([10,10])
    sleep(0.75)
    touch([10,10])
    sleep(0.75)
    touch(Template(r"tpl1677989130749.png", record_pos=(0.347, -0.205), resolution=(1280, 720)))
    sleep(0.75)
    touch([10,10])
    
    
# 处理查看商店
def handle_view_store():
    while True:
        if exists(Template(r"tpl1677999420039.png", record_pos=(0.187, -0.03), resolution=(1280, 720))):
            handle_click()
            sleep(0.75)
            continue
            
        touch(Template(r"tpl1677989190366.png", record_pos=(-0.341, 0.212), resolution=(1280, 720)))
        sleep(1)
        handle_click()
        sleep(1)
        handle_click()
        sleep(1)
        touch(Template(r"tpl1677996112312.png", record_pos=(0.196, 0.226), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1677989213252.png", record_pos=(0.416, -0.252), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1677989217184.png", record_pos=(0.409, 0.243), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1677989231339.png", record_pos=(0.406, 0.229), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1677989237398.png", record_pos=(0.412, 0.233), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1677989245697.png", record_pos=(0.471, -0.253), resolution=(1280, 720)))
        sleep(1.5)
        touch(Template(r"tpl1677989252116.png", record_pos=(-0.436, 0.205), resolution=(1280, 720)))
        while True:
            if exists(Template(r"tpl1677989265447.png", record_pos=(0.409, 0.225), resolution=(1280, 720))):
                touch(Template(r"tpl1677989265447.png", record_pos=(0.409, 0.225), resolution=(1280, 720)));
                break
        sleep(1)
        touch(Template(r"tpl1677989269509.png", record_pos=(0.409, 0.23), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677989275868.png", record_pos=(-0.161, 0.025), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677989281026.png", record_pos=(0.295, 0.211), resolution=(1280, 720)))
        sleep(1.5)
        while True:
            if exists(Template(r"tpl1677996277753.png", record_pos=(-0.002, 0.175), resolution=(1280, 720))):
                touch(Template(r"tpl1677996277753.png", record_pos=(-0.002, 0.175), resolution=(1280, 720)));
                break
        sleep(0.75)
        touch(Template(r"tpl1677989297844.png", record_pos=(0.403, 0.231), resolution=(1280, 720)))
        sleep(0.75)
        touch(Template(r"tpl1677989301321.png", record_pos=(0.468, -0.245), resolution=(1280, 720)))
        sleep(0.75)
        break
    
    
# 处理查看任务
def handle_view_task():
    touch([10,10])
    sleep(0.75)
    touch(Template(r"tpl1677989341586.png", record_pos=(0.467, -0.136), resolution=(1280, 720)))
    sleep(1)
    touch(Template(r"tpl1677989350444.png", record_pos=(0.406, 0.233), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989356247.png", record_pos=(0.406, 0.231), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989359688.png", record_pos=(0.405, 0.23), resolution=(1280, 720)))
    sleep(1.25)
    touch(Template(r"tpl1677996372704.png", record_pos=(0.14, -0.171), resolution=(1280, 720)))
    sleep(1)
    touch(Template(r"tpl1677989378792.png", record_pos=(0.406, 0.232), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989383518.png", record_pos=(0.472, -0.247), resolution=(1280, 720)))
    sleep(0.75)
    
    
# 处理查看账户
def handle_view_account():
    touch(Template(r"tpl1677989401356.png", record_pos=(0.407, 0.228), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989406178.png", record_pos=(0.461, -0.249), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989410992.png", record_pos=(0.011, 0.06), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989414733.png", record_pos=(0.402, 0.228), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989419029.png", record_pos=(0.402, 0.23), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989422833.png", record_pos=(0.416, 0.22), resolution=(1280, 720)))
    sleep(2)
    
    
# 处理获取英雄
def handle_get_hero():
    touch(Template(r"tpl1677989470258.png", record_pos=(0.217, -0.243), resolution=(1280, 720)))
    sleep(0.75)
    touch(Template(r"tpl1677989473546.png", record_pos=(0.463, -0.237), resolution=(1280, 720)))
#     sleep(2.5)
    touch(Template(r"tpl1677989487392.png", record_pos=(0.459, -0.233), resolution=(1280, 720)))
    sleep(2)
    touch(Template(r"tpl1677989497907.png", record_pos=(-0.447, -0.116), resolution=(1280, 720)))
    sleep(1.5)
    while True:
        if not exists(Template(r"tpl1677996603699.png", record_pos=(0.234, -0.077), resolution=(1280, 720))):
            touch(Template(r"tpl1677997045972.png", record_pos=(0.308, -0.205), resolution=(1280, 720)));
            sleep(0.5)
            touch(Template(r"tpl1677997068256.png", record_pos=(0.231, 0.216), resolution=(1280, 720)))
            break
            
            
        touch(Template(r"tpl1677996603699.png", record_pos=(0.234, -0.077), resolution=(1280, 720)));
        sleep(1)
        
        # 如果是5星契约书
        if exists(Template(r"tpl1677996677812.png", record_pos=(0.002, -0.077), resolution=(1280, 720))):
            touch(Template(r"tpl1677996704909.png", record_pos=(0.091, 0.173), resolution=(1280, 720)));

            sleep(1)

            swipe(Template(r"tpl1677991883594.png", record_pos=(-0.028, 0.066), resolution=(1280, 720)), vector=[-0.0089, -0.4055])     
            sleep(1)
            
            touch(Template(r"tpl1677996886372.png", record_pos=(0.396, 0.233), resolution=(1280, 720)))
            sleep(0.75)
        
        if exists(Template(r"tpl1677996954010.png", record_pos=(0.002, -0.075), resolution=(1280, 720))):
            touch(Template(r"tpl1677996965342.png", record_pos=(0.093, 0.172), resolution=(1280, 720)));
            sleep(1.5)
            touch([10,10])
            sleep(0.5)
            touch(Template(r"tpl1677997011838.png", record_pos=(-0.001, 0.176), resolution=(1280, 720)))




    
    



    













 


    



