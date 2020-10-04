# -*- encoding=utf8 -*-
__author__ = "A"
import threading
from airtest.core.api import *

auto_setup(__file__)

using("fgo.air")
from fgo import *
#获取当前设备分辨率
w,h = device().get_current_resolution()
tens = Template(r"tpl1601701667430.png", record_pos=(0.912, 0.363), resolution=(869, 578))
resetP = Template(r"tpl1601708954062.png", record_pos=(1.463, 0.207), resolution=(895, 593))
go = Template(r"tpl1601704886623.png", record_pos=(1.259, 0.415), resolution=(869, 578))
clo = Template(r"tpl1601704910228.png", record_pos=(1.104, 0.415), resolution=(869, 578))
drawsDone = True 
finish = 0
def draws():
    global finish
    finish = 10
    while(finish > 0):
        global drawsDone
        drawsDone = True
        t1 = threading.Thread(target = drawsOut, args = (drawsDone,))
        t1.start()
        while(drawsDone):
            touch((0.250*w, 0.600*h))
            sleep(0.5)
        #结算
        touch((0.850*w, 0.340*h))
        touch(go)
        touch(clo)
        sleep(1.5)
        drawsDone = False
        finish = finish - 1

            
            
def drawsOut(typr):
    global drawsDone
    while(drawsDone):
        sleep(2.0)
        if(exists(resetP)):
            drawsDone = False


draws()