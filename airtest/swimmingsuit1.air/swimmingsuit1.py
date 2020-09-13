# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

using("fgo.air")
from fgo import *
#获取当前设备分辨率
w,h = device().get_current_resolution()

#全局使用图片定义
head=Template(r"tpl1599061246578.png", record_pos=(1.345, 0.211), resolution=(852, 568))
head2=Template(r"tpl1599305179332.png", record_pos=(1.605, 0.015), resolution=(812, 546))
littleDFQ=Template(r"tpl1594959367052.png", record_pos=(0.051, 0.162), resolution=(1440, 802))
littleMX=Template(r"tpl1598084278396.png", record_pos=(0.061, 0.018), resolution=(1246, 790))
kongmingWithMX=Template(r"tpl1595155663680.png", record_pos=(0.54, 0.338), resolution=(899, 593),threshold=0.85)
kongmingWithDFQ=Template(r"tpl1599061140339.png", threshold=0.9, record_pos=(0.683, 0.166), resolution=(852, 568))
cba=Template(r"tpl1596257560180.png", record_pos=(0.931, 0.222), resolution=(801, 540))
jiaGong=Template(r"tpl1595156871397.png", record_pos=(1.32, 0.066), resolution=(899, 593))
jiaFang=Template(r"tpl1595157663041.png", record_pos=(0.67, 0.273), resolution=(899, 593))
attack=Template(r"tpl1595157002971.png", record_pos=(1.429, 0.298), resolution=(899, 593))
bMoFang=Template(r"tpl1595157953631.png", record_pos=(0.918, 0.274), resolution=(899, 593))
downDEF=Template(r"tpl1596259366831.png", record_pos=(1.308, 0.38), resolution=(801, 540))
changingMan=Template(r"tpl1599304666681.png", record_pos=(1.18, 0.429), resolution=(812, 546))

#开始任务
def startCheck():
    if(exists(Template(r"tpl1595156794886.png", record_pos=(1.472, 0.35), resolution=(899, 593)))):
        touch(Template(r"tpl1595156794886.png", record_pos=(1.472, 0.35), resolution=(899, 593)))
        iscontinue=True
        sleep(5.0)
    sleep(10.0)

#结算
def resultCheck():
    while(not exists(Template(r"tpl1595161841879.png", record_pos=(1.304, 0.385), resolution=(899, 593)))):
        sleep(1.0)
        touch((0.500*w, 0.300*h))
        sleep(1.0)
    #出门
    touch(Template(r"tpl1595161841879.png", record_pos=(1.304, 0.385), resolution=(899, 593)))
    sleep(1.0)
    touch(Template(r"tpl1598074711519.png", record_pos=(1.468, 0.475), resolution=(785, 531)))
    sleep(2.0)

#主方法入口
def actMain():
    #根据礼装找助战
    findHelperByLiZhuang(kongmingWithDFQ)
    startCheck()
    #archerJ()
    #
    riderDFQ()
    #结算
    resultCheck()
    
def archerJ():
    wait(head)
    #1的回合
    skills(9)
    skills(6)
    skills(1)
    skills(3)
    touch(attack)
    sleep(1.5)
    skills(31)
    wait(head)
    
    #2
    skills(2)
    skills(5)
    skills(8)
    touch(attack)
    sleep(1.5)
    skills(31)
    wait(head)
    
    #3
    skills(4)
    skills(11)
    skills(7)
    skills(11)
    skills(20)
    skills(22)
    skills(11)
    touch(attack)
    sleep(1.5)
    skills(31)
    sleep(5.0)
    
    
def riderDFQ():
    wait(head2)
    #1
    skills(9)
    skills(1)
    touch(attack)
    sleep(1.5)
    skills(33)
    wait(head2)
    #2
    skills(3)
    skills(6)
    skills(9)
    skills(4)
    skills(11)
    skills(7)
    skills(11)
    touch(attack)
    sleep(1.5)
    skills(31)
    wait(head2)
    #3
    skills(5)
    skills(8)
    skills(20)
    skills(21)
    skills(20)
    skills(23)
    skills(42)
    skills(44)
    touch(changingMan)
    sleep(3.0)
    skills(5)
    skills(11)
    touch(attack)
    sleep(1.5)
    skills(31)
    sleep(5.0)
    

#while(not exists(Template(r"tpl1595161841879.png", record_pos=(1.304, 0.385), resolution=(899, 593)))):
    #    sleep(1.0)
    #    touch((0.500*w, 0.300*h))
    #    sleep(1.0)
    #1
    #touch((0.500*w, 0.300*h))
    #touch((0.500*w, 0.880*h))
    #sleep(1.5)
    #2
    #touch((0.500*w, 0.300*h))
    #touch((0.500*w, 0.880*h))
    #sleep(1.5)
    #出门
    #touch(Template(r"tpl1595161841879.png", record_pos=(1.304, 0.385), resolution=(899, 593)))
    #sleep(1.0)
    #touch(Template(r"tpl1598074711519.png", record_pos=(1.468, 0.475), resolution=(785, 531)))
    #sleep(2.0)