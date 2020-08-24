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
cba=Template(r"tpl1596257560180.png", record_pos=(0.931, 0.222), resolution=(801, 540))
jiaGong=Template(r"tpl1595156871397.png", record_pos=(1.32, 0.066), resolution=(899, 593))
jiaFang=Template(r"tpl1595157663041.png", record_pos=(0.67, 0.273), resolution=(899, 593))
attack=Template(r"tpl1595157002971.png", record_pos=(1.429, 0.298), resolution=(899, 593))
bMoFang=Template(r"tpl1595157953631.png", record_pos=(0.918, 0.274), resolution=(899, 593))
downDEF=Template(r"tpl1596259366831.png", record_pos=(1.308, 0.38), resolution=(801, 540))

#主方法入口
def act1():
    #根据礼装找助战
    findHelperByLiZhuang(cba)
    #开始任务
    touch(Template(r"tpl1595156794886.png", record_pos=(1.472, 0.35), resolution=(899, 593)))
    sleep(20.0)
    #大英雄的回合
    #充能
    touch((0.445*w, 0.730*h))
    sleep(3.0)
    #攻击
    touch(attack)
    sleep(1.5)
    #stella
    touch((0.500*w, 0.300*h))
    selectCard()
    sleep(25.0)
    wait(jiaGong)
    #孔明
    #充能
    touch((0.445*w, 0.730*h))
    sleep(3.0)
    touch((0.375*w, 0.730*h))
    sleep(3.0)
    touch((0.305*w, 0.730*h))
    sleep(0.5)
    touch((0.250*w, 0.600*h))
    sleep(3.0)
    #cba充能
    touch((0.700*w, 0.730*h))
    sleep(0.5)
    touch((0.250*w, 0.600*h))
    sleep(3.0)
    #攻击
    touch(attack)
    sleep(1.5)
    #尼托宝具1
    touch((0.300*w, 0.300*h))
    selectCard()
    sleep(30.0)
    wait(downDEF)
    #cba降防
    touch((0.630*w, 0.730*h))
    sleep(3.0)
    touch((0.120*w, 0.730*h))
    sleep(3.0)
    #衣服打开
    touch((0.940*w, 0.430*h))
    sleep(0.8)
    touch((0.780*w, 0.430*h))
    sleep(0.8)
    touch((0.250*w, 0.600*h))
    sleep(3.0)
    #攻击
    touch(attack)
    sleep(1.5)
    #尼托宝具2
    touch((0.300*w, 0.300*h))
    selectCard()
    sleep(35.0)

    #结算
    #1
    touch((0.500*w, 0.300*h))
    touch((0.500*w, 0.880*h))
    sleep(1.5)
    #2
    touch((0.500*w, 0.300*h))
    touch((0.500*w, 0.880*h))
    sleep(1.5)
    #出门
    touch(Template(r"tpl1595161841879.png", record_pos=(1.304, 0.385), resolution=(899, 593)))
    sleep(10.0)
    touch((0.050*w, 0.850*h))
    sleep(5.0)


