# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:39:10 2018

@author: Sam
"""
from mcpi.minecraft import Minecraft
sam = Minecraft.create()

x,y,z=sam.player.getTilePos()

for i in range(50):
    sam.setBlock(x+i,y-1,z+i,11)
    sam.setBlock(x+i+1,y-1,z+i,166)
    sam.setBlock(x+i+2,y-1,z+i,166)
    sam.setBlock(x+i+3,y-1,z+i,11)