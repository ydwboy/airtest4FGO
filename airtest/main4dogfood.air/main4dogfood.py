# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

using("fgo.air")
from fgo import *
#获取当前设备分辨率
w,h = device().get_current_resolution()

#全局使用图片定义
littleDFQ=Template(r"tpl1594959367052.png", record_pos=(0.051, 0.162), resolution=(1440, 802))
littleMX=Template(r"tpl1595155439751.png", record_pos=(1.302, 0.49), resolution=(592, 422))
kongmingWithMX=Template(r"tpl1595155663680.png", record_pos=(0.54, 0.338), resolution=(899, 593),threshold=0.85)
jiaGong=Template(r"tpl1595156871397.png", record_pos=(1.32, 0.066), resolution=(899, 593))
jiaFang=Template(r"tpl1595157663041.png", record_pos=(0.67, 0.273), resolution=(899, 593))
attack=Template(r"tpl1595157002971.png", record_pos=(1.429, 0.298), resolution=(899, 593))
bMoFang=Template(r"tpl1595157953631.png", record_pos=(0.918, 0.274), resolution=(899, 593))

#主方法入口
def dogfood():
    #根据礼装找助战
    findHelperByLiZhuang(kongmingWithMX)
    #开始任务
    touch(Template(r"tpl1595156794886.png", record_pos=(1.472, 0.35), resolution=(899, 593)))
    sleep(8.0)
    #大英雄的回合
    #充能
    touch(Template(r"tpl1595156835362.png", record_pos=(0.744, 0.274), resolution=(899, 593)))
    sleep(1.0)
    touch(Template(r"tpl1595156854788.png", record_pos=(1.474, 0.068), resolution=(899, 593)))
    sleep(0.5)
    touch(jiaGong)
    sleep(0.5)
    touch(Template(r"tpl1595156890380.png", record_pos=(0.808, 0.196), resolution=(899, 593)))
    sleep(1.0)
    touch(attack)
    sleep(1.0)

    #stella
    touch((0.300*w, 0.300*h))
    selectCard()
    sleep(20.0)
    wait(jiaGong)

    #孔明
    #充能
    touch(jiaGong)
    sleep(1.5)
    touch(jiaFang)
    sleep(1.5)
    touch(attack)
    sleep(1.0)
    
    #狂兰宝具
    touch((0.700*w,0.300*h))
    selectCard()
    sleep(20.0)
    wait(bMoFang)

    #奶光魔放
    touch(bMoFang)
    sleep(1.5)
    touch(attack)
    sleep(1.0)

    #奶光宝具
    touch((0.500*w, 0.300*h))
    selectCard()
    sleep(30.0)

    #结算
    touch((0.500*w, 0.300*h))
    touch((0.500*w, 0.900*h))
    sleep(1.5)
    touch((0.500*w, 0.300*h))
    touch((0.500*w, 0.900*h))
    sleep(1.5)
    touch(Template(r"tpl1595161841879.png", record_pos=(1.304, 0.385), resolution=(899, 593)))
    sleep(8.0)



