# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
w,h = device().get_current_resolution()
print(w)
print(h)
touch((0.150*w, 0.500*h))

#1 号技能：touch((0.050*w, 0.730*h))
#2 号技能：touch((0.120*w, 0.730*h))
#3 号技能：touch((0.200*w, 0.730*h))

#4 号技能：touch((0.305*w, 0.730*h))
#5 号技能：touch((0.375*w, 0.730*h))
#6 号技能：touch((0.445*w, 0.730*h))

#7 号技能：touch((0.550*w, 0.730*h))
#8 号技能：touch((0.630*w, 0.730*h))
#9 号技能：touch((0.700*w, 0.730*h))

#1人：touch((0.250*w, 0.600*h))
#2人：touch((0.500*w, 0.600*h))
#3人：touch((0.750*w, 0.600*h))

#衣服打开：touch((0.940*w, 0.430*h))
#1衣：touch((0.700*w, 0.430*h))
#2衣：touch((0.780*w, 0.430*h))
#3衣：touch((0.850*w, 0.430*h))