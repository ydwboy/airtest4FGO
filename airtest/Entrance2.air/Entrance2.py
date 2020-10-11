# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
using("swimmingsuit1.air")
from swimmingsuit1 import *
#获取当前设备分辨率
w,h = device().get_current_resolution()
dogFoodMap=Template(r"tpl1595161921148.png", record_pos=(1.146, 0.013), resolution=(899, 593))
actMap=Template(r"tpl1596260029595.png", record_pos=(1.365, 0.046), resolution=(801, 540))
goldenApple = Template(r"tpl1595162203983.png", record_pos=(0.731, 0.112), resolution=(899, 593))
silverApple = Template(r"tpl1601554325985.png", record_pos=(0.811, 0.43), resolution=(805, 542))
copperApple = Template(r"tpl1601739150611.png", record_pos=(0.517, 0.469), resolution=(917, 605))
#循环肝
while(True):
    #体力不够 吃苹果
    if(exists(Template(r"tpl1595162167265.png", record_pos=(0.94, -0.09), resolution=(899, 593)))):
        swipe((0.500*w, 0.600*h),(0.500*w, 0.400*h))
        sleep(1.0)
        touch(goldenApple)
        sleep(1.0)
        touch(Template(r"tpl1595162231877.png", record_pos=(1.094, 0.298), resolution=(899, 593)))
        sleep(2.0)
    
    actMain()

        
    

