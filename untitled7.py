# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:35:14 2018

@author: Sam
"""
from mcpi.minecraft import Minecraft
sam = Minecraft.create()
x,y,z=sam.player.getTilePos()

block=int(input("請輸入要放的方塊ID:"))
sam.setBlock(x,y,z,block)
