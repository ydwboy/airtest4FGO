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
resetP = Template(r"tpl1601701980626.png", record_pos=(1.453, 0.159), resolution=(869, 578))
go = Template(r"tpl1601704886623.png", record_pos=(1.259, 0.415), resolution=(869, 578))
clo = Template(r"tpl1601704910228.png", record_pos=(1.104, 0.415), resolution=(869, 578))
def draws():
    finish = True
    while(finish):
        drawsDone = True
        t1 = threading.Thread(target = drawsOut, args = (drawsDone,))
        t1.start()
        while(drawsDone):
            touch((0.250*w, 0.600*h))

            
            
def drawsOut():
    while(drawsDone):
        if(exists(resetP)):
            drawsDone = False


draws()