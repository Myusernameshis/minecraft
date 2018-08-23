# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:15:14 2018

@author: NTPU
"""

from random import randrange
from mcpi.minecraft import Minecraft
sam = Minecraft.create()



for j in range(30):
    x,y,z=sam.player.getTilePos()
    x=x+j
    for i in range(30):
        r=randrange(0,10)
        sam.setBlock(x,y,z,35,r)
        z=z+1
        
sam.postToChat("!GAME START!")
r = randrange(0,16)
while True:
    hits=sam.events.pollBlockHits()
    if len(hits)>0:
        h= hits[0]
        
        block=sam.getBlockWithData(h.pos)
        data = block.data
        if data == r:
            sam.postToChat("恭喜你找到了!")
            sam.setBlock(h.pos,57)
            break
        elif data>r:
            sam.postToChat("要找更小的顏色")
        elif data<r:
            sam.postToChat("要找更大的顏色")
            
 
       