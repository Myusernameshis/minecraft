# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:42:14 2018

@author: Sam

-
"""

from mcpi.minecraft import Minecraft
sam = Minecraft.create()

x,y,z=sam.player.getTilePos()
def plantTree(x,y,z):
    sam.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    sam.setBlocks(x,y,z,x,y+4,z,17)
for i in range(50):
    for j in range(10):
        for k in range(50):
            plantTree(x+i*5,y,z)