# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:32:46 2018

@author: Sam
"""
import random, time
from mcpi.minecraft import Minecraft
sam = Minecraft.create()
pos=sam.player.getTilepos()
while True:
    x=pos.x+random.uniform(-50,50)
    y=pos.y+40
    z=pos.z+random.uniform(-50,50)
    sam.spawnEntity(x,y,z,53)
    time.sleep(0.01)