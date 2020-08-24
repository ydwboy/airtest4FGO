# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

using("fgo.air")
from fgo import *
#获取当前设备分辨率
w,h = device().get_current_resolution()

#全局使用图片定义
head=Template(r"tpl1598082276272.png", record_pos=(1.78, -0.062), resolution=(785, 531))
littleDFQ=Template(r"tpl1594959367052.png", record_pos=(0.051, 0.162), resolution=(1440, 802))
littleMX=Template(r"tpl1598084278396.png", record_pos=(0.061, 0.018), resolution=(1246, 790))
kongmingWithMX=Template(r"tpl1595155663680.png", record_pos=(0.54, 0.338), resolution=(899, 593),threshold=0.85)
cba=Template(r"tpl1596257560180.png", record_pos=(0.931, 0.222), resolution=(801, 540))
jiaGong=Template(r"tpl1595156871397.png", record_pos=(1.32, 0.066), resolution=(899, 593))
jiaFang=Template(r"tpl1595157663041.png", record_pos=(0.67, 0.273), resolution=(899, 593))
attack=Template(r"tpl1595157002971.png", record_pos=(1.429, 0.298), resolution=(899, 593))
bMoFang=Template(r"tpl1595157953631.png", record_pos=(0.918, 0.274), resolution=(899, 593))
downDEF=Template(r"tpl1596259366831.png", record_pos=(1.308, 0.38), resolution=(801, 540))
#主方法入口
def actMain():
    #根据礼装找助战
    findHelperByLiZhuang(littleMX)
    #开始任务
    if(exists(Template(r"tpl1595156794886.png", record_pos=(1.472, 0.35), resolution=(899, 593)))):
        touch(Template(r"tpl1595156794886.png", record_pos=(1.472, 0.35), resolution=(899, 593)))
        iscontinue=True
        sleep(5.0)
    sleep(10.0)
    wait(head)
    #斯巴达克斯的回合
    #1充能
    skills(5)
    #2红魔放
    skills(6)
    #3茶茶缓冲
    skills(7)
    #点击攻击
    touch(attack)
    sleep(1.5)
    #3宝具
    skills(32)
    wait(head)
    
    #bnn
    #4充能
    skills(2)
    #点击攻击
    touch(attack)
    sleep(1.5)
    #5宝具
    skills(31)
    wait(head)
    
    #茶茶
    #攻击
    touch(attack)
    sleep(1.5)
    #6宝具
    skills(33)
    sleep(5.0)

    #结算
    while(not exists(Template(r"tpl1595161841879.png", record_pos=(1.304, 0.385), resolution=(899, 593)))):
        sleep(1.0)
        touch((0.500*w, 0.300*h))
        sleep(1.0)
    #1
    #touch((0.500*w, 0.300*h))
    #touch((0.500*w, 0.880*h))
    #sleep(1.5)
    #2
    #touch((0.500*w, 0.300*h))
    #touch((0.500*w, 0.880*h))
    #sleep(1.5)
    #出门
    touch(Template(r"tpl1595161841879.png", record_pos=(1.304, 0.385), resolution=(899, 593)))
    sleep(1.0)
    touch(Template(r"tpl1598074711519.png", record_pos=(1.468, 0.475), resolution=(785, 531)))
    sleep(2.0)

