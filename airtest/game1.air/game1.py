# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
using("main4dogfood.air")
using("activity1.air")
from main4dogfood import *
from activity1 import *
dogFoodMap=Template(r"tpl1595161921148.png", record_pos=(1.146, 0.013), resolution=(899, 593))
actMap=Template(r"tpl1596260029595.png", record_pos=(1.365, 0.046), resolution=(801, 540))
#循环肝
while(True):
    touch(actMap)
    sleep(1.2)
    #体力不够 吃苹果
    if(exists(Template(r"tpl1595162167265.png", record_pos=(0.94, -0.09), resolution=(899, 593)))):
        touch(Template(r"tpl1595162203983.png", record_pos=(0.731, 0.112), resolution=(899, 593)))
        sleep(1.0)
        touch(Template(r"tpl1595162231877.png", record_pos=(1.094, 0.298), resolution=(899, 593)))
    act1()

        
    
