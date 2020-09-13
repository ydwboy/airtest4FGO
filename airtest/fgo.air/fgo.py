# -*- encoding=utf8 -*-
__author__ = "A"

from airtest.core.api import *

auto_setup(__file__)
#获取当前设备分辨率
w,h = device().get_current_resolution()
#全局使用图片定义
listRenew=Template(r"tpl1595156115284.png", record_pos=(1.247, 0.049), resolution=(899, 593))
Yes=Template(r"tpl1595156164047.png", record_pos=(1.235, 0.385), resolution=(899, 593))
No=Template(r"tpl1595156178075.png", record_pos=(0.927, 0.387), resolution=(899, 593))
Close=Template(r"tpl1595156196119.png", record_pos=(1.081, 0.387), resolution=(899, 593))
head=Template(r"tpl1598082276272.png", record_pos=(1.78, -0.062), resolution=(785, 531))
# cases={
#     #1 号技能：
#     '1':touch((0.050*w, 0.730*h)),
#     #2 号技能：
#     '2':touch((0.120*w, 0.730*h)),
#     #3 号技能：
#     '3':touch((0.200*w, 0.730*h)),
#     #4 号技能：
#     '4':touch((0.305*w, 0.730*h)),
#     #5 号技能：
#     '5':touch((0.375*w, 0.730*h)),
#     #6 号技能：
#     '6':touch((0.445*w, 0.730*h)),
#     #7 号技能：
#     '7':touch((0.550*w, 0.730*h)),
#     #8 号技能：
#     '8':touch((0.630*w, 0.730*h)),
#     #9 号技能：
#     '9':touch((0.700*w, 0.730*h)),
#     #1人：
#     '11':touch((0.250*w, 0.600*h)),
#     #2人：
#     '12':touch((0.500*w, 0.600*h)),
#     #3人：
#     '13':touch((0.750*w, 0.600*h)),
#     #衣服打开：
#     '20':touch((0.940*w, 0.430*h)),
#     #1衣：
#     '21':touch((0.700*w, 0.430*h)),
#     #2衣：
#     '22':touch((0.780*w, 0.430*h)),
#     #3衣：
#     '23':touch((0.850*w, 0.430*h)),
#     #1宝：
#     '31':touch((0.300*w, 0.300*h)),
#     #2宝：
#     '32':touch((0.500*w, 0.300*h)),
#     #3宝：
#     '33':touch((0.700*w, 0.300*h))
# }
def findHelperByLiZhuang(lizhuang):
    findTheLiZhuang=False
    times=0
    while(not findTheLiZhuang):
        findTheLiZhuang=exists(lizhuang)
        if(findTheLiZhuang):
            times=0
            touch(lizhuang)
        elif(times >= 5):
            times=0
            touch(listRenew)
            touch(Yes)
            if(exists(Close)):
                times=5
                sleep(5.0)
        else:
            times=times+1
            swipe((0.500*w, 0.800*h),(0.500*w, 0.300*h))
def selectCard():
    sleep(0.5)
    #2卡
    touch((0.100*w, 0.700*h))
    sleep(0.5)
    #3卡
    touch((0.300*w, 0.700*h))
# 放技能方法
def skills(skillNum): 
    if(skillNum==1):
        #1 号技能：
        touch((0.050*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==2):
        #2 号技能：
        touch((0.120*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==3):
        #3 号技能：
        touch((0.200*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==4):
        #4 号技能：
        touch((0.305*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==5):
        #5 号技能：
        touch((0.375*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==6):
        #6 号技能：
        touch((0.445*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==7):
        #7 号技能：
        touch((0.550*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==8):
        #8 号技能：
        touch((0.630*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==9):
        #9 号技能：
        touch((0.700*w, 0.730*h))
        sleep(3.0)
    elif(skillNum==11):
        #1人：
        touch((0.250*w, 0.600*h))
        sleep(3.0)
    elif(skillNum==12):
        #2人：
        touch((0.500*w, 0.600*h))
        sleep(3.0)
    elif(skillNum==13):
        #3人：
        touch((0.750*w, 0.600*h))
        sleep(3.0)
    elif(skillNum==20):
        #衣服打开：
        touch((0.940*w, 0.430*h))
        sleep(3.0)
    elif(skillNum==21):
        #1衣：
        touch((0.700*w, 0.430*h))
        sleep(3.0)
    elif(skillNum==22):
        #2衣：
        touch((0.780*w, 0.430*h))
        sleep(3.0)
    elif(skillNum==23):
        #3衣：
        touch((0.850*w, 0.430*h))
        sleep(3.0)
    elif(skillNum==31):
        #1宝：
        touch((0.300*w, 0.300*h))
        selectCard()
        sleep(20.0)
    elif(skillNum==32):
        #2宝：
        touch((0.500*w, 0.300*h))
        selectCard()
        sleep(20.0)
    elif(skillNum==33):
        #3宝：
        touch((0.700*w, 0.300*h))
        selectCard()
        sleep(20.0)
    elif(skillNum==41):
        #1前：
        touch((0.100*w, 0.500*h))
        sleep(1.0)
    elif(skillNum==42):
        #2前：
        touch((0.250*w, 0.500*h))
        sleep(1.0)
    elif(skillNum==43):
        #3前：
        touch((0.400*w, 0.500*h))
        sleep(1.0)
    elif(skillNum==44):
        #4后：
        touch((0.550*w, 0.500*h))
        sleep(1.0)
    elif(skillNum==45):
        #5后：
        touch((0.700*w, 0.500*h))
        sleep(1.0)
    elif(skillNum==46):
        #6后：
        touch((0.900*w, 0.500*h))
        sleep(1.0)
"""
    switch(skillNum):
        case 1:
            #1 号技能：
            touch((0.050*w, 0.730*h))
            sleep(3.0)
            break
        case 2:
            #2 号技能：
            touch((0.120*w, 0.730*h))
            sleep(3.0)
            break
        case 3:
            #3 号技能：
            touch((0.200*w, 0.730*h))
            sleep(3.0)
            break
        case 4:
            #4 号技能：
            touch((0.305*w, 0.730*h))
            sleep(3.0)
            break
        case 5:
            #5 号技能：
            touch((0.375*w, 0.730*h))
            sleep(3.0)
            break
        case 6:
            #6 号技能：
            touch((0.445*w, 0.730*h))
            sleep(3.0)
            break
        case 7:
            #7 号技能：
            touch((0.550*w, 0.730*h))
            sleep(3.0)
            break
        case 8:
            #8 号技能：
            touch((0.630*w, 0.730*h))
            sleep(3.0)
            break
        case 9:
            #9 号技能：
            touch((0.700*w, 0.730*h))
            sleep(3.0)
            break
        case 11:
            #1人：
            touch((0.250*w, 0.600*h))
            sleep(3.0)
            break
        case 12:
            #2人：
            touch((0.500*w, 0.600*h))
            sleep(3.0)
            break
        case 13:
            #3人：
            touch((0.750*w, 0.600*h))
            sleep(3.0)
            break
        case 20:
            #衣服打开：
            touch((0.940*w, 0.430*h))
            sleep(3.0)
            break
        case 21:
            #1衣：
            touch((0.700*w, 0.430*h))
            sleep(3.0)
            break
        case 22:
            #2衣：
            touch((0.780*w, 0.430*h))
            sleep(3.0)
            break
        case 23:
            #3衣：
            touch((0.850*w, 0.430*h))
            sleep(3.0)
            break
        case 31:
            #1宝：
            touch((0.300*w, 0.300*h))
            selectCard()
            sleep(30.0)
            break
        case 32:
            #2宝：
            touch((0.500*w, 0.300*h))
            selectCard()
            sleep(30.0)
            break
        case 33:
            #3宝：
            touch((0.700*w, 0.300*h))
            selectCard()
            sleep(30.0)
            break
"""
#end
    
    

