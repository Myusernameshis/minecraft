# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:48:01 2018

@author: Sam
"""
from mcpi.minecraft import Minecraft
sam = Minecraft.create()
x,y,z=sam.player.getTilePos()
a=sam.getBlock(x+1,y-1,z)
b=sam.getBlock(x-1,y-1,z)
c=sam.getBlock(x,y-1,z+1)
d=sam.getBlock(x,y-1,z-1)
if a==8 or a==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9:
    sam.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,46)