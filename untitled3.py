# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:29:17 2018

@author: Sam
"""
import time
from mcpi.minecraft import Minecraft
sam = Minecraft.create()
while True:
    x,y,z=sam.player.getTilePos()
    sam.setBlock(x,y,z,52)
    time.sleep(3)