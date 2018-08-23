# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:36:37 2018

@author: Sam
"""
import random
from mcpi.minecraft import Minecraft
sam = Minecraft.create()

x,y,z=sam.player.getTilePos()

for i in range(500):
    l=randrange(2,16)
    r=randrange(1,9)
    c=randrange(1,16)
    
    if r == 1:
        sam.setBlocks(x,y,z,x+4,y,z,35,c)
        x = x+4
    elif r == 2:
        sam.setBlocks(x,y,z,x-4,y,z,35,c)
        x = x-4    
    elif r == 3:
        sam.setBlocks(x,y,z,x,y,z+4,35,c)
        z = z + 4
    elif r == 4:
        sam.setBlocks(x,y,z,x,y,z-4,35,c)
        z = z - 4
    elif r == 5:
        sam.setBlocks(x,y,z,x,y+4,z,35,c)
        y = y + 4
    elif r == 6:
        sam.setBlocks(x,y,z,x,y-4,z,35,c)
        y = y - 4