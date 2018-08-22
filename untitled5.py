# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:36:21 2018

@author: Sam
"""

from mcpi.minecraft import Minecraft
sam = Minecraft.create()
x,y,z=sam.player.getTilePos()
a=0
while a<100:
    sam.setBlocks(x,y-1,z+30,x,y-30,z-30,19)
    x=x-5
    a=a+1