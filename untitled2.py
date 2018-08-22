# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:44:43 2018

@author: Sam
"""
from mcpi.minecraft import Minecraft
sam = Minecraft.create()

while True:
    hits = sam.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        x,y,z = h.pos.x, h.pos.y, h.pos.z
        block = sam.getBlock(x,y,z)
         sam.postToChat("恭喜你獵到了:"+str(block))