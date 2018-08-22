# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:08:10 2018

@author: Sam
"""
from mcpi.minecraft import Minecraft
sam = Minecraft.create()
x,y,z=sam.player.getTilePos()
width=10
length=6
height=20
block=11
air=0
sam.setBlocks(x,y,z,x+width,y+height,z+length,block)
sam.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,air)