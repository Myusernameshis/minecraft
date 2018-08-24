# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:28:21 2018

@author: NTPU
"""

from random import choice
from mcpi.minecraft import Minecraft
sam = Minecraft.create()

list2 = [[1,1,0,1,1,1,1,1,1,0],
         [1,1,1,1,1,0,1,1,1,0],
         [1,1,1,1,1,1,1,0,1,0],
         [1,1,1,0,1,1,0,1,1,0],
         [0,1,1,1,1,1,1,1,1,0],
         [1,1,0,1,1,0,1,1,1,0],
         [1,1,1,1,0,1,1,1,1,0],
         [0,1,0,1,1,1,0,1,1,0],
         [1,1,1,0,1,1,1,1,0,0]]

myID=sam.getPlayerEntityId("sam0617")
x,y,z=sam.entity.getTilePos(myID)
StartX = x

for list1 in list2:
    for i in list1:
        sam.setBlock(x,y,z,i)
        x=x+1
    x = StartX
    z=z+1